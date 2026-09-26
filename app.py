
import streamlit as st

st.set_page_config(
    page_title="FitBuddy",
    page_icon="🏋️",
    layout="wide"
)

st.title("🏋️ FitBuddy")
st.subheader("Personalized Fitness Plan Generator")

st.info("Enter your fitness details and generate your personalized workout plan.")

st.header("👤 Personal Details")

name = st.text_input("Name")
age = st.number_input("Age", 10, 100, 20)

st.header("🎯 Fitness Goal")

goal = st.selectbox(
    "Select your goal",
    ["Weight Loss", "Muscle Building", "General Fitness", "Strength Improvement", "Flexibility"]
)

level = st.selectbox(
    "Fitness Level",
    ["Beginner", "Intermediate", "Advanced"]
)

days = st.slider("Workout Days Per Week", 1, 7, 4)

duration = st.slider("Workout Duration (minutes)", 15, 120, 30, step=5)

if st.button("🤖 Generate My Fitness Plan", use_container_width=True):

    st.success("✅ Fitness plan generated successfully!")

    st.header("📋 Your Fitness Profile")
    st.write(f"**Name:** {name if name else 'User'}")
    st.write(f"**Age:** {age}")
    st.write(f"**Goal:** {goal}")
    st.write(f"**Fitness Level:** {level}")
    st.write(f"**Workout Days:** {days} days/week")
    st.write(f"**Duration:** {duration} minutes")

    st.header("📅 Weekly Workout Plan")

    exercises = {
        "Weight Loss": [
            "Brisk Walking – 10 minutes",
            "Squats – 3 × 10",
            "Jumping Jacks – 3 × 15",
            "Mountain Climbers – 3 × 10"
        ],
        "Muscle Building": [
            "Push-ups – 3 × 10",
            "Squats – 3 × 12",
            "Lunges – 3 × 10",
            "Plank – 3 × 30 seconds"
        ],
        "General Fitness": [
            "Walking – 10 minutes",
            "Squats – 3 × 10",
            "Push-ups – 3 × 10",
            "Plank – 3 × 20 seconds"
        ],
        "Strength Improvement": [
            "Squats – 4 × 10",
            "Push-ups – 4 × 10",
            "Lunges – 3 × 10",
            "Plank – 3 × 30 seconds"
        ],
        "Flexibility": [
            "Neck Stretch – 30 seconds",
            "Shoulder Stretch – 30 seconds",
            "Hamstring Stretch – 30 seconds",
            "Butterfly Stretch – 30 seconds"
        ]
    }

    for day in range(1, days + 1):
        st.subheader(f"🔥 Day {day}")

        for exercise in exercises[goal]:
            st.write("• " + exercise)

    st.header("🥗 Basic Nutrition Guidance")
    st.write("• Eat a balanced diet.")
    st.write("• Include fruits and vegetables.")
    st.write("• Drink enough water.")
    st.write("• Include suitable protein sources.")

    st.header("🛡️ Safety")
    st.warning(
        "FitBuddy provides general fitness guidance only. "
        "Consult a qualified professional if you have an injury or medical condition."
    )

st.markdown("---")
st.caption("🏋️ FitBuddy – College Project")
