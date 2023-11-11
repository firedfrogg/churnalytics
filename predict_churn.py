import numpy as np
import pickle
import warnings
import streamlit as st
warnings.filterwarnings("ignore", category=UserWarning)
loaded_model = pickle.load(open("trained_model3.sav", "rb"))


def churn_prediction(input_data):
    input_data_as_numpy_array_reshaped = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(input_data_as_numpy_array_reshaped)
    if prediction[0] == 0:
        return "The person does not churn"
    else:
        return "The person churns"


def main():

    # Setting a title
    st.title("Churnalytics Web App")

    # Tenure Months
    tenure_months = st.slider("Months of tenure", min_value=0, max_value=120, step=1)

    # Device Class
    selected_device_class = st.selectbox("Select Device Class", ["Low End", "Mid End", "High End"])
    device_class_mapping = {"Low End": 1, "Mid End": 2, "High End": -1}
    selected_value = device_class_mapping[selected_device_class]

    # Games Product
    games_product_class = st.selectbox("Do you use internet service for games product?", ["Yes", "No",
                                                                                          "No Internet Service"])
    games_product_mapping = {"Yes": 1, "No": 0, "No Internet Service": -1}
    games_product = games_product_mapping[games_product_class]

    # Music Product
    music_product_class = st.selectbox("Do you use internet service for music product?", ["Yes", "No",
                                                                                          "No Internet Service"])
    music_product_mapping = {"Yes": 1, "No": 0, "No Internet Service": -1}
    music_product = music_product_mapping[music_product_class]

    # Education Product
    education_product_class = st.selectbox("Do you use internet service for education product?", ["Yes", "No",
                                                                                                  "No Internet Service"]
                                           )
    education_product_mapping = {"Yes": 1, "No": 0, "No Internet Service": -1}
    education_product = education_product_mapping[education_product_class]

    # Call Center Product
    call_center_product_class = st.selectbox("Do you own the call service?", ["Yes", "No"])
    call_center_product_mapping = {"Yes": 1, "No": 0}
    call_center_product = call_center_product_mapping[call_center_product_class]

    # Video Product
    video_product_class = st.selectbox("Do you use a video product service?", ["Yes", "No", "No Internet Service"])
    video_product_mapping = {"Yes": 1, "No": 0, "No Internet Service": -1}
    video_product = video_product_mapping[video_product_class]

    # Use MyApp
    my_app_class = st.selectbox("Do you use MyApp service?", ["Yes", "No", "No Internet Service"])
    my_app_mapping = {"Yes": 1, "No": 0, "No Internet Service": -1}
    my_app = my_app_mapping[my_app_class]

    # Monthly purchase
    monthly_purchase = st.slider("How much did you spend for all services? In Thousand Rupiahs", min_value=0,
                                 max_value=1000, step=10)

    # Customer Lifetime Value (CLTV)
    cltv = st.slider("How much is your Customer Lifetime Value (CLTV)? In Thousand Rupiahs", min_value=0,
                     max_value=10000, step=100)

    # Customer Location
    selected_location = st.selectbox("Where do you live, Jakarta or Bandung?", ["Jakarta", "Bandung"])
    if selected_location == "Jakarta":
        jakarta = 1
        bandung = 0
    else:
        jakarta = 0
        bandung = 1

    # Payment Method
    selected_payment = st.selectbox("How do you pay for the service?", ["Credit", "Debit", "Digital Wallet", "Pulsa"])
    credit = 0
    debit = 0
    digital_wallet = 0
    pulsa = 0
    # Update the selected payment method
    if selected_payment == "Credit":
        credit = 1
        debit = 0
        digital_wallet = 0
        pulsa = 0
    elif selected_payment == "Debit":
        debit = 1
        credit = 0
        digital_wallet = 0
        pulsa = 0
    elif selected_payment == "Digital Wallet":
        digital_wallet = 1
        pulsa = 0
        credit = 0
        debit = 0
    elif selected_payment == "Pulsa":
        pulsa = 1
        credit = 0
        debit = 0
        digital_wallet = 0

    number_of_services = games_product + music_product + education_product + call_center_product + video_product + my_app
    if (number_of_services == -5):
        number_of_services: 0

    total_product_usage = games_product + music_product + education_product

    games_music_interaction = games_product + music_product

    engagement_score = call_center_product + video_product

    total_spending = monthly_purchase * tenure_months
    if (tenure_months == 0):
        average_monthly_spending = total_spending
    else:
        average_monthly_spending = total_spending / tenure_months

    if (cltv > 5000):
        high_cltv = 1
    else:
        high_cltv = 0

    recent_interactions = call_center_product + video_product + my_app



    # Code for prediction
    predicted_churn = ''

    # Creating a button for prediction
    if st.button('Churn Predict Result'):
        predicted_churn = churn_prediction([tenure_months, selected_value, games_product,
                                            music_product, education_product, call_center_product,
                                            video_product, my_app, monthly_purchase, cltv, bandung,
                                            jakarta, credit, debit, digital_wallet, pulsa, number_of_services,
                                            total_product_usage, games_music_interaction, engagement_score,
                                            total_spending, average_monthly_spending, high_cltv, 
                                            recent_interactions])

    st.success(predicted_churn)


if __name__ == '__main__':
    main()
