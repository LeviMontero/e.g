import scipy.stats
import streamlit as st
import time

# Función para simular el lanzamiento de la moneda
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

# Aquí defines el control deslizante para el número de intentos y el botón para ejecutar
st.header('Lanzar una moneda')

chart = st.line_chart([0.5])  # Muestra el gráfico de líneas

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)  # Deslizador para el número de intentos
start_button = st.button('Ejecutar')  # Botón para ejecutar el experimento

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    mean = toss_coin(number_of_trials)  # Llama a la función toss_coin con el número de intentos seleccionados
