import streamlit as st
st.set_page_config(page_title="YOASOBI", page_icon=":musical_note:")
image='https://namu.wiki/w/YOASOBI?uuid=08c2038b-cf0c-475a-b0f8-3b16e0d0198b'
sound=open("Blue _ 群青.mp3","rb")
st.title("Bài hát yêu thích của tôi: YOASOBI - Blue _ 群青")
st.audio(sound, format="audio/mp3")
st.title("Video âm nhạc của YOASOBI - Blue _ 群青")
video='https://www.youtube.com/watch?v=Y4nEEZwckuU'
st.video(video)
st.image(image, caption="YOASOBI")
with st.sidebar:
 st.image(image, caption="YOASOBI")
 st.write("YOASOBI is a Japanese music duo consisting of producer Ayase and vocalist Ikura. They are known for creating songs based on short stories and novels, blending various genres such as pop, rock, and electronic music. YOASOBI gained significant popularity with their debut single 'Yoru ni Kakeru' in 2019, which became a viral hit in Japan and internationally. Their music often features emotional lyrics and catchy melodies, resonating with a wide audience. YOASOBI has released several successful singles and albums, solidifying their position in the Japanese music industry.") 