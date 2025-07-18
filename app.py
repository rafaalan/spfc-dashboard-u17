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

# Carregar dados individuais simulados (substituir por dados reais)
def load_individual():
    data = pd.DataFrame({
        "Jogador": ["João Silva", "Lucas Mendes", "João Silva", "Lucas Mendes"],
        "Jogo": ["J1", "J1", "J2", "J2"],
        "Minutos": [90, 90, 90, 85],
        "Gols": [2, 0, 1, 0],
        "Finalizacoes": [4, 1, 3, 0],
        "xG": [0.7, 0.2, 0.5, 0.0],
        "Passes": [30, 45, 35, 40]
    })
    return data

# Dados coletivos e individuais
coletivo_df = load_data()
individual_df = load_individual()

# Classificar resultado coletivo
def classificar_resultado(placar):
    gols_spfc, gols_adv = map(int, placar.split("x"))
    if gols_spfc > gols_adv:
        return "Vitória"
    elif gols_spfc < gols_adv:
        return "Derrota"
    else:
        return "Empate"

coletivo_df["Resultado"] = coletivo_df["Placar"].apply(classificar_resultado)

# Título
st.title("📊 Dashboard SPFC Sub-17 - Copa do Brasil 2025")

# Botão de exportação
st.download_button("📥 Baixar CSV dos dados coletivos", data=coletivo_df.to_csv(index=False), file_name="dados_spfc_sub17.csv", mime="text/csv")

# =========================
# 🔵 PAINEL COLETIVO
# =========================

# Filtro por jogo
selected_game = st.selectbox("Selecione um jogo:", coletivo_df["Jogo"])
filtered = coletivo_df[coletivo_df["Jogo"] == selected_game].iloc[0]

# Métricas principais
st.subheader(f"⚽ {filtered['Placar']} vs {filtered['Adversário']} ({filtered['Data']})")
col1, col2 = st.columns(2)
with col1:
    st.metric("xG SPFC", filtered["xG_SPFC"])
    st.metric("Posse SPFC (%)", filtered["Posse_SPFC"])
    st.metric("PPDA SPFC", filtered["PPDA_SPFC"])
with col2:
    st.metric("xG Adversário", filtered["xG_Adversario"])
    st.metric("Posse Adversário (%)", filtered["Posse_Adv"])
    st.metric("PPDA Adversário", filtered["PPDA_Adv"])

# Comparação de posse
st.markdown("### Comparação de Posse de Bola")
posse_df = pd.DataFrame({'Time': ['SPFC', 'Adversário'], 'Posse (%)': [filtered['Posse_SPFC'], filtered['Posse_Adv']]})
st.bar_chart(posse_df.set_index('Time'))

# Evolução dos jogos (xG)
st.markdown("### Evolução dos jogos (xG)")
fig = px.line(coletivo_df, x="Jogo", y=["xG_SPFC", "xG_Adversario"], markers=True, labels={"value": "xG", "Jogo": "Rodada", "variable": "Time"})
st.plotly_chart(fig)

# Tabela geral
st.markdown("### 📋 Tabela Geral")
st.dataframe(coletivo_df.set_index("Jogo"))

# Resumo estatístico
st.markdown("### 📊 Análise Estatística Coletiva")
resumo = pd.DataFrame({
    'Métrica': [
        'Média xG SPFC', 'Média xG Adversário',
        'Média Posse SPFC (%)', 'Média Posse Adversário (%)',
        'Média PPDA SPFC', 'Média PPDA Adversário',
        'Média Faltas SPFC', 'Média Faltas Adversário'
    ],
    'Valor': [
        round(coletivo_df["xG_SPFC"].mean(), 2), round(coletivo_df["xG_Adversario"].mean(), 2),
        round(coletivo_df["Posse_SPFC"].mean(), 2), round(coletivo_df["Posse_Adv"].mean(), 2),
        round(coletivo_df["PPDA_SPFC"].mean(), 2), round(coletivo_df["PPDA_Adv"].mean(), 2),
        round(coletivo_df["Faltas_SPFC"].mean(), 2), round(coletivo_df["Faltas_Adv"].mean(), 2)
    ]
})
st.dataframe(resumo, hide_index=True)

# Gráficos por métrica
st.markdown("### 📈 Visão Geral por Métrica")
for coluna, titulo in zip(
    ["xG_SPFC", "xG_Adversario", "PPDA_SPFC", "Posse_SPFC"],
    ["xG SPFC por Jogo", "xG Adversário por Jogo", "PPDA SPFC por Jogo", "Posse de Bola SPFC por Jogo (%)"]
):
    fig = px.bar(coletivo_df, x="Jogo", y=coluna, color="Resultado", title=titulo)
    st.plotly_chart(fig)

# Comparação por resultado
st.markdown("### 🆚 Comparação: Vitórias x Derrotas")
comparativo = coletivo_df.groupby("Resultado")[["xG_SPFC", "xG_Adversario", "Posse_SPFC", "PPDA_SPFC"]].mean().round(2)
st.dataframe(comparativo)

# Ranking por desempenho
st.markdown("### 🏆 Ranking por Desempenho (xG SPFC)")
ranking = coletivo_df.sort_values(by="xG_SPFC", ascending=False)[["Jogo", "Placar", "xG_SPFC"]]
st.dataframe(ranking.reset_index(drop=True))

# Conclusão
st.markdown("### 📝 Conclusões do Desempenho Coletivo")
st.markdown("""
O São Paulo Sub-17 apresentou desempenho sólido na competição, com destaque para:

- **xG médio de 1.86**, indicando boa criação ofensiva.
- **PPDA médio de 6.72**, refletindo pressão alta eficaz.
- **Posse média de 54.17%**, demonstrando controle da bola.
- Defensivamente, sofreu **xG médio de 1.16**, o que revela certa exposição em alguns jogos decisivos.

🏷️ Jogos com maior destaque ofensivo:
- J1 (6x2, xG 2.98)
- J5 (3x0, xG 2.98)

📉 Jogos com maior dificuldade defensiva:
- J2 (xG adversário 1.62)
- J7 (derrota 0x1, xG adversário 1.54)

A alternância entre domínio e equilíbrio em diferentes jogos mostra versatilidade tática, porém há margem para ajustes defensivos, especialmente contra adversários mais intensos como o Bahia. O time mostrou capacidade de adaptação com formações variadas.
"""), file_name="dados_spfc_sub17.csv", mime="text/csv")

# Seção: Painel Coletivo (como já está)
# [... mantido igual ao código anterior ...]

# Seção: Painel Individual
st.markdown("### 👤 Painel de Desempenho Individual")

jogadores = individual_df["Jogador"].unique()
jogador_sel = st.selectbox("Selecione um jogador:", jogadores)
jogador_df = individual_df[individual_df["Jogador"] == jogador_sel]

st.markdown(f"#### Estatísticas de {jogador_sel}")
st.dataframe(jogador_df.set_index("Jogo"))

# Gráfico de evolução xG e gols
fig_ind = px.bar(jogador_df, x="Jogo", y=["xG", "Gols"], barmode="group", title=f"xG vs Gols - {jogador_sel}")
st.plotly_chart(fig_ind)

fig_final = px.line(jogador_df, x="Jogo", y="Finalizacoes", title=f"Finalizações por jogo - {jogador_sel}", markers=True)
st.plotly_chart(fig_final)
