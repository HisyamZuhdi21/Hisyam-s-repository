import streamlit as st

st.set_page_config(page_title="My Webpage", layout="wide")

#header
with st.container():
    st.subheader('Internationale')
    st.title('Tempat mem-posting video yang dilarang youtube')
    
    

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('apa yg kulakukan')
        st.write('##')
        st.write(
            """
            IYYYYYYYYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            BBBBBBBBBBAAAAAAAAAAAAAAAAANGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
            """
        )
        st.write('[Channel utama>](https://www.youtube.com/@2023-ONW)')
    with right_column:
        st.header('Deutschland über alles (Germany Above Everything)')
        video_files = open('/Users/Hisyam/Documents/Python web/Video/German above everything.mp4','rb')
        video_bytes = video_files.read()
        st.video(video_bytes)

        st.header('Njett Molotoff (No Molotov)')
        video_files = open('/Users/Hisyam/Documents/Python web/Video/Njet molotoff.mp4','rb')
        video_bytes = video_files.read()
        st.video(video_bytes)

        st.header('Memri TV')
        video_files = open('/Users/Hisyam/Documents/Python web/Video/IDK.mp4','rb')
        video_bytes = video_files.read()
        st.video(video_bytes)

