import streamlit as st


import controller.cliente as cliente

def inserir():
    st.title('Tabela Alunes')
    turno = ['Matutino', 'Vespertino']

    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome:')
        input_age = st.number_input(label='Insira a idade', format='%d', step=1)
        input_turno = st.selectbox(label='Insira o Turno', options=turno)
        input_matricula = st.number_input(label='Insira sua Matricula:', format='%d', step=1)
        input_periodo = st.number_input(label='Insira seu Periodo:', format='%d', step=1)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_name, input_age, input_turno, input_matricula, input_periodo)
            st.success('Aluno incluido com sucesso')