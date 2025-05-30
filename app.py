from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Set your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("⚠️ WARNING: Using hardcoded API key. It's recommended to set it via environment variable.")
    api_key = "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"

openai.api_key = api_key

# GPT system prompt
base_prompt = "You are a legal assistant. Answer queries accurately and concisely."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message", "").strip()

        if not user_message:
            return jsonify({"response": "Please enter a valid message."})

        # Simple greeting handler
        if "hello" in user_message.lower() or "hi" in user_message.lower():
            return jsonify({"response": "Hello! Welcome to Legal Assistant. What can I help you with today?"})

        # GPT response (updated for openai>=1.0.0)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": base_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content.strip()
        return jsonify({"response": reply})

    except Exception as e:
        print("❌ Error:", str(e))  # Log the actual error
        return jsonify({"response": "Sorry, there was an error. Please try again."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
