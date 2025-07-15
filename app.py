import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados principais
@st.cache_data
def load_data():
    data = pd.DataFrame([...])  # Mantém os dados existentes
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
