import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('streamlit_template/data/kart_stats.csv')
# st.dataframe(df_kart)

df_kart = df_kart[['Body','Weight','Acceleration','Ground Speed','Water Speed','Anti-Gravity Speed','Air Speed']]

# Visualization 1
st.dataframe(df_kart.style
             .highlight_max(color='green',axis=0,subset=['Weight','Acceleration','Ground Speed','Water Speed','Anti-Gravity Speed','Air Speed'])
             .highlight_min(color='red',axis=0,subset=['Weight','Acceleration','Ground Speed','Water Speed','Anti-Gravity Speed','Air Speed'])
)

st.write('# Visualizations')
# Visualization 2 - Line Chart
df_kart_swift = df_kart.sort_values('Acceleration', ascending=False)
st.write('Viz 1: Relationship between Kart Weight and Acceleration')
st.line_chart(df_kart_swift, x='Weight',y='Acceleration')

# Visualization 3 - Bar Chart
st.write('Viz 2: Kart Speeds by Medium')
st.bar_chart(df_kart, x='Body', y=['Ground Speed', 'Water Speed', 'Anti-Gravity Speed', 'Air Speed'])

# Part 3
st.write('# Single Kart Statistics')
st.write('Viz 3: Dynamic Visualization')
chosen_kart = st.selectbox('Pick a Kart:', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns=['Body'])

# Unpivot
df_unp_kart = df_kart.unstack().rename_axis(['Category','row number']).reset_index().drop(columns='row number').rename({0:'Strength'}, axis=1)
st.bar_chart(df_unp_kart, x='Category', y='Strength')

