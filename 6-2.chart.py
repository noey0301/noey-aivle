import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
# px 모듈이 없다고 에러가 나는 경우에만 아래 방법으로 plotly 라이브러리 설치
# File > New > Terminal 선택 후, 창에 다음 구분 실행 pip install plotly 

st.header('Unit 3. Streamlit Simple chart')

# # https://raw.githubusercontent.com/huhshin/streamlit/master/data_sales.csv 읽고 확인하기
chart_data = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_sales.csv')
st.dataframe(chart_data)

st.subheader('3-1. Simple Line chart')
# #use_container_width=True 가로로 화면에 꽉 채워 줌
st.line_chart(chart_data,use_container_width=True)

st.subheader('3-2. Simple Bar chart')
st.bar_chart(chart_data)

st.subheader('3-3. Simple area chart')
st.area_chart(chart_data)


st.header('Unit 4. Altair chart') 
# https://raw.githubusercontent.com/huhshin/streamlit/master/data_retail.csv 읽고 
# melt 함수를 사용하여 데이터프레임 unpivot하기
df = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_retail.csv')
st.dataframe(df)
df_melted = pd.melt(df,id_vars=['date'],var_name=['teams'],value_name='sales')
st.dataframe(df_melted)

# columns 함수를 이용하여 좌-원본 데이터, 우-변환 데이터 확인하기
col1,col2=st.columns(2)
with col1:
    st.text('원본 데이터')
    st.dataframe(df)
with col2:
    st.text('변경 데이터')
    st.dataframe(df_melted)

    
st.subheader('4-1. Altair Line chart')
chart = alt.Chart(df_melted,title='일별 팀 매출 비교').mark_line().encode(x='date',y='sales',color='teams',strokeDash='teams').properties(width=650,height=350)
st.altair_chart(chart, use_container_width=True)

st.subheader('4-2. Altair Bar chart')

chart = alt.Chart(df_melted,title='일별 팀 매출').mark_bar().encode(x='date',y='sales',color='teams',order=alt.Order('sales'))
text=alt.Chart(df_melted).mark_text(color='black',baseline='line-top').encode(x='date',y='sales',detail='teams',text=alt.Text('sales:Q'))

st.altair_chart(chart+text,use_container_width=True)
    
    
st.subheader('4-3. Altair Scatter chart')

# https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv 읽고 확인하기
iris = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv')
st.dataframe(iris)

# # caption으로 'sepal:꽃받침, petal:꽃잎' 설명 출력하기 


# # petal_length, petal_width로 Altair Circle chart 그리기
chart = alt.Chart(iris).mark_circle().encode(x='petal_length',y='petal_width',color='species')
st.altair_chart(chart,use_container_width=True)    

st.header('Unit 5. Plotly chart')

# # https://raw.githubusercontent.com/huhshin/streamlit/master/data_medal.csv 읽고 확인하기
medal = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_medal.csv')
st.dataframe(medal)
    

st.subheader('5-1. Plotly Pie/Donut chart') 
fig = px.pie(medal,values='gold',names='nation',title='올림픽 양궁 금메달 현황',hole=0.2)
fig.update_traces(textposition='inside',textinfo='percent+label+value')
fig.update_layout(font=dict(size=16))
st.plotly_chart(fig)

# # fig.update(layout_showlegend=False)  # 범례 표시 제거

st.subheader('5-2. Plotly Bar chart')
# text_auto=True 값 표시 여부
fig = px.bar(medal,x='nation',y=['gold','silver','bronze'],title='올림픽 양궁 메달 현황',text_auto=True)


st.plotly_chart(fig)


col1,col2=st.columns(2)
with col1:
    fig = px.pie(medal,values='gold',names='nation',hole=0.2)
    fig.update_traces(textposition='inside',textinfo='percent+label+value')
    fig.update_layout(font=dict(size=16))
    st.plotly_chart(fig,use_container_width=True)
with col2:
    fig = px.pie(medal,values='gold',names='nation')
    fig.update_traces(textposition='inside',textinfo='percent+label+value')
    fig.update_layout(font=dict(size=16))
    st.plotly_chart(fig,use_container_width=True)
# # 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\6-2.chart.py
