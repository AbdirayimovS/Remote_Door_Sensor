import streamlit as st
import pyrebase #pip install pyrebase4
import time
from datetime import datetime
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

firebaseConfig = {
  'apiKey': st.secrets["apikey"],
  'authDomain': "remote-door-sensor.firebaseapp.com",
  'databaseURL': "https://remote-door-sensor-default-rtdb.firebaseio.com",
  'projectId': "remote-door-sensor",
  'storageBucket': "remote-door-sensor.appspot.com",
  'messagingSenderId': "51676097347",
  'appId': "1:51676097347:web:886a976da0c3e3eb181df6",
  'measurementId': "G-Y6HGEP1K38"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
users = db.get()
df = pd.DataFrame(users.val(), index=[0]).T
print(df)
df.index = df.index.astype(int)
last_update = df.tail(1)
last_time_update = last_update.index[0]
st.header("Is Door Opened?")

print(last_update)
#
dttime = datetime.utcfromtimestamp(last_time_update).strftime('%Y-%m-%d %H:%M:%S')


#-----------------------------------------------------#

st.header('Hello 🌎! Door Sensor of Sardor Abdiraimov')
if st.button('Update'):
    st.header(last_update)
    # show the last update
    st.header(dttime)
    #visualize the true false data over the time in streamlit

    st.line_chart(df)
    st.table(df.tail(10))
    st.balloons()





