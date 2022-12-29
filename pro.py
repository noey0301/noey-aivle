import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from PIL import Image

stop = "stop.png"
come = "come.png"
empty= "empty.png"
img1 = Image.open(stop).convert('RGB')
img2 = Image.open(come).convert('RGB')
img3 = Image.open(empty)
def main():
    st.image('logo.png')
    df=pd.read_excel('df.xlsx')
    df['인구']=df['인구']/10
    df1=df.iloc[::2,:]
    df2=df.iloc[1::2,:]
    st.pydeck_chart(pdk.Deck(map_style=None,initial_view_state=pdk.ViewState(latitude=37.5215737,longitude=126.9221228,zoom=11,pitch=50,),
        layers=[pdk.Layer('ColumnLayer',data=df1,get_position='[lon, lat]',radius=100,elevation_scale=4,get_elevation='인구',
                          get_fill_color=[161, 243, 114],pickable=True,extruded=True,auto_highlight=True),
               pdk.Layer('ColumnLayer',data=df2,get_position='[lon, lat]',radius=100,elevation_scale=4,get_elevation='인구',
                         get_fill_color=[239, 92, 88],pickable=True,extruded=True,auto_highlight=True)]))
    st.image('img_mic0.png')
    
def 개화():
    st.title('901-개화')
    st.image('개화.png')
    
def 김포공항():
    original_title = '<p style="color:Red; font-size: 50px;font-weight:bold;">902-김포공항</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.image('김포공항.png')
def 공항시장():
    st.title('903-공항시장')
    st.image('공항시장.png')
def 신방화():
    st.title('904-신방화')
    st.image('신방화.png')
def 마곡나루():
    original_title = '<p style="color:Red; font-size: 50px;font-weight:bold;">905-마곡나루</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.image('마곡나루.png')
def 양천향교():
    st.title('906-양천향교')
    st.image('양천향교.png')
def 가양():
    original_title = '<p style="color:Red; font-size: 50px;font-weight:bold;">907-가양</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.image('가양.png')
def 증미():
    st.title('908-증미')
    st.image('증미.png')
def 등촌():
    st.title('909-등촌')
    st.image('등촌.png')
def 염창():
    original_title = '<p style="color:Red; font-size: 50px;font-weight:bold;">910-염창</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.image('염창.png')
def 신목동():
    st.title('911-신목동')
    st.image('신목동.png')
def 선유도():
    st.title('912-선유도')
    st.image('선유도.png')
def 당산():
    original_title = '<p style="color:Red; font-size: 50px;font-weight:bold;">913-당산</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    from datetime import datetime
    df3=pd.read_csv('./10.31/당산.csv',encoding='cp949')
    df3['사용일자'].astype('str')
    df=pd.read_excel('df.xlsx')
    
    
    number=st.number_input('시간을 입력하세요',min_value=5,max_value=23,value=5,step=1)
    st.write('입력 시간', f'2022-10-31 {number}:00:00')
    if number<10:
        x=f'2022-10-31 0{number}:00:00'
    else:
        x=f'2022-10-31 {number}:00:00'

        
    df3=df3.loc[df3['사용일자']==x,]
    df3['new_승차수']=df3['new_승차수']/10
    df3['new_하차수']=df3['new_하차수']/10
    df=df.loc[df['역이름']=='당산',]
    df.loc[df['lon']==126.902,'인구']=df3['new_승차수'][df3['new_승차수'].index[0]]
    df.loc[df['lon']==126.904,'인구']=df3['new_하차수'][df3['new_하차수'].index[0]]
    df1=df.iloc[::2,:]
    df2=df.iloc[1::2,:]
    df1['text']=str(int(df1['인구'][df1['인구'].index[0]]*10))
    df2['text']=str(int(df2['인구'][df2['인구'].index[0]]*10))        
    df.reset_index(drop=True,inplace=True)
    df1.reset_index(drop=True,inplace=True)
    df2.reset_index(drop=True,inplace=True)
    df3.reset_index(drop=True,inplace=True)
    tab1,tab2,tab3,tab4=st.tabs(['역사지도','승/하차 예상인원','개찰구제어','에스컬레이터제어'])
    with tab1:
        st.text('당산')
        st.image('당산.png')
    with tab2:
        st.text('승/하차 예상인원')

        st.pydeck_chart(pdk.Deck(map_style=None,initial_view_state=pdk.ViewState(latitude=37.534,longitude=126.902,zoom=13,pitch=50,),
            layers=[pdk.Layer('ColumnLayer',data=df1,get_position='[lon, lat]',radius=100,elevation_scale=4,get_elevation='인구',
                              get_fill_color=[161, 243, 114],pickable=True,extruded=True,auto_highlight=True),
                   pdk.Layer('ColumnLayer',data=df2,get_position='[lon, lat]',radius=100,elevation_scale=4,get_elevation='인구',
                             get_fill_color=[239, 92, 88],pickable=True,extruded=True,auto_highlight=True),
                   pdk.Layer('TextLayer', data=df1, get_position=[126.898,37.534],get_text='text',get_color='[0, 0, 0]',sizeScale=1,pickable=True,  auto_highlight=True),
                   pdk.Layer('TextLayer', data=df2, get_position=[126.908,37.534],get_text='text',get_color='[0, 0, 0]',sizeScale=1,pickable=True,  auto_highlight=True)]))
        

    with tab3:
        st.text('개찰구 제어')
        
        control=[[img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2],[img2,img3,img2,img3,img2,img3,img2,img3,img2],[img2,img3,img2,img3,img2,img3,img2,img3,img2]]
        a=df1.loc[0,'인구']*10
        b=df2.loc[0,'인구']*10
        c=df3.loc[0,'하차비율']
        
        if (a+b)>=2000:
            x1=control[0].count(img3)
            x2=control[1].count(img3)
            y1=round(x1*(c*0.1))+1
            y2=round(x2*(c*0.1))+1
            count1=0
            for i in range(len(control[0])):
                if control[0][i]==img2:
                    control[0][i]=img1
                    count1+=1
                if count1==y1:
                    break
            count2=0
            for i in range(len(control[1])):
                if control[1][i]==img2:
                    control[1][i]=img1
                    count2+=1
                if count2==y2:
                    break
            count3=0
            for i in range(len(control[2])):
                if control[2][i]==img2:
                    control[2][i]=img1
                    count3+=1
                if count3==y2:
                    break
        
        
        st.subheader('개찰구1')
        st.image(control[0],width=35)
        st.subheader('개찰구2')
        st.image(control[1],width=40)
        st.subheader('개찰구3')
        st.image(control[2],width=40)
    with tab4:
        st.text('에스컬레이터 제어')
        im1=Image.open('el-come.png').convert('RGB')
        im2=Image.open('el-stop.png').convert('RGB')
        im3=Image.open('el-velt.png').convert('RGB')
        im4 = Image.open('empty.png')
        sim1=Image.open('el-come.png').convert('RGB')
        sim2=Image.open('el-stop.png').convert('RGB')
        xim=Image.open('el-x.png').convert('RGB')

        control=[im3,im4,im4,im3,im2,im3,im4,im4,im3,sim2,im4,im3,im4,im4,im3,sim1,im3,im4,im4,im3,im1]
        a=df1.loc[0,'인구']*10
        b=df2.loc[0,'인구']*10
        c=df3.loc[0,'하차비율']
        d=df3.loc[0,'승차비율']
        if (a+b)>=2000:
            if d>c and round(d)>5:
                control[9]=sim1
            if c>d and round(c)>5:
                control[15]=sim2
        if number>=10 and number<=17:
            control=[im3,im4,im4,im3,im2,im3,im4,im4,im3,sim2,im4,im3,im4,im4,im3,xim,im3,im4,im4,im3,im1]

                
        st.subheader('에스컬레이터')
        st.image(control,width=30)    
    
    
def 국회의사당():
    st.title('914-국회의사당')
    st.image('국회의사당.png')
    
    
