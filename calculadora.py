import streamlit as st

st.title("Calculadora Simples")

num1 = st.number_input("Digite o primeiro número")
num2 = st.number_input("Digite o segundo número")
operacao = st.selectbox("Selecione a operação", ["Somar", "Subtrair", "Multiplicar", "Dividir"])

if st.button("Calcular"):
    if operacao == "Somar":
        resultado = num1 + num2
    elif operacao == "Subtrair":
        resultado = num1 - num2
    elif operacao == "Multiplicar":
        resultado = num1 * num2
    elif operacao == "Dividir":
        resultado = num1 / num2 if num2 != 0 else "Erro: divisão por zero"
    
    st.success(f"Resultado: {resultado}")