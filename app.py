import streamlit as st
import json
from story_gen import generate_ramayana_story
from image_gen import generate_image
from pdf_maker import create_story_pdf
import os

def set_background(img_path):
    import base64
    with open(img_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode()

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            color: white !important;
        }}
        .main::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: rgba(255, 255, 255, 0.3);  /* white overlay with 60% opacity */
            z-index: -1;
        }}
        
        </style>
        <div class="centered-container">
    """, unsafe_allow_html=True)


set_background("shri_ram.jpg")
st.title("Ramayana Story Generator")

theme = st.text_input("Enter a theme / word / incident related to Ramayana")

if st.button("✨ Generate Story Card"):
    if theme.strip() == "":
        st.warning("Please enter a theme to continue.")
    else:
        with st.spinner("Generating story..."):
            try:
                story_data = generate_ramayana_story(theme)

                title = story_data["title"]
                story = story_data["story"]
                moral = story_data["moral"]
                prompts = story_data["image_prompts"]

                st.success("✅ Story Generated!")
                st.write(f"### {title}")
                st.write(story)
                st.markdown(f"**Moral:** _{moral}_")

                st.info("🎨 Generating images...")
                for idx, prompt in enumerate(prompts):
                    st.write(f"🖼️ Prompt {idx+1}: {prompt}")
                    generate_image(prompt, f"image_{idx + 1}.png")

                pdf_path = "story_card.pdf"
                create_story_pdf(title, story, moral, "image_1.png", "image_2.png", output_path=pdf_path)

                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="📥 Download Story Card as PDF",
                        data=pdf_file,
                        file_name=pdf_path,
                        mime="application/pdf"
                    )

            except json.JSONDecodeError as e:
                st.error("❌ JSON Decode Error")
            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")
