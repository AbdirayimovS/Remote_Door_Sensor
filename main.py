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

print(last_update)
#
dttime = datetime.utcfromtimestamp(last_time_update).strftime('%Y-%m-%d %H:%M:%S')


#-----------------------------------------------------#
def main():
    st.header('Hello 🌎! Let`s check the Door Sensor Status')
    st.metric("Door Status", dttime, last_update[1])
    if st.button('Update'):
        st.header(dttime)
        st.table(last_update)
        st.balloons()
        st.line_chart(last_update)

if __name__ == '__main__':
    main()