def 여의도():
    original_title = '<p style="color:Red; font-size: 50px;font-weight:bold;">915-여의도</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    from datetime import datetime
    df3=pd.read_csv('./10.31/여의도.csv',encoding='cp949')
    df3['사용일자'].astype('str')
    df=pd.read_excel('df.xlsx')
    
    
    number=st.number_input('시간을 입력하세요',min_value=5,max_value=24,value=5,step=1)
    st.write('입력 시간', f'2022-10-31 {number}:00:00')
    if number<10:
        x=f'2022-10-31 0{number}:00:00'
    else:
        x=f'2022-10-31 {number}:00:00'

        
    df3=df3.loc[df3['사용일자']==x,]
    df3['new_승차수']=df3['new_승차수']/10
    df3['new_하차수']=df3['new_하차수']/10
    df=df.loc[df['역이름']=='여의도',]
    df.loc[df['lon']==126.926,'인구']=df3['new_승차수'][df3['new_승차수'].index[0]]
    df.loc[df['lon']==126.928,'인구']=df3['new_하차수'][df3['new_하차수'].index[0]]
    df1=df.iloc[::2,:]
    df2=df.iloc[1::2,:]
    df1['text']=str(int(df1['인구'][df1['인구'].index[0]]*10))
    df2['text']=str(int(df2['인구'][df2['인구'].index[0]]*10))        
    df.reset_index(drop=True,inplace=True)
    df1.reset_index(drop=True,inplace=True)
    df2.reset_index(drop=True,inplace=True)
    df3.reset_index(drop=True,inplace=True)
    tab1,tab2,tab3=st.tabs(['역사지도','승/하차 예상인원','개찰구제어'])
    with tab1:
        st.text('여의도')
        st.image('여의도.png')
    with tab2:
        st.text('승/하차 예상인원')

        st.pydeck_chart(pdk.Deck(map_style=None,initial_view_state=pdk.ViewState(latitude=37.5215737,longitude=126.9221228,zoom=13,pitch=50,),
            layers=[pdk.Layer('ColumnLayer',data=df1,get_position='[lon, lat]',radius=100,elevation_scale=4,get_elevation='인구',
                              get_fill_color=[161, 243, 114],pickable=True,extruded=True,auto_highlight=True),
                   pdk.Layer('ColumnLayer',data=df2,get_position='[lon, lat]',radius=100,elevation_scale=4,get_elevation='인구',
                             get_fill_color=[239, 92, 88],pickable=True,extruded=True,auto_highlight=True),
                   pdk.Layer('TextLayer', data=df1, get_position=[126.922,37.522],get_text='text',get_color='[0, 0, 0]',sizeScale=1,pickable=True,  auto_highlight=True),
                   pdk.Layer('TextLayer', data=df2, get_position=[126.932,37.522],get_text='text',get_color='[0, 0, 0]',sizeScale=1,pickable=True,  auto_highlight=True)]))
        

    with tab3:
        st.text('개찰구 제어')
        
        control=[[img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2],[img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2,img3,img2]]
        a=df1.loc[0,'인구']*10
        b=df2.loc[0,'인구']*10
        c=df3.loc[0,'하차비율']
    
        if (a+b)>=2000:
            x1=control[0].count(img3)
            x2=control[1].count(img3)
            y1=round(x1*(c*0.1))+1
            y2=round(x2*(c*0.1))+1
            count1=0
            for i in range(len(control[0])):
                if control[0][i]==img2:
                    control[0][i]=img1
                    count1+=1
                if count1==y1:
                    break
            count2=0
            for i in range(len(control[1])):
                if control[1][i]==img2:
                    control[1][i]=img1
                    count2+=1
                if count2==y2:
                    break
        
        
        st.subheader('개찰구1')
        st.image(control[0],width=35)
        st.subheader('개찰구2')
        st.image(control[1],width=30)
        

    
def 샛강():
    st.title('916-샛강')
    st.image('샛강.png')
def 노량진():
    original_title = '<p style="color:Red; font-size: 50px;font-weight:bold;">917-노량진</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.image('노량진.png')
def 노들():
    st.title('918-노들')
    st.image('노들.png')
def 흑석():
    st.title('919-흑석')
    st.image('흑석.png')
def 동작():
    original_title = '<p style="color:Red; font-size: 50px;font-weight:bold;">920-동작</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.image('동작.png')
def 구반포():
    st.title('921-구반포')
    st.image('구반포.png')
def 신반포():
    st.title('922-신반포')
    st.image('신반포.png')
def 고속터미널():
    original_title = '<p style="color:Red; font-size: 50px;font-weight:bold;">923-고속터미널</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.image('고속터미널.png')
def 사평():
    st.title('924-사평')
    st.image('사평.png')
def 신논현():
    original_title = '<p style="color:Red; font-size: 50px;font-weight:bold;">925-신논현</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.image('신논현.png')
page_name={'Main page':main,'901-개화':개화,'902-김포공항':김포공항,'903-공항시장':공항시장,'904-신방화':신방화,'905-마곡나루':마곡나루,
                                           '906-양천향교':양천향교,'907-가양':가양,'908-증미':증미,'909-등촌':등촌,'910-염창':염창,
                                           '911-신목동':신목동,'912-선유도':선유도,'913-당산':당산,'914-국회의사당':국회의사당,
                                           '915-여의도':여의도,'916-샛강':샛강,'917-노량진':노량진,'918-노들':노들,'919-흑석':흑석,
                                           '920-동작':동작,'921-구반포':구반포,'922-신반포':신반포,'923-고속터미널':고속터미널,
                                           '924-사평':사평,'925-신논현':신논현}

st.title('METRO 9 통합관제 시스템')

# if st.button('통합관제'):
with st.sidebar:
    st.image('cha.png')
selected=st.sidebar.selectbox('역을 선택하세요',page_name.keys())
page_name[selected]()
