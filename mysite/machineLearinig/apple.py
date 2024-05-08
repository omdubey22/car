import pickle as pk
import streamlit as st
import pandas as pd

# Load the trained model
model = pk.load(open('model.pkl', 'rb'))

# Header for the Streamlit app
st.header('Car Prediction ML Model')

# Read the car data
cars_data = pd.read_csv("CarPrice_Assignment.csv")

# Function to extract brand name from car name
def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()

# Apply the function to get brand names
cars_data['CarName'] = cars_data['CarName'].apply(get_brand_name)

# Select box for car brand
CarName = st.selectbox('Select Car Brand', cars_data['CarName'].unique())

# Select box for fuel type
fueltype = st.selectbox('Select Fuel Type', cars_data['fueltype'].unique())

# Slider for aspiration
aspiration = st.slider('Select Aspiration', 10, 50)

# Select box for doornumber
doornumber = st.selectbox('Select Doornumber', ['two', 'four'])

# Select box for car body
carbody = st.selectbox('Select Car Body', ['sedan', 'hatchback', 'wagon', 'hardtop', 'convertible'])

# Select box for drive wheel
drivewheel = st.selectbox('Select Drive Wheel', ['fwd', 'rwd', '4wd'])

# Slider for engine location
enginelocation = st.slider('Select Engine Location', 10, 50)

# Slider for wheelbase
wheelbase = st.slider('Select Wheelbase', 80, 120)

# Slider for car length
carlength = st.slider('Select Car Length', 150, 250)

# Slider for car width
carwidth = st.slider('Select Car Width', 50, 100)

# Slider for car height
carheight = st.slider('Select Car Height', 40, 80)

# Slider for curb weight
curbweight = st.slider('Select Curb Weight', 1500, 4500)

# Slider for engine type
enginetype = st.slider('Select Engine Type', 10, 50)

# Slider for cylinder number
cylindernumber = st.slider('Select Cylinder Number', 2, 12)

# Slider for engine size
enginesize = st.slider('Select Engine Size', 50, 500)

# Slider for fuel system
fuelsystem = st.slider('Select Fuel System', 2, 12)

# Slider for bore ratio
boreratio = st.slider('Select Bore Ratio', 2, 12)

# Slider for stroke
stroke = st.slider('Select Stroke', 2, 12)

# Slider for compression ratio
compressionratio = st.slider('Select Compression Ratio', 2, 12)

# Slider for horsepower
horsepower = st.slider('Select Horsepower', 50, 400)

# Slider for peak RPM
peakrpm = st.slider('Select Peak RPM', 2000, 7000)

# Slider for city MPG
citympg = st.slider('Select City MPG', 10, 50)

# Slider for highway MPG
highwaympg = st.slider('Select Highway MPG', 10, 50)
if st.button("Predict"):
    # Create input data DataFrame
    input_data = {
        'car_ID': [0],  # Just a placeholder for 'car_ID' since it's not used in prediction but might be in the model
        'carcompany': ['carcompany'],  # Placeholder for 'carcompany'
        'symboling': [0],  # Placeholder for 'symboling'
        'CarName': [CarName],
        'fueltype': [fueltype],
        'aspiration': [aspiration],
        'doornumber': [doornumber],
        'carbody': [carbody],
        'drivewheel': [drivewheel],
        'enginelocation': [enginelocation],
        'wheelbase': [wheelbase],
        'carlength': [carlength],
        'carwidth': [carwidth],
        'carheight': [carheight],
        'curbweight': [curbweight],
        'enginetype': [enginetype],
        'cylindernumber': [cylindernumber],
        'enginesize': [enginesize],
        'fuelsystem': [fuelsystem],
        'boreratio': [boreratio],
        'stroke': [stroke],
        'compressionratio': [compressionratio],
        'horsepower': [horsepower],
        'peakrpm': [peakrpm],
        'citympg': [citympg],
        'highwaympg': [highwaympg]
    }

    # Convert input data into a DataFrame
    inp_df = pd.DataFrame(input_data)

    # Reorder columns to match the order during model training
    inp_df = inp_df[['car_ID', 'carcompany', 'symboling', 'CarName', 'fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel', 'enginelocation', 'wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight', 'enginetype', 'cylindernumber', 'enginesize', 'fuelsystem', 'boreratio', 'stroke', 'compressionratio', 'horsepower', 'peakrpm', 'citympg', 'highwaympg']]

    # Predict using the model
    pred_price = model.predict(inp_df)

    # Display the predicted price
    st.write('Predicted Price:', pred_price[0])

