# carregando as bibliotecas
import streamlit as st
# carregando as funções em outros arquivos .py
import controller.cliente as cliente
st.session_state.upda = False
# função para a página de alterar dados
def atualizar():
         
    st.title('Alterar Dados')
    update_matricula = st.number_input(label='Insira a sua Matricula', format='%d', step=1)
    button_update_select = st.button('Consultar')
    #st.write(st.session_state)
    if button_update_select or st.session_state.upda:

        st.session_state.upda = True     

        item = cliente.atualizar(update_matricula)[0]
        with st.form(key='update'):
            update_name = st.text_input(label='Insira o nome', value=item[1])
            update_age = st.number_input(label='Insira a idade', format='%d', value=item[2])
            update_turno = st.selectbox(label='Insira o seu Turno', index=turno.index(item[3]))
            update_periodo = st.number_input(label='Insira o seu Periodo', index=periodo.index(item[4]))
          
            button_update = st.form_submit_button('Alterar')
            
            if button_update:
                data = cliente.alterar(update_name, update_age, update_turno, update_periodo, item[0])
                st.write(data)
                st.success('Aluno alterado com sucesso!!!')
                