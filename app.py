# -*- coding: utf-8 -*-
"""
Created on Sat May 22 20:22:21 2021

@author: André
"""

import streamlit as st
import math


st.title("RedCalc")
st.write('Ainda estamos em Teste')

st.sidebar.title('Informe os dados do paciente')
                
peso = st.sidebar.slider('Qual o peso em Kg?',40,150,70)
altura = st.sidebar.slider('E a altura em cm?',140,220,170)
alturaem_m = altura / 100
imc = peso / (alturaem_m * alturaem_m)
idade = st.sidebar.slider('E a idade?', 16,100,30)
gastoenergetico_h = 66.5 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
gastoenergetico_m = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

## saber o sexo do paciente, se for homem = 1, se for mulher = 2
sexo = st.sidebar.selectbox('Qual o sexo do paciente?',('Homem', 'Mulher'))

if sexo == 'Homem':
    sexo_real = 1
    kcal = gastoenergetico_h

if sexo == 'Mulher':
    sexo_real = 2
    kcal = gastoenergetico_m

st.sidebar.write('O IMC do paciente é de', round(imc))
st.sidebar.write('Com gasto energético basal de ', round(kcal), 'kcal')
#######

st.header("Cálculo de doses de drogas")

# drogas 
st.warning('Selecione a droga escolhida, não esqueça de ajustar o peso no meuno lateral!')

# sedação
st.subheader("Sedação")

#midazolan
midazolan = st.checkbox("Midazolan")
if midazolan:
    with st.beta_expander('Ajustar diluições') :
        mida_doseamp = st.number_input('Qual a concentração por ml da ampola? (mg/ml)', 0, 100, 5)
        mida_dosesol = st.number_input('Qual a concentração final da solução? (ml/ml)', 0, 100, 2)
        mida_volsol = st.number_input('Qual o volume da medicação? (ml)', 0, 100, 40)
        mida_voltotal = st.number_input('Qual volume final da solução? (ml)', 0, 500, 100)
        mida_dosemax = st.number_input('Qual a dose máxima? (mcg/kg/h)', 0, 1000, 600)
        mida_dosemin = st.number_input('Qual a dose mínima? (mcg/kg/h)', 0, 1000, 20)

    mida_mlhmax = (mida_dosemax * peso) / (mida_dosesol * 1000) # ml/h máximo
    mida_mlhmin = (mida_dosemin * peso) / (mida_dosesol * 1000) # ml/h mínimo

    mida_mlhatual = st.number_input('Qual ml/h atual?', 0, 200, 10)
    st.write('Conforme peso, dose mínima é', round(mida_mlhmin), 'ml/h, e a dose máxima é', round(mida_mlhmax), 'ml/h')

    mida_doseatual = ((mida_mlhatual * mida_dosesol) / peso) * 1000
    st.write('A dose atual corresponde a ', round(mida_doseatual), 'mcg/kg/h')

#propofol
#fentanil
#cetamina
#precedex
#morfina
