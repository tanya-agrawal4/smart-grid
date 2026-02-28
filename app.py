import streamlit as st
import pandas as pd
import random
import requests
import plotly.express as px

# ---------- CONFIG ----------

st.set_page_config(
    page_title="Smart AI Grid Guardian",
    layout="wide"
)

st.title("⚡ Smart AI Grid Guardian Dashboard")

# ----------------------------
# SIDEBAR
# ----------------------------

region = st.sidebar.selectbox(
    "Select Grid Region",
    ["Assam", "Tripura", "Delhi", "Gujarat"]
)

st.sidebar.write("Monitoring Live Grid...")

# ----------------------------
# 1 ENERGY GRID DASHBOARD
# ----------------------------

st.header("📊 Energy Flow Monitoring")

power_generated = random.randint(900,1100)
power_delivered = random.randint(750,900)

loss = power_generated - power_delivered

col1,col2,col3 = st.columns(3)

col1.metric("Power Generated",f"{power_generated} MW")
col2.metric("Power Delivered",f"{power_delivered} MW")
col3.metric("Loss",f"{loss} MW")

df = pd.DataFrame({
"Type":["Generated","Delivered"],
"Power":[power_generated,power_delivered]
})

fig = px.bar(df,x="Type",y="Power")

st.plotly_chart(fig,use_container_width=True)

# ----------------------------
# 2 TRANSMISSION LOSS ALERT
# ----------------------------

st.header("🚨 Transmission Line Loss")

if loss >150:
    st.error("High Loss Detected ⚠️")
else:
    st.success("Loss within safe range")

# ----------------------------
# 3 SMART METER SIMULATION
# ----------------------------

st.header("🏠 Smart Meter Consumption")

houses = {}

for i in range(1,11):
    houses[f"House {i}"] = random.randint(80,130)

# create theft
houses["House 4"] = random.randint(300,400)

meter_df = pd.DataFrame(
houses.items(),
columns=["House","Units"]
)

st.dataframe(meter_df)

# ----------------------------
# 4 THEFT DETECTION
# ----------------------------

st.header("🕵️ Theft Detection AI")

avg_use = meter_df["Units"].mean()

alerts=[]

for house,value in houses.items():

    if value > avg_use*2:
        alerts.append(f"{house} abnormal consumption detected")

if alerts:
    for a in alerts:
        st.warning(a)
else:
    st.success("No theft detected")

# ----------------------------
# 5 TRANSFORMER HEALTH
# ----------------------------

st.header("🔥 Transformer Health Prediction")

temp=random.randint(60,100)
load=random.randint(50,100)

col1,col2 = st.columns(2)

col1.metric("Transformer Temp",f"{temp} °C")
col2.metric("Load",f"{load}%")

if temp>90 or load>85:

    st.error(
    "Transformer Failure Risk ⚠️ Maintenance Required"
    )

else:

    st.success("Transformer Healthy")

# ----------------------------
# 6 WEATHER API
# ----------------------------

st.header("🌧 Weather Risk Monitoring")

API_KEY="PUT_YOUR_OPENWEATHER_KEY"

city="Agartala"

try:

    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    data=requests.get(url).json()

    temp=data["main"]["temp"]

    weather=data["weather"][0]["main"]

    st.write(f"City : {city}")
    st.write(f"Temperature : {temp}°C")
    st.write(f"Condition : {weather}")

    if weather in ["Rain","Storm"]:

        st.warning("Storm Risk → Line Damage Probability High")

except:

    st.info("Weather API Not Connected (Demo Mode)")

# ----------------------------
# 7 ALERT CENTER
# ----------------------------

st.header("🚨 Control Room Alerts")

if loss>150:

    st.write("⚠️ Transmission Loss Alert")

if temp>90:

    st.write("⚠️ Transformer Overheating")

if alerts:

    st.write("⚠️ Possible Electricity Theft")

# ----------------------------
# 8 POLICY RECOMMENDATION
# ----------------------------

st.header("🤖 AI Policy Recommendation")

if st.button("Generate Strategy"):

    suggestion=random.choice([

    "Deploy Smart meters in rural feeders",

    "Upgrade aging transformers",

    "Introduce AI drone inspection",

    "Underground cabling in high theft zones"

    ])

    st.success(suggestion)