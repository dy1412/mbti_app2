import streamlit as st

st.set_page_config(
    page_title="MBTI Pokémon Music Recommender",
    page_icon="🎧",
    layout="centered"
)

st.title("🎧 MBTI Music & Pokémon Recommender")
st.write("MBTI 성격에 어울리는 **포켓몬과 음악**을 추천합니다! 🎶⚡")

mbti_data = {

"INTJ":{
"pokemon":"Mewtwo 🧬",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
"reason":"뮤츠는 매우 높은 지능과 독립적인 성격을 가진 포켓몬입니다. 전략적이고 계획적인 INTJ와 매우 잘 어울립니다.",
"songs":[
("Time - Hans Zimmer","웅장한 영화 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png"),
("Experience - Ludovico Einaudi","사색적인 피아노 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png"),
("Outro - M83","몽환적인 신스 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/376.png")
]},

"INTP":{
"pokemon":"Alakazam 🔮",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
"reason":"후딘은 높은 지능과 분석 능력을 가진 포켓몬으로 논리적인 INTP와 잘 어울립니다.",
"songs":[
("Weightless","집중을 돕는 앰비언트 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png"),
("Daydreaming","몽환적인 사운드","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"),
("Experience","미니멀 클래식","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png")
]},

"ENTJ":{
"pokemon":"Charizard 🔥",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
"reason":"리자몽은 강력한 카리스마와 리더십을 가진 포켓몬으로 ENTJ와 잘 어울립니다.",
"songs":[
("Believer - Imagine Dragons","강렬한 록 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"),
("Stronger - Kanye West","자신감 넘치는 힙합","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/392.png"),
("Hall of Fame","동기부여 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png")
]},

"ENTP":{
"pokemon":"Gengar 😈",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
"reason":"팬텀은 장난스럽고 창의적인 성격으로 ENTP의 자유로운 성격과 닮았습니다.",
"songs":[
("Can't Hold Us","에너지 넘치는 힙합","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png"),
("Feel It Still","개성있는 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/197.png"),
("On Top of the World","밝은 록 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png")
]},

"INFJ":{
"pokemon":"Lugia 🌊",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/249.png",
"reason":"루기아는 조용하지만 강력한 존재로 깊은 통찰력을 가진 INFJ와 잘 어울립니다.",
"songs":[
("Fix You","감정적인 록 발라드","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/249.png"),
("Runaway","몽환적인 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"),
("Saturn","철학적인 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png")
]},

"INFP":{
"pokemon":"Mew 🌸",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
"reason":"뮤는 순수하고 신비로운 포켓몬으로 감성적인 INFP와 잘 어울립니다.",
"songs":[
("Until I Found You","감성적인 팝 발라드","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png"),
("Bloom","인디 포크","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"),
("Holocene","잔잔한 인디 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png")
]},

"ENFJ":{
"pokemon":"Lucario 🥋",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
"reason":"루카리오는 정의감과 리더십을 가진 포켓몬으로 ENFJ와 닮았습니다.",
"songs":[
("Count on Me","따뜻한 우정의 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png"),
("Brave","용기를 주는 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png"),
("A Sky Full of Stars","희망적인 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png")
]},

"ENFP":{
"pokemon":"Pikachu ⚡",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
"reason":"피카츄는 밝고 에너지 넘치는 포켓몬으로 ENFP의 활발함과 잘 어울립니다.",
"songs":[
("Happy","긍정적인 팝 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"),
("Good Time","신나는 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"),
("Walking on Sunshine","에너지 넘치는 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png")
]},

"ISTJ":{
"pokemon":"Snorlax 😴",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
"reason":"잠만보는 안정적이고 차분한 성격으로 책임감 있는 ISTJ와 어울립니다.",
"songs":[
("Viva La Vida","서사적인 록 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png"),
("Clocks","차분한 록","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/376.png"),
("Bohemian Rhapsody","구조적인 명곡","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png")
]},

"ISFJ":{
"pokemon":"Blissey 💖",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
"reason":"해피너스는 따뜻하고 배려심 많은 포켓몬으로 ISFJ와 닮았습니다.",
"songs":[
("You Are The Reason","감성적인 발라드","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png"),
("Perfect","사랑 노래","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"),
("A Thousand Years","로맨틱 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png")
]},

"ESTJ":{
"pokemon":"Tyranitar 🦖",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/248.png",
"reason":"마기라스는 강력한 힘과 존재감을 가진 포켓몬으로 ESTJ와 잘 어울립니다.",
"songs":[
("Stronger","강렬한 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/248.png"),
("Centuries","강력한 록 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png"),
("Power","에너지 넘치는 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/392.png")
]},

"ESFJ":{
"pokemon":"Eevee 🐾",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
"reason":"이브이는 친근하고 사람들과 잘 어울리는 포켓몬으로 ESFJ와 닮았습니다.",
"songs":[
("Dynamite","밝은 팝 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"),
("Sugar","경쾌한 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"),
("Best Day of My Life","밝은 록 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png")
]},

"ISTP":{
"pokemon":"Greninja 🌊",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/658.png",
"reason":"개굴닌자는 조용하지만 강한 능력을 가진 포켓몬으로 ISTP와 닮았습니다.",
"songs":[
("Blinding Lights","세련된 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/658.png"),
("Midnight City","신스팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/376.png"),
("Animals","강렬한 EDM","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png")
]},

"ISFP":{
"pokemon":"Sylveon 🎀",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/700.png",
"reason":"님피아는 감성적이고 아름다운 포켓몬으로 예술적인 ISFP와 어울립니다.",
"songs":[
("Ocean Eyes","몽환적인 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/700.png"),
("Yellow","감성적인 록","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"),
("Peaches & Cream","로파이 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png")
]},

"ESTP":{
"pokemon":"Infernape 🔥",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/392.png",
"reason":"초염몽(?) → 아니고 인페르노몽(초염몽)?? → 정확히는 초염몽이 아니라 초염몽 아님. Infernape는 활동적이고 공격적인 스타일로 ESTP와 잘 어울립니다.",
"songs":[
("Uptown Funk","펑키한 댄스 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/392.png"),
("Titanium","강렬한 EDM","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"),
("Can't Stop The Feeling","신나는 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png")
]},

"ESFP":{
"pokemon":"Jigglypuff 🎤",
"img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
"reason":"푸린은 노래하고 사람들을 즐겁게 하는 포켓몬으로 ESFP와 잘 어울립니다.",
"songs":[
("Shape of You","리듬감 있는 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"),
("Party Rock Anthem","파티 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"),
("Dynamite","밝은 디스코 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png")
]}

}

mbti = st.selectbox("🧠 MBTI를 선택하세요", list(mbti_data.keys()))

if st.button("🎵 추천 받기"):

    st.balloons()

    data = mbti_data[mbti]

    st.subheader(f"대표 포켓몬: {data['pokemon']}")
    st.image(data["img"], width=220)

    st.write("🐾 **추천 이유**")
    st.write(data["reason"])

    st.write("---")

    st.subheader("🎧 추천 음악")

    for song, desc, img in data["songs"]:
        st.markdown(f"### 🎵 {song}")
        st.write(desc)
        st.image(img, width=150)
