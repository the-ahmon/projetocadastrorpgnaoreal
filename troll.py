import streamlit as st
import pandas as pd
st.set_page_config(
    page_title='Cadastro de Personagens',
    page_icon='📝'
)
st.title('Gerenciador de Ficha de Personagem')
st.divider()
st.header('Cadastro')

st.text('Bem-vindo(a) ao gerenciador de fichas de personagens.')
nome=st.text_input('Para iniciar, digite seu nome de usuário:')

if nome:
    st.text(f'Saudações, {nome}.')
else:
    st.text('Aguardando nome.')


st.divider()

st.selectbox('Selecione o sistema de jogo com o qual está mais familiarizado:',
                   ['Selecionar', 'Dungeons & Dragons 5e', 'Daggerheart', 'Tormenta RPG', 'Tormenta20', 'Mutantes e Malfeitores 3e', 'Pesadelo'])

st.divider()

input_skill=st.number_input('De 1 a 10, o quão experiente você se considera com RPGs? Considere "1" como "nunca joguei" e "10" como "domino todos da lista acima".',
                key='input_skill',
                min_value=0,
                max_value=10,
                step=1,
                value=0)
if input_skill >= 8:
    st.text('Interessante...')
if input_skill > 1 and input_skill <= 8:
    st.text('Sem problemas. O importante é se divertir.')
if input_skill == 1:
    st.text('Primeira vez, né?')
if input_skill == 0:
    st.text('Selecione um nível de habilidade para continuar.')
st.divider()

if nome and st.selectbox != 'Selecionar' and input_skill != 0:
    interesse = st.checkbox('Tenho interesse em fazer parte da comunidade à qual fui solenemente convidado e ciência de que, caso contrário, não poderei prosseguir.',
                            key='check_interesse')   
    if interesse:
        st.write('Que assim seja...')
        st.divider()
        pronto = st.checkbox('Declaro estar pronto e ciente de que, uma vez que prossiga, não há mais retorno.',
                         key='check_return')
        if pronto:
            st.write('...')

            st.divider()

            st.write('Agora, você é um de nós.')
            st.divider()
            if interesse and pronto:
                botao_continuar = st.button('Clique para continuar.',
                                        key='btn_cadastro')

                if botao_continuar:
                    st.image('troll.jpg')