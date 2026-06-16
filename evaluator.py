import faiss
import numpy as np
import torch
import difflib
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GPT2LMHeadModel, GPT2TokenizerFast

class AIEvaluator:
    def __init__(self):
        print("Loading models... This may take a while.")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # 1. Embedding model for semantic search
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        
        # 2. Grammar correction model
        grammar_model_name = "pszemraj/flan-t5-large-grammar-synthesis"
        self.grammar_tokenizer = AutoTokenizer.from_pretrained(grammar_model_name)
        self.grammar_model = AutoModelForSeq2SeqLM.from_pretrained(grammar_model_name).to(self.device)
        
        # 3. Fluency/Perplexity model
        self.gpt2_tokenizer = GPT2TokenizerFast.from_pretrained("distilgpt2")
        self.gpt2_tokenizer.pad_token = self.gpt2_tokenizer.eos_token
        self.gpt2_model = GPT2LMHeadModel.from_pretrained("distilgpt2").to(self.device)
        
        print(f"Models loaded successfully on {self.device}.")

    def compute_semantic_similarity(self, user_answer, reference_answers):
        """Computes semantic similarity using FAISS."""
        ref_embeddings = self.embedder.encode(reference_answers)
        user_embedding = self.embedder.encode([user_answer])
        
        d = ref_embeddings.shape[1]
        index = faiss.IndexFlatL2(d)
        index.add(np.array(ref_embeddings))
        
        distances, indices = index.search(np.array(user_embedding), 1)
        best_distance = distances[0][0]
        
        # Normalize distance to 0-100 score (L2 distance approximation)
        score = max(0.0, 100.0 - (best_distance * 10))
        return score

    def compute_grammar_score(self, user_answer):
        """Checks and corrects grammar, returning a score based on sequence matching."""
        inputs = self.grammar_tokenizer(user_answer, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.grammar_model.generate(**inputs, max_length=128)
        corrected_text = self.grammar_tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        similarity = difflib.SequenceMatcher(None, user_answer.lower(), corrected_text.lower()).ratio()
        return corrected_text, similarity * 100.0

    def compute_fluency_score(self, user_answer):
        """Calculates fluency using perplexity from a GPT-2 model."""
        encodings = self.gpt2_tokenizer(user_answer, return_tensors='pt').to(self.device)
        max_length = self.gpt2_model.config.n_positions
        seq_len = encodings.input_ids.size(1)
        
        if seq_len == 0:
            return 0.0

        nlls = []
        stride = 512
        prev_end_loc = 0
        for begin_loc in range(0, seq_len, stride):
            end_loc = min(begin_loc + max_length, seq_len)
            trg_len = end_loc - prev_end_loc
            input_ids = encodings.input_ids[:, begin_loc:end_loc].to(self.device)
            target_ids = input_ids.clone()
            target_ids[:, :-trg_len] = -100

            with torch.no_grad():
                outputs = self.gpt2_model(input_ids, labels=target_ids)
                neg_log_likelihood = outputs.loss

            nlls.append(neg_log_likelihood)
            prev_end_loc = end_loc
            if end_loc == seq_len:
                break
                
        ppl = torch.exp(torch.stack(nlls).mean()).item()
        
        # Lower perplexity is better, normalized to 100
        score = max(0.0, 100.0 - (ppl / 1.5)) 
        return min(100.0, score)

    def compute_keyword_score(self, user_answer, keywords):
        """Checks for presence of target keywords."""
        if not keywords:
            return 100.0
        user_answer_lower = user_answer.lower()
        matched = [kw for kw in keywords if kw.lower() in user_answer_lower]
        return (len(matched) / len(keywords)) * 100.0

    def evaluate_answer(self, user_answer, question_dict):
        """Generates the multi-dimensional scoring framework output."""
        reference_answers = question_dict.get("answers", [])
        keywords = question_dict.get("keywords", [])
        
        sem_score = self.compute_semantic_similarity(user_answer, reference_answers)
        corrected_txt, gram_score = self.compute_grammar_score(user_answer)
        fluency_score = self.compute_fluency_score(user_answer)
        kw_score = self.compute_keyword_score(user_answer, keywords)
        
        # Weighted Final Score based on your description
        final_score = (sem_score * 0.4) + (kw_score * 0.3) + (gram_score * 0.15) + (fluency_score * 0.15)
        
        return {
            "final_score": round(final_score, 2),
            "semantic_score": round(sem_score, 2),
            "grammar_score": round(gram_score, 2),
            "fluency_score": round(fluency_score, 2),
            "keyword_score": round(kw_score, 2),
            "corrected_text": corrected_txt
        }

# Lazy loading instance for API usage
_evaluator_instance = None
def get_evaluator():
    global _evaluator_instance
    if _evaluator_instance is None:
        _evaluator_instance = AIEvaluator()
    return _evaluator_instance
