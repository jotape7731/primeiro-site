import streamlit as st

st.title("Questionário")
st.write('Olá, me chamo Bot, como posso lhe ajudar?')

nome = st.text_input('Qual seu nome?')
idade = st.text_input('Qual sua idade?')
altura = st.text_input('Qual sua altura?')

if st.button('Ver Resumo'):
    st.write(f'Seu nome é {nome}, sua idade é {idade} e sua altura é {altura}.')

st.divider()
st.subheader("Calculadora")
n1 = st.number_input('Digite um número:', step=1)
n2 = st.number_input('Digite outro número:', step=1)

if st.button('Somar'):
    st.success(f'A soma vale {n1 + n2}')