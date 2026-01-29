print("\n====================================")
print("💬 AI Auto-Reply Bot")
print("Simulating Instagram / WhatsApp Automation")
print("🚀 Powered by AI Automation Agency")
print("Type a customer message. Type 'exit' to stop.")
print("====================================\n")

auto_replies = {
    "price": "Our plans start at ₹999/month. Would you like a personalized demo?",
    "cost": "We offer affordable automation plans. Shall I send pricing details?",
    "hours": "We provide 24/7 AI-powered customer support to help grow your business.",
    "services": "We automate customer replies, lead capture, and sales to save time and increase revenue.",
    "contact": "Please share your WhatsApp number and our team will contact you shortly.",
    "demo": "We’d love to schedule a demo for you. When would you like to see it?",
    "trial": "We offer a free trial so you can experience our automation risk-free.",
    "business": "We help businesses generate more leads and automate customer engagement.",
    "support": "Our support team is available 24/7. How can we assist you today?"
}

default_reply = (
    "Thank you for contacting AI Automation Agency! "
    "Our team will respond shortly. Would you like a free demo?"
)

while True:
    msg = input("👤 Customer: ").strip()

    if msg.lower() == "exit":
        print("\n🛑 Auto-Reply Bot stopped. Thank you!")
        break

    reply = default_reply

    for keyword in auto_replies:
        if keyword in msg.lower():
            reply = auto_replies[keyword]
            break

    print("\n🤖 Bot Reply:", reply)
    print("— Powered by AI Automation Agency\n")
