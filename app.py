import os
from flask import Flask, request, jsonify, render_template
import anthropic

app = Flask(__name__)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """Tu ek friendly AI Study Assistant hai.
Tera kaam hai students ko concepts easy language mein samjhana.

Rules:
- Hamesha simple, short sentences use kar
- Real life examples de (jaise cricket, movies, roz ki zindagi)
- Pehle 1 line mein simple definition, phir example, phir thoda detail
- Hinglish mein baat kar — jaise koi dost samjhata ho
- Fun rakho!"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}]
    )
    return jsonify({"reply": response.content[0].text})

if __name__ == "__main__":
    app.run(debug=True)
