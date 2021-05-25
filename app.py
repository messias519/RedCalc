# -*- coding: utf-8 -*-
"""
Created on Sat May 22 20:22:21 2021

@author: André
"""
#imports
import streamlit as st

#page config
st.set_page_config(
    page_title="Redcalc 💊",
page_icon="⚕️",
layout="wide",
initial_sidebar_state="expanded",
)

#titulo
st.markdown('<h1>RedCalc</h1>', unsafe_allow_html=True)
st.markdown('<small> Ainda estamos em teste </small>', unsafe_allow_html=True)

#sidebar
st.sidebar.title('Informe os dados do paciente')
peso = st.sidebar.slider('Peso em Kg?',40,150,70)
altura = st.sidebar.slider('Altura em cm?',140,220,170)
alturaem_m = altura / 100
imc = peso / (alturaem_m * alturaem_m)
idade = st.sidebar.slider('Idade em anos?', 16,100,30)
gastoenergetico_h = 66.5 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
gastoenergetico_m = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

## saber o sexo do paciente, se for homem = 1, se for mulher = 2
sexo = st.sidebar.selectbox('Sexo?',('Homem', 'Mulher'))
st.sidebar.markdown("---") #separador
if sexo == 'Homem':
    sexo_real = 1
    kcal = gastoenergetico_h

if sexo == 'Mulher':
    sexo_real = 2
    kcal = gastoenergetico_m

st.sidebar.write('O IMC é de', round(imc))
st.sidebar.write('Gasto energético basal de ', round(kcal), 'kcal')

#######
st.markdown("<h2>Calculadora de doses</h2>", unsafe_allow_html=True)

# drogas
st.markdown("---") #separador
st.warning('Ajuste o peso no menu lateral!')
st.markdown("---") #separador


