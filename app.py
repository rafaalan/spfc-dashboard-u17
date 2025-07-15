import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados principais
@st.cache_data
def load_data():
    data = pd.DataFrame([
        {"Jogo": "J1", "Data": "11/03/2025", "Adversário": "Instituto Ismaily", "Placar": "6x2", "xG_SPFC": 2.98, "xG_Adversario": 0.24, "Posse_SPFC": 65, "Posse_Adv": 35, "PPDA_SPFC": 3.2, "PPDA_Adv": 21.5, "Finalizacoes_SPFC": "26/9", "Finalizacoes_Adv": "5/3", "Faltas_SPFC": 13, "Faltas_Adv": 3, "Escanteios_SPFC": 2, "Escanteios_Adv": 1, "Formacao_1T": "4-1-4-1", "Formacao_2T": "4-1-4-1"},
        {"Jogo": "J2", "Data": "18/03/2025", "Adversário": "Athletico PR", "Placar": "1x0", "xG_SPFC": 0.74, "xG_Adversario": 1.62, "Posse_SPFC": 41, "Posse_Adv": 59, "PPDA_SPFC": 10.8, "PPDA_Adv": 9.8, "Finalizacoes_SPFC": "11/4", "Finalizacoes_Adv": "20/4", "Faltas_SPFC": 13, "Faltas_Adv": 3, "Escanteios_SPFC": 4, "Escanteios_Adv": 10, "Formacao_1T": "4-2-3-1", "Formacao_2T": "4-2-3-1"},
        {"Jogo": "J3", "Data": "25/03/2025", "Adversário": "Athletico PR", "Placar": "3x2", "xG_SPFC": 1.48, "xG_Adversario": 1.29, "Posse_SPFC": 43, "Posse_Adv": 57, "PPDA_SPFC": 10.3, "PPDA_Adv": 8.6, "Finalizacoes_SPFC": "19/9", "Finalizacoes_Adv": "19/5", "Faltas_SPFC": 15, "Faltas_Adv": 17, "Escanteios_SPFC": 2, "Escanteios_Adv": 3, "Formacao_1T": "4-1-4-1", "Formacao_2T": "4-1-4-1"},
        {"Jogo": "J5", "Data": "15/04/2025", "Adversário": "Sport Recife", "Placar": "3x0", "xG_SPFC": 2.98, "xG_Adversario": 0.25, "Posse_SPFC": 59, "Posse_Adv": 41, "PPDA_SPFC": 4.7, "PPDA_Adv": 15.1, "Finalizacoes_SPFC": "20/10", "Finalizacoes_Adv": "6/2", "Faltas_SPFC": 15, "Faltas_Adv": 15, "Escanteios_SPFC": 2, "Escanteios_Adv": 1, "Formacao_1T": "4-2-3-1", "Formacao_2T": "4-2-3-1"},
        {"Jogo": "J6", "Data": "22/04/2025", "Adversário": "Bahia", "Placar": "4x4", "xG_SPFC": 1.86, "xG_Adversario": 1.00, "Posse_SPFC": 56, "Posse_Adv": 44, "PPDA_SPFC": 8.9, "PPDA_Adv": 8.7, "Finalizacoes_SPFC": "20/6", "Finalizacoes_Adv": "10/4", "Faltas_SPFC": 14, "Faltas_Adv": 12, "Escanteios_SPFC": 3, "Escanteios_Adv": 2, "Formacao_1T": "4-2-3-1", "Formacao_2T": "4-2-3-1"},
        {"Jogo": "J7", "Data": "29/04/2025", "Adversário": "Bahia", "Placar": "0x1", "xG_SPFC": 1.00, "xG_Adversario": 1.54, "Posse_SPFC": 61, "Posse_Adv": 39, "PPDA_SPFC": 5.4, "PPDA_Adv": 8.0, "Finalizacoes_SPFC": "19/4", "Finalizacoes_Adv": "12/4", "Faltas_SPFC": 12, "Faltas_Adv": 17, "Escanteios_SPFC": 8, "Escanteios_Adv": 8, "Formacao_1T": "4-3-3", "Formacao_2T": "4-3-3"}
    ])
    return data
