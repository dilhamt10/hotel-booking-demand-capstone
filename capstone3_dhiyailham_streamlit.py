import streamlit as st
import pickle
import joblib
import pandas as pd

# Load model
model = joblib.load("xgb_tuned_pipeline.joblib")

st.title("Hotel Booking Cancellation Predictor")

# Example input form
st.sidebar.header("Booking Details")
market_segment = st.sidebar.selectbox("Market Segment", ['Online TA', 'Offline TA/TO', 'Groups'])
deposit_type = st.sidebar.selectbox("Deposit Type", ['No Deposit', 'Refundable', 'Non Refund'])
customer_type = st.sidebar.selectbox("Customer Type", ['Transient', 'Transient-Party'])
reserved_room_type = st.sidebar.selectbox("Reserved Room Type", ['A', 'B','C','D','E'])
country = st.sidebar.selectbox("Country", ['PRT', 'International', 'Other'])

previous_cancellations = st.sidebar.number_input("Previous Cancellations", min_value=0, max_value=5, step=1)
booking_changes = st.sidebar.number_input("Booking Change", min_value=0, max_value=5, step=1)
days_in_waiting_list = st.sidebar.number_input("Days in Waiting List", min_value=0, max_value=84, step=7)
car_parking_spaces = st.sidebar.number_input("Required Car Parking Spaces", min_value=0, max_value=5, step=1)
total_of_special_requests = st.sidebar.number_input("Total of Special Requests", min_value=0, max_value=3, step=1)

# Convert inputs to DataFrame (must match your model’s expected features)
input_data = pd.DataFrame({
    'market_segment': [market_segment],
    'deposit_type': [deposit_type],
    'customer_type': [customer_type],
    'reserved_room_type': [reserved_room_type],
    'country': [country],

    'previous_cancellations': [previous_cancellations],
    'booking_changes': [booking_changes],
    'days_in_waiting_list': [days_in_waiting_list],
    'required_car_parking_spaces': [car_parking_spaces],
    'total_of_special_requests': [total_of_special_requests],
})

# Add any other required columns with default or dummy values if needed
# input_data['other_feature'] = [...]

# Predict
if st.button("Predict Cancellation"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Booking is likely to be canceled (probability: {probability:.2f})")
    else:
        st.success(f"✅ Booking is likely to be honored (probability of cancellation: {probability:.2f})")
