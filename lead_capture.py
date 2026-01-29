import csv

print("\n====================================")
print("🚀 AI Lead Capture System")
print("Powered by AI Automation Agency")
print("Please enter lead details below.")
print("Type 'exit' anytime to stop.")
print("====================================\n")

file_name = "leads.csv"

# Create CSV file with headers if not exists
try:
    with open(file_name, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Phone", "Business"])
except FileExistsError:
    pass

while True:
    name = input("👤 Full Name: ")
    if name.lower() == "exit":
        print("\n🛑 Lead capture stopped. Have a great day!")
        break

    email = input("📧 Email Address: ")
    phone = input("📱 Phone Number: ")
    business = input("🏢 Business Type: ")

    # Save to CSV inside the loop
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, email, phone, business])

    print("✅ Lead saved successfully!\n— Powered by AI Automation Agency")
    print("🙏 Thank you! Our team will contact you shortly.\n")
