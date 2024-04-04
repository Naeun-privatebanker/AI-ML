import google.generativeai as genai
from env import settings
import base64
import json

GOOGLE_API_KEY = settings.CONFIG_GLOBAL['google-api-key']
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_desc():
    with open('env/file1.pdf', 'rb') as f:
        pdf_content = f.read()

    encoded_pdf = base64.b64encode(pdf_content).decode("utf-8")
    prompt = settings.CONFIG_DESC['prompt']

    response = model.generate_content([prompt, encoded_pdf])

    return response.text


def get_caution(conversation: str):
    prompt = settings.CONFIG_CAUTION['prompt'] + "\n" + conversation
    response = model.generate_content(prompt)

    return json.loads(response.text)
