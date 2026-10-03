AI-Based Room Interior Theme Recommendation System

Project Overview

The AI-Based Room Interior Theme Recommendation System is a simple
web application that uses Generative AI to recommend interior design
themes based on a user's room details and preferences.
The user selects the room type, room size, budget, preferred style,
color, and lighting. The application sends these details to Google's
Gemini AI and displays a practical interior recommendation.
The project also includes a basic connection with Indian Knowledge
Systems (IKS) by incorporating selected Indian traditional design
ideas, natural materials, colors, craft traditions, and decorative
elements.

Features
- Select room type
- Select room size
- Select budget
- Select preferred interior style
- Select preferred color
- Select lighting preference
- Generate AI-based interior recommendations
- Get suggestions for:
  - Recommended theme
  - Colors
  - Furniture
  - Decoration
  - Materials
  - IKS inspiration
- Simple and beginner-friendly Streamlit interface
  
Technologies Used
- Python
- Streamlit -- web application interface
- Google Gemini API -- Generative AI recommendations
- python-dotenv -- secure environment variable handling
- Google GenAI Python SDK
  
Project Structure
AI-Interior-Theme-Recommendation/
│
├── app.py
├── requirements.txt
├── .gitignore
└── .env
The .env file contains the Gemini API key and must not be uploaded
to GitHub.

How to Run the Project Locally
1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate
2. Install required packages
pip install -r requirements.txt
3. Create .env
Create a file named .env in the project folder:
GEMINI_API_KEY=YOUR_API_KEY
Replace YOUR_API_KEY with your own Gemini API key.
4. Run the application
python -m streamlit run app.py
The application will open in the browser at the local Streamlit address.

How the System Works
1. User opens the application.
2. User enters/selects room details.
3. The application collects the selected preferences.
4. A prompt is created using those preferences.
5. Gemini Generative AI processes the prompt.
6. The AI generates an interior theme recommendation.
7. The recommendation is displayed in the Streamlit application.
8. The result includes an IKS-inspired section.
   
Indian Knowledge Systems (IKS) Connection
The project connects with IKS through selected Indian traditional design
elements. The recommendations can refer to:
- Indian-inspired color combinations
- Natural materials such as wood and cotton
- Traditional craft and decorative elements
- Indian-inspired textures and aesthetics
- Traditional design influences adapted for modern rooms
  
The IKS component is kept simple and is intended to provide culturally
inspired interior recommendations rather than claim that every
AI-generated recommendation represents a historical IKS principle.
Security
The Gemini API key is stored in an environment variable using .env.
The .gitignore file prevents the following from being uploaded to
GitHub:
.env
venv/
__pycache__/

Testing
The application was tested using different combinations of:
- Bedroom
- Living Room
- Study Room
- Different room sizes
- Different budgets
- Modern, Traditional, Minimalist and Luxury styles
- Different colors
- Different lighting preferences
The application successfully generated AI recommendations for the tested
combinations.

Limitations
- Recommendations depend on the Gemini AI response.
- The application does not generate actual room images.
- It does not calculate exact renovation costs.
- It does not use room photographs or measurements.
- Internet access is required for Gemini API requests.
- Gemini API usage may be subject to quota limits.
  
Future Scope
- Add room image upload
- Generate visual room designs
- Add furniture price estimates
- Add more Indian regional craft traditions
- Add a larger verified IKS knowledge base
- Add user accounts and saved recommendations
Live Deployment
Live Application: Add your Streamlit Community Cloud URL here after
deployment.

GitHub Repository
GitHub: 

Student Information
- Student Name: Priya Vadeti
- Roll Number: 19060
- Class: TY IT
- Project: AI-Based Room Interior Theme Recommendation System
- Academic Year: 2026-27
