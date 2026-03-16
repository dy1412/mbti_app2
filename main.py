import streamlit as st

st.set_page_config(
    page_title="MBTI Pokémon Music Recommender",
    page_icon="🎧",
    layout="centered"
)

st.title("🎧 MBTI Music & Pokémon Recommender")
st.write("당신의 MBTI 성격에 어울리는 **포켓몬과 음악**을 추천합니다! 🎶⚡")

mbti_data = {

"INTJ": {
"pokemon":"Mewtwo 🧬",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
"pokemon_reason":"뮤츠는 매우 높은 지능과 독립적인 성격을 가진 포켓몬입니다. 전략적이고 논리적인 사고를 하는 INTJ의 특징과 잘 맞기 때문에 대표 포켓몬으로 추천됩니다.",
"description":"INTJ는 깊이 사고하고 계획을 세우는 전략가 유형입니다.",
"songs":[
("Time - Hans Zimmer","웅장한 오케스트라가 점점 고조되며 깊은 몰입을 만들어내는 영화 음악입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png"),
("Experience - Ludovico Einaudi","반복되는 피아노 패턴이 사색적인 분위기를 만드는 미니멀 클래식 음악입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png"),
("Outro - M83","우주적인 스케일과 몽환적인 신스가 특징인 드림팝 음악입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/376.png")
]
},

"ENFP":{
"pokemon":"Pikachu ⚡",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
"pokemon_reason":"피카츄는 밝고 에너지 넘치며 사람들과 잘 어울리는 포켓몬입니다. 긍정적이고 활발한 ENFP의 성격과 매우 비슷합니다.",
"description":"ENFP는 에너지 넘치고 창의적인 성격으로 사람들과 즐거움을 나누는 유형입니다.",
"songs":[
("Happy - Pharrell Williams","밝고 긍정적인 에너지를 전달하는 대표적인 팝 음악입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"),
("Good Time - Owl City","친구들과 함께 들으면 더욱 즐거운 밝은 팝 음악입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"),
("Walking on Sunshine","에너지 넘치는 클래식 팝 음악입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png")
]
},

"INFJ":{
"pokemon":"Lugia 🌊",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/249.png",
"pokemon_reason":"루기아는 바다의 균형을 지키는 신비로운 전설 포켓몬입니다. 깊은 통찰과 조용한 카리스마를 가진 INFJ와 잘 어울립니다.",
"description":"INFJ는 통찰력과 공감 능력이 뛰어난 성격 유형입니다.",
"songs":[
("Fix You - Coldplay","감정적인 위로와 희망을 주는 록 발라드입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/249.png"),
("Runaway - AURORA","몽환적이고 신비로운 분위기의 팝 음악입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"),
("Saturn - Sleeping At Last","철학적인 가사와 잔잔한 멜로디가 특징입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png")
]
},

"ENTJ":{
"pokemon":"Charizard 🔥",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
"pokemon_reason":"리자몽은 강력한 힘과 리더십을 가진 포켓몬입니다. 목표지향적이고 추진력이 강한 ENTJ와 매우 잘 어울립니다.",
"description":"ENTJ는 리더십이 강하고 목표를 향해 나아가는 전략가 유형입니다.",
"songs":[
("Believer - Imagine Dragons","강렬한 드럼과 에너지가 특징인 록 음악입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"),
("Stronger - Kanye West","자신감과 추진력을 높여주는 힙합 음악입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/392.png"),
("Hall of Fame - The Script","성공과 도전을 주제로 한 동기부여 음악입니다.","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png")
]
}

}

mbti = st.selectbox("🧠 MBTI를 선택하세요", list(mbti_data.keys()))

if st.button("🎵 추천 받기"):

    st.balloons()

    data = mbti_data[mbti]

    st.success(f"{mbti} 유형에게 어울리는 포켓몬과 음악 ✨")

    st.subheader(f"대표 포켓몬: {data['pokemon']}")
    st.image(data["pokemon_img"], width=220)

    st.write("🐾 **추천 이유**")
    st.write(data["pokemon_reason"])

    st.write("---")

    st.subheader("🎧 추천 음악")

    for song, desc, img in data["songs"]:
        st.markdown(f"### 🎵 {song}")
        st.write(desc)
        st.image(img, width=150)
        st.write("")
