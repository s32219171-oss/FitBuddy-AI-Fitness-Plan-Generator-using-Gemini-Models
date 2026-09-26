
import streamlit as st
from google import genai

st.set_page_config(
    page_title="FitBuddy",
    page_icon="🏋️",
    layout="wide"
)

st.title("🏋️ FitBuddy")
st.subheader("AI-Powered Personalized Fitness Plan Generator")

st.info(
    "Enter your fitness details and Gemini AI will generate "
    "a personalized fitness plan."
)

# Gemini API setup
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    client = None

st.header("👤 Personal Details")

name = st.text_input("Name")
age = st.number_input("Age", 10, 100, 20)

st.header("🎯 Fitness Goal")

goal = st.selectbox(
    "Select your goal",
    [
        "Weight Loss",
        "Muscle Building",
        "General Fitness",
        "Strength Improvement",
        "Flexibility"
    ]
)

level = st.selectbox(
    "Fitness Level",
    ["Beginner", "Intermediate", "Advanced"]
)

days = st.slider(
    "Workout Days Per Week",
    1,
    7,
    4
)

duration = st.slider(
    "Workout Duration (minutes)",
    15,
    120,
    30,
    step=5
)

if st.button(
    "🤖 Generate My AI Fitness Plan",
    use_container_width=True
):

    if client is None:
        st.error(
            "Gemini API key is not configured. "
            "Please check Streamlit Secrets."
        )

    else:

        prompt = f"""
You are FitBuddy, an AI fitness plan generator.

Create a simple and personalized weekly fitness plan.

User details:
Name: {name if name else "User"}
Age: {age}
Fitness Goal: {goal}
Fitness Level: {level}
Workout Days Per Week: {days}
Workout Duration: {duration} minutes

Generate:

1. Fitness summary
2. Weekly workout plan
3. Warm-up
4. Cool-down
5. Basic nutrition guidance
6. Recovery and rest guidance
7. Safety advice

Make the plan suitable for the user's fitness level.
Keep the explanation simple and easy to follow.

Important:
This is general fitness guidance and not medical advice.
"""

        try:

            with st.spinner(
                "🤖 Gemini is creating your personalized plan..."
            ):

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

            st.success(
                "✅ AI Fitness Plan Generated Successfully!"
            )

            st.header("📋 Your Fitness Profile")

            st.write(
                f"**Name:** {name if name else 'User'}"
            )

            st.write(f"**Age:** {age}")
            st.write(f"**Goal:** {goal}")
            st.write(f"**Fitness Level:** {level}")
            st.write(
                f"**Workout Days:** {days} days/week"
            )

            st.write(
                f"**Duration:** {duration} minutes"
            )

            st.header("🤖 Gemini AI Fitness Plan")

            st.markdown(response.text)

            st.header("🛡️ Safety")

            st.warning(
                "FitBuddy provides general fitness guidance only. "
                "If you have an injury, medical condition, or health concern, "
                "consult a qualified healthcare or fitness professional."
            )

        except Exception as e:

            st.error(
                "Unable to generate the AI fitness plan."
            )

            st.caption(
                f"Error: {e}"
            )

st.markdown("---")

st.caption(
    "🏋️ FitBuddy – AI Fitness Plan Generator using Gemini Models | College Project"
)