# sedação
st.subheader("Sedação")
with st.beta_container():
    #midazolan
    midazolan = st.checkbox("Midazolan")
    if midazolan:
        with st.beta_expander('Padrão Mida 40ml + Sf 60ml - Clique para modificar') :
            mida_doseamp = st.number_input('Qual a concentração por ml da ampola? (mg/ml)', 0, 100, 5)
            mida_dosesol = st.number_input('Qual a concentração final da solução? (mg/ml)', 0, 100, 2)
            mida_volsol = st.number_input('Qual o volume da medicação? (ml)', 0, 100, 40)
            mida_voltotal = st.number_input('Qual volume final da solução? (ml)', 0, 500, 100)
            mida_dosemax = st.number_input('Qual a dose máxima? (mcg/kg/h)', 0, 1000, 600)
            mida_dosemin = st.number_input('Qual a dose mínima? (mcg/kg/h)', 0, 1000, 20)

        mida_mlhmax = (mida_dosemax * peso) / (mida_dosesol * 1000) # ml/h máximo
        mida_mlhmin = (mida_dosemin * peso) / (mida_dosesol * 1000) # ml/h mínimo


        mida_mlhatual = st.number_input('Ml/h atual?', 0, 200, 10)
        mida_doseatual = ((mida_mlhatual * mida_dosesol) / peso) * 1000
        st.write('Dose atual', round(mida_doseatual, 2), 'mcg/kg/h')
        st.write('MIN', round(mida_mlhmin, 1), 'ml/h  MAX', round(mida_mlhmax, 1), 'ml/h')

        st.info('É um hipnótico da classe dos benzodiazepínicos, que atua inibindo o GABA. Risco C na gestação, liberado o uso na amamentação. Metabolismo hepático, eliminação renal. Pode causar hipotensão, tendo uma meia vida de 1:30 a 2:30 horas.')
        st.markdown("---")  # separador

    #propofol
    propofol = st.checkbox("Propofol")
    if propofol:
        with st.beta_expander('Padrão Propofol 80ml - Clique para modificar') :
            prop_doseamp = st.number_input('Qual a concentração por ml da ampola? (mg/ml)', 0, 100, 10)
            prop_dosesol = st.number_input('Qual a concentração final da solução? (mg/ml)', 0, 100, 10)
            prop_volsol = st.number_input('Qual o volume da medicação? (ml)', 0, 200, 80)
            prop_voltotal = st.number_input('Qual volume final da solução? (ml)', 0, 500, 80)
            prop_dosemax = st.number_input('Qual a dose máxima? (mg/kg/h)', 0, 1000, 5)
            prop_dosemin = st.number_input('Qual a dose mínima? (mg/kg/h)', 0.0, 100.0, 0.5)

        prop_mlhmax = (prop_dosemax * peso) / (prop_dosesol) # ml/h máximo
        prop_mlhmin = (prop_dosemin * peso) / (prop_dosesol) # ml/h mínimo


        prop_mlhatual = st.number_input('Ml/h atual?', 0, 201, 10)
        prop_doseatual = ((prop_mlhatual * prop_dosesol) / peso)
        st.write('Dose atual', round(prop_doseatual, 2), 'mg/kg/h')
        st.write('MIN', round(prop_mlhmin, 1), 'ml/h  MAX', round(prop_mlhmax, 1), 'ml/h')

        st.info('add texto.')
        st.markdown("---")  # separador

    #fentanil
    fentanil = st.checkbox("Fentanil")
    if fentanil:
        with st.beta_expander('Padrão Fenta 10ml + Sf 40ml - Clique para modificar') :
            fenta_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 100.0, 0.05)
            fenta_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 100.0, 10.0)
            fenta_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 200.0, 10.0)
            fenta_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 180.0, 50.0)
            fenta_dosemax = st.number_input('Qual a dose máxima? (mcg/kg/h)', 0.0, 100.0, 5.0)
            fenta_dosemin = st.number_input('Qual a dose mínima? (mcg/kg/h)', 0.0, 100.0, 0.5)

        fenta_mlhmax = (fenta_dosemax * peso) / (fenta_dosesol) # ml/h máximo
        fenta_mlhmin = (fenta_dosemin * peso) / (fenta_dosesol) # ml/h mínimo


        fenta_mlhatual = st.number_input('Ml/h atual?', 0, 201, 10)
        fenta_doseatual = ((fenta_mlhatual * fenta_dosesol) / peso)
        st.write('Dose atual', round(fenta_doseatual, 2), 'mcg/kg/h')
        st.write('MIN', round(fenta_mlhmin, 1), 'ml/h  MAX', round(fenta_mlhmax, 1), 'ml/h')

        st.info('add texto.')
        st.markdown("---")  # separador

    #cetamina
    cetamina = st.checkbox("Cetamina")
    if cetamina:
        with st.beta_expander('Padrão Cetamina 10ml + Sf 490ml - Clique para modificar') :
            ceta_doseamp = st.number_input('Qual a concentração por ml da ampola? (mg/ml)', 0.0, 100.0, 50.0)
            ceta_dosesol = st.number_input('Qual a concentração final da solução? (mg/ml)', 0.0, 100.0, 1.0)
            ceta_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 100.0, 10.0)
            ceta_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 1000.0, 500.0)
            ceta_dosemax = st.number_input('Qual a dose máxima? (mg/min)', 0.0, 100.0, 0.5)
            ceta_dosemin = st.number_input('Qual a dose mínima? (mg/min)', 0.0, 100.0, 0.1)

        ceta_mlhmax = (ceta_dosemax * 60) / (ceta_dosesol) # ml/h máximo
        ceta_mlhmin = (ceta_dosemin * 60) / (ceta_dosesol) # ml/h mínimo


        ceta_mlhatual = st.number_input('Ml/h atual?', 0, 201, 10)
        ceta_doseatual = ((ceta_mlhatual * ceta_dosesol) / 60)
        st.write('Dose atual', round(ceta_doseatual, 2), 'mg/h')
        st.write('MIN', round(ceta_mlhmin, 1), 'ml/h  MAX', round(ceta_mlhmax, 1), 'ml/h')

        st.info('add texto.')
        st.markdown("---")  # separador

    #precedex
    precedex = st.checkbox("Precedex")
    if precedex:
        with st.beta_expander('Padrão Precedex 2ml + Sf 48ml - Clique para modificar') :
            prec_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 100.0, 0.1)
            prec_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 100.0, 4.0)
            prec_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 100.0, 2.0)
            prec_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 1000.0, 50.0)
            prec_dosemax = st.number_input('Qual a dose máxima? (mcg/min)', 0.0, 100.0, 0.7)
            prec_dosemin = st.number_input('Qual a dose mínima? (mcg/min)', 0.0, 100.0, 0.2)

        prec_mlhmax = (prec_dosemax * peso) / (prec_dosesol) # ml/h máximo
        prec_mlhmin = (prec_dosemin * peso) / (prec_dosesol) # ml/h mínimo


        prec_mlhatual = st.number_input('Ml/h atual?', 0, 201, 10)
        prec_doseatual = ((prec_mlhatual * prec_dosesol) / peso)
        st.write('Dose atual', round(prec_doseatual, 2), 'mcg/kg/h')
        st.write('MIN', round(prec_mlhmin, 1), 'ml/h  MAX', round(prec_mlhmax, 1), 'ml/h')

        st.info('add texto.')
        st.markdown("---")  # separador



