import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuração da página
st.set_page_config(page_title="Kobe Bryant Previsão de Arremessos", layout="wide")
st.title("🏀 Kobe Bryant Previsão de Arremesso - Monitoramente")

# Sidebar para configurações
with st.sidebar:
    st.header("🔧 Configuração da API")
    api_url = st.text_input("URL da API", "http://localhost:5001/invocations")

# Container principal com rolagem
with st.container():
    st.subheader("📝 Entrada de Dados do Arremesso")

    # Cria colunas para organização
    col1, col2 = st.columns(2)

    with col1:
        # Coordenadas com validação
        st.markdown("### 🌍 Posição na Quadra")
        lat = st.slider("Latitude", 33.0, 35.0, 34.0443, 0.0001, format="%.4f")
        lon = st.slider("Longitude", -119.0, -117.0, -118.2625, 0.0001, format="%.4f")

    with col2:
        # Dados do jogo
        st.markdown("### ⏱ Tempo de Jogo")
        minutes_remaining = st.slider("Minutos Restantes", 0, 12, 5)
        period = st.slider("Período", 1, 7, 4)
        playoffs = st.selectbox("Playoffs?", ["Não", "Sim"], index=0)

    # Distância do arremesso
    st.markdown("### 🎯 Distância do Arremesso")
    shot_distance = st.slider("Distância (pés)", 0, 50, 15)

    # Botão de previsão
    if st.button("🔮 Prever Resultado do Arremesso", use_container_width=True):
        # Prepara os dados
        input_data = {
            "lat": lat,
            "lon": lon,
            "minutes_remaining": minutes_remaining,
            "period": period,
            "playoffs": 1 if playoffs == "Sim" else 0,
            "shot_distance": float(shot_distance)
        }

        # Formata a requisição
        request_data = {
            "dataframe_split": {
                "columns": list(input_data.keys()),
                "data": [list(input_data.values())]
            }
        }

        # Envia para a API
        try:
            response = requests.post(api_url, json=request_data)

            if response.status_code == 200:
                prediction = response.json()["predictions"][0]
                proba = prediction if isinstance(prediction, float) else (1 if prediction else 0)

                # Exibe resultados
                st.markdown("---")
                st.subheader("📊 Resultado da Previsão")

                # Layout dos resultados
                res_col1, res_col2 = st.columns(2)

                with res_col1:
                    # Medidor visual
                    st.metric("Probabilidade de Acerto",
                              f"{proba * 100:.1f}%",
                              delta="Alta chance" if proba > 0.5 else "Baixa chance")

                    # Gauge meter
                    fig, ax = plt.subplots(figsize=(8, 2))
                    ax.barh(0, proba, height=0.3, color='#4CAF50' if proba > 0.5 else '#F44336')
                    ax.set_xlim(0, 1)
                    ax.set_xticks([0, 0.5, 1])
                    ax.set_xticklabels(["0%", "50%", "100%"])
                    ax.set_yticks([])
                    ax.set_title("Confiança da Previsão", pad=10)
                    st.pyplot(fig)

                with res_col2:
                    # Mapa simplificado
                    st.image("https://i.imgur.com/3JYQZ7L.png",
                             caption=f"Posição: ({lat:.4f}, {lon:.4f})",
                             width=300)

                # Armazena histórico
                if "history" not in st.session_state:
                    st.session_state.history = []

                st.session_state.history.append({
                    **input_data,
                    "probability": proba,
                    "prediction": "Acerto" if proba > 0.5 else "Erro"
                })

            else:
                st.error(f"Erro na API: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"Falha na conexão: {str(e)}")

# Seção de histórico (com rolagem independente)
if "history" in st.session_state and st.session_state.history:
    st.markdown("---")
    st.subheader("📜 Histórico de Previsões")

    history_df = pd.DataFrame(st.session_state.history)

    # Formatação especial para o DataFrame
    styled_df = history_df.style.format({
        "lat": "{:.4f}",
        "lon": "{:.4f}",
        "probability": "{:.1%}"
    }).background_gradient(subset=["probability"], cmap="RdYlGn")

    st.dataframe(styled_df, height=300, use_container_width=True)

    # Botão para limpar
    if st.button("🧹 Limpar Histórico", use_container_width=True):
        st.session_state.history = []
        st.experimental_rerun()

# Rodapé
st.markdown("---")
st.caption("Sistema de previsão de arremessos do Kobe Bryant | Desenvolvido com Streamlit")