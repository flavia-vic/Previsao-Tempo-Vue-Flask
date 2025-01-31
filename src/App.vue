<template>
  <main class="container" :style="{ backgroundImage: `url(${imagemFundoUrl})` }">
    <div class="content">
      <h1>🌤️ Previsão do Tempo</h1>

      <article class="form-group">
        <input v-model="cidade" placeholder="Digite a cidade" aria-label="Cidade" />
        <button @click="buscarClima" class="primary" :disabled="loading">
            <span v-if="loading" class="loader"></span>
            <span v-else class="icon">🔍</span>
            <span class="text">{{ loading ? 'Buscando...' : 'Buscar' }}</span>
        </button>
      </article>

      <article v-if="dadosClima" class="card">
        <div class="card-header">
          <h2>
            <span class="pais-info">
              {{ dadosClima.name }} 
              {{ dadosClima.sys.country }}
              <img :src="flagUrl" alt="Bandeira do país" style="width: 25px; height: auto;" />
            </span>
          </h2>
        </div>
        <div class="card-body">
          <p>
            <i class="fas fa-thermometer-half"></i>
            <strong>Temperatura:</strong> {{ dadosClima.main.temp.toFixed(1) }}°C
          </p>
          <p>
            <i class="fas fa-cloud"></i>
            <strong>Clima:</strong> {{ dadosClima.weather[0].description }}
          </p>
          <p>
            <i class="fas fa-tint"></i>
            <strong>Umidade:</strong> {{ dadosClima.main.humidity }}%
          </p>
          <p>
            <i class="fas fa-wind"></i>
            <strong>Vento:</strong> {{ dadosClima.wind.speed }} m/s
          </p>
        </div>
      </article>
      <article v-if="graficoUrl" class="card">
        <h2>📈 Gráfico de Temperatura</h2>
        <div class="grafico-container">
          <img :src="graficoUrl" alt="Gráfico da previsão do tempo" />
        </div>
      </article>

      <p v-if="erro" class="erro">{{ erro }}</p>
    </div>
  </main>
</template>

<script>
import { ref } from "vue";
import axios from "axios";

export default {
  setup() {
    const cidade = ref("");
    const dadosClima = ref(null);
    const graficoUrl = ref("");
    const flagUrl = ref("");
    const erro = ref(null);
    const imagemFundoUrl = ref("");

    const buscarClima = async () => {
      if (!cidade.value) {
        erro.value = "Por favor, digite uma cidade!";
        return;
      }

      try {
        const resposta = await axios.get(`http://127.0.0.1:5000/previsao?cidade=${cidade.value}`);
        
        if (resposta.data && resposta.data.name) {
          dadosClima.value = resposta.data;
          erro.value = null;

          graficoUrl.value = `http://127.0.0.1:5000/grafico?cidade=${cidade.value}`;

          buscarBandeira(dadosClima.value.sys.country);
          buscarImagemFundo(cidade.value);
        } else {
          erro.value = "Cidade não encontrada!";
          dadosClima.value = null;
          graficoUrl.value = "";
          flagUrl.value = "";
          imagemFundoUrl.value = "";
        }
      } catch (error) {
        console.error("Erro na requisição:", error);
        erro.value = "Erro ao buscar dados da cidade!";
        dadosClima.value = null;
        graficoUrl.value = "";
        flagUrl.value = "";
        imagemFundoUrl.value = "";
      }
    };

    const buscarBandeira = async (codigoPais) => {
      try {
        const resposta = await axios.get(`https://restcountries.com/v3.1/alpha/${codigoPais}`);
        if (resposta.data && resposta.data[0]?.flags?.svg) {
          flagUrl.value = resposta.data[0].flags.svg;
        } else {
          flagUrl.value = "";
        }
      } catch (error) {
        console.error("Erro ao buscar a bandeira:", error);
        flagUrl.value = "";
      }
    };

    const buscarImagemFundo = async (cidade) => {
      try {
        const resposta = await axios.get(`https://api.unsplash.com/photos/random`, {
          params: {
            query: cidade,
            client_id: "SUA-CHAVE-AQUI",
          },
        });

        if (resposta.data?.urls?.regular) {
          imagemFundoUrl.value = resposta.data.urls.regular;
        } else {
          imagemFundoUrl.value = "";
        }
      } catch (error) {
        console.error("Erro ao buscar imagem de fundo:", error);
        imagemFundoUrl.value = "";
      }
    };

    return { cidade, dadosClima, graficoUrl, flagUrl, erro, imagemFundoUrl, buscarClima };
  },
};
</script>


<style scoped>
#app {
  height: 100vh; 
  width: 100vw; 
  display: flex;
  flex-direction: column;
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh; 
  width: 100vw; 
  background-color: #f0f0f0; 
  background-image: var(--imagem-fundo);
  background-size: cover; 
  background-position: center; 
  background-repeat: no-repeat;
}

.card-body {
  text-align: center;
}

.card-body p {
    display: flex;
    align-items: center;
    margin: 0.2rem 0;
    font-size: 0.9rem;
    color: #555;
}

.card-body i {
    margin-right: 0.5rem;
    color: #007BFF; 
    font-size: 1rem; 
    min-width: 20px; 
}

.content {
  background: rgba(250, 249, 249, 0.669); 
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  width: 100%;
  text-align: center;
}

h1 {
  margin-bottom: 0.75rem;
  font-size: 1.5rem;
  color: #333;
  font-weight: bold;
  font-family: verdana;
}

.card {
  padding: 0.75rem;
  border-radius: 8px;
  margin-top: 0.75rem;
  background-color: rgba(255, 255, 255, 0.95);
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
  color: #333;
  text-align: center;
  font-family: verdana;

}

.card-header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.card-header h2 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #007BFF;

}

.card-body {
  text-align: center;
  font-family: verdana;
}

.card-body p {
  margin: 0.3rem 0;
  font-size: 0.9rem;
  color: #555;
  margin-left: 180px;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
}


/* Gráfico */
.grafico-container {
  display: flex;
  justify-content: center;
  margin-top: 0.5rem;
  
}

.grafico-container img {
  border-radius: 6px;
  max-width: 100%;
  height: auto;
}

/* Formulário de busca */
.form-group {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  width: 100%;
  max-width: 350px;
  margin: 0 auto;
  font-family: verdana;

}

input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 0.85rem;
  outline: none;
  transition: border-color 0.3s ease;
  font-family: verdana;

}

input:focus {
  border-color: #007BFF;
}

button {
  padding: 0.4rem 0.8rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85rem;
  background-color: #007BFF;
  color: white;
  transition: background-color 0.3s ease;
}


button:hover {
  background-color: #0056b3;
}

button:active {
  transform: scale(0.95);
}



.loader {
  border: 3px solid #f3f3f3;
  border-top: 3px solid #007BFF;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
}

/* Estilizando erros */
.erro {
  color: red;
  font-weight: bold;
  margin-top: 0.5rem;
  font-size: 0.85rem;
}

/* Informações do país */
.pais-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.pais-info img {
  border-radius: 3px;
}

@media (max-width: 768px) {
  .content {
    padding: 1rem;
    max-width: 90%;
  }

  .form-group {
    flex-direction: column;
  }

  button {
    width: 100%;
    justify-content: center;
  }
}
</style>
