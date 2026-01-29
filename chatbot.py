import subprocess

chat_history = []

SYSTEM_PROMPT = """
You are a professional AI customer support assistant for a business.

Tone rules:
- Friendly
- Clear
- Professional
- Business-ready
- Sales-focused
- Confident

Your goals:
- Answer customer questions clearly
- Explain services in a simple business tone
- Encourage demos, trials, or lead signups
- Sound human, polite, and trustworthy
- Keep replies short, helpful, and persuasive

Always:
- Be polite
- Offer next steps
- Encourage contact or demo when relevant
"""

print("\n===================================")
print("🤖 Customer Support AI Bot Running")
print("Ask about pricing, demos, services, or support.")
print("Type 'exit' to quit.")
print("===================================\n")


while True:
    user_input = input("Customer: ")

    if user_input.lower() == "exit":
        print("Exiting chatbot...")
        break

    chat_history.append(f"Customer: {user_input}")
    memory_context = "\n".join(chat_history[-6:])

    prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{memory_context}

Customer: {user_input}
Support Agent Reply:
"""

    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )

    bot_reply = result.stdout.strip()

    chat_history.append(f"Support Agent: {bot_reply}")

    print("Bot:", bot_reply)
