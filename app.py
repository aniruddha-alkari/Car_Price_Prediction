import streamlit as st

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# ---------------------------------------
# Page Title
# ---------------------------------------
st.title("🚗 Used Car Price Prediction")

st.write("Enter car details and click Predict.")

# ---------------------------------------
# Input Fields
# ---------------------------------------

gender = st.selectbox(
    "Gender",
    ["male", "female"]
)

model = st.selectbox(
    "Model",
    ['Alto', 'Grand', 'i20', 'Ecosport', 'Wagon R', 'i10', 'Venue', 'Swift', 'Verna', 'Duster', 
    'Cooper', 'Ciaz', 'C-Class', 'Innova', 'Baleno', 'Swift Dzire', 'Vento', 'Creta', 'City', 
    'Bolero', 'Fortuner', 'KWID', 'Amaze', 'Santro', 'XUV500', 'KUV100', 'Ignis', 'RediGO', 
    'Scorpio', 'Marazzo', 'Aspire', 'Figo', 'Vitara', 'Tiago', 'Polo', 'Seltos', 'Celerio', 'GO', 
    '5', 'CR-V', 'Endeavour', 'KUV', 'Jazz', '3', 'A4', 'Tigor', 'Ertiga', 'Safari', 'Thar', 'Hexa', 
    'Rover', 'Eeco', 'A6', 'E-Class', 'Q7', 'Z4', '6', 'XF', 'X5', 'Hector', 'Civic', 'D-Max', 
    'Cayenne', 'X1', 'Rapid', 'Freestyle', 'Superb', 'Nexon', 'XUV300', 'Dzire VXI', 'S90', 'WR-V', 
    'XL6', 'Triber', 'ES', 'Wrangler', 'Camry', 'Elantra', 'Yaris', 'GL-Class', '7', 'S-Presso', 
    'Dzire LXI', 'Aura', 'XC', 'Ghibli', 'Continental', 'CR', 'Kicks', 'S-Class', 'Tucson', 'Harrier', 
    'X3', 'Octavia', 'Compass', 'CLS', 'redi-GO', 'Glanza', 'Macan', 'X4', 'Dzire ZXI', 'XC90', 
    'F-PACE', 'A8', 'MUX', 'GTC4Lusso', 'GLS', 'X-Trail', 'XE', 'XC60', 'Panamera', 'Alturas', 
    'Altroz', 'NX', 'Carnival', 'C', 'RX', 'Ghost', 'Quattroporte', 'Gurkha']
)

vehicle_age = st.number_input(
    "vehicle_age",
    min_value=0,
    max_value=30,
    value=15
)

km_driven = st.number_input(
    "km_driven",
    min_value=100,
    max_value=4000000,
    value=50000
)

seller_type = st.selectbox(
    "seller_type",
    ['Individual', 
    'Dealer', 
    'Trustmark Dealer']
)

fuel_type = st.selectbox(
    "fuel_type",
    ['Petrol', 
    'Diesel', 
    'CNG', 
    'LPG', 
    'Electric']
)

transmission_type = st.selectbox(
    "transmission_type",
    ['Manual', 'Automatic']
)

mileage = st.number_input(
    "mileage",
    min_value=2,
    max_value=35,
    value=15
)

engine = st.number_input(
    "engine",
    min_value=700,
    max_value=7000,
    value=5000
)

max_power = st.number_input(
    "max_power",
    min_value=35,
    max_value=650,
    value=250
)

seats = st.number_input(
    "seats",
    min_value=0,
    max_value=9,
    value=5
)

# ---------------------------------------
# Predict Button
# ---------------------------------------

if st.button("Predict Car Price"):

    data = CustomData(
        model = model,
        vehicle_age = vehicle_age,
        km_driven = km_driven,
        seller_type = seller_type,
        fuel_type = fuel_type,
        transmission_type = transmission_type,
        mileage = mileage,
        engine = engine,
        max_power = max_power,
        seats = seats
    )

    pred_df = data.get_data_as_data_frame()

    pipeline = PredictPipeline()

    result = pipeline.predict(pred_df)

    st.success(f"Predicted Car Price : {result[0]:.2f}")
