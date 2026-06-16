document.addEventListener('DOMContentLoaded', () => {
    const difficultySelect = document.getElementById('difficulty');
    const loadBtn = document.getElementById('load-question-btn');
    const questionText = document.getElementById('question-text');
    const answerInput = document.getElementById('user-answer');
    const submitBtn = document.getElementById('submit-btn');
    const loader = document.getElementById('loader');
    const resultsPanel = document.getElementById('results-panel');

    let currentQuestions = [];
    let currentQuestionIndex = -1;

    async function loadQuestions() {
        const difficulty = difficultySelect.value;
        try {
            loadBtn.textContent = 'Loading...';
            loadBtn.disabled = true;
            
            const response = await fetch(`/questions/${difficulty}`);
            const data = await response.json();
            
            if (data.questions && data.questions.length > 0) {
                currentQuestions = data.questions;
                pickRandomQuestion();
            } else {
                questionText.textContent = "No questions available for this difficulty level. (Please add data to data.py)";
                answerInput.disabled = true;
                submitBtn.disabled = true;
            }
        } catch (error) {
            console.error(error);
            questionText.textContent = "Error loading questions.";
        } finally {
            loadBtn.textContent = 'Load Random Question';
            loadBtn.disabled = false;
        }
    }

    function pickRandomQuestion() {
        if (currentQuestions.length === 0) return;
        const randomIndex = Math.floor(Math.random() * currentQuestions.length);
        const selected = currentQuestions[randomIndex];
        currentQuestionIndex = selected.index;
        questionText.textContent = selected.question;
        
        answerInput.value = '';
        answerInput.disabled = false;
        submitBtn.disabled = true;
        resultsPanel.classList.add('hidden');
    }

    answerInput.addEventListener('input', () => {
        submitBtn.disabled = answerInput.value.trim().length === 0;
    });

    loadBtn.addEventListener('click', loadQuestions);

    submitBtn.addEventListener('click', async () => {
        if (currentQuestionIndex === -1) return;
        
        const answer = answerInput.value.trim();
        if (!answer) return;

        // UI updates
        submitBtn.disabled = true;
        answerInput.disabled = true;
        resultsPanel.classList.add('hidden');
        loader.classList.remove('hidden');

        try {
            const response = await fetch('/evaluate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    difficulty: difficultySelect.value,
                    question_index: currentQuestionIndex,
                    user_answer: answer
                })
            });

            if (!response.ok) {
                throw new Error("Failed to evaluate");
            }

            const data = await response.json();
            displayResults(data.evaluation_results);
            
        } catch (error) {
            console.error(error);
            alert("An error occurred during evaluation. The backend might still be loading the AI models (this can take a minute). Check terminal logs.");
        } finally {
            loader.classList.add('hidden');
            answerInput.disabled = false;
            submitBtn.disabled = false;
        }
    });

    function displayResults(results) {
        animateValue('final-score', results.final_score);
        animateValue('semantic-score', results.semantic_score);
        animateValue('grammar-score', results.grammar_score);
        animateValue('fluency-score', results.fluency_score);
        animateValue('keyword-score', results.keyword_score);
        
        document.getElementById('corrected-text').textContent = results.corrected_text || "No correction needed.";
        
        resultsPanel.classList.remove('hidden');
        resultsPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function animateValue(id, target) {
        const obj = document.getElementById(id);
        const duration = 1500;
        const start = 0;
        const end = parseFloat(target);
        if(isNaN(end)) return;
        
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            
            // easeOutQuart
            const easeProgress = 1 - Math.pow(1 - progress, 4);
            obj.innerHTML = (easeProgress * end).toFixed(1) + '<span style="font-size: 0.5em; color: var(--text-muted)">/100</span>';
            
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }
});
