import pandas as pd
import scipy.stats
import streamlit as st
import time

# Estas son variables de estado que se conservan cuando Streamlit vuelve a ejecutar este script
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

st.header('Lanzar una moneda')

# Inicializa el gráfico con un valor de 0.5
chart = st.line_chart([0.5])

# Función que emula el lanzamiento de la moneda
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)  # Lanza la moneda n veces

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    # Calcula la media a medida que se hacen los lanzamientos
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no  # Calcula la media
        chart.add_rows([mean])  # Actualiza el gráfico con la nueva media
        time.sleep(0.05)  # Pausa de 50ms para ver los resultados en tiempo real

    return mean

# Deslizador para elegir el número de intentos
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)

# Botón para iniciar el experimento
start_button = st.button('Ejecutar')

# Si el botón es presionado, ejecutar el experimento
if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)
    
    # Guardar los resultados del experimento en el DataFrame
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],
                            number_of_trials,
                            mean]],
                     columns=['no', 'iterations', 'mean'])
    ], axis=0)

    # Restablecer los índices del DataFrame
    st.session_state['df_experiment_results'] = st.session_state['df_experiment_results'].reset_index(drop=True)

# Mostrar el DataFrame con los resultados de todos los experimentos
st.write(st.session_state['df_experiment_results'])

# Este es el gráfico de líneas que irá actualizándose
chart = st.line_chart([0.5])

def toss_coin(n):
    # Simula el lanzamiento de la moneda
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])  # Actualiza el gráfico de líneas con la nueva media
        time.sleep(0.05)

    return mean

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    mean = toss_coin(number_of_trials)
