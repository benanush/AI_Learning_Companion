from PIL import Image, ImageDraw

# Paste the BIG questions dictionary here
questions = {
    1: [
        "Artificial Intelligence is the simulation of human intelligence in machines.",
        "AI enables computers to perform tasks that require human intelligence.",
        "Artificial Intelligence helps machines learn and make decisions.",
        "AI is a branch of computer science focused on intelligent systems.",
        "Artificial Intelligence allows computers to solve complex problems.",
        "AI uses algorithms to mimic human thinking processes.",
        "Artificial Intelligence enables automation of intelligent tasks.",
        "AI systems can reason, learn and adapt to new situations.",
        "Artificial Intelligence powers modern technologies like chatbots.",
        "AI helps machines analyze data and make predictions.",
        "Artificial Intelligence improves decision making using data.",
        "AI is used in healthcare, finance and education.",
        "Artificial Intelligence simulates cognitive functions of humans.",
        "AI enables smart systems that can learn continuously.",
        "Artificial Intelligence combines data, algorithms and computing power.",
        "AI helps automate tasks traditionally performed by humans.",
        "Artificial Intelligence allows machines to recognize patterns.",
        "AI systems can process information intelligently.",
        "Artificial Intelligence drives innovation in many industries.",
        "AI makes computers capable of learning from experience."
    ],

    2: [
        "Machine Learning is a subset of AI that learns from data.",
        "ML enables computers to improve without explicit programming.",
        "Machine Learning finds patterns in large datasets.",
        "ML uses algorithms to make predictions.",
        "Machine Learning improves performance through experience.",
        "ML trains models using historical data.",
        "Machine Learning helps automate decision making.",
        "ML is widely used in recommendation systems.",
        "Machine Learning identifies trends in data.",
        "ML enables predictive analytics.",
        "Machine Learning supports fraud detection systems.",
        "ML learns relationships between variables.",
        "Machine Learning uses training and testing datasets.",
        "ML powers image recognition applications.",
        "Machine Learning can classify and cluster data.",
        "ML helps systems adapt to new information.",
        "Machine Learning uses statistical techniques.",
        "ML is important in data science.",
        "Machine Learning improves accuracy over time.",
        "ML is applied in healthcare and finance."
    ],

    3: [
        "NLP enables computers to understand human language.",
        "Natural Language Processing deals with text analysis.",
        "NLP helps machines interpret spoken language.",
        "Natural Language Processing combines AI and linguistics.",
        "NLP powers chatbots and virtual assistants.",
        "Natural Language Processing supports translation systems.",
        "NLP helps computers process text documents.",
        "Natural Language Processing extracts meaning from language.",
        "NLP is used in sentiment analysis.",
        "Natural Language Processing enables speech recognition.",
        "NLP helps machines generate human-like text.",
        "Natural Language Processing supports question answering systems.",
        "NLP analyzes grammar and sentence structure.",
        "Natural Language Processing improves communication with machines.",
        "NLP is widely used in customer support.",
        "Natural Language Processing identifies keywords in text.",
        "NLP enables automatic summarization.",
        "Natural Language Processing processes textual data efficiently.",
        "NLP supports language translation applications.",
        "Natural Language Processing helps computers understand context."
    ],

    4: [
        "Deep Learning uses neural networks with multiple layers.",
        "Deep Learning is a subset of Machine Learning.",
        "Deep Learning learns complex patterns from data.",
        "Deep Learning powers image recognition systems.",
        "Deep Learning uses artificial neural networks.",
        "Deep Learning processes large volumes of data.",
        "Deep Learning is inspired by the human brain.",
        "Deep Learning supports speech recognition applications.",
        "Deep Learning improves computer vision systems.",
        "Deep Learning automatically extracts features.",
        "Deep Learning performs well on unstructured data.",
        "Deep Learning enables autonomous vehicles.",
        "Deep Learning is widely used in AI applications.",
        "Deep Learning trains deep neural networks.",
        "Deep Learning helps solve complex prediction tasks.",
        "Deep Learning uses backpropagation for training.",
        "Deep Learning powers modern recommendation systems.",
        "Deep Learning supports natural language processing.",
        "Deep Learning requires significant computational resources.",
        "Deep Learning achieves high accuracy in many tasks."
    ],

    5: [
        "Transformers use self-attention mechanisms.",
        "Transformers are widely used in NLP applications.",
        "Transformers process sequences in parallel.",
        "Transformers form the basis of GPT models.",
        "Transformers improve language understanding.",
        "Transformers capture long-range dependencies in text.",
        "Transformers outperform traditional RNN models.",
        "Transformers are used in machine translation.",
        "Transformers enable efficient training of language models.",
        "Transformers support text generation tasks.",
        "Transformers use encoder and decoder architectures.",
        "Transformers power modern AI assistants.",
        "Transformers are used in BERT and GPT.",
        "Transformers handle contextual information effectively.",
        "Transformers rely on attention rather than recurrence.",
        "Transformers are effective for sequence modeling.",
        "Transformers enable large language models.",
        "Transformers improve NLP performance significantly.",
        "Transformers support summarization and translation.",
        "Transformers are the foundation of Generative AI."
    ]
}

# 20 students × 5 questions = 100 JPG files

for student in range(1, 21):

    for q in range(1, 6):

        img = Image.new("RGB", (1000, 500), "white")

        draw = ImageDraw.Draw(img)

        # Unique answer for each student
        answer = questions[q][student - 1]

        text = f"""
Student {student}

Question {q}

{answer}
"""

        draw.text(
            (50, 50),
            text,
            fill="black"
        )

        img.save(
            f"student_{student}_q{q}.jpg"
        )

print("100 JPG files created successfully!")