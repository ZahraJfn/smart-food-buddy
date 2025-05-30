
import streamlit as st
import random
import json

st.set_page_config(page_title="Smart Food Buddy", layout="centered")
st.title("🥗 Smart Food Buddy")
st.markdown("Select a **meal** and a **goal**, then click below to get a healthy food suggestion.")

# Load the food database
with open("smart_food_buddy_database.json", "r", encoding="utf-8") as f:
    food_data = json.load(f)

meal = st.selectbox("Select Meal", ["breakfast", "lunch", "dinner", "snack"])
goal = st.selectbox("Select Goal", ["lose_weight", "gain_weight", "energy"])

if st.button("Get Suggestion"):
    try:
        if meal not in food_data or goal not in food_data[meal]:
            st.warning("Invalid meal or goal selected.")
        else:
            suggestion = random.choice(food_data[meal][goal])
            st.success(f"🍽️ Suggested food: **{suggestion}**")
    except Exception as e:
        st.error("❌ Something went wrong. Please try again.")
