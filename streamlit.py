import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
import boto3
import io
import os

bucket_name = "forestclassification"  
model_key = os.getenv("MODEL_KEY")             
encoder_key = os.getenv("ENCODER_KEY")         
skew_key = os.getenv("SKEW_KEY")               
label_encoder_key = os.getenv("LABEL_ENCODER_KEY")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")


s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)
@st.cache_resource
def load_all_from_s3():
    # Load OneHotEncoder
    ohe_obj = s3.get_object(Bucket=bucket_name, Key=encoder_key)
    loaded_encoder = pickle.load(io.BytesIO(ohe_obj['Body'].read()))

    # Load skew constants
    skew_obj = s3.get_object(Bucket=bucket_name, Key=skew_key)
    loader_skewconstant = pickle.load(io.BytesIO(skew_obj['Body'].read()))

    # Load model
    model_obj = s3.get_object(Bucket=bucket_name, Key=model_key)
    model = joblib.load(io.BytesIO(model_obj['Body'].read()))

    # Load label encoder
    label_obj = s3.get_object(Bucket=bucket_name, Key=label_encoder_key)
    label_encoder = pickle.load(io.BytesIO(label_obj['Body'].read()))

    return loaded_encoder, loader_skewconstant, model, label_encoder
# with open('ohe_wildernessandsoil.pkl', 'rb') as file:
#     loaded_encoder = pickle.load(file)
# with open('skew_constants.pkl','rb') as file:
#     loader_skewconstant=pickle.load(file)
# model = joblib.load('model_cal_lightgbm_adasyn_pipeline.pkl')
# with open('label_encoder_cover_type.pkl', 'rb') as file:
#     label_encoder = pickle.load(file)
# st.title("Forest Class Classification")


st.title("Terrain Feature Input")

# --- Elevation ---
col1, col2 = st.columns(2)
with col1:
    elevation_slider = st.slider("Elevation (drag)", 1500, 4000, 2000)
with col2:
    elevation_input = st.number_input("Elevation (type)", 1500, 4000, elevation_slider)

# Keep both in sync (typed value overrides drag)
elevation = elevation_input if elevation_input != elevation_slider else elevation_slider

# --- Aspect ---
col1, col2 = st.columns(2)
with col1:
    aspect_slider = st.slider("Aspect (drag)", 0, 360, 180)
with col2:
    aspect_input = st.number_input("Aspect (type)", 0, 360, aspect_slider)

aspect = aspect_input if aspect_input != aspect_slider else aspect_slider

# --- Slope ---
col1, col2 = st.columns(2)
with col1:
    slope_slider = st.slider("Slope (drag)", 0, 62, 10)
with col2:
    slope_input = st.number_input("Slope (type)", 0, 62, slope_slider)

slope = slope_input if slope_input != slope_slider else slope_slider

# --- Horizontal_Distance_To_Hydrology ---
col1, col2 = st.columns(2)
with col1:
    Horizontal_Distance_To_Hydrology_slider = st.slider("Horizontal Distance To Hydrology (drag)", 0, 1340, 100)
with col2:
    Horizontal_Distance_To_Hydrology_input = st.number_input("Slope (type)", 0, 1340, Horizontal_Distance_To_Hydrology_slider)

Horizontal_Distance_To_Hydrology = Horizontal_Distance_To_Hydrology_input if Horizontal_Distance_To_Hydrology_input != Horizontal_Distance_To_Hydrology_slider else Horizontal_Distance_To_Hydrology_slider

# --- Vertical_Distance_To_Hydrology ---
col1, col2 = st.columns(2)
with col1:
    Vertical_Distance_To_Hydrology_slider = st.slider("Vertical Distance To Hydrology (drag)", -148, 555, 0)
with col2:
    Vertical_Distance_To_Hydrology_input = st.number_input("Slope (type)", -148, 555, Vertical_Distance_To_Hydrology_slider)

Vertical_Distance_To_Hydrology = Vertical_Distance_To_Hydrology_input if Vertical_Distance_To_Hydrology_input != Vertical_Distance_To_Hydrology_slider else Vertical_Distance_To_Hydrology_slider

# --- Horizontal_Distance_To_Roadways ---
col1, col2 = st.columns(2)
with col1:
    Horizontal_Distance_To_Roadways_slider = st.slider("Horizontal Distance To Roadways (drag)", 0, 7200, 3600)
with col2:
    Horizontal_Distance_To_Roadways_input = st.number_input("Horizontal Distance To Roadways (type)", 0, 7200, Horizontal_Distance_To_Roadways_slider)

Horizontal_Distance_To_Roadways = Horizontal_Distance_To_Roadways_input if Horizontal_Distance_To_Roadways_input != Horizontal_Distance_To_Roadways_slider else Horizontal_Distance_To_Roadways_slider

# --- Horizontal_Distance_To_Fire_Points ---
col1, col2 = st.columns(2)
with col1:
    Horizontal_Distance_To_Fire_Points_slider = st.slider("Horizontal Distance To Fire Points (drag)", 0, 7200, 3600)
with col2:
    Horizontal_Distance_To_Fire_Points_input = st.number_input("Horizontal Distance To Fire Points (type)", 0, 7200, Horizontal_Distance_To_Fire_Points_slider)

Horizontal_Distance_To_Fire_Points = Horizontal_Distance_To_Fire_Points_input if Horizontal_Distance_To_Fire_Points_input != Horizontal_Distance_To_Fire_Points_slider else Horizontal_Distance_To_Fire_Points_slider


# --- HillShade 9AM ---
col1, col2 = st.columns(2)
with col1:
    HS9_slider = st.slider("HillShade 9AM (drag)", 0, 255, 155)
with col2:
    HS9_input = st.number_input("HillShade 9AM (type)", 0, 255, HS9_slider)

HS9 = HS9_input if HS9_input != HS9_slider else HS9_slider

# --- HillShade 12PM ---
col1, col2 = st.columns(2)
with col1:
    HSnoon_slider = st.slider("HillShade Noon (drag)", 0, 255, 155)
with col2:
    HSnoon_input = st.number_input("HillShade Noon (type)", 0, 255, HSnoon_slider)

HSnoon = HSnoon_input if HSnoon_input != HSnoon_slider else HSnoon_slider

# --- HillShade 3PM ---
col1, col2 = st.columns(2)
with col1:
    HS3_slider = st.slider("HillShade 3PM (drag)", 0, 255, 155)
with col2:
    HS3_input = st.number_input("HillShade 3PM (type)", 0, 255, HS3_slider)

HS3 = HS3_input if HS3_input != HS3_slider else HS3_slider

# --- Wildfire ---
col1, col2 = st.columns(2)
with col1:
    Wildfire_slider = st.slider("Wildfire (drag)", 1, 4, 2)
with col2:
    Wildfire_input = st.number_input("Wildfire (type)", 1, 4, Wildfire_slider)

Wildfire = Wildfire_input if Wildfire_input != Wildfire_slider else Wildfire_slider

# --- Soil Type ---
col1, col2 = st.columns(2)
with col1:
    Soil_Type_slider = st.slider("Soil Type (drag)", 1, 40, 20)
with col2:
    Soil_Type_input = st.number_input("Soil Type (type)", 1, 40, Soil_Type_slider)

Soil_Type = Soil_Type_input if Soil_Type_input != Soil_Type_slider else Soil_Type_slider

# Block or warn for invalid value
if Soil_Type == 15:
    st.warning("Soil Type 15 is not trained in this Model. Please select another value.")
   
loaded_encoder, loader_skewconstant, model, label_encoder = load_all_from_s3()
if Soil_Type != 15:
    raww_data = pd.DataFrame([{
            'Elevation':elevation,
            'Aspect':aspect,
            'Slope':slope,
            'Horizontal_Distance_To_Hydrology':Horizontal_Distance_To_Hydrology,
            'Vertical_Distance_To_Hydrology':Vertical_Distance_To_Hydrology,
            'Horizontal_Distance_To_Roadways':Horizontal_Distance_To_Roadways,
            'Hillshade_9am': HS9,
            'Hillshade_Noon':HSnoon,
            'Hillshade_3pm':HS3,
            'Horizontal_Distance_To_Fire_Points':Horizontal_Distance_To_Fire_Points,
            'Wilderness_Area': Wildfire,
            'Soil_Type': Soil_Type
        }])
    raw_data=raww_data.copy()
    # Encoding 
    encoded = loaded_encoder.transform(raw_data[['Wilderness_Area', 'Soil_Type']]).toarray().astype(int)
    cols = loaded_encoder.get_feature_names_out(['Wilderness_Area', 'Soil_Type'])
    encoded_df = pd.DataFrame(encoded, columns=cols)
    
    #Skewness
    raw_data['Hillshade_9am_trans'] = np.sqrt(
                                    loader_skewconstant["Hillshade_9am_max"] + 1 - raw_data['Hillshade_9am'])
    raw_data['Vertical_Distance_To_Hydrologyr2'] = np.sqrt(
                                    raw_data['Vertical_Distance_To_Hydrology'] - loader_skewconstant["Vertical_Distance_To_Hydrology_min"] + 1 )
    raw_data['Horizontal_Distance_To_Hydrologyr2'] = np.sqrt(raw_data['Horizontal_Distance_To_Hydrology'])
    raw_data['Aspectr2'] = np.sqrt(raw_data['Aspect'])

    raw_data.drop(columns=(['Hillshade_9am','Vertical_Distance_To_Hydrology','Horizontal_Distance_To_Hydrology','Aspect','Wilderness_Area', 'Soil_Type']),inplace=True)
    final_df = pd.concat(
    [raw_data, encoded_df],
    axis=1
    )
    out=model.predict(final_df)
    encoded_value = out
    predicted_class = label_encoder.inverse_transform([encoded_value])[0]
    st.json(raww_data.to_dict(orient='records'))
    st.markdown(f"### The Predicted Class is **:green[{predicted_class}]**")





