import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Visualização de Dados")

# Criar dados aleatórios
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'valor': np.random.rand(100)
})

# Mostrar tabela
st.write("Dados:", data)

# Gráfico de dispersão
st.scatter_chart(data, x='x', y='y', size='valor')

# Histograma
st.bar_chart(data['x'])