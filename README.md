# Previsão do Tempo

Este projeto é uma aplicação web para exibir a previsão do tempo de diversas cidades. Ele utiliza um backend em Flask para obter dados climáticos da API OpenWeatherMap e um frontend em Vue.js para exibir as informações ao usuário. Além disso, ele busca imagens de fundo relacionadas à cidade através da API Unsplash e exibe a bandeira do país da cidade consultada utilizando a API RestCountries.

## Tecnologias Utilizadas

### Backend
- Python (Flask)
- OpenWeatherMap API
- Matplotlib (para geração de gráficos)
- Flask-CORS

### Frontend
- Vue.js (Vite)
- Axios
- Unsplash API (para imagens de fundo)
- RestCountries API (para bandeiras)

## Instalação e Execução
### 1. Clonar o repositório
Primeiro, clone o repositório para o seu ambiente local:
```sh
git clone <URL do repositório>
cd <diretório do repositório>
```
### 2. Configurar o Frontend (Vue.js)
Execute o seguintes comandos no terminal:
```sh
npm install
```

Para iniciar o frontend:
```sh
npm run dev
```

### 3. Configurar o Backend (Flask)
Certifique-se de ter o Python instalado. Em seguida, instale as dependências do backend:
```sh
pip install -r requirements.txt
```

Para rodar o servidor Flask:
```sh
python app.py
```

## Uso
1. Acesse o frontend via navegador na URL fornecida pelo Vite (normalmente `http://localhost:5173`).
2. Digite o nome de uma cidade e clique em "Buscar".
3. O sistema exibirá a temperatura atual, descrição do clima, umidade e velocidade do vento.
4. Será gerado um gráfico com a variação da temperatura ao longo do dia.
5. O plano de fundo mudará com uma imagem correspondente à cidade buscada.
6. A bandeira do país será exibida ao lado do nome da cidade.

## APIs Utilizadas
- **OpenWeatherMap**: Obtém dados de previsão do tempo.
- **Unsplash API**: Obtém imagens relacionadas à cidade buscada.
- **RestCountries API**: Obtém a bandeira do país da cidade consultada.

## Autor
Projeto desenvolvido por mim. 💙
