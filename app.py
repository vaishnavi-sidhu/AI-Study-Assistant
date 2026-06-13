from flask import Flask, render_template, request

app = Flask(__name__)

def get_knowledge(query):
    query = query.lower()

    with open("knowledge_base.txt", "r") as file:
        data = file.read().lower()

    if "python" in query:
        return "Python is a programming language used for AI and development."

    elif "machine learning" in query:
        return "Machine learning means learning from data."

    elif "photosynthesis" in query:
        return "Photosynthesis is how plants make food using sunlight."

    else:
        return "No trusted knowledge found in Foundry IQ layer. Using AI fallback response."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["message"]

    context = get_knowledge(user_input)

    final_prompt = f"""
You are an AI Study Assistant.

Use this trusted knowledge first:
{context}

Now answer the question clearly and simply:
{user_input}
"""

    response = f"""
🤖 AI Response:

{final_prompt}

(Source: Foundry IQ Knowledge Layer - Simulated)
"""

    return render_template("index.html", answer=response)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(debug=True)
