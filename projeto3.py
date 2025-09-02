import streamlit as st

st.set_page_config(
    page_title="Painel de Estudos",
    page_icon="😝",
    layout="wide"
)

st.title("Painel de Estudos")
st.subheader("Registre e visualize seus hábitos nos estudos")

st.sidebar.header("Seus hábitos")
horas = st.sidebar.slider("Horas de estudo", 0, 12, 8)
pausas = st.sidebar.slider("Pausas no dia", 0, 10, 5)
att_realizada = st.sidebar.selectbox("Atividade realizada", ["Leitura", "Exercícios", "Revisão"])

st.metric("Horas de Estudo", f"{horas} horas")
st.metric("Pausas", f"{pausas} pausas")
st.metric("Atividade realizada", att_realizada)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Detalhes das Horas de estudo")
    st.write("Wowww!!" if horas >= 7 else "Você pode mais!!") 

with col2:
    st.header("Pausas durante o estudo")
    st.write("Boa estratégia!" if pausas <= 1 else "Pra quê tanta pausa meu chefe?")

with col3:
    st.header("Atividade realizada")
    st.write("Boa escolha" if att_realizada != "Nenhum" else "Tente escolher uma atividade")

with st.expander ("Dicas rápidas"):
    st.write("🕰️ Estude por pelo menos 7 horas por dia")
    st.write("⏸️ Faça no máximo 1 pausa por dia")
    st.write("📚 Faça alguma atividade todos os dias")

st.markdown("---")
st.markdown("Projeto com streamlit")