import streamlit as st

st.title('analise de gasometria')

#variaveis
ph = st.slider("Ph", 6.90, 7.60, 7.30)
co2 = st.slider("Co2", 10.00, 100.00, 35.00)
o2 = st.slider("O2", 30.00, 400.00, 80.00)
hco3 = st.slider("HCO3", 10.00, 50.00, 20.00)
be = st.slider("BE", -20.00, 20.00, 0.00)

co2esperadoacdiose = (1.5 * hco3) + 8

co2esperadoalcalose = hco3 + 15

st.write(co2esperadoacdiose, "+-2")
st.write(co2esperadoalcalose)


#mostrar na tela
if ph < 7.35:
    disturbio = "Acidose"
elif ph > 7.45:
    disturbio = "Alcalose"
else:
    disturbio = "Normal ou Distúrbio compensado"

if co2 > 45:
fonte = "Respiratória"

elif co2 < 35:
fonte = "Metabólica"
# resultado

st.write(disturbio, )

# ph < 7,35 acidose / > 7,45 alcalose
# po2 < 60 hipoxia / > 100 hiperóxia
# pco2 < 35 lavando co2 / > 45 retendo co2


#aniongap = na - (cl + hco3)
# ag > 14 acumulo de acidos // 12+-2 -> perda de bic

# acidose
    #respiratória -> retem co2
        #ph baixo / co2 alto / hco3 alto
    #metabólica -> queda de hco3
        #ph baixo / co2 alto / hco3 alto -> co2 esperado = (1,5 x hco3) + 8  (+-2)

# alcalose
    #respiratória -> lava co2
        #ph alto / co2 baixo / hco3 baixo
    #metabólica -> sobre hco3
        #ph alto / co2 baixo / hco3 baixo -> #co2 esperado = hco3 + 15




