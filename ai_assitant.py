from dotenv import load_dotenv
load_dotenv()

from boltiotai import openai
import os
import sys

openai.api_key = os.environ.get("OPENAI_API_KEY")

if not openai.api_key:
    sys.stderr.write("""
You haven't set up your API key yet.
""")
    exit(1)

# Store conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]

print("Chatbot started! Type 'exit' to quit.\n")

while True:
    user_input = input("Ask Any Question : ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Add user message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Get response from OpenAI
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    assistant_reply = response['choices'][0]['message']['content']

    print("Answer : ", assistant_reply)
 
    # Add assistant response to history
    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })