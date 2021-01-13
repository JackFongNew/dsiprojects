#import package
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import pickle

#import the data
hdb_raw = pd.read_csv("dataset/hdb_17_features_dropped_3.csv")
image = Image.open("hdb.JPG")
st.title("Welcome to the HDB Flat Resale Price Prediction App")
st.image(image, use_column_width=True)

#checking the data
st.write("This application will show you the range of the HDB flat resale prices based on your selected options")
check_data = st.checkbox("See the simple data")
if check_data:
    st.write(hdb_raw.head())
st.write("Now let's find out how much the prices when we choosing some parameters.")

#input the numbers
def user_input_features():
    floor_area_sqm = st.slider("Living area (sqm)",int(hdb_raw.floor_area_sqm.min()),int(hdb_raw.floor_area_sqm.max()),int(hdb_raw.floor_area_sqm.mean()))
    bedroom      = st.slider("Number of bedroom (unit)",int(hdb_raw.bedroom.min()),int(hdb_raw.bedroom.max()),int(hdb_raw.bedroom.mean()))
    mean_floor    = st.slider("Mean floor (level)",int(hdb_raw.mean_floor.min()),int(hdb_raw.mean_floor.max()),int(hdb_raw.mean_floor.mean()))
    remaining_year = st.slider("Remaing lease (year) ",int(hdb_raw.remaining_year.min()),int(hdb_raw.remaining_year.max()),int(hdb_raw.remaining_year.mean()))
    dist_to_mrt = st.slider("Distance to MRT (meter) ",int(hdb_raw.dist_to_mrt.min()),int(hdb_raw.dist_to_mrt.max()),int(hdb_raw.dist_to_mrt.mean()))
    dist_to_mall = st.slider("Distance to Mall (meter) ",int(hdb_raw.dist_to_mall.min()),int(hdb_raw.dist_to_mall.max()),int(hdb_raw.dist_to_mall.mean()))
    dist_to_hawker = st.slider("Distance to Hawker (meter) ",int(hdb_raw.dist_to_hawker.min()),int(hdb_raw.dist_to_hawker.max()),int(hdb_raw.dist_to_hawker.mean()))
    dist_to_child_centre = st.slider("Distance to Child Care/Kindergarten (meter) ",int(hdb_raw.dist_to_child_centre.min()),int(hdb_raw.dist_to_child_centre.max()),int(hdb_raw.dist_to_child_centre.mean()))
    dist_to_city = st.slider("Distance to City (meter) ",int(hdb_raw.dist_to_city.min()),int(hdb_raw.dist_to_city.max()),int(hdb_raw.dist_to_city.mean()))
    dist_to_pri_sch = st.slider("Distance to Primary School (meter) ",int(hdb_raw.dist_to_pri_sch.min()),int(hdb_raw.dist_to_pri_sch.max()),int(hdb_raw.dist_to_pri_sch.mean()))
    town = st.selectbox('Town',('ANG MO KIO','BEDOK','BISHAN','BUKIT BATOK','BUKIT MERAH','BUKIT PANJANG',
                                        'BUKIT TIMAH','CENTRAL AREA','CHOA CHU KANG','CLEMENTI','GEYLANG','HOUGANG',
                                        'JURONG EAST','JURONG WEST','KALLANG/WHAMPOA','MARINE PARADE','PASIR RIS','PUNGGOL',
                                        'QUEENSTOWN','SENGKANG','SERANGOON','TAMPINES','TOA PAYOH','YISHUN'))
    flat_type = st.selectbox('Flat type',('2 ROOM','3 ROOM','4 ROOM','5 ROOM','EXECUTIVE'))
    flat_model = st.selectbox('Flat model',('DBSS','Improved','Maisonette','Model A','New Generation',
                                                    'Premium Apartment','Standard','Terrace','Type S2'))
    data = {'floor_area_sqm': floor_area_sqm,
            'bedroom': bedroom,
            'mean_floor': mean_floor,
            'remaining_year': remaining_year,
            'town': town,
            'flat_type': flat_type,
            'flat_model': flat_model,
            'dist_to_mrt': dist_to_mrt,
            'dist_to_mall': dist_to_mall,
            'dist_to_hawker': dist_to_hawker,
            'dist_to_child_centre': dist_to_child_centre,
            'dist_to_city': dist_to_city,
            'dist_to_pri_sch': dist_to_pri_sch}
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()

# Combines user input features with entire penguins dataset
# This will be useful for the encoding phase
hdb = hdb_raw.drop(columns=['resale_price'])
df = pd.concat([input_df,hdb],axis=0)

# Encoding of ordinal features
df = pd.get_dummies(data=df, columns=['town','flat_type','flat_model'])
df = df.drop(columns=['town_SEMBAWANG', 'town_WOODLANDS', 'flat_type_1 ROOM', 'flat_model_2-room', 'flat_type_MULTI-GENERATION',
                      'flat_model_Adjoined flat', 'flat_model_Improved-Maisonette', 'flat_model_Model A-Maisonette',
                      'flat_model_Model A2', 'flat_model_Multi Generation', 'flat_model_Premium Apartment Loft',
                      'flat_model_Premium Maisonette', 'flat_model_Simplified', 'flat_model_Type S1', 'flat_model_Apartment'])
df = df[:1] # Selects only the first row (the user input data)

# Displays the user input features
st.subheader('User Input features')
st.write(df)

# Reads in saved regression model
pickle_model = pickle.load(open('finalized_model.pkl', 'rb'))

hdb_final = pd.read_csv("dataset/hdb_17_final_features.csv")
#splitting your data
X = hdb_final.drop(columns=['resale_price'], axis=1)
y = hdb_final['resale_price']

# Apply model to make predictions
pickle_model.predict(X)
errors = np.sqrt(mean_squared_error(y, pickle_model.predict(X)))
predictions = pickle_model.predict(df)

#checking prediction house price
if st.button("Click Me!"):
    st.header("Your house price prediction is SGD {}".format(int(predictions)))
    st.subheader("Your range of prediction is SGD {} - SGD {}".format(int(predictions-errors),int(predictions+errors)))
