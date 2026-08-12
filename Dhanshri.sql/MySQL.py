import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="registration"
)


import streamlit as st 
from datetime import date

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="Bus Ticket Booking", page_icon="🚌")

st.title("🚌 Bus Ticket Booking System")

st.markdown("---")

# -------------------------------
# Fare Details (Backend)
# -------------------------------
fare = {
    "Ordinary": 250,
    "Express": 400,
    "Sleeper": 650,
    "Luxury AC": 900
}

# -------------------------------
# Frontend Form
# -------------------------------
with st.form("booking_form"):

    name = st.text_input("Passenger Name")

    age = st.number_input("Age", 1, 100)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    source = st.selectbox(
        "Source",
        ["Mumbai", "Pune", "Nashik", "Nagpur", "Aurangabad"]
    )

    destination = st.selectbox(
        "Destination",
        ["Mumbai", "Pune", "Nashik", "Nagpur", "Aurangabad"]
    )

    bus_type = st.selectbox(
        "Bus Type",
        list(fare.keys())
    )

    journey_date = st.date_input(
        "Journey Date",
        min_value=date.today()
    )

    seats = st.number_input(
        "Number of Seats",
        min_value=1,
        max_value=6,
        value=1
    )

    submit = st.form_submit_button("Book Ticket")

# -------------------------------
# Backend Logic
# -------------------------------
if submit:

    if name == "":
        st.error("Please enter passenger name.")

    elif source == destination:
        st.error("Source and Destination cannot be the same.")

    else:

        total_fare = fare[bus_type] * seats

        st.success("✅ Ticket Booked Successfully!")

        st.markdown("## 🎫 Ticket")

        st.write("**Passenger:**", name)
        st.write("**Age:**", age)
        st.write("**Gender:**", gender)
        st.write("**Source:**", source)
        st.write("**Destination:**", destination)
        st.write("**Journey Date:**", journey_date)
        st.write("**Bus Type:**", bus_type)
        st.write("**Seats:**", seats)
        st.write("**Fare per Seat:** ₹", fare[bus_type])
        st.write("### 💰 Total Fare: ₹", total_fare)

        st.balloons()

conn.close()






































































