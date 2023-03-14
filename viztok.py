import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")
df = pd.read_csv('Kendaraan Bali.csv')

st.write("""

        # HELLO

""")

col1, col2 = st.columns(2)
fig = px.line(df, 
    x = "TAHUN", y = "BUS",title = "BUS")
col1.plotly_chart(fig,use_container_width = True)

fig = px.line(df, 
  x = "TAHUN", y = "SEPEDA MOTOR",title = "SEPEDA MOTOR")
col2.plotly_chart(fig,use_container_width = True)

fig = px.line(df, 
    x = "TAHUN", y = "MOBIL PENUMPANG",title = "MOBIL PENUMPANG")
col1.plotly_chart(fig,use_container_width = True)

fig = px.line(df, 
  x = "TAHUN", y = "TRUK",title = "TRUK")
col2.plotly_chart(fig,use_container_width = True)

x1 = df['BUS']
x2 = df['TRUK']

# Group data together
hist_data = [x1, x2]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)
