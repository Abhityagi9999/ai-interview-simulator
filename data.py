# data.py
# Contains the QA dataset for the AI Interview Simulator.

qa_data = {
    "easy": [
        {
            "question": "What is reinforcement learning?",
            "answers": [
                "Reinforcement learning is a type of ML where agents learn by rewards and penalties.",
                "The agent interacts with the environment to achieve a goal.",
                "It is used in robotics, games, and self-driving cars.",
                "Actions are chosen based on maximizing cumulative reward.",
                "It learns through trial and error.",
                "The agent improves over time by learning optimal policies.",
                "Q-learning is a popular reinforcement learning algorithm.",
                "It differs from supervised learning as it uses feedback instead of labels."
            ],
            "keywords": ["reinforcement learning", "agent", "environment", "reward", "policy"]
        },
        {
            "question": "What is a neural network?",
            "answers": [
                "A neural network is a computing system inspired by the human brain.",
                "It consists of layers of interconnected nodes called neurons.",
                "Neural networks are used for pattern recognition.",
                "They are the foundation of deep learning.",
                "Neurons apply weights to inputs and pass through activation functions.",
                "Networks are trained using backpropagation.",
                "They can model complex non-linear relationships.",
                "Applications include image recognition, NLP, and autonomous systems."
            ],
            "keywords": ["neural network", "neurons", "layers", "deep learning", "activation"]
        },
        {
            "question": "What is a convolutional neural network (CNN)?",
            "answers": [
                "CNNs are neural networks specialized for image data.",
                "They use convolutional layers to extract features.",
                "Pooling layers reduce dimensionality.",
                "CNNs are used in image classification and object detection.",
                "They can recognize patterns regardless of location in images.",
                "They are widely used in computer vision tasks.",
                "CNNs are composed of convolution, pooling, and fully connected layers.",
                "They require large datasets to achieve high accuracy."
            ],
            "keywords": ["CNN", "convolution", "image", "pooling", "feature extraction"]
        },
        {
            "question": "What is a recurrent neural network (RNN)?",
            "answers": [
                "RNNs are neural networks designed for sequential data.",
                "They maintain memory of previous inputs through hidden states.",
                "RNNs are used in NLP, speech recognition, and time series prediction.",
                "They can model temporal dependencies.",
                "Variants include LSTM and GRU to address vanishing gradient issues.",
                "They are effective for language modeling tasks.",
                "RNNs process data step by step in sequences.",
                "Training RNNs can be computationally challenging."
            ],
            "keywords": ["RNN", "sequence", "hidden state", "LSTM", "GRU"]
        },
        {
            "question": "What is an embedding in NLP?",
            "answers": [
                "An embedding is a vector representation of words or phrases.",
                "It captures semantic meaning and similarity.",
                "Word2Vec and GloVe are common embedding models.",
                "Embeddings allow machines to process textual data numerically.",
                "They reduce dimensionality of vocabulary space.",
                "Embeddings are used in search, recommendation, and translation.",
                "Contextual embeddings like BERT improve representation accuracy.",
                "They help NLP models understand word relationships."
            ],
            "keywords": ["embedding", "vector", "NLP", "semantic", "BERT"]
        },
        {
            "question": "What is a chatbot?",
            "answers": [
                "A chatbot is an AI system that interacts with users via text or voice.",
                "It can answer questions and provide assistance.",
                "Chatbots are used in customer support and virtual assistants.",
                "Rule-based chatbots follow predefined scripts.",
                "AI chatbots use NLP and machine learning.",
                "They can understand and respond to human language.",
                "Advanced chatbots maintain context in conversations.",
                "Chatbots reduce workload and improve response time."
            ],
            "keywords": ["chatbot", "AI", "conversation", "NLP", "virtual assistant"]
        },
        {
            "question": "What is text classification?",
            "answers": [
                "Text classification assigns categories to text data.",
                "It is used in spam detection and sentiment analysis.",
                "Machine learning models can be trained for classification.",
                "Deep learning techniques improve accuracy for large datasets.",
                "It transforms text into numerical features before classification.",
                "Supervised learning is commonly used.",
                "It helps organize and filter large volumes of text.",
                "Applications include topic labeling and email filtering."
            ],
            "keywords": ["text classification", "NLP", "spam detection", "sentiment analysis", "supervised learning"]
        },
        {
            "question": "What is sentiment analysis?",
            "answers": [
                "Sentiment analysis identifies emotions in text.",
                "It can classify opinions as positive, negative, or neutral.",
                "Used in social media monitoring and customer feedback.",
                "NLP models process and analyze textual sentiment.",
                "Machine learning improves prediction accuracy.",
                "It helps businesses understand customer feelings.",
                "Deep learning models like LSTM are effective for this task.",
                "It is also called opinion mining."
            ],
            "keywords": ["sentiment analysis", "NLP", "emotion", "text", "opinion mining"]
        },
        {
            "question": "What is a generative model?",
            "answers": [
                "A generative model generates new data similar to training data.",
                "It learns the distribution of input data.",
                "Examples include GANs and Variational Autoencoders.",
                "Used in image generation, text generation, and music synthesis.",
                "They can create realistic artificial data.",
                "Generative models are used for data augmentation.",
                "They learn complex patterns and representations.",
                "Training can be challenging due to instability."
            ],
            "keywords": ["generative model", "GAN", "VAE", "data generation", "distribution"]
        },
        {
            "question": "What is overfitting prevention?",
            "answers": [
                "Overfitting prevention ensures models generalize well to new data.",
                "Techniques include regularization, dropout, and early stopping.",
                "Using more data helps reduce overfitting.",
                "Simplifying model complexity can prevent overfitting.",
                "Cross-validation is used to monitor overfitting.",
                "Overfitting occurs when a model memorizes training data.",
                "Prevention improves model performance on unseen data.",
                "It is crucial for reliable AI systems."
            ],
            "keywords": ["overfitting", "regularization", "dropout", "early stopping", "generalization"]
        },
        {
            "question": "What is a feature in machine learning?",
            "answers": [
                "A feature is an individual measurable property of data.",
                "Features are used as input for ML models.",
                "Choosing relevant features improves model performance.",
                "Feature engineering creates new meaningful features.",
                "Normalization helps in scaling features.",
                "Features can be numeric, categorical, or text-based.",
                "Feature selection reduces dimensionality and overfitting.",
                "Features are essential for model learning."
            ],
            "keywords": ["feature", "data", "input", "feature engineering", "ML"]
        },
        {
            "question": "What is a label in machine learning?",
            "answers": [
                "A label is the output or target in supervised learning.",
                "Models learn to predict labels from input features.",
                "Examples include spam/not-spam or price prediction.",
                "Labels are essential for training accurate models.",
                "Unlabeled data is used in unsupervised learning.",
                "Correct labeling improves model reliability.",
                "Label quality impacts the model's performance.",
                "They guide the model's learning process."
            ],
            "keywords": ["label", "supervised learning", "target", "output", "training"]
        },
        {
            "question": "What is feature scaling?",
            "answers": [
                "Feature scaling normalizes input data for ML models.",
                "It ensures features contribute equally to the model.",
                "Common techniques include min-max scaling and standardization.",
                "Scaling prevents features with large values from dominating.",
                "It improves convergence in gradient-based algorithms.",
                "It is important for distance-based models like KNN.",
                "Scaling is applied to numeric features.",
                "It enhances model accuracy and stability."
            ],
            "keywords": ["feature scaling", "normalization", "standardization", "ML", "input data"]
        },
        {
            "question": "What is cross-validation?",
            "answers": [
                "Cross-validation evaluates model performance on unseen data.",
                "It splits data into multiple training and validation sets.",
                "K-fold is a popular cross-validation method.",
                "It helps prevent overfitting.",
                "Cross-validation ensures model generalization.",
                "It is used to tune hyperparameters.",
                "It provides a more reliable estimate of model performance.",
                "It is essential for model selection."
            ],
            "keywords": ["cross-validation", "training", "validation", "overfitting", "model evaluation"]
        },
        {
            "question": "What is a hyperparameter?",
            "answers": [
                "Hyperparameters are parameters set before training a model.",
                "They control model behavior and learning process.",
                "Examples include learning rate, number of layers, and batch size.",
                "Hyperparameters are tuned for optimal performance.",
                "They differ from model parameters, which are learned.",
                "Grid search and random search are used for tuning.",
                "Choosing proper hyperparameters improves accuracy.",
                "Hyperparameters influence convergence speed and stability."
            ],
            "keywords": ["hyperparameter", "learning rate", "batch size", "model tuning", "parameters"]
        },
        {
            "question": "What is batch size in machine learning?",
            "answers": [
                "Batch size is the number of samples processed before updating the model.",
                "Smaller batches provide noisy updates but may generalize better.",
                "Larger batches are more stable but require more memory.",
                "Batch size affects training speed and convergence.",
                "It is a key hyperparameter in deep learning.",
                "Mini-batch gradient descent is widely used.",
                "Proper batch size improves efficiency and accuracy.",
                "It balances computation and model performance."
            ],
            "keywords": ["batch size", "training", "gradient descent", "deep learning", "hyperparameter"]
        },
        {
            "question": "What is early stopping?",
            "answers": [
                "Early stopping halts training when validation performance stops improving.",
                "It prevents overfitting by not over-training the model.",
                "Monitors loss or accuracy on validation set.",
                "Common in deep learning for efficient training.",
                "Improves model generalization.",
                "Training stops automatically based on patience parameter.",
                "It saves computation time.",
                "It ensures best model selection during training."
            ],
            "keywords": ["early stopping", "training", "overfitting", "validation", "deep learning"]
        },
        {
            "question": "What is dimensionality reduction?",
            "answers": [
                "Dimensionality reduction reduces the number of features in data.",
                "It simplifies models and improves performance.",
                "PCA and t-SNE are common techniques.",
                "Reduces computation cost and overfitting.",
                "Helps visualize high-dimensional data.",
                "It captures important information while discarding noise.",
                "Used in preprocessing for ML tasks.",
                "It improves model interpretability and speed."
            ],
            "keywords": ["dimensionality reduction", "PCA", "t-SNE", "features", "ML"]
        },
        {
            "question": "What is a confusion matrix?",
            "answers": [
                "A confusion matrix evaluates classification model performance.",
                "It shows true positives, true negatives, false positives, and false negatives.",
                "Helps compute metrics like accuracy, precision, and recall.",
                "Used to visualize model predictions vs actual labels.",
                "It identifies where the model is making errors.",
                "Essential in multi-class classification analysis.",
                "Supports model debugging and improvement.",
                "Provides insights beyond simple accuracy."
            ],
            "keywords": ["confusion matrix", "classification", "accuracy", "precision", "recall"]
        }
    ],
    "medium": [
        {
            "question": "What is a chatbot?",
            "answers": [
                "A chatbot is an AI system that interacts with users via text or speech.",
                "It can answer questions, provide information, or perform tasks.",
                "Chatbots are used in customer support, virtual assistants, and e-commerce.",
                "They use NLP to understand user inputs and generate responses.",
                "Chatbots can be rule-based or AI-powered.",
                "AI chatbots learn from conversations to improve over time.",
                "They are widely used in apps like Messenger, WhatsApp, and websites.",
                "Simply, a chatbot is a computer program designed to have conversations with humans."
            ],
            "keywords": ["chatbot", "ai", "nlp", "virtual assistant", "conversation", "customer support"]
        },
        {
            "question": "What is an algorithm?",
            "answers": [
                "An algorithm is a step-by-step procedure to solve a problem.",
                "It is a set of instructions that a computer follows.",
                "Algorithms are used in programming, AI, and data processing.",
                "They can be simple, like addition, or complex, like sorting data.",
                "Efficiency and correctness are important characteristics of algorithms.",
                "AI models rely on algorithms for decision making.",
                "Algorithms can be implemented in various programming languages.",
                "In short, an algorithm tells the computer how to solve a problem systematically."
            ],
            "keywords": ["algorithm", "steps", "instructions", "problem-solving", "programming", "ai"]
        },
        {
            "question": "What is a dataset?",
            "answers": [
                "A dataset is a collection of structured or unstructured data.",
                "It is used to train or evaluate AI and machine learning models.",
                "Datasets can include images, text, audio, or numerical data.",
                "Proper dataset preparation ensures model accuracy.",
                "It can be labeled or unlabeled depending on the task.",
                "Datasets are split into training, validation, and testing sets.",
                "Large datasets help improve machine learning performance.",
                "Simply, a dataset is the information used by machines to learn and make decisions."
            ],
            "keywords": ["dataset", "data", "training", "testing", "labels", "ml", "ai"]
        },
        {
            "question": "What is transfer learning in AI?",
            "answers": [
                "Transfer learning reuses a pre-trained model on a new related task.",
                "Reduces training time and required data.",
                "Commonly used in computer vision and NLP.",
                "Helps improve performance for tasks with limited labeled data.",
                "Techniques include fine-tuning and feature extraction.",
                "Pre-trained models like BERT, ResNet are often used.",
                "Can be applied across different domains if tasks are related.",
                "Improves model generalization and efficiency."
            ],
            "keywords": ["transfer learning", "pre-trained model", "fine-tuning", "feature extraction", "domain adaptation"]
        },
        {
            "question": "What is an activation function?",
            "answers": [
                "An activation function introduces non-linearity to a neural network.",
                "It decides whether a neuron should be activated or not.",
                "Common activation functions include ReLU, Sigmoid, and Tanh.",
                "They help neural networks learn complex patterns in data.",
                "Activation functions affect convergence speed and model performance.",
                "Without them, networks would behave like linear models.",
                "Choosing the right activation function is critical for training deep networks.",
                "In short, it determines how neurons respond to input signals."
            ],
            "keywords": ["activation function", "relu", "sigmoid", "tanh", "non-linearity", "neural network"]
        },
        {
            "question": "What is backpropagation in neural networks?",
            "answers": [
                "Backpropagation is an algorithm for training neural networks.",
                "It calculates gradients of the loss function with respect to weights.",
                "Gradients are used to update weights via optimization methods like gradient descent.",
                "It propagates error backward from output to input layers.",
                "Backpropagation enables deep networks to learn complex patterns.",
                "It is essential for supervised learning in neural networks.",
                "Variants like stochastic and mini-batch backpropagation improve efficiency.",
                "Simply, backpropagation helps neural networks learn by adjusting weights based on errors."
            ],
            "keywords": ["backpropagation", "gradient", "loss", "weights", "neural network", "training"]
        },
        {
            "question": "What is attention mechanism in AI?",
            "answers": [
                "Attention allows models to focus on important parts of input data.",
                "Widely used in NLP for translation, summarization, and Q&A.",
                "Computes a weighted sum of input features based on relevance.",
                "Helps capture long-range dependencies in sequences.",
                "Forms the basis of Transformer models like BERT and GPT.",
                "Reduces information bottleneck in sequence models.",
                "Can be applied in vision tasks to highlight key regions.",
                "Improves interpretability by showing which input tokens were attended."
            ],
            "keywords": ["attention mechanism", "weighted sum", "Transformer", "sequence modeling", "interpretability"]
        },
        {
            "question": "What is overfitting in machine learning?",
            "answers": [
                "Overfitting occurs when a model learns training data too well.",
                "Model performs poorly on unseen test data.",
                "Common in complex models with small datasets.",
                "Techniques to reduce overfitting include regularization, dropout, and early stopping.",
                "Cross-validation helps detect overfitting.",
                "Simplifying the model can improve generalization.",
                "Data augmentation increases dataset diversity to prevent overfitting.",
                "Overfitting indicates model memorized noise instead of patterns."
            ],
            "keywords": ["overfitting", "generalization", "regularization", "dropout", "cross-validation"]
        },
        {
            "question": "What is gradient descent?",
            "answers": [
                "Gradient descent is an optimization algorithm for minimizing loss functions.",
                "Adjusts model parameters in the direction of negative gradient.",
                "Variants include SGD, mini-batch, and Adam optimizer.",
                "Used to train neural networks and other ML models.",
                "Learning rate controls the step size for updates.",
                "Helps reach local or global minima in parameter space.",
                "Can be combined with momentum to accelerate convergence.",
                "Crucial for backpropagation in deep learning."
            ],
            "keywords": ["gradient descent", "optimization", "learning rate", "SGD", "backpropagation"]
        },
        {
            "question": "What is natural language processing (NLP)?",
            "answers": [
                "NLP enables machines to understand, interpret, and generate human language.",
                "Applications include translation, sentiment analysis, and chatbots.",
                "Techniques include tokenization, stemming, and embeddings.",
                "Combines linguistics, computer science, and AI.",
                "Can process text and speech for diverse applications.",
                "Used in information retrieval and question answering.",
                "Recent models include transformers and large language models.",
                "Challenges include ambiguity, context, and idiomatic expressions."
            ],
            "keywords": ["NLP", "text processing", "language model", "tokenization", "transformer"]
        },
        {
            "question": "What is the difference between supervised and unsupervised learning?",
            "answers": [
                "Supervised learning uses labeled data for training.",
                "Unsupervised learning finds patterns in unlabeled data.",
                "Supervised methods include regression and classification.",
                "Unsupervised methods include clustering and dimensionality reduction.",
                "Supervised learning predicts outcomes for new data.",
                "Unsupervised learning explores data structure without explicit labels.",
                "Evaluation differs: supervised uses accuracy, unsupervised uses clustering metrics.",
                "Both are foundational techniques in machine learning."
            ],
            "keywords": ["supervised learning", "unsupervised learning", "classification", "clustering", "regression"]
        },
        {
            "question": "What is batch normalization?",
            "answers": [
                "Batch normalization normalizes inputs of each layer to improve training.",
                "It helps reduce internal covariate shift in deep networks.",
                "Batch norm allows using higher learning rates without instability.",
                "It can act as a regularizer and reduce overfitting.",
                "Normalization occurs across mini-batches during training.",
                "It accelerates convergence and improves performance.",
                "Batch normalization is widely used in CNNs and RNNs.",
                "Simply, batch normalization keeps neural network inputs balanced for faster and stable learning."
            ],
            "keywords": ["batch normalization", "normalization", "cnn", "rnn", "training", "stability"]
        },
        {
            "question": "What is dropout in neural networks?",
            "answers": [
                "Dropout randomly disables neurons during training.",
                "Prevents overfitting by reducing co-adaptation.",
                "Increases model generalization on unseen data.",
                "Applied in fully connected layers or convolution layers.",
                "Dropout rate controls probability of deactivation.",
                "Combines with other regularization techniques for better results.",
                "Disabled during evaluation for full model utilization.",
                "Widely used in deep learning architectures."
            ],
            "keywords": ["dropout", "regularization", "overfitting", "neural network", "generalization"]
        },
        {
            "question": "What is LSTM in deep learning?",
            "answers": [
                "LSTM is a type of RNN that handles long-term dependencies.",
                "Uses memory cells and gates to control information flow.",
                "Solves vanishing gradient problems in standard RNNs.",
                "Applied in sequence prediction, NLP, and time series analysis.",
                "Includes input, forget, and output gates.",
                "Captures temporal patterns efficiently.",
                "Can be stacked for deeper architectures.",
                "Used in translation, speech recognition, and text generation."
            ],
            "keywords": ["LSTM", "RNN", "memory cell", "sequence modeling", "temporal dependencies"]
        },
        {
            "question": "What is K-means clustering?",
            "answers": [
                "K-means groups data into K clusters based on similarity.",
                "Minimizes within-cluster variance.",
                "Used in unsupervised learning for pattern discovery.",
                "Centroids are updated iteratively until convergence.",
                "Requires predefining the number of clusters.",
                "Sensitive to initial centroids and outliers.",
                "Used in market segmentation, image compression, and anomaly detection.",
                "Simple and efficient for large datasets."
            ],
            "keywords": ["K-means", "clustering", "unsupervised learning", "centroid", "variance"]
        }
    ],
    "hard": [
        {
            "question": "Explain the Transformer architecture in detail.",
            "answers": [
                "The Transformer uses self-attention mechanisms instead of recurrence.",
                "It consists of an encoder-decoder structure with multi-head attention.",
                "Positional encodings provide sequence order information.",
                "Self-attention computes relationships between all tokens simultaneously.",
                "Multi-head attention allows attending to different representation subspaces.",
                "Feed-forward networks process attention outputs in each layer.",
                "Layer normalization and residual connections stabilize training.",
                "Transformers are the basis for BERT, GPT, and modern LLMs."
            ],
            "keywords": ["Transformer", "self-attention", "encoder-decoder", "multi-head attention", "positional encoding"]
        },
        {
            "question": "What is Generative Adversarial Network (GAN)?",
            "answers": [
                "GANs consist of a generator and discriminator trained adversarially.",
                "The generator creates fake data while the discriminator identifies real vs fake.",
                "Training is a minimax game between the two networks.",
                "GANs can generate realistic images, text, and audio.",
                "Mode collapse and training instability are common challenges.",
                "Variants include DCGAN, StyleGAN, and CycleGAN.",
                "Used in image synthesis, data augmentation, and super-resolution.",
                "Loss functions like Wasserstein loss improve training stability."
            ],
            "keywords": ["GAN", "generator", "discriminator", "adversarial training", "mode collapse"]
        },
        {
            "question": "What is BERT and how does it work?",
            "answers": [
                "BERT is a bidirectional transformer model for NLP tasks.",
                "It is pre-trained on masked language modeling and next sentence prediction.",
                "BERT reads text in both directions simultaneously.",
                "Fine-tuning BERT achieves state-of-the-art on many NLP benchmarks.",
                "It produces contextual word embeddings unlike static embeddings.",
                "BERT uses attention to capture relationships between all words.",
                "Variants include RoBERTa, ALBERT, and DistilBERT.",
                "It revolutionized transfer learning in NLP."
            ],
            "keywords": ["BERT", "bidirectional", "masked language model", "fine-tuning", "contextual embeddings"]
        },
        {
            "question": "Explain the concept of attention in deep learning.",
            "answers": [
                "Attention allows models to focus on relevant parts of the input.",
                "Scaled dot-product attention computes compatibility scores between queries and keys.",
                "Multi-head attention runs multiple attention functions in parallel.",
                "Self-attention relates different positions of a single sequence.",
                "Cross-attention relates positions across two different sequences.",
                "Attention weights provide interpretability of model decisions.",
                "It replaced recurrence as the primary mechanism in modern NLP.",
                "Efficient attention variants handle long sequences better."
            ],
            "keywords": ["attention", "query", "key", "value", "multi-head", "self-attention"]
        },
        {
            "question": "What is Reinforcement Learning from Human Feedback (RLHF)?",
            "answers": [
                "RLHF fine-tunes language models using human preference data.",
                "A reward model is trained on human comparisons of outputs.",
                "PPO (Proximal Policy Optimization) is commonly used for RL training.",
                "It aligns model behavior with human values and preferences.",
                "Used in ChatGPT and other conversational AI systems.",
                "Combines supervised fine-tuning with reinforcement learning.",
                "Reduces harmful and incorrect outputs from language models.",
                "Challenges include reward hacking and preference noise."
            ],
            "keywords": ["RLHF", "human feedback", "reward model", "PPO", "alignment"]
        }
    ],
    "advanced": [
        {
            "question": "Explain the mathematical formulation of the Transformer self-attention mechanism.",
            "answers": [
                "Self-attention computes Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) * V.",
                "Q, K, V are linear projections of the input embeddings.",
                "The scaling factor sqrt(d_k) prevents vanishing gradients in softmax.",
                "Multi-head attention concatenates h parallel attention outputs.",
                "Each head learns different representation subspaces.",
                "Positional encodings use sinusoidal functions to encode position.",
                "Computational complexity is O(n^2 * d) for sequence length n.",
                "Efficient variants like linear attention reduce this to O(n * d)."
            ],
            "keywords": ["self-attention", "softmax", "query", "key", "value", "multi-head", "complexity"]
        },
        {
            "question": "Compare and contrast different optimization algorithms for deep learning.",
            "answers": [
                "SGD updates weights using the gradient of a single sample or mini-batch.",
                "Adam combines momentum and adaptive learning rates per parameter.",
                "AdaGrad adapts learning rates based on historical gradient magnitudes.",
                "RMSProp uses exponential moving average of squared gradients.",
                "Learning rate scheduling (cosine, step) improves convergence.",
                "Weight decay acts as L2 regularization in Adam variants.",
                "Second-order methods like L-BFGS are expensive but converge faster.",
                "Choice of optimizer depends on model architecture and dataset characteristics."
            ],
            "keywords": ["SGD", "Adam", "AdaGrad", "RMSProp", "learning rate", "convergence", "optimization"]
        },
        {
            "question": "Explain Variational Autoencoders (VAEs) and their mathematical foundation.",
            "answers": [
                "VAEs learn a latent representation by maximizing the evidence lower bound (ELBO).",
                "The encoder maps input to a distribution in latent space (mean and variance).",
                "The reparameterization trick enables backpropagation through stochastic sampling.",
                "KL divergence regularizes the latent space toward a prior distribution.",
                "The decoder reconstructs input from sampled latent vectors.",
                "VAEs generate new data by sampling from the learned latent distribution.",
                "They balance reconstruction quality and latent space regularity.",
                "Applications include image generation, anomaly detection, and drug discovery."
            ],
            "keywords": ["VAE", "ELBO", "KL divergence", "reparameterization", "latent space", "generative model"]
        },
        {
            "question": "What are the key challenges in scaling Large Language Models (LLMs)?",
            "answers": [
                "Training requires massive compute with thousands of GPUs/TPUs.",
                "Memory constraints require techniques like model parallelism and gradient checkpointing.",
                "Data quality and deduplication significantly impact model performance.",
                "Mixture of Experts (MoE) enables scaling parameters without proportional compute.",
                "Emergent capabilities appear unpredictably at certain scale thresholds.",
                "Alignment and safety become harder to control as models scale.",
                "Inference optimization includes quantization, pruning, and distillation.",
                "Cost-performance tradeoffs drive architectural decisions like sparse attention."
            ],
            "keywords": ["LLM", "scaling", "model parallelism", "MoE", "quantization", "alignment"]
        }
    ]
}
