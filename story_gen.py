import google.generativeai as genai
import json

genai.configure(api_key="api_key")
model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")

def generate_ramayana_story(user_input):
    prompt = f"""
    You are an AI specialized in generating children's stories based on the Indian epic, the Ramayana. Your task is to create a story based on a given theme, moral, incident, or keyword. The story should be engaging, suitable for children, and should include:

    Title: A captivating title for the story.

    Story: A concise narrative that fits within half the page of A4 size page, ensuring it's neither too brief nor overly detailed.

    Moral: A clear moral derived from the story.

    Image Prompts: Two detailed prompts for generating images that visually represent key scenes or elements from the story from ramayana. Make them short and simple to generate. But detailed with their dressings and everything according to the the great epic ramayana 

    Please provide the output in the in the following JSON format
    "title": "Story Title",
    "story": "The main content of the story...",
    "moral": "The moral of the story...",
    "image_prompts": [
        "Detailed description for the first image prompt...",
        "Detailed description for the second image prompt..."
    ]

    The user input is :{user_input}

    """
    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()

        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "").replace("```", "").strip()

        return json.loads(response_text)

    except Exception as e:
        print("❌ Error parsing response:", e)
        print("Returned text:", response.text if response else "No response")
        return None
