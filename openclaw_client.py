import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# IMPORTANT: Put GROQ_API_KEY in .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ==============================
# 🔹 SUMMARY FUNCTION
# ==============================

def generate_summary(transcript, language="English"):

    prompt = f"""
You are a professional AI research assistant.

Create a structured summary with:

🎥 Video Title
📌 5 Key Points
⏱ Important Timestamps
🧠 Core Takeaway

Language: {language}

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content


# ==============================
# 🔹 Q&A FUNCTION (STRICT)
# ==============================

def answer_question(transcript, question, language="English"):

    prompt = f"""
You are a strict transcript-based assistant.

Rules:
- Answer ONLY using the transcript.
- Do NOT invent information.
- If the answer is not clearly present, reply exactly:
"This topic is not covered in the video."

Language: {language}

Transcript:
{transcript}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
