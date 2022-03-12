import streamlit as st


st.title("Reputation")

label = "Ranks"
ranks = ["None", "Neutral", "Recognized", "Friendly", "Trusted", "Respected", "Honored", "Sworn", "Allied (A Realm Reborn) / Bloodsworn", "Allied (Heavensward and Stormblood)"]

options = st.radio(label, ranks)

st.write('You selected:', options)

