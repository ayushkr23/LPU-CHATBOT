import json
import ollama
import sys
import time
from fuzzywuzzy import process

with open('lpu.json', 'r') as file:
    lpu_dataset = json.load(file)

def generate_answer_with_ai(user_input):
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": f"Answer this question related to Lovely Professional University: {user_input}"}],
        stream=False  
    )
    return response['message']['content']

def get_lpu_response(user_input):
    all_questions = []
    all_answers = {}

    for category, category_info in lpu_dataset["LPU_FAQ_Dataset"]["categories"].items():
        for topic, topic_info in category_info["topics"].items():
            for entry in topic_info["questions"]:
                if isinstance(entry, dict) and "question" in entry and "answer" in entry:
                    all_questions.append(entry["question"].lower())
                    all_answers[entry["question"].lower()] = entry["answer"]

    user_input_lower = user_input.lower().strip()
    if user_input_lower in all_answers:
        return all_answers[user_input_lower]

    best_match = process.extractOne(user_input_lower, all_questions)

    if best_match:
        matched_question, score = best_match
        if score >= 90:
            return all_answers[matched_question]

    return generate_answer_with_ai(user_input)

def smooth_typing(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def handle_greeting():
    introduction = (
        "Hello! I'm here to help you with information about Lovely Professional University (LPU). "
        "LPU is a vibrant institution offering a wide range of programs and opportunities for students. "
        "How can I assist you today?"
    )
    smooth_typing(introduction)

if __name__ == "__main__":
    print("Welcome to the LPU Chatbot! Type 'quit', 'exit', or 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            smooth_typing("AI: Goodbye! 👋")
            break
        
        greetings = ["hi", "hello", "hey", "greetings", "what's up"]
        if any(greet in user_input.lower() for greet in greetings):
            handle_greeting()
            continue

        lpu_response = get_lpu_response(user_input)
        time.sleep(1)
        smooth_typing("AI: " + lpu_response)