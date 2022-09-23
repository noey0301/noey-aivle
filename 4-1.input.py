# streamlit 라이브러리와 datetime 모듈 불러오기
import streamlit as st
from datetime import datetime  

st.title('Unit 4. Input Widgets')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/widgets')

st.header('1. Button')

if st.button('누르지 마셈'):
    st.write('누르지 말랬자너!!!')
else:
    st.write('누르고 싶지?')


st.header('2. Radio button')
genre = st.radio('좋아하는 가수를 선택하시오',('야마시타타츠로','자미로콰이','언니네이발관'))

if genre == '야마시타타츠로':
    st.write('일뽕쉨')
elif genre=='자미로콰이':
    st.write('에시드째즈충')
else:
    st.write('홍머병쉨')


st.header('3. Checkbox')
agree = st.checkbox('사람이십니까?')
if agree:
    st.write('로봇이군요 '*5)


st.header('4. Select box')
option = st.selectbox('장르선택 해보세요',('재즈','모던락','시티팝'))
st.write('네',option,'충이시군요')


st.header('5. Multi select')
options = st.multiselect('싫어하는 사람을 모두 고르세요',['아카지현','아오은태','키민정'])

for i in options:
    st.write(i)




st.header('6. Input: Text/Number')

st.subheader('**_text_input_**')
title =st.text_input('좋아하는 사람을 입력하세요','적당히해라')
st.write('당신이 좋아하는 사람은:',title)

st.subheader('**_number_input_**')
number = st.number_input('insert a number(1-10)',min_value=1,max_value=10000,value=5,step=100)
st.write('The current number is:',number)

st.header('7. Date input')
ymsd = st.date_input('When is your birthday',datetime(2022, 3, 11))
st.write('Your birthday is:', ymsd)

st.header('8. Slider')

st.subheader('**_Slider- 이전 구간_**')
age = st.slider('나이가 어떻게 되세요 ? ', 0, 130, 25)
st.write('I m ', age, ' years old')

st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
values = st.slider('값 구간을 선택하세요 ', 0.0, 100.0, (25.0, 75.0))
st.write('Values: ', values)

st.subheader('**_년 월 일 사이 구간_**')

slider_date = st.slider('날짜 구간을 선택하셈 ',min_value=datetime(2022,1,1),max_value=datetime(2022,12,31),value=(datetime(2022,6,1),datetime(2022,7,31)),
              format='YY/MM/DD')
st.write('slider_date',slider_date)
st.write('시작',slider_date[0].date(),'종료',slider_date[1].date())


# 년 월 일 시 사이 구간
# slider_time = st.slider(
#     'Select a range of datetime?',
#     datetime(2022, 1, 1, 0, 30), datetime(2022, 12, 31, 0, 30),
#     value=(datetime(2022, 7, 1, 0, 30), datetime(2022, 10, 31, 9, 30)),
#     format='MM/DD/YY - hh:mm')
# st.write('Slider time: ', slider_time)

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\4-1.input.py