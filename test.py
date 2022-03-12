import streamlit as st


st.title("Reputation")

label = "Choose your rank"
ranks = ["None", "Neutral", "Recognized", "Friendly", "Trusted", "Respected", "Honored", "Sworn", "Allied (A Realm Reborn) / Bloodsworn", "Allied (Heavensward and Stormblood)"]


options = st.sidebar.radio(label, ranks)

st.write('Your ranks is:', options)


if options == "Friendly":
    quests = {
        "Amal'jaa": {"cost": 20, "days": 9, "per day": 3},
        "Kobold": {"cost": 20, "days": 9, "per day": 3},
        "Sahagin": {"cost": 20, "days": 9, "per day": 3},
        "Sylph": {"cost": 20, "days": 9, "per day": 3},
        "Ixali": {"cost": 29, "days": 6, "per day": 3},
        "Moogle": {"cost": 50, "days": 4, "per day": 3},
        "Vanu Vanu": {"cost": 50, "days": 4, "per day": 3},
        "Namazu": {"cost": 60, "days": 3, "per day": 3},
        "Ananta": {"cost": 60, "days": 3, "per day": 3},
        "Kojin": {"cost": 60, "days": 3, "per day": 3},
        "Pixie": {"cost": 60, "days": 3, "per day": 3},
        "Qitari": {"cost": 60, "days": 3, "per day": 3},
        "Dwarf": {"cost": 60, "days": 3, "per day": 3},
        "Vath": {"cost": 70, "days": 3, "per day": 3},
    }
    start_value = 510
    win_value = 720
else:
    quests = {}
    start_value = 0


for name, value in quests.items():
    int_val = st.slider(
        f"{name}: {value['days']} days with {value['per day']} quests per day",
        min_value=0,
        max_value=value["days"] * value["per day"],
        value=0,
        step=1
    )
    start_value += int_val * value["cost"]

st.sidebar.write("You had pass ", start_value)
st.sidebar.write(win_value - start_value, "left to the next rank")