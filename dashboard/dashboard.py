import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bike Sharing Dataset", layout="wide")

st.title("Bike Sharing Data Analysis Dashboard")

@st.cache
def load_data():
    day_data = pd.read_csv(r'./dashboard/day.csv')  # Pastikan path sesuai
    return day_data

data = load_data()

st.sidebar.title("Filter Options")

season = st.sidebar.selectbox("Select Season", (1, 2, 3, 4), format_func=lambda x: {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}[x])

weather = st.sidebar.selectbox("Select Weather Situation", (1, 2, 3), format_func=lambda x: {
    1: "Clear, Few clouds, Partly cloudy",
    2: "Mist + Cloudy, Mist + Broken clouds",
    3: "Light Snow, Light Rain"
}[x])

filtered_data = data[(data['season'] == season) & (data['weathersit'] == weather)]

st.write(f"**Filtered Data:** Season: {season}, Weather: {weather}")
st.write(filtered_data.head())

st.write("### Data Visualizations")

st.write("**Rental Count Distribution by Weather**")
plt.figure(figsize=(8, 5))
sns.barplot(x='weathersit', y='cnt', data=data, estimator=sum)
plt.title('Effect of Weather on Bike Rentals')
plt.xlabel('Weather Situation')
plt.ylabel('Total Bike Rentals')
st.pyplot(plt)

st.write("**Rental Count Distribution by Season**")
plt.figure(figsize=(8, 5))
sns.barplot(x='season', y='cnt', data=data, estimator=sum)
plt.title('Bike Rentals Across Seasons')
plt.xlabel('Season')
plt.ylabel('Total Bike Rentals')
st.pyplot(plt)

st.write("### Conclusion")
st.write("""
1. Cuaca yang cerah atau berawan ringan (clear, partly cloudy) cenderung meningkatkan jumlah penyewaan sepeda. Cuaca buruk seperti salju ringan atau hujan ringan mengurangi jumlah penyewaan sepeda.
2. Jumlah penyewaan sepeda mencapai puncaknya selama musim panas (summer) dan musim gugur (fall), sementara musim semi (spring) dan musim dingin (winter) menunjukkan jumlah penyewaan yang lebih rendah.
""")
