import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Sensex Option Chain", page_icon="📈", layout="wide")

st.title("📈 Sensex Option Chain")
st.caption("Demo app for option chain layout. Real trading ke liye broker API connect karni padegi.")

spot = st.number_input("Sensex Spot Value", value=80000, step=50)
expiry = st.selectbox("Expiry", ["This Week", "Next Week", "Monthly"])

st.subheader("Option Chain Table")

strikes = list(range(int(spot - 1000), int(spot + 1001), 100))

rows = []
for strike in strikes:
    ce_ltp = max(1, round(abs(spot - strike) / 10 + random.uniform(5, 50), 2))
    pe_ltp = max(1, round(abs(spot - strike) / 10 + random.uniform(5, 50), 2))
    rows.append({
        "Strike": strike,
        "CE LTP": ce_ltp,
        "CE OI": random.randint(1000, 50000),
        "CE Volume": random.randint(100, 10000),
        "PE LTP": pe_ltp,
        "PE OI": random.randint(1000, 50000),
        "PE Volume": random.randint(100, 10000),
    })

df = pd.DataFrame(rows)
st.dataframe(df, use_container_width=True)

st.subheader("Trade Panel")
col1, col2, col3 = st.columns(3)

with col1:
    side = st.selectbox("Side", ["Buy", "Sell"])
with col2:
    opt_type = st.selectbox("Option Type", ["CE", "PE"])
with col3:
    strike_sel = st.selectbox("Strike Price", df["Strike"].tolist())

qty = st.number_input("Quantity", min_value=1, value=1, step=1)

st.info("Ye demo panel hai. Real trade placement broker API se hoga.")

if st.button("Place Trade"):
    st.success(f"{side} {opt_type} at strike {strike_sel} x {qty} selected.")
    st.warning("Is demo me actual order place nahi ho raha.")

st.subheader("Deployment Note")
st.write("GitHub repo me ye file `streamlit_app.py` naam se upload karo, phir Streamlit Community Cloud me deploy karo.")