st.subheader("Bloqueadores neuro-muscular")
with st.beta_container():
    #cisatracúrio
    cisatracurio = st.checkbox("Cisatracúrio")
    if cisatracurio:
        with st.beta_expander('Padrão Cisatracúrio 25ml + Sf 75ml - Clique para modificar'):
            cisa_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 100.0, 2.0)
            cisa_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 100.0, 0.5)
            cisa_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 100.0, 25.0)
            cisa_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 1000.0, 100.0)
            cisa_dosemax = st.number_input('Qual a dose máxima? (mcg/min)', 0.0, 100.0, 4.0)
            cisa_dosemin = st.number_input('Qual a dose mínima? (mcg/min)', 0.0, 100.0, 1.0)

        cisa_mlhmax = ((cisa_dosemax * peso * 60) / 1000) / (cisa_dosesol)  # ml/h máximo
        cisa_mlhmin = ((cisa_dosemin * peso * 60) / 1000) / (cisa_dosesol)  # ml/h mínimo

        cisa_mlhatual = st.number_input('Ml/h atual?', 0, 201, 10)
        cisa_doseatual = (((cisa_mlhatual * cisa_dosesol) / 60) / peso) * 1000
        st.write('Dose atual', round(cisa_doseatual, 2), 'mcg/kg/h')
        st.write('MIN', round(cisa_mlhmin, 1), 'ml/h  MAX', round(cisa_mlhmax, 1), 'ml/h')

        st.info('add texto.')
        st.markdown("---")  # separador

    #rocurônio
    rocuronio = st.checkbox("Rocurônio")
    if cisatracurio:
        with st.beta_expander('Padrão Rocurônio 25ml + Sf 225ml - Clique para modificar'):
            rocu_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 100.0, 10.0)
            rocu_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 100.0, 1.0)
            rocu_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 100.0, 25.0)
            rocu_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 1000.0, 250.0)
            rocu_dosemax = st.number_input('Qual a dose máxima? (mcg/min)', 0.0, 100.0, 0.6)
            rocu_dosemin = st.number_input('Qual a dose mínima? (mcg/min)', 0.0, 100.0, 0.3)

        rocu_mlhmax = (rocu_dosemax * peso) / rocu_dosesol  # ml/h máximo
        rocu_mlhmin = (rocu_dosemin * peso) / rocu_dosesol  # ml/h mínimo

        rocu_mlhatual = st.number_input('Ml/h atual?', 0, 201, 10)
        rocu_doseatual = (rocu_mlhatual * rocu_dosesol) / peso
        st.write('Dose atual', round(rocu_doseatual, 2), 'mcg/kg/h')
        st.write('MIN', round(rocu_mlhmin, 1), 'ml/h  MAX', round(rocu_mlhmax, 1), 'ml/h')

        st.info('add texto.')
        st.markdown("---")  # separador
    #atracúrio
    #pancurônio

#nitroglicerina
#nitroprussiato

#noradrenalina
#vasopressina
#adrenalina

#dobutamina
#dopamina


st.info('Novas drogas em breve')