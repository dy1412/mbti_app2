import streamlit as st

st.set_page_config(
    page_title="MBTI Music Recommender",
    page_icon="🎧",
    layout="centered"
)

st.title("🎧 MBTI Music Recommender")
st.write("당신의 MBTI에 맞는 음악을 추천해드립니다 🎵")
st.write("아래에서 MBTI를 선택해보세요!")

mbti_music = {
    "INTJ": ("🎼 Time - Hans Zimmer", "깊은 생각에 잠길 때 어울리는 웅장한 음악"),
    "INTP": ("🎼 Experience - Ludovico Einaudi", "분석적이고 차분한 분위기의 피아노곡"),
    "ENTJ": ("🎼 Believer - Imagine Dragons", "강한 리더십과 에너지 넘치는 음악"),
    "ENTP": ("🎼 Can't Hold Us - Macklemore", "창의적이고 활발한 분위기"),
    
    "INFJ": ("🎼 Fix You - Coldplay", "감성적이고 깊은 위로를 주는 음악"),
    "INFP": ("🎼 Until I Found You - Stephen Sanchez", "몽환적이고 감성적인 음악"),
    "ENFJ": ("🎼 Count on Me - Bruno Mars", "사람들과의 따뜻한 관계를 표현하는 음악"),
    "ENFP": ("🎼 Happy - Pharrell Williams", "밝고 긍정적인 에너지"),
    
    "ISTJ": ("🎼 Viva La Vida - Coldplay", "차분하지만 강한 메시지"),
    "ISFJ": ("🎼 You Are The Reason - Calum Scott", "따뜻하고 헌신적인 분위기"),
    "ESTJ": ("🎼 Stronger - Kanye West", "목표지향적이고 강한 에너지"),
    "ESFJ": ("🎼 Dynamite - BTS", "사람들과 함께 즐기기 좋은 음악"),
    
    "ISTP": ("🎼 Blinding Lights - The Weeknd", "세련되고 자유로운 분위기"),
    "ISFP": ("🎼 Peaches & Cream - Lo-fi", "감성적이고 편안한 음악"),
    "ESTP": ("🎼 Uptown Funk - Mark Ronson ft. Bruno Mars", "파티 분위기 가득"),
    "ESFP": ("🎼 Shape of You - Ed Sheeran", "즐겁고 리듬감 있는 음악")
}

mbti = st.selectbox(
    "🧠 MBTI 유형을 선택하세요",
    list(mbti_music.keys())
)

if st.button("🎵 음악 추천 받기"):
    song, desc = mbti_music[mbti]
    
    st.balloons()
    
    st.success(f"✨ {mbti}에게 추천하는 음악 ✨")
    st.subheader(song)
    st.write(desc)
    
    st.write("🎧 좋은 음악 감상하세요!")
