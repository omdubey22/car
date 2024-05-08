import streamlit as st
import pandas as pd
import numpy as np
import joblib

brand_dic={'Audi':0,
           'BMW':1,
           'Mercedes-Benz':3,
           'Renault':4,
           'Toyota':5,
           'Volkswagen':6,
           'Mitsubishi':7}

body_dic={'crossover':0,'hatch':1,'other':2,'sedan':3,'vagon':4,'van':5}

engine_type_dic={'Diesel':0,'Gas':1,'Other':2,'Petrol':3}

registration_dic={'no':0,'yes':1}

model_dic={'320': 1, 'Sprinter 212': 2, 'S 500': 3, 'Q7': 4, 'Rav 4': 5, 'A6': 6, 'Megane': 7, 'Golf IV': 8, '19': 9, 'A6 Allroad': 10, 'Passat B6': 11, 'Land Cruiser 100': 12, 'Clio': 13, '318': 14, 'Hilux': 15, 'Polo': 16, 'Outlander': 17, 'A8': 18, 'Touareg': 19, 'Vito': 20, 'Colt': 21, '100': 22, 'Z4': 23, 'Pajero Wagon': 24, 'X5': 25, 'Caddy': 26, 'Camry': 27, '528': 28, 'TT': 29, 'G 55 AMG': 30, 'X6': 31, '525': 32, 'Kangoo': 33, 'ML 350': 34, '730': 35, 'Trafic': 36, 'S 350': 37, 'Lancer': 38, 'E-Class': 39, 'Scenic': 40, '330': 41, 'Passat B5': 42, 'A3': 43, 'Land Cruiser Prado': 44, 'Caravelle': 45, 'Avensis': 46, 'GL 320': 47, 'GL 450': 48, 'Lancer X': 49, '200': 50, '520': 51, 'Tiguan': 52, 'Outlander XL': 53, 'GLS 350': 54, 'A5': 55, 'X6 M': 56, 'Golf III': 57, 'A 150': 58, 'FJ Cruiser': 59, 'Koleos': 60, 'Passat B7': 61, 'Scirocco': 62, 'M5': 63, 'Venza': 64, 'V 250': 65, 'ML 270': 66, 'C-Class': 67, 'Lupo': 68, '5 Series': 69, 'CLA 200': 70, 'T5 (Transporter)': 71, 'Highlander': 72, 'Corolla': 73, 'Galant': 74, 'CLK 240': 75, 'I3': 76, 'Land Cruiser 200': 77, 'Multivan': 78, 'Vaneo': 79, 'X1': 80, 'T5 (Transporter) ': 81, 'S 400': 82, 'S 550': 83, 'Passat CC': 84, 'A4 Allroad': 85, 'Passat B4': 86, 'Golf II': 87, 'L 200': 88, 'Jetta': 89, 'Logan': 90, 'Pajero Sport': 91, 'Sprinter 312': 92, 'Lancer X Sportback': 93, 'Golf Plus': 94, 'Up': 95, 'Amarok': 96, 'G 320': 97, 'Auris': 98, '530': 99, 'CL 500': 100, 'Dokker': 101, '540': 102, 'ML 320': 103, 'Golf VI': 104, 'Golf VII': 105, 'A 170': 106, 'Passat B3': 107, 'Laguna': 108, 'New Beetle': 109, 'Pajero': 110, 'Sprinter 319': 111, 'Viano': 112, 'Sharan': 113, 'Prius': 114, 'B 180': 115, 'Fluence': 116, '90': 117, 'T4 (Transporter)': 118, 'Duster': 119, '523': 120, 'Hiace': 121, '745': 122, 'S 320': 123, 'CLC 200': 124, 'A4': 125, '325': 126, 'Sprinter 316': 127, 'Golf V': 128, 'Fortuner': 129, 'LT': 130, 'Symbol': 131, 'A7': 132, '640': 133, 'Yaris': 134, 'CLK 200': 135, 'X3': 136, 'Sprinter 313': 137, 'S 600': 138, 'Z3': 139, '735': 140, 'Espace': 141, 'Golf Variant': 142, 'Touran': 143, 'Q5': 144, 'Master': 145, 'Sprinter 211': 146, 'Tacoma': 147, '328': 148, 'Q3': 149, 'Phaeton': 150, 'CLK 220': 151, 'Sprinter 318': 152, 'Grand Scenic': 153, 'Land Cruiser 76': 154, 'ML 280': 155, 'Land Cruiser 80': 156, 'CL 63 AMG': 157, 'T6 (Transporter) ': 158, 'R8': 159, 'GLE-Class': 160, '116': 161, 'M6': 162, 'S 63 AMG': 163, 'Sandero': 164, 'CLK 320': 165, 'SLK 200': 166, 'CLK 280': 167, '535': 168, '118': 169, 'ML 63 AMG': 170, '190': 171, '550': 172, 'Pajero Pinin': 173, 'Bora': 174, '750': 175, '80': 176, 'GLK 220': 177, 'ML 250': 178, 'IQ': 179, 'Celica': 180, '5 Series GT': 181, '740': 182, 'S4': 183, 'CLK 430': 184, 'X5 M': 185, 'A1': 186, '300': 187, '1 Series': 188, 'Grandis': 189, 'Tundra': 190, 'G 500': 191, 'GL 350': 192, 'ASX': 193, 'CLS 350': 194, 'Sienna': 195, 'T4 (Transporter) ': 196, 'B 200': 197, 'Vento': 198, '323': 199, '524': 200, '645': 201, 'T6 (Transporter)': 202, 'A 140': 203, 'Latitude': 204, 'Space Star': 205, 'Passat B8': 206, '230': 207, 'Previa': 208, 'Beetle': 209, 'Sprinter 311': 210, 'Carisma': 211, 'Eclipse': 212, 'T3 (Transporter)': 213, 'Vista': 214, '25': 215, '316': 216, 'Carina': 217, 'S5': 218, 'GL 550': 219, 'B 170': 220, '9': 221, 'GL 420': 222, 'A 180': 223, '335': 224, 'Avalon': 225, 'S8': 226, 'Modus': 227, 'R 320': 228, 'Aygo': 229, 'GL 500': 230, 'S 140': 231, 'Cross Touran': 232, 'Matrix': 233, '210': 234, '630': 235, 'ML 430': 236, 'S 65 AMG': 237, 'Virage': 238, 'Land Cruiser 105': 239, 'CLS 400': 240, '250': 241, 'S 430': 242, 'CLK 230': 243, '220': 244, 'Space Wagon': 245, 'GLS 400': 246, 'G 63 AMG': 247, 'CL 550': 248, 'Smart': 249, 'SL 500 (550)': 250, 'Sprinter 210': 251, 'S 300': 252, 'MB': 253, 'Sprinter 208': 254, 'CLS 500': 255, 'CL 55 AMG': 256, 'S 250': 257, 'SLK 350': 258, 'Sprinter 213': 259, 'ML 400': 260, 'Lancer Evolution': 261, 'CL 180': 262, 'CLS 63 AMG': 263, 'Corolla Verso': 264, 'CLA-Class': 265, '4 Series Gran Coupe': 266, '120': 267, '428': 268, 'GLK 300': 269, 'Pointer': 270, 'Captur': 271, '760': 272, 'GLC-Class': 273, 'Sandero StepWay': 274, 'CLA 220': 275, 'G 350': 276, '545': 277, 'Eos': 278, 'ML 550': 279, 'CLC 180': 280, 'Golf GTI': 281, 'ML 500': 282, '6 Series Gran Coupe': 283, 'SL 55 AMG': 284, '650': 285, '4Runner': 286, 'Sequoia': 287, '11': 288, 'Sprinter 315': 289, 'Syncro': 290, 'Scion': 291}
brand_list=['BMW', 'Mercedes-Benz', 'Audi', 'Toyota', 'Renault', 'Volkswagen', 'Mitsubishi']
body_list=['sedan', 'van', 'crossover', 'vagon', 'other', 'hatch']

engine_type_list= ['Diesel','Gas','Other','Petrol']
registration_list=['no','yes']

st.set_page_config(page_title='Used Car Prediction' )

car=pd.read_csv('Car_cleaned.csv')

def find_model(brand):
    model=car[car['Brand']==brand]['Model']
    return list(model)

@st.cache(allow_output_mutation=True)

def model_loader(path):
    model=joblib.load(path)
    return model

with st.spinner('Hold on the app is loading'):
    model_forest=model_loader("rf1_base_rf.pkl")


st.markdown("<h2 style='text-align:center;'> Used Car Prediction </h2>",unsafe_allow_html=True)

col1, col2 = st.columns(2)

mileage=col1.number_input(label='No of Miles Driven',help='hown much car drive?')

year=col1.slider('Enter the year when car was manufactured',1980,2020,2005,help='The year when car is manufactured')

brand_inp=col1.selectbox(label='Enter the brand of the car',options=brand_list,help='From which brand the car belongs')
brand = brand_dic[brand_inp]

engine_type=col1.selectbox(label='enter the engine type(fuel)',options=engine_type_list,help='in which gas the car is run')
engine_type=engine_type_dic[engine_type]

engineV=col1.number_input(label='enter the volume of car engine', max_value=6.4, help='enter the volume of  engine')
engineV=float(engineV)

body_type=col2.selectbox(label='enter the body type of the car',options=body_list,help='select the body type of the car')
body_type=body_dic[body_type]

if brand_inp=='Audi':
    model_inp=col2.selectbox('enter the model of the audi',options=find_model('Audi'))
    model=model_dic[model_inp]

elif brand_inp=='Renault':
    model_inp=col2.selectbox('enter the model of the Renault',options=find_model('Renault'))
    model=model_dic[model_inp]

elif brand_inp=='Toyota':
    model_inp=col2.selectbox('enter the model of the Toyota',options=find_model('Toyota'))
    model=model_dic[model_inp]

elif brand_inp=='BMW':
    model_inp=col2.selectbox('enter the model of the BMW',options=find_model('BMW'))
    model=model_dic[model_inp]

elif brand_inp=='Mercedes-Benz':
    model_inp=col2.selectbox('enter the model of the Mercedes-Benz',options=find_model('Mercedes-Benz'))
    model=model_dic[model_inp]

elif brand_inp=='Mitsubishi':
    model_inp=col2.selectbox('enter the model of the Mitsubishi',options=find_model('Mitsubishi'))
    model=model_dic[model_inp]

elif brand_inp=='Volkswagen':
    model_inp=col2.selectbox('enter the model of the Volkswagen',options=find_model('Volkswagen'))
    model=model_dic[model_inp]


regis=col2.selectbox(label='The car have registration',options=registration_list, help='the car have registration or not')
regis=registration_dic[regis]

inp_array=np.array([[mileage,engineV,year,brand,body_type,engine_type,regis,model]])

predict=col1.button('Predict')

if predict:
    pred=model_forest.predict(inp_array)
    if pred<0:
        st.error('the values must be irrelevent,try again by giving relevant information')
    pred=round(float(pred),3)
    # Define the exchange rate
    exchange_rate_usd_to_inr = 75  # Example exchange rate, replace with the current rate

# Convert the predicted price from dollars to Indian Rupees
    predicted_price_inr = pred * exchange_rate_usd_to_inr

# Display the predicted price in Indian Rupees
    st.write('The predicted price of the car is ₹' + str(predicted_price_inr))
