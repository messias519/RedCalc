# -*- coding: utf-8 -*-
"""
@author: Messias6
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

#sidebar
with st.beta_container():
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

#calculadora de doses
with st.beta_container():
    st.markdown("<h2>Sua calculadora de doses</h2>", unsafe_allow_html=True)

    st.markdown('<small> Envie seu feedback para contato@redcalc.com.br </small>', unsafe_allow_html=True)

    # drogas
    st.markdown("---") #separador
    st.warning('Ajuste o peso no menu lateral!')
    st.markdown("---") #separador

    #sedação
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


            fenta_mlhatual = st.number_input('Ml/h atual?', 0, 203, 10)
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


            ceta_mlhatual = st.number_input('Ml/h atual?', 0, 207, 10)
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


            prec_mlhatual = st.number_input('Ml/h atual?', 0, 208, 10)
            prec_doseatual = ((prec_mlhatual * prec_dosesol) / peso)
            st.write('Dose atual', round(prec_doseatual, 2), 'mcg/kg/h')
            st.write('MIN', round(prec_mlhmin, 1), 'ml/h  MAX', round(prec_mlhmax, 1), 'ml/h')

            st.info('add texto.')
            st.markdown("---")  # separador

    #bloqueador neuro-muscular
    st.subheader("Bloqueador neuro-muscular")
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

            cisa_mlhatual = st.number_input('Ml/h atual?', 0, 209, 10)
            cisa_doseatual = (((cisa_mlhatual * cisa_dosesol) / 60) / peso) * 1000
            st.write('Dose atual', round(cisa_doseatual, 2), 'mcg/kg/h')
            st.write('MIN', round(cisa_mlhmin, 1), 'ml/h  MAX', round(cisa_mlhmax, 1), 'ml/h')

            st.info('add texto.')
            st.markdown("---")  # separador
        #rocurônio
        rocuronio = st.checkbox("Rocurônio")
        if rocuronio:
            with st.beta_expander('Padrão Rocurônio 25ml + Sf 225ml - Clique para modificar'):
                rocu_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 100.0, 10.0)
                rocu_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 100.0, 1.0)
                rocu_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 101.0, 25.0)
                rocu_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 1000.0, 250.0)
                rocu_dosemax = st.number_input('Qual a dose máxima? (mcg/min)', 0.0, 100.0, 0.6)
                rocu_dosemin = st.number_input('Qual a dose mínima? (mcg/min)', 0.0, 100.0, 0.3)

            rocu_mlhmax = (rocu_dosemax * peso) / rocu_dosesol  # ml/h máximo
            rocu_mlhmin = (rocu_dosemin * peso) / rocu_dosesol  # ml/h mínimo

            rocu_mlhatual = st.number_input('Ml/h atual?', 0, 2011, 10)
            rocu_doseatual = (rocu_mlhatual * rocu_dosesol) / peso
            st.write('Dose atual', round(rocu_doseatual, 2), 'mcg/kg/h')
            st.write('MIN', round(rocu_mlhmin, 1), 'ml/h  MAX', round(rocu_mlhmax, 1), 'ml/h')

            st.info('add texto.')
            st.markdown("---")  # separador
        #atracúrio
        atracurio = st.checkbox("Atracúrio")
        if atracurio:
            with st.beta_expander('Padrão Atracúrio 25ml + Sf 225ml - Clique para modificar'):
                atra_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 101.0, 10.0)
                atra_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 102.0, 1.0)
                atra_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 103.0, 25.0)
                atra_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 1001.0, 250.0)
                atra_dosemax = st.number_input('Qual a dose máxima? (mcg/min)', 0.0, 102.0, 10.0)
                atra_dosemin = st.number_input('Qual a dose mínima? (mcg/min)', 0.0, 102.0, 5.0)

            atra_mlhmax = ((atra_dosemax * peso * 60) / 1000) / atra_dosesol  # ml/h máximo
            atra_mlhmin = ((atra_dosemin * peso * 60) / 1000) / atra_dosesol  # ml/h mínimo

            atra_mlhatual = st.number_input('Ml/h atual?', 0, 210, 10)
            atra_doseatual = (((atra_mlhatual * atra_dosesol) / 60) / peso) * 1000
            st.write('Dose atual', round(atra_doseatual, 2), 'mcg/kg/h')
            st.write('MIN', round(atra_mlhmin, 1), 'ml/h  MAX', round(atra_mlhmax, 1), 'ml/h')

            st.info('add texto.')
            st.markdown("---")  # separador
        #pancurônio
        pancuronio = st.checkbox("Pancurônio")
        if pancuronio:
            with st.beta_expander('Padrão Pancurônio 20ml + Sf 80ml - Clique para modificar'):
                panc_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 101.0, 2.0)
                panc_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 102.0, 0.4)
                panc_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 103.0, 20.0)
                panc_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 1001.0, 100.0)
                panc_dosemax = st.number_input('Qual a dose máxima? (mcg/min)', 0.0, 102.0, 0.1)
                panc_dosemin = st.number_input('Qual a dose mínima? (mcg/min)', 0.0, 102.0, 0.0)

            panc_mlhmax = (panc_dosemax * peso) / panc_dosesol  # ml/h máximo
            panc_mlhmin = (panc_dosemin * peso) / panc_dosesol  # ml/h mínimo

            panc_mlhatual = st.number_input('Ml/h atual?', 0, 216, 10)
            panc_doseatual = (panc_mlhatual * panc_dosesol) / peso
            st.write('Dose atual', round(panc_doseatual, 2), 'mcg/kg/h')
            st.write('MIN', round(panc_mlhmin, 1), 'ml/h  MAX', round(panc_mlhmax, 1), 'ml/h')

            st.info('add texto.')
            st.markdown("---")

    #DVAs
    st.subheader("DVAs")
    with st.beta_container():
        # nitroglicerina
        nitroglicerina = st.checkbox("Nitroglicerina")
        if nitroglicerina:
            with st.beta_expander('Padrão Tridil 10ml + Sf 240ml - Clique para modificar'):
                nitro_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 102.0, 5.0)
                nitro_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 102.0, 0.2)
                nitro_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 103.0, 10.0)
                nitro_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 999.0, 250.0)
                nitro_dosemax = st.number_input('Qual a dose máxima? (mcg/min)', 0.0, 102.0, 20.0)
                nitro_dosemin = st.number_input('Qual a dose mínima? (mcg/min)', 0.0, 102.0, 5.0)

            nitro_mlhmax = (nitro_dosemax * peso * 6) / (100 / nitro_dosesol)  # ml/h máximo
            nitro_mlhmin = (nitro_dosemin * peso * 6) / (100 / nitro_dosesol)  # ml/h mínimo

            nitro_mlhatual = st.number_input('Ml/h atual?', 0, 216, 10)
            nitro_doseatual = (((nitro_mlhatual * nitro_dosesol) / 60) / peso) * 1000
            st.write('Dose atual', round(nitro_doseatual, 2), 'mcg/kg/h')
            st.write('MIN', round(nitro_mlhmin, 1), 'ml/h  MAX', round(nitro_mlhmax, 1), 'ml/h')

            st.info('add texto.')
            st.markdown("---")

        # nitroprussiato
        nitroprussiato = st.checkbox("Nitroprussiato")
        if nitroprussiato:
            with st.beta_expander('Padrão Nipride 2ml + Sf 248ml - Clique para modificar'):
                nipri_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 103.0, 25.0)
                nipri_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 103.0, 0.2)
                nipri_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 103.0, 2.0)
                nipri_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 998.0, 250.0)
                nipri_dosemax = st.number_input('Qual a dose máxima? (mcg/min)', 0.0, 102.1, 10.0)
                nipri_dosemin = st.number_input('Qual a dose mínima? (mcg/min)', 0.0, 102.1, 0.3)

            nipri_mlhmax = ((nipri_dosemax * peso * 60 ) / 1000) / nipri_dosesol  # ml/h máximo
            nipri_mlhmin = ((nipri_dosemin * peso * 60 ) / 1000) / nipri_dosesol  # ml/h mínimo

            nipri_mlhatual = st.number_input('Ml/h atual?', 0, 217, 10)
            nipri_doseatual = (((nipri_mlhatual * nipri_dosesol) / 60) / peso) * 1000
            st.write('Dose atual', round(nipri_doseatual, 2), 'mcg/kg/h')
            st.write('MIN', round(nipri_mlhmin, 1), 'ml/h  MAX', round(nipri_mlhmax, 1), 'ml/h')

            st.info('add texto.')
            st.markdown("---")

        #noradrenalina
        noradrenalina = st.checkbox("Noradrenalina")
        if noradrenalina:
            with st.beta_expander('Padrão Noradrenalina 16ml + Sf 236ml - Clique para modificar'):
                nora_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 103.1, 1.0)
                nora_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 300.0, 64.0)
                nora_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 103.0, 16.0)
                nora_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 998.0, 250.0)
                nora_dosemax = st.number_input('Qual a dose máxima? (mcg/kg/min)', 0.0, 102.1, 4.0)
                nora_dosemin = st.number_input('Qual a dose mínima? (mcg/kg/min)', 0.0, 103.0, 0.0)

            nora_mlhmax = ((nora_dosemax * peso) / nora_dosesol) * 60  # ml/h máximo
            nora_mlhmin = ((nora_dosemin * peso) / nora_dosesol) * 60  # ml/h mínimo

            nora_mlhatual = st.number_input('Ml/h atual?', 0, 218, 10)
            nora_doseatual = ((nora_mlhatual * nora_dosesol) / 60) / peso
            st.write('Dose atual', round(nora_doseatual, 2), 'mcg/kg/min')
            st.write('MIN', round(nora_mlhmin, 1), 'ml/h  MAX', round(nora_mlhmax, 1), 'ml/h')

            st.info('add texto.')
            st.markdown("---")

        #vasopressina
        vasopressina = st.checkbox("Vasopressina")
        if vasopressina:
            with st.beta_expander('Padrão Vasopressina 2ml + Sf 248ml - Clique para modificar'):
                   vaso_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 103.1, 20.0)
                   vaso_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 300.0, 0.2)
                   vaso_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 103.0, 2.0)
                   vaso_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 997.0, 250.0)
                   vaso_dosemax = st.number_input('Qual a dose máxima? (mcg/kg/min)', 0.0, 102.1, 0.04)
                   vaso_dosemin = st.number_input('Qual a dose mínima? (mcg/kg/min)', 0.0, 103.0, 0.01)

            vaso_mlhmax = (vaso_dosemax / vaso_dosesol) * 60  # ml/h máximo
            vaso_mlhmin = (vaso_dosemin / vaso_dosesol) * 60  # ml/h mínimo

            vaso_mlhatual = st.number_input('Ml/h atual?', 0, 216, 10)
            vaso_doseatual = (vaso_mlhatual * vaso_dosesol) / 60
            st.write('Dose atual', round(vaso_doseatual, 2), 'mcg/kg/min')
            st.write('MIN', round(vaso_mlhmin, 1), 'ml/h  MAX', round(vaso_mlhmax, 1), 'ml/h')

            st.info('add texto.')
            st.markdown("---")

        #adrenalina
        adrenalina = st.checkbox("Adrenalina")
        if adrenalina:
            with st.beta_expander('Padrão Adrenalina 16ml + Sf 236ml - Clique para modificar'):
                adr_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 103.1, 1.0)
                adr_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 301.0, 64.0)
                adr_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 103.0, 16.0)
                adr_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 997.0, 250.0)
                adr_dosemax = st.number_input('Qual a dose máxima? (mcg/kg/min)', 0.0, 102.1, 10.0)
                adr_dosemin = st.number_input('Qual a dose mínima? (mcg/kg/min)', 0.0, 103.0, 2.0)

            adr_mlhmax = (adr_dosemax * 60) / adr_dosesol  # ml/h máximo
            adr_mlhmin = (adr_dosemin * 60) / adr_dosesol  # ml/h mínimo

            adr_mlhatual = st.number_input('Ml/h atual?', 0, 217, 10)
            adr_doseatual = (adr_mlhatual * adr_dosesol) / 60
            st.write('Dose atual', round(adr_doseatual, 2), 'mcg/kg/min')
            st.write('MIN', round(adr_mlhmin, 1), 'ml/h  MAX', round(adr_mlhmax, 1), 'ml/h')

            st.info('add texto.')
            st.markdown("---")

        #dobutamina
        dobutamina = st.checkbox("Dobutamina")
        if dobutamina:
            with st.beta_expander('Padrão Dobutamina 20ml + Sf 230ml - Clique para modificar'):
                dobu_doseamp = st.number_input('Qual a concentração por ml da ampola? (mcg/ml)', 0.0, 103.1, 12.5)
                dobu_dosesol = st.number_input('Qual a concentração final da solução? (mcg/ml)', 0.0, 301.0, 1.0)
                dobu_volsol = st.number_input('Qual o volume da medicação? (ml)', 0.0, 103.0, 20.0)
                dobu_voltotal = st.number_input('Qual volume final da solução? (ml)', 0.0, 996.0, 250.0)
                dobu_dosemax = st.number_input('Qual a dose máxima? (mcg/kg/min)', 0.0, 102.1, 20.0)
                dobu_dosemin = st.number_input('Qual a dose mínima? (mcg/kg/min)', 0.0, 103.0, 2.5)

            dobu_mlhmax = ((dobu_dosemax * peso) / (dobu_dosesol * 1000)) * 60  # ml/h máximo
            dobu_mlhmin = ((dobu_dosemin * peso) / (dobu_dosesol * 1000)) * 60# ml/h mínimo

            dobu_mlhatual = st.number_input('Ml/h atual?', 0, 215, 10)
            dobu_doseatual = ((((dobu_mlhatual * dobu_dosesol) / 60) / peso) * 1000)
            st.write('Dose atual', round(dobu_doseatual, 2), 'mcg/kg/min')
            st.write('MIN', round(dobu_mlhmin, 1), 'ml/h  MAX', round(dobu_mlhmax, 1), 'ml/h')

            st.info('add texto.')
            st.markdown("---")
        #dopamina




