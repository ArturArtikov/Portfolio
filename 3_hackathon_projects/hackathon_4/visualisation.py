import streamlit as st
import pandas as pd

st.write("""
## Графики выбросов в временных рядах
График данных для каждой из метрик представлен в виде ярко зеленого цвета,
за выбросы отвечает фиолетовый график.
В области скачков фиолетового графика (резкое падение вниз) и находятся
выбросы в данных.
""")

st.write("""
## Web response
График метрики **web response**
""")

df1 = pd.read_csv("web_response_vis.csv")
df1['timestamp'] = df1['timestamp'].astype('datetime64[ns]')
df1 = df1[:]

st.line_chart(
   df1, x="timestamp", y=["value", "pred"], color=["#8A2BE2", "#4cff00"]  # Optional
)



st.write("""
## Throughput
График метрики **throughput**
""")

df2 = pd.read_csv("throughput_vis.csv")
df2['timestamp'] = df2['timestamp'].astype('datetime64[ns]')
df2 = df2[:]

st.line_chart(
   df2, x="timestamp", y=["value", "pred"], color=["#8A2BE2", "#4cff00"]  # Optional
)



st.write("""
## Apdex
График метрики **apdex**
""")

df3 = pd.read_csv("apdex_vis.csv")
df3['timestamp'] = df3['timestamp'].astype('datetime64[ns]')
df3 = df3[:]

st.line_chart(
   df3, x="timestamp", y=["value", "pred"], color=["#8A2BE2", "#4cff00"]  # Optional
)


st.write("""
## Error
График метрики **error**
""")

df4 = pd.read_csv("error_vis.csv")
df4['timestamp'] = df4['timestamp'].astype('datetime64[ns]')
df4 = df4[:]

st.line_chart(
   df4, x="timestamp", y=["value", "pred"], color=["#8A2BE2", "#4cff00"]  # Optional
)