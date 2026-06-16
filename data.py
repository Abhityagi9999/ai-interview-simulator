# data.py
# Contains the QA dataset for the AI Interview Simulator.
# Note: Some data was truncated in the chat, please replace this with your complete qa_data dictionary.

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
                "Neurons apply weights to inputs and pass through activation functions."
            ],
            "keywords": ["neural network", "neurons", "layers", "deep learning", "activation"]
        }
        # ... Add your remaining easy questions here ...
    ],
    "medium": [
        {
            "question": "What is a chatbot?",
            "answers": [
                "A chatbot is an AI system that interacts with users via text or speech.",
                "It can answer questions, provide information, or perform tasks.",
                "Chatbots are used in customer support, virtual assistants, and e-commerce.",
                "They use NLP to understand user inputs and generate responses.",
                "Chatbots can be rule-based or AI-powered."
            ],
            "keywords": ["chatbot", "ai", "nlp", "virtual assistant", "conversation", "customer support"]
        }
        # ... Add your remaining medium questions here ...
    ],
    "hard": [
        # ... Add your hard questions here ...
    ],
    "advanced": [
        # ... Add your advanced questions here ...
    ]
}
