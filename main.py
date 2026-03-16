import streamlit as st

st.set_page_config(
    page_title="MBTI Pokemon Music Recommender",
    page_icon="🎧",
    layout="centered"
)

st.title("🎧 MBTI Music & Pokémon Recommender")
st.write("MBTI 성격에 어울리는 **포켓몬과 음악**을 추천합니다! 🎶⚡")

mbti_data = {

"INTJ": {
"pokemon":"Mewtwo 🧬",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
"description":"전략적이고 지적인 INTJ는 강력한 지능과 독립성을 가진 포켓몬과 잘 어울립니다.",
"songs":[
("Time - Hans Zimmer","웅장한 오케스트라가 특징인 서사적인 영화 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png"),
("Experience - Ludovico Einaudi","차분하고 깊은 몰입을 유도하는 미니멀 피아노 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png"),
("Outro - M83","몽환적이면서 거대한 사운드를 가진 드림팝 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/376.png")
]
},

"INTP":{
"pokemon":"Alakazam 🔮",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
"description":"논리적이고 분석적인 INTP는 지능적이고 신비로운 포켓몬과 잘 어울립니다.",
"songs":[
("Weightless - Ambient","깊은 집중과 사색에 어울리는 앰비언트 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png"),
("Daydreaming - Instrumental","생각에 잠기기 좋은 몽환적인 사운드","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"),
("Experience - Ludovico Einaudi","반복적인 피아노 패턴이 특징인 클래식 곡","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png")
]
},

"ENTJ":{
"pokemon":"Charizard 🔥",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
"description":"리더십과 추진력이 강한 ENTJ는 강력하고 카리스마 있는 포켓몬과 잘 어울립니다.",
"songs":[
("Believer - Imagine Dragons","강렬한 드럼과 에너지 넘치는 록 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"),
("Stronger - Kanye West","자신감과 추진력을 느끼게 하는 힙합","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/392.png"),
("Hall of Fame - The Script","목표와 성공을 주제로 한 동기부여 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png")
]
},

"ENTP":{
"pokemon":"Gengar 😈",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
"description":"창의적이고 장난기 많은 ENTP는 개성 넘치는 포켓몬과 잘 어울립니다.",
"songs":[
("Can't Hold Us - Macklemore","빠른 템포와 자유로운 에너지","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png"),
("Feel It Still","독특한 리듬과 개성 있는 사운드","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/197.png"),
("On Top of the World","도전적이고 밝은 분위기","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png")
]
},

"INFJ":{
"pokemon":"Lugia 🌊",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/249.png",
"description":"깊은 통찰과 감성을 가진 INFJ는 신비롭고 평온한 포켓몬과 어울립니다.",
"songs":[
("Fix You - Coldplay","감정적인 위로와 희망을 주는 록 발라드","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/249.png"),
("Runaway - AURORA","몽환적인 분위기의 팝 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"),
("Saturn - Sleeping At Last","철학적인 가사가 특징인 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png")
]
},

"INFP":{
"pokemon":"Mew 🌸",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
"description":"이상적이고 감성적인 INFP는 귀엽고 신비로운 포켓몬과 잘 어울립니다.",
"songs":[
("Until I Found You","따뜻한 복고풍 팝 발라드","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png"),
("Bloom - The Paper Kites","부드러운 인디 포크 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"),
("Holocene - Bon Iver","잔잔하고 깊은 감성의 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png")
]
},

"ENFP":{
"pokemon":"Pikachu ⚡",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
"description":"밝고 에너지 넘치는 ENFP는 활발하고 귀여운 포켓몬과 잘 어울립니다.",
"songs":[
("Happy - Pharrell Williams","밝고 긍정적인 팝 음악","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"),
("Good Time","친구들과 듣기 좋은 신나는 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"),
("Walking on Sunshine","에너지 넘치는 클래식 팝","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png")
]
}

}

mbti = st.selectbox("🧠 MBTI를 선택하세요", list(mbti_data.keys()))

if st.button("🎵 추천 받기"):

    st.balloons()

    data = mbti_data[mbti]

    st.success(f"{mbti}에게 어울리는 포켓몬과 음악 ✨")

    st.subheader(f"대표 포켓몬: {data['pokemon']}")
    st.image(data["pokemon_img"], width=200)

    st.write(data["description"])

    st.write("---")

    st.subheader("🎧 추천 음악")

    for song, desc, img in data["songs"]:
        st.markdown(f"### 🎵 {song}")
        st.write(desc)
        st.image(img, width=150)
        st.write("")
