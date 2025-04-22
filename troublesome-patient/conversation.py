import ollama
import random
from faker import Faker

# Choose a chat-capable model (ensured it is pulled)
#model_name = 'troublesome-patient:latest'
model_name = 'granite3.2:latest'
fake = Faker()

age = random.randrange(21,60)
level = random.choice(["minor","major","critical"])
intensity = random.choice(["low","medium","high"])
name = fake.name()
job = fake.job()
spirits = random.choice(["low","medium","high"])

# Initialize conversation with a system prompt (optional) and a user message
messages = [
    {"role": "user", "content": f"""
You are a patient based off of the following individuals:

Jimmy is 28 and a software programmer who has been feeling jittery and having trouble sleeping. He drinks around four energy drinks per day to stay focused during long coding sessions. He admits to skipping meals and relying on snacks and caffeine. Jimmy wants to feel more rested and manage his anxiety, but he's unsure how to stay productive without his usual routine.

Felix is 32 and a graphic designer who enjoys playing soccer and running on weekends. Lately, he's been experiencing a persistent cough and shortness of breath during exercise. He vapes socially, mostly in the evenings and on weekends. He doesn’t consider himself addicted and sees vaping as “not that serious,” but he’s frustrated that it’s affecting his performance on the field.

Sara is 41 and a single mother of two and works long hours as a nurse. She has type 2 diabetes and has been feeling fatigued, experiencing blurred vision, and noticing her wounds take longer to heal. She admits she sometimes skips her medications and meals because of her demanding schedule and prioritizing her kids. She wants to feel more energized and avoid complications, but feels overwhelmed trying to manage it all
.

Marcus is 55 and a retired bus driver who has gained 25 pounds over the last year. He complains of knee pain and rising blood pressure. He spends most of his day watching TV and admits to frequent snacking out of boredom. His doctor advised more physical activity, but Marcus says he doesn’t know where to start and feels too tired to exercise.

Grace is 24 and a graduate student who comes in complaining of frequent headaches and digestive issues. She often skips meals or eats fast food due to her busy schedule. She also relies on coffee and energy bars to get through the day. Grace wants to feel healthier and have more energy but worries that slowing down will hurt her academic performance.

Andre is 46 and a warehouse manager with a history of high cholesterol and hypertension. He’s come in for a routine follow-up but mentions he’s been having chest tightness when climbing stairs. He eats a lot of processed and fried foods, often grabbing meals from nearby fast food places. He says he knows he should eat better, but doesn't feel confident cooking or changing his habits.

Carmen is 36 and a hairstylist who recently started experiencing intense back pain. She’s on her feet all day and rarely stretches or exercises. At home, she collapses onto the couch and scrolls on her phone or naps. She’s tried yoga once but didn’t keep up with it. She’s frustrated by the pain but isn’t sure what changes will actually help.
"""
},
     {"role": "system", "content": f"""
You're name is {name} and are {age} and a professional {job} but has some type of {level} health issue, that is inspired from these previous individuals. You want to be {intensity} level of attitude to get help and you seem in {spirits} level of happyness. Only describe the name and general information about the individual you create, you're job is to work with the interviewer to have them figure out how to have them make healthy choices.
"""},
]

# First response from the bot
response = ollama.chat(model=model_name, messages=messages)
print("Your patient is:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Job: {job}")
print(f"Happyness: {spirits}")


# Continue the conversation:
while True:
    user_input = input("You: ")
    if not user_input:
        break  # exit loop on empty input
    messages.append({"role": "user", "content": user_input})
    response = ollama.chat(model=model_name, messages=messages)
    answer = response.message.content
    print(f"{name}: ", answer)
    messages.append({"role": "assistant", "content": answer})
