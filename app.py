def get_knowledge(query):
    file = open("knowledge_base.txt", "r")
    data = file.read().lower()

    if "python" in query.lower():
        return "Python is a programming language used for AI and development."
    
    elif "machine learning" in query.lower():
        return "Machine learning means learning from data."
    
    elif "photosynthesis" in query.lower():
        return "Photosynthesis is how plants make food using sunlight."
    
    else:
        return "No trusted knowledge found. Using general AI response."
