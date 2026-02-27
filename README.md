# 📺 Telegram YouTube Summarizer

An AI-powered Telegram bot that:
- Accepts YouTube links
- Extracts video transcripts
- Generates structured summaries
- Supports Hindi translation
- Allows contextual Q&A based on video content

Built using Python, async architecture, and AI integration.

---

## 🚀 Features

🎥 Accepts YouTube video links  
📄 Automatically fetches transcripts  
🧠 Generates structured summaries  
🌍 Supports Hindi summaries  
💬 Allows follow-up questions based on video content  
⚡ Async-based Telegram bot  
🔒 Session-based user memory  

---

## 🏗️ System Architecture

### Workflow

1. User sends a YouTube link to the bot
2. Bot extracts the video ID
3. Transcript is fetched using YouTube Transcript API / yt-dlp
4. Transcript is stored in user session (in-memory)
5. AI generates structured summary
6. User can:
   - Request Hindi summary
   - Ask contextual questions

### Architecture Flow
```bash
User
↓
Telegram Bot
↓
Transcript Extraction Module
↓
AI Summary / Q&A Engine
↓
Response to User
```


---

## 🛠️ Tech Stack

- Python 3.x
- python-telegram-bot (v20+)
- YouTube Transcript API
- yt-dlp
- OpenAI/Groq LLM (for summary generation)
- Async programming (ApplicationBuilder)
- Environment variable management (.env)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Rakshanayak24/telegram-youtube-summarizer-bot.git
cd telegram-youtube-summarizer-bot

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```
Activate:
Windows
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a .env file in root directory:
```bash
BOT_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
```
⚠️ Never hardcode tokens inside code.

### 5️⃣ Run the Bot
```bash
python app.py
```
You should see:
🚀 Bot is running...

💬 How to Use the Bot
Step 1 — Send YouTube Link

Example:
https://youtube.com/watch?v=XXXXXXXXXXX

Bot Response:

- Structured Summary
- Key Points
- Important Timestamps
- Core Takeaway

## Attached screenshots 
![alt text](<Screenshot 2026-02-26 203320.png>)

