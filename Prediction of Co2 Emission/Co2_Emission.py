import pandas as pd
import streamlit as st
import pickle

# Load the trained model
with open('model_Co2_1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Create a Streamlit web app
st.image('https://www.ledgerinsights.com/wp-content/uploads/2021/10/co2-carbon-emissions-vehicle-car-auto.jpg', use_column_width=True)


st.title('CO2 Emission Prediction App')

col1, col2 = st.columns(2)

# Input Features in the first column
with col1:
    st.header('Input Features')
    engine_size = st.number_input('Engine Size', step=1)
    cylinders = st.number_input('Cylinders', step=1)
    transmission = st.selectbox('Transmission', ['AS', 'M', 'AV', 'AM', 'A'])
    fuel_type = st.selectbox('Fuel Type', ['Z', 'D', 'X', 'E', 'N'])
    fuel_consumption_city = st.number_input('Fuel Consumption City (l/100km)', step=1)
    fuel_consumption_hwy = st.number_input('Fuel Consumption Hwy (l/100km)', step=1)

# Additional Input Features in the second column
with col2:
    st.header('Additional Features')
    fuel_consumption_comb_l_100km = st.number_input('Fuel Consumption Comb (l/100km)', step=1)
    fuel_consumption_comb_mpg = st.number_input('Fuel Consumption Comb (mpg)', step=1)
    make_type = st.selectbox('Make Type', ['Luxury', 'Premium', 'Sports', 'General'])
    vehicle_class_type = st.selectbox('Vehicle Class Type', ['Hatchback', 'SUV', 'Sedan', 'Truck'])

# Make a prediction based on user input
if st.button('Predict CO2 Emissions'):
    features = pd.DataFrame({
        'engine_size': [engine_size],
        'cylinders': [cylinders],
        'transmission': [transmission],
        'fuel_type': [fuel_type],
        'fuel_consumption_city': [fuel_consumption_city],
        'fuel_consumption_hwy': [fuel_consumption_hwy],
        'fuel_consumption_comb(l/100km)': [fuel_consumption_comb_l_100km],
        'fuel_consumption_comb(mpg)': [fuel_consumption_comb_mpg],
        'Make_Type': [make_type],
        'Vehicle_Class_Type': [vehicle_class_type]
    })

    prediction = model.predict(features)[0]

    if prediction <= 100:
        st.success(f'Predicted CO2 Emissions: {prediction:.2f} g/km')
        st.markdown('<p style="color: green;">Low CO2 Emissions</p>', unsafe_allow_html=True)
    elif 160 <= prediction <= 255:
        st.success(f'Predicted CO2 Emissions: {prediction:.2f} g/km')
        st.markdown('<p style="color: orange;">Medium CO2 Emissions</p>', unsafe_allow_html=True)
    else:
        st.success(f'Predicted CO2 Emissions: {prediction:.2f} g/km')
        st.markdown('<p style="color: red;">High CO2 Emissions</p>', unsafe_allow_html=True)
