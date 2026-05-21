import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="OMS Pediatría", layout="centered")

st.title("Calculadora OMS Pediátrica < 2 años")

sexo = st.selectbox(
    "Sexo",
    ["Masculino", "Femenino"]
)

edad = st.number_input(
    "Edad (meses)",
    min_value=0.0,
    max_value=24.0,
    step=0.1
)

peso = st.number_input(
    "Peso (kg)",
    min_value=0.0,
    step=0.1
)

talla = st.number_input(
    "Talla/Longitud (cm)",
    min_value=0.0,
    step=0.1
)

pc = st.number_input(
    "Perímetro cefálico (cm)",
    min_value=0.0,
    step=0.1
)

def clasificar_z(z):
    if z < -3:
        return "Desnutrición severa"
    elif z < -2:
        return "Desnutrición"
    elif z > 3:
        return "Muy elevado"
    elif z > 2:
        return "Elevado"
    else:
        return "Normal"

if st.button("Calcular"):

    # SIMULACIÓN TEMPORAL
    # Luego se reemplaza por tablas OMS reales

    z_peso_edad = (peso - (edad * 0.25 + 3)) / 1
    z_talla_edad = (talla - (edad * 2 + 50)) / 3
    z_peso_talla = (peso - ((talla - 45) * 0.25)) / 1
    z_pc = (pc - (34 + edad * 0.5)) / 1.5

    st.subheader("Resultados")

    st.write(f"Peso/Edad Z-score: {round(z_peso_edad,2)}")
    st.write(clasificar_z(z_peso_edad))

    st.write(f"Talla/Edad Z-score: {round(z_talla_edad,2)}")
    st.write(clasificar_z(z_talla_edad))

    st.write(f"Peso/Talla Z-score: {round(z_peso_talla,2)}")
    st.write(clasificar_z(z_peso_talla))

    st.write(f"Perímetro Cefálico Z-score: {round(z_pc,2)}")

    if z_pc < -2:
        st.error("Microcefalia")
    elif z_pc > 2:
        st.warning("Macrocefalia")
    else:
        st.success("Perímetro cefálico normal")
