import openai
from dotenv import load_dotenv
import os

load_dotenv()
# Set up your OpenAI API credentials
api_key = os.getenv("token") 
openai.api_key = api_key 

def generate_dsa_question(context):
    # Define your prompt
    prompt = f"Generate a advance and hard DSA question based on the following context:\n\n{context}\n\nExamples:\n"

    # Generate a question with sample inputs and outputs using OpenAI GPT-3
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.8
    )

    # Extract the generated question from the OpenAI GPT-3 response
    question = response.choices[0].text.strip()

    return question

def generate_dsa_examples(question):
    # Define your prompt
    prompt = f"Generate example inputs and outputs for the following DSA question:\n\nQuestion: {question}\n\n"

    # Generate examples with inputs and outputs using OpenAI GPT-3
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=3,  # You can adjust the number of examples you want to generate
        stop=None,
        temperature=0.8
    )

    # Extract the generated examples from the OpenAI GPT-3 response
    examples = [choice.text.strip() for choice in response.choices]

    return examples

# Define your DSA context
context = "You are given an array of integers. Write a function that finds the maximum element in the array."

# Generate a DSA question
question = generate_dsa_question(context)
print("Generated Question:", question)

# Generate example inputs and outputs for the DSA question
examples = generate_dsa_examples(question)
print("\nGenerated Examples:")
for i, example in enumerate(examples):
    print(f"\nExample {i+1}:\n{example}")

