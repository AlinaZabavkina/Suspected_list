import random
from faker import Faker
from faker.providers import phone_number
fake = Faker()
fake.add_provider(phone_number)
pnumbers = [fake.phone_number() for i in range(60)]
calls = [ {"caller": random.choice(pnumbers), "recipient": random.choice(pnumbers), "duration_s": random.randint(5, 600)} for i in range(1500) ]

suspects = random.choices(pnumbers,k=10)
print(suspects)

with open("numbers.txt", "w+") as file:
    file.writelines([f'{str(number)}\n' for number in pnumbers])

with open("suspects.txt", "w+") as file:
    file.writelines([f'{str(number)}\n' for number in suspects])

with open("calls.txt", "w+") as file:
        file.writelines([f'caller:{call.get("caller")}|recipient:{call.get("recipient")}|duration_s:{call.get("duration_s")}\n' for call in calls])