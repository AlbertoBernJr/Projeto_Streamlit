import streamlit as st

st.title("App com Múltiplas Funcionalidades")

# Sidebar
st.sidebar.header("Configurações")
nome = st.sidebar.text_input("Digite seu nome")

# Abas
tab1, tab2, tab3 = st.tabs(["Informações", "Calculadora", "Sobre"])

with tab1:
    st.header(f"Olá, {nome if nome else 'visitante'}!")
    st.write("Esta é a aba de informações")

with tab2:
    st.header("Calculadora")
    num1 = st.number_input("Número 1")
    num2 = st.number_input("Número 2")
    st.write(f"Soma: {num1 + num2}")

with tab3:
    st.header("Sobre")
    st.write("Este é um exemplo de app com Streamlit")