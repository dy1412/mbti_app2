import streamlit as st

st.set_page_config(
    page_title="MBTI Music Recommender",
    page_icon="🎧",
    layout="centered"
)

st.title("🎧 MBTI Music Recommender")
st.write("당신의 **MBTI 성격 유형**에 어울리는 음악을 추천해드립니다 🎵")
st.write("각 음악은 성격의 분위기와 감정 흐름을 고려해 선정되었습니다 ✨")

mbti_music = {

"INTJ": {
"description": "🧠 전략적이고 깊이 사고하는 INTJ는 감정이 과하지 않으면서도 웅장하고 서사적인 음악을 선호하는 경향이 있습니다.",
"songs": [
("Time - Hans Zimmer", "🎬 영화 음악 / 웅장한 오케스트라. 점점 고조되는 구조가 특징이며 깊은 몰입과 사색을 유도합니다."),
("Experience - Ludovico Einaudi", "🎹 미니멀 피아노 음악. 반복되는 피아노 패턴이 논리적이고 차분한 사고 흐름과 잘 어울립니다."),
("Outro - M83", "🌌 몽환적인 신스와 거대한 사운드 스케일이 특징인 곡으로 미래지향적인 분위기를 느낄 수 있습니다.")
]
},

"INTP": {
"description": "🔬 분석적이고 호기심 많은 INTP는 실험적이거나 몽환적인 음악을 좋아하는 경우가 많습니다.",
"songs": [
("Daydreaming - Instrumental", "☁️ 몽환적인 분위기의 앰비언트 음악으로 생각에 잠기기 좋은 곡입니다."),
("Weightless - Ambient", "🌌 매우 차분한 앰비언트 음악으로 집중과 사색에 도움을 줍니다."),
("Experience - Ludovico Einaudi", "🎹 반복적인 피아노 선율이 논리적인 사고와 잘 어울립니다.")
]
},

"ENTJ": {
"description": "🔥 리더십이 강하고 추진력이 있는 ENTJ는 에너지 넘치고 동기부여가 되는 음악을 선호합니다.",
"songs": [
("Believer - Imagine Dragons", "⚡ 강렬한 드럼과 보컬이 특징인 에너지 넘치는 곡입니다."),
("Stronger - Kanye West", "💪 전자음 기반 힙합으로 자신감과 추진력을 느끼게 합니다."),
("Hall of Fame - The Script", "🏆 목표와 성공을 주제로 한 동기부여 음악입니다.")
]
},

"ENTP": {
"description": "🎲 창의적이고 아이디어가 넘치는 ENTP는 활기차고 개성 있는 음악을 좋아합니다.",
"songs": [
("Can't Hold Us - Macklemore", "🚀 빠른 템포와 자유로운 에너지가 특징입니다."),
("Feel It Still - Portugal. The Man", "🎸 독특한 리듬과 개성 있는 스타일이 돋보입니다."),
("On Top of the World - Imagine Dragons", "🌍 밝고 도전적인 분위기의 팝 록 음악입니다.")
]
},

"INFJ": {
"description": "🌙 깊은 감성과 통찰력을 가진 INFJ는 감정적인 메시지가 있는 음악을 좋아합니다.",
"songs": [
("Fix You - Coldplay", "💡 감정의 위로와 희망을 담은 서정적인 록 발라드입니다."),
("Runaway - AURORA", "❄️ 몽환적이고 감성적인 분위기의 음악입니다."),
("Saturn - Sleeping At Last", "🌌 철학적인 가사와 아름다운 멜로디가 특징입니다.")
]
},

"INFP": {
"description": "🌸 이상적이고 감성적인 INFP는 서정적이고 감정 표현이 풍부한 음악을 좋아합니다.",
"songs": [
("Until I Found You - Stephen Sanchez", "💗 따뜻한 복고풍 팝 발라드입니다."),
("Bloom - The Paper Kites", "🌿 부드러운 인디 포크 음악입니다."),
("Holocene - Bon Iver", "🌲 잔잔하면서도 깊은 감정을 담은 곡입니다.")
]
},

"ENFP": {
"description": "🎉 활발하고 긍정적인 ENFP는 밝고 기분 좋은 에너지를 주는 음악을 좋아합니다.",
"songs": [
("Happy - Pharrell Williams", "😊 밝고 긍정적인 분위기의 대표적인 팝 음악입니다."),
("Good Time - Owl City & Carly Rae Jepsen", "☀️ 친구들과 듣기 좋은 밝은 팝 음악입니다."),
("Walking on Sunshine - Katrina & The Waves", "🌞 에너지 넘치는 클래식 팝곡입니다.")
]
},

"ISTJ": {
"description": "📚 책임감 있고 안정적인 ISTJ는 구조적이고 완성도 높은 음악을 선호합니다.",
"songs": [
("Viva La Vida - Coldplay", "🎻 오케스트라와 록이 결합된 서사적인 곡입니다."),
("Bohemian Rhapsody - Queen", "🎼 다양한 음악 구조가 결합된 명곡입니다."),
("Clocks - Coldplay", "⏰ 반복되는 피아노 리프가 인상적인 록 음악입니다.")
]
},

"ISFP": {
"description": "🎨 예술적 감각이 뛰어난 ISFP는 감성적이고 분위기 있는 음악을 좋아합니다.",
"songs": [
("Ocean Eyes - Billie Eilish", "🌊 몽환적이고 부드러운 팝 음악입니다."),
("Peaches & Cream - Lo-fi", "☕ 편안하게 듣기 좋은 로파이 음악입니다."),
("Yellow - Coldplay", "⭐ 따뜻하고 감성적인 록 발라드입니다.")
]
},

"ESTP": {
"description": "🏎 활동적이고 즉흥적인 ESTP는 리듬감 강하고 신나는 음악을 선호합니다.",
"songs": [
("Uptown Funk - Mark Ronson ft. Bruno Mars", "🕺 펑키한 리듬이 매력적인 댄스곡입니다."),
("Titanium - David Guetta", "💥 강한 EDM 사운드가 특징입니다."),
("Can't Stop The Feeling - Justin Timberlake", "🎉 신나는 팝 댄스 음악입니다.")
]
},

"ESFP": {
"description": "🎤 파티를 즐기고 사람들과 어울리기 좋아하는 ESFP는 밝고 리듬감 있는 음악을 좋아합니다.",
"songs": [
("Shape of You - Ed Sheeran", "🎶 리듬감 있는 팝 음악입니다."),
("Dynamite - BTS", "💃 디스코 팝 스타일의 밝은 음악입니다."),
("Party Rock Anthem - LMFAO", "🎉 파티 분위기의 대표 EDM 곡입니다.")
]
}

}

mbti = st.selectbox("🧠 MBTI 유형을 선택하세요", list(mbti_music.keys()))

if st.button("🎵 음악 추천 받기"):
    
    st.balloons()

    data = mbti_music[mbti]

    st.success(f"✨ {mbti} 유형을 위한 음악 추천 ✨")

    st.write(data["description"])

    st.write("---")

    st.subheader("🎧 추천 음악 3곡")

    for song, desc in data["songs"]:
        st.markdown(f"**{song}**")
        st.write(desc)
        st.write("")
