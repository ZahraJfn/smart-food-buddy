
import streamlit as st
import requests

st.set_page_config(page_title="Smart Food Buddy", layout="centered")

st.title("🥗 Smart Food Buddy")
st.markdown("Select a **meal** and a **goal**, then click below to get a food suggestion.")

meal = st.selectbox("Select Meal", ["breakfast", "lunch", "dinner", "snack"])
goal = st.selectbox("Select Goal", ["lose_weight", "gain_weight", "energy"])

if st.button("Get Suggestion"):
    try:
        response = requests.post(
            "https://YOUR_NGROK_URL_HERE.ngrok-free.app/recommend",
            json={"meal": meal, "goal": goal},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            st.success(f"🍽️ Suggested food: **{data['suggestion']}**")
        else:
            st.error("⚠️ Invalid response from server.")
    except Exception as e:
        st.error("❌ Could not connect to the server.")
