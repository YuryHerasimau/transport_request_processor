import openai
import json
import os
from dotenv import load_dotenv
from prompts.prompt_template import extract_information_by_keys_template


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Text Analysis Function with GPT
def process_text_with_gpt(text):
    prompt = extract_information_by_keys_template.format(text=text)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=500,
    )
    # The response from the model is in 'choices[0].message.content'
    response_text = response["choices"][0]["message"]["content"]
    return format_response_to_json(response_text)


# Formatting the response to JSON
def format_response_to_json(response_text):
    return json.loads(response_text)
