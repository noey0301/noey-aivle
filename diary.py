import streamlit as st
from PIL import Image
st.title('어느 하루')
for i in range(0,3):
    st.markdown('\n')
if st.button('김연빈의 잡생각 모음집'):
    st.balloons()

    tab1,tab2,tab3=st.tabs(['나미일','2차 회식','.'])
    with tab1:
        st.subheader('나.미.일')
        def main() :
    
            img = Image.open('미프.jpg')
            st.image(img)

        if __name__ == "__main__" :
            main()

#         image1 = Image.open('미프.jpg')
        
#         st.image('')
        
        st.text('''이번 미프 3차에서 1등을 했다.
매일 하루도 쉬지않고 공부를 했기에
어쩌면 너무 만만하게 봤지 않나 싶었다.

사실 점심시간까지도 스코어는 50퍼였고
에러는 내 마음도 모른채 1도 봐주지 않았다.

급할수록 돌아가라는 말이 떠올라
다시 맨 처음으로 돌아가
train,test_dataset을 1간동안 바라봤다.

우연히 두 dataset간에 비슷함을 느꼈고,
하나하나 찾아 하드코딩으로 채워넣은 후
나머지를 imputer로 채운 덕에
2시가 다 돼서야 성과를 낼 수 있었다.

스코어는 1등이지만 부족했던 시간과
다른 분들의 발표를 듣고 아직도 모자람을 느꼈다.

앞으로 다음 미프에서 코딩을 할지 잘 모르겠지만
다시 기초를 쌓아야겠다는 생각이 들었다.''')        
    
    with tab2:
        st.subheader('2차 회식')
#         from PIL import Image
#         image = Image.open('20221002_193459.jpg')
#         image=image.rotate(180)
        st.image('https://postfiles.pstatic.net/MjAyMjEwMDNfMjE0/MDAxNjY0NzcwODUyMzgz.kIVVfvkhONtc0DVSPwWVYC2B6xWP2QLF6WIeN9CoUN4g.GRkZnOFl1RAiXkwM53IO7PboyGh8xX17ErQI7Y1IGBog.JPEG.cutybiny/20221002_193459.jpg?type=w773')
        st.text('''2차 3반 회식을 진행했습니다.
처음엔 투표율도 저조했고
수가 적으면 그냥 없애버리려고했으나
몇명의 수고로 참석율이 늘었습니다.
(그분들께는 감사를 전합니다.)

1차 3반 회식때처럼
이번에도 처음 대면하는 분들과 대화하며
특히 서로 너무나 다른점들이 신기했고
뛰어난 분들이 우리반에 모여있는거 같아
반장으로써 너무나 뿌듯합니다.

무척이나 재밌었습니다.
여러분들도 그렇게 느꼈을거라 생각합니다.
이제 우리 모두 친구가 됐으니까(??)
낯가리지 말고 매일 웃으며
수료때까지 즐거운 인연 이어나가길!''')
        

    with tab3:
        st.subheader('사색')
        st.text('''요즘 이런저런 생각이 많이든다.
사실 조금은 조급하고,
부담감이 문득 나를 찾아온다.
'혼자서도 잘하고 있다, 이 정도만 하자.',
열심히 하고 있다고 느끼지만
역시 나는 나를 잘 알아서 걱정이된다.

나는,
여태까지 살면서 노력이란걸 해본적이 없다.
노는걸 좋아하고 금방 질려해서 
어떤거든 마무리를 지어본게 없다.

10년 넘게 아무 생각 없이
하루하루 무념무상으로 보냈던 나에서
코딩이 재밌고 더 배우고 싶은,
처음으로 목표가 생긴 내가,
이 열정이 식을까 걱정이다.

다행히도 우리반 구성원들을 만나
소통도 하고 장난도 치고 하루하루 웃으며
인생에 처음으로 힘든걸 잊고 산다.

그러나 나는,
정말이지 공감능력이 낮고
남에게 의지하지 않으려 한다

하지만 조금은,
아주 조금은 이들에게 의지하며
내 여정을 이어 나가고 싶다.''')