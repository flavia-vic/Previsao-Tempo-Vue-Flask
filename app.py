from flask import Flask, request, jsonify, send_file
import matplotlib
matplotlib.use('Agg')  # Define o backend como Agg
import matplotlib.pyplot as plt
import requests
import io
from flask_cors import CORS
import random  # Para gerar variações realistas

app = Flask(__name__)
CORS(app)

API_KEY = "SUA-CHAVE-AQUI"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def obter_previsao(cidade):
    """Busca a previsão do tempo para a cidade."""
    params = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br",
    }
    resposta = requests.get(WEATHER_URL, params=params)
    return resposta.json()


@app.route("/previsao", methods=["GET"])
def previsao():
    """Retorna os dados da previsão do tempo."""
    cidade = request.args.get("cidade", "São Paulo")
    dados = obter_previsao(cidade)

    if "main" not in dados:
        return jsonify({"erro": "Cidade não encontrada"}), 404

    return jsonify(dados)


@app.route("/grafico", methods=["GET"])
def gerar_grafico():
    """Gera e retorna um gráfico de temperatura."""
    cidade = request.args.get("cidade", "São Paulo")
    dados = obter_previsao(cidade)

    if "main" not in dados:
        return jsonify({"erro": "Cidade não encontrada"}), 404

    # Extrai temperatura atual
    temperatura_atual = dados["main"]["temp"]

    # Simular variações de temperatura ao longo do dia
    horarios = ["06:00","08:00", "10:00","12:00","14:00", "16:00", "18:00","20:00", "22:00", "00:00"]
    temperaturas = [
        round(temperatura_atual + random.uniform(-2, 2), 1) for _ in range(len(horarios))
    ]

    # Criar o gráfico
    plt.figure(figsize=(8, 4))
    plt.plot(horarios, temperaturas, marker="o", linestyle="-", color="b")
    plt.xlabel("Horário")
    plt.ylabel("Temperatura (°C)")
    plt.title(f"Previsão de temperatura - {cidade}")
    plt.grid(True)

    # Salvar imagem em um buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return send_file(buffer, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
