# 🛕✨ Ramayana Story Generator


---

## 📌 Overview
This is a fun and creative AI-powered project built for **Sri Rama Navami**. It takes any keyword or theme, generates a **Ramayana-based story**, creates matching images, and compiles everything into a cute and engaging **Story Card PDF** — perfect for kids, students, or story lovers.

---

## ⚙️ Tech Stack
- **Gemini API (Google)** – For story generation using LLM  
- **Hugging Face API** – For generating story-based images  
- **ReportLab** – For creating the final PDF Story Card  
- **Streamlit** – Web interface for user interaction  

---

## 🚀 Features
- Generates a story from Ramayana based on input theme  
- Uses generative AI to create story illustrations  
- Converts it all into a clean and attractive story PDF  
- Simple and customizable UI using Streamlit  

---

## 🧠 How It Works
1. User gives a keyword or theme.
2. Gemini API generates a structured JSON with title, story, moral, and image prompts.
3. Hugging Face API converts prompts into images.
4. ReportLab assembles the story and images into a PDF.
5. Streamlit allows the user to run everything easily from the browser.

---

## 🔑 API Keys Required
- **Gemini API Key**
- **Hugging Face API Key** 

---

## 🛠️ Installation
```bash
git clone https://github.com/vishnuvardhan369/RamayanaStorycardGenerator
cd Ramayana-Story-Generator
python -m venv env
env\Scripts\activate   # On Windows
pip install -r requirements.txt
streamlit run app.py
