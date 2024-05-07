import os
import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am fine, thanks for asking.']),
    (r'what is your name?', ["I'm a chatbot. You can call me BOT!"]),
    (r'what can you do?', ["I can assist you with a variety of tasks. Just ask!"]),
    (r'who created you?', ["I was created by MOHAMMED SAHIL"]),
    (r'where are you from?', ["I exist in the digital realm, but I'm here to help you wherever you are!"]),
    (r'how old are you?', ["I don't have an age in the way humans do. I'm always learning and improving!"]),
    (r'what is the meaning of life?', ["That's a philosophical question! Different people have different perspectives on it."]),
    (r'quit', ['Bye! Take care.', 'Goodbye!']),
    (r'what is the weather like today?', ["I'm a chatbot and I can't check the weather, but you can use weather websites or apps for that!"]),
    (r'can you help me?', ["Of course! I'll do my best to assist you."]),
    (r'what is the capital of France?', ["The capital of France is Paris."]),
    (r'what time is it?', ["I'm sorry, I don't have access to real-time information like the current time."]),
    (r'how do I reset my password?', ["You can usually reset your password through the 'Forgot Password' link on the login page."]),
    (r'what is your favorite color?', ["I don't have personal preferences like humans do."]),
    (r'can you tell me a joke?', ["Sure! Why don't scientists trust atoms? Because they make up everything!"]),
    (r'what is your favorite food?', ["I don't eat, so I don't have a favorite food."]),
    (r'what is machine learning?', ["Machine learning is a subset of artificial intelligence that allows computers to learn and improve from experience."]),
    (r'what languages can you speak?', ["I can understand and respond in multiple languages, but currently, we're communicating in English."]),
    (r'how do I install Python?', ["You can download and install Python from the official Python website."]),
    (r'what is the population of China?', ["As of the latest data, the population of China is over 1.4 billion people."]),
    (r'what is the largest mammal?', ["The blue whale is the largest mammal on Earth."]),
    (r'what is the square root of 144?', ["The square root of 144 is 12."]),
    (r'how do I get to the nearest post office?', ["You can use navigation apps like Google Maps to find the nearest post office."]),
    (r'what is your favorite movie?', ["I don't have preferences for movies."]),
    (r'what is the speed of light?', ["The speed of light in a vacuum is approximately 299,792 kilometers per second."]),
    (r'what is the meaning of AI?', ["AI stands for Artificial Intelligence, which refers to the simulation of human intelligence by computers."]),
    (r'how do I create a website?', ["You can create a website using HTML, CSS, and JavaScript, or use website builders like WordPress or Wix."]),
    (r'what is the currency of Japan?', ["The currency of Japan is the Japanese Yen."]),
    (r'how do I cook pasta?', ["Boil water, add pasta, cook until al dente, then drain and serve with your favorite sauce."]),
    (r'what is the tallest mountain in the world?', ["Mount Everest is the tallest mountain above sea level."]),
    (r'what is your favorite book?', ["I don't have personal preferences for books."]),
    (r'how do I say hello in Spanish?', ["Hello in Spanish is 'Hola'."]),
    (r'what is the largest ocean?', ["The Pacific Ocean is the largest ocean on Earth."]),
    (r'what is the atomic number of carbon?', ["The atomic number of carbon is 6."]),
    (r'how do I bake a cake?', ["You can bake a cake by mixing flour, sugar, eggs, and other ingredients, then baking in an oven."]),
    (r'what is the capital of Australia?', ["The capital of Australia is Canberra."]),
    (r'what is the boiling point of water?', ["The boiling point of water at sea level is 100 degrees Celsius (212 degrees Fahrenheit)."]),
    (r'what is your favorite animal?', ["I don't have preferences for animals."]),
    (r'how do I tie a tie?', ["There are many ways to tie a tie, but a common method is the Windsor knot."]),
    (r'what is the diameter of the Earth?', ["The diameter of the Earth is approximately 12,742 kilometers."]),
    (r'how do I start a business?', ["Starting a business involves creating a business plan, securing funding, and registering your company."]),
    (r'what is the longest river in the world?', ["The Nile River is often considered the longest river in the world."]),
    (r'what is the pH of water?', ["The pH of pure water is 7, making it neutral."]),
    (r'how do I meditate?', ["To meditate, find a quiet place, sit comfortably, focus on your breath, and let go of distractions."]),
    (r'what is the capital of Brazil?', ["The capital of Brazil is Brasília."]),
    (r'what is the meaning of HTML?', ["HTML stands for Hypertext Markup Language, which is used to create web pages."]),
    (r'how do I invest in stocks?', ["You can invest in stocks through brokerage accounts, mutual funds, or exchange-traded funds (ETFs)."]),
    (r'what is the largest desert in the world?', ["The largest desert in the world is the Antarctic Desert."]),
    (r'what is the chemical symbol for gold?', ["The chemical symbol for gold is Au."]),
    (r'how do I learn to code?', ["You can learn to code by taking online courses, reading books, and practicing regularly."]),
    (r'what is the capital of Canada?', ["The capital of Canada is Ottawa."]),
    (r'what is the melting point of ice?', ["The melting point of ice at sea level is 0 degrees Celsius (32 degrees Fahrenheit)."]),
    (r'how do I make a resume?', ["To make a resume, include your contact information, work"])
]


chatbot = Chat(patterns, reflections)


print("Hello! I'm your BOT. How can I help you today?")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("BOT:", response)
    if user_input.lower() == 'quit':
        break
