import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

from utils import extract_video_id
from transcript import get_transcript
from openclaw_client import generate_summary

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Store user transcripts (optional)
user_sessions = {}

# ==============================
# Handle Messages
# ==============================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.text:
        return

    text = update.message.text.strip()
    user_id = update.effective_user.id

    video_id = extract_video_id(text)

    # --------------------------
    # If user sends YouTube link
    # --------------------------
    if video_id:

        await update.message.reply_text("Fetching transcript... ⏳")

        transcript = get_transcript(text)

        if not transcript:
            await update.message.reply_text("❌ No transcript available for this video.")
            return

        user_sessions[user_id] = transcript

        await update.message.reply_text("Generating summary... 🧠")

        summary = generate_summary(transcript, "English")

        # Telegram message limit protection
        if len(summary) > 4000:
            summary = summary[:4000] + "\n\n...(truncated)"

        await update.message.reply_text(summary)
        return

    # --------------------------
    # Any other message
    # --------------------------
    await update.message.reply_text("Please send a YouTube link first.")


# ==============================
# Start Bot
# ==============================

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
