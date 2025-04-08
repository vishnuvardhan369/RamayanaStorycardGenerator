import requests
from PIL import Image
from io import BytesIO

API_TOKEN = "api_key"
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def generate_image(prompt, filename):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save(filename)
        print(f"✅ Image saved as {filename}")
    else:
        print("❌ Failed:", response.status_code)
        print(response.text)
