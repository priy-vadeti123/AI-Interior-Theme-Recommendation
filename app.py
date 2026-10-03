import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Page settings
st.set_page_config(
    page_title="AI Interior Theme Recommendation",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 AI-Based Room Interior Theme Recommendation System")

st.write(
    "Get a simple AI-powered interior theme recommendation "
    "based on your room preferences."
)

st.divider()

# -----------------------------
# USER INPUTS
# -----------------------------

st.subheader("📋 Enter Your Room Details")

room_type = st.selectbox(
    "Room Type",
    ["Bedroom", "Living Room", "Study Room", "Kitchen"]
)

room_size = st.selectbox(
    "Room Size",
    ["Small", "Medium", "Large"]
)

budget = st.selectbox(
    "Budget",
    ["Below ₹25,000", "₹25,000 - ₹50,000", "₹50,000 - ₹1,00,000"]
)

style = st.selectbox(
    "Preferred Style",
    ["Modern", "Traditional", "Minimalist", "Luxury"]
)

color = st.selectbox(
    "Preferred Color",
    ["Earthy", "Blue", "Green", "White", "Warm Colors"]
)

lighting = st.selectbox(
    "Lighting",
    ["Warm", "Cool", "Natural"]
)

st.divider()

# -----------------------------
# AI RECOMMENDATION
# -----------------------------

if st.button("🤖 Generate AI Recommendation"):

    if not api_key:

        st.error("Gemini API key was not found.")

    else:

        client = genai.Client(api_key=api_key)

        prompt = f"""
You are an interior design assistant.

Create a simple Indian-inspired interior design recommendation.

Room Type: {room_type}
Room Size: {room_size}
Budget: {budget}
Preferred Style: {style}
Preferred Color: {color}
Lighting: {lighting}

Give the answer using these sections:

1. Recommended Theme
2. Recommended Colors
3. Furniture Suggestions
4. Decoration Ideas
5. Recommended Materials
6. IKS Inspiration

Keep the answer simple, practical and suitable for a student project.

For IKS Inspiration, mention relevant Indian traditional design,
craft, material or decorative practices without making unsupported
historical claims.
"""

        try:

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            st.success("Recommendation generated successfully!")

            st.subheader("🎨 AI Interior Recommendation")

            st.write(response.text)

        except Exception as e:

            st.error(
                "The AI service is temporarily unavailable. "
                "Please wait and try again."
            )

st.divider()

# -----------------------------
# IKS INFORMATION
# -----------------------------

st.subheader("🇮🇳 Indian Knowledge Systems (IKS)")

st.write(
    "This project connects interior recommendations with selected "
    "Indian traditional design ideas, natural materials, colours, "
    "craft traditions and decorative elements."
)

st.info(
    "The IKS component is used to provide culturally inspired "
    "interior recommendations while keeping the application simple."
)

# -----------------------------
# PROJECT INFORMATION
# -----------------------------

st.subheader("ℹ️ About the Project")

st.write(
    "This application uses Generative AI to suggest interior themes "
    "based on room type, size, budget, style, colour and lighting "
    "preferences."
)