import streamlit as st
import joblib

# Load trained model
model = joblib.load("spam_model.joblib")

st.title("📩 Spam Message Detector")
st.write("Enter a message and check whether it is Spam or Ham.")

message = st.text_area("Enter your message:")

if st.button("Check Message"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("🚨 This message is SPAM")
        else:
            st.success("✅ This message is HAM")