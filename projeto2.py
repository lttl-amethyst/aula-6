import streamlit as st

st.set_page_config(
    page_title="Painel de Hábitos",
    page_icon="😝",
    layout="wide"
)

st.title("Painel de Hábitos")
st.subheader("Registre e visualize seus hábitos diários")

st.sidebar.header("Seus hábitos")
sono = st.sidebar.slider("Horas de Sono", 0, 12, 8)
agua = st.sidebar.slider("Copos d'água", 0, 10, 5)
exercicio = st.sidebar.selectbox("Exercício", ["Nenhum", "Leve", "Moderado", "Intenso"])

st.metric("Sono", f"{sono} horas")
st.metric("Água", f"{agua} copos")
st.metric("Exercícios", exercicio)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Detalhes do sono")
    st.write("Você dormiu bem" if sono >= 7 else "Tente dormir mais") 

with col2:
    st.header("Hidratação")
    st.write("Ótimo, você está se hidratando" if agua >= 6 else "Beba mais água")

with col3:
    st.header("Exercício")
    st.write("Parabéns" if exercicio != "Nenhum" else "Tente se exercitar hoje")

with st.expander ("Dicas rápidas"):
    st.write("- Durma pelo menos 7 horas")
    st.write("- Beba pelo menos 6 copos d'água")
    st.write("- Faça algum exercício todos os dias")

st.markdown("---")
st.markdown("Projeto com streamlit")