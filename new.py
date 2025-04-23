import streamlit as st
import time
import random

# Unique emojis for design
EMOJI_TITLE = "⌨️🚀"
EMOJI_RESULT = "🎯"
EMOJI_TIMER = "⏱️"

# List of 32 English sentences for testing
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Coding opens a door to endless possibilities.",
    "Practice makes perfect, so keep typing!",
    "Streamlit is a powerful tool for building apps.",
    "Learning new skills every day improves your life.",
    "Focus on progress, not perfection.",
    "Every challenge is an opportunity in disguise.",
    "Creativity is intelligence having fun.",
    "Believe in yourself and all that you are.",
    "The best time to start was yesterday, the next best time is now.",
    "Success comes to those who work hard.",
    "Embrace every moment and learn from it.",
    "Innovation distinguishes between a leader and a follower.",
    "The future belongs to those who believe in their dreams.",
    "Every mistake is a step closer to success.",
    "Stay positive, work hard, and make it happen.",
    "Your only limit is the one you set yourself.",
    "Small steps every day lead to big changes.",
    "Success is a journey, not a destination.",
    "Every day is a new opportunity to improve.",
    "Dream big, work hard, and stay focused.",
    "The secret to getting ahead is getting started.",
    "Believe you can and you're halfway there.",
    "Difficult roads often lead to beautiful destinations.",
    "Don't wait for opportunity; create it.",
    "The power of imagination makes us infinite.",
    "Every accomplishment starts with the decision to try.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "A smooth sea never made a skilled sailor.",
    "Your future is created by what you do today.",
    "Don't limit your challenges; challenge your limits.",
    "Great things never come from comfort zones."
]

# Initialize session state variables if not already present
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "end_time" not in st.session_state:
    st.session_state.end_time = None
if "test_sentence" not in st.session_state:
    st.session_state.test_sentence = None

st.title(f"{EMOJI_TITLE} Typing Speed Tester {EMOJI_TITLE}")

# Start test button: sets a random sentence and start time
if st.button("🚀 Start Test!"):
    st.session_state.test_sentence = random.choice(sentences)
    st.session_state.start_time = time.time()

# If a test sentence is available, display it and show the text area
if st.session_state.test_sentence:
    st.subheader("👇 Type the following sentence:")
    st.info(st.session_state.test_sentence, icon="💡")
    
    user_input = st.text_area("Type here...", height=150)

    # When the Submit button is clicked, calculate typing speed
    if st.button("✅ Submit"):
        if not user_input:
            st.warning("Please type the sentence before submitting!")
        else:
            st.session_state.end_time = time.time()
            elapsed_time = st.session_state.end_time - st.session_state.start_time
            word_count = len(user_input.split())
            # Calculate words per minute (WPM)
            wpm = (word_count / elapsed_time) * 60

            st.success(f"{EMOJI_RESULT} Your Typing Speed: {wpm:.2f} WPM")
            st.write(f"{EMOJI_TIMER} Total Time: {elapsed_time:.2f} seconds")
            st.balloons()

# Footer 
st.write("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
st.write("Developed by Faisal Hayat. 🚀🤍✨")  # Name Of Creator 🤍🚀✨