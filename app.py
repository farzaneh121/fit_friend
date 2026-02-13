import streamlit as st
from fit_friend import wellnessBot

st.set_page_config(page_title="Fit Friend", page_icon="💪", layout="wide")

# our UI part :)
st.markdown("""
    <style>
    .stApp { background-color: #caf0f8; }
    .chat-bubble { border-radius: 30px; padding: 30px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar for Navigation since we don't want to mix everything---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1099/1099672.png", width=100)
    st.title("Fit Friend Settings")
    mode = st.radio("Choose your mode:", ["🧁 Healthy Desserts", "🏋️ Workout Planner"])
    st.divider()
    if st.button("Clear Chat"):
        st.session_state.messages = []

# 1. Initialize a dictionary to hold separate histories
if "histories" not in st.session_state:
    st.session_state.histories = {
        "🧁 Healthy Desserts": [],
        "🏋️ Workout Planner": []
    }

# 2. Identify which history we are currently looking at
current_history = st.session_state.histories[mode]

st.title("💪 Fit Friend AI")
st.write(f"Currently in **{mode}** mode. Let's reach those goals!")

# 3. Display ONLY the history for the active mode
for message in current_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle new input
if prompt := st.chat_input(f"Message {mode}..."):
    # Add user message to the SPECIFIC history
    current_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        bot = wellnessBot()
        with st.spinner("Coach is thinking..."):
            if mode == "🧁 Healthy Desserts":
                response = bot.give_healthy_recipe(prompt)
            else:
                response = bot.give_workout_plan(prompt)
            st.markdown(response)

    # Add assistant response to the SPECIFIC history
    current_history.append({"role": "assistant", "content": response})