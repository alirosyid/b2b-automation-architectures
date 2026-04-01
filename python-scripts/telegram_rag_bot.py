import os
from dotenv import load_dotenv
import google.generativeai as genai
from telegram.ext import Application, MessageHandler, filters

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

with open("knowledge_base.txt", "r", encoding="utf-8") as f:
    COMPANY_DOC = f.read()

async def handle_message(update, context):
    prompt = f"""You are an elite B2B Customer Support AI for Elevate Automation Solutions.
   Your tone must be highly professional, polite, and concise.
   Answer the user's question STRICTLY based on the following company document.
   If the answer is NOT explicitly written in the document, you MUST say: "I apologize, but I don't have that information. Please reach out to our team at human-support@elevateautomation.com."
   DO NOT hallucinate. DO NOT invent prices or policies.
   
   Company Document:
   {COMPANY_DOC}
   
   User Question: {update.message.text}
   """
    
    response = model.generate_content(prompt)
    await update.message.reply_text(response.text)

if __name__ == "__main__":
    application = Application.builder().token(os.environ.get("TELEGRAM_TOKEN")).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()
