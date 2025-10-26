import csv
import random
from faker import Faker

fake = Faker("en_US")

num_records = 1000
output_file = "fake_leads.csv"

states = ["FL", "TX", "NY", "NJ", "MA", "CT"]
interests = [
    "Kitchen Remodel",
    "Bathroom Upgrade",
    "Roofing",
    "Windows Replacement",
    "Flooring",
    "Painting"
]

def generate_us_phone():
    """Generate a valid-format U.S. phone number (XXX) XXX-XXXX."""
    area = random.randint(200, 999)   # area code can’t start with 0/1
    exchange = random.randint(200, 999)
    subscriber = random.randint(1000, 9999)
    return f"({area}) {exchange}-{subscriber}"

# ---- GENERATE CSV ----
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["FullName", "Phone", "State", "Interest", "Email"])

    for _ in range(num_records):
        name = fake.name()
        phone = generate_us_phone()
        state = random.choice(states)
        interest = random.choice(interests)
        email = fake.email()
        writer.writerow([name, phone, state, interest, email])


print(f"Generated {num_records} fake leads and saved to '{output_file}'")
