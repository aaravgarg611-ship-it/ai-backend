from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os

app = Flask(__name__)
CORS(app)

client = Groq(api_key= os.getenv"GROQ_API_KEY"))

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        user_question = data.get("message", "")

        if not user_question:
            return jsonify({"answer": "Please ask something."})

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a smart, helpful AI assistant."},
                {"role": "user", "content": user_question}
            ]
        )

        return jsonify({"answer": completion.choices[0].message.content})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"answer": "Server error. Check backend console."})

if __name__ == "__main__":
    app.run(debug=True)
