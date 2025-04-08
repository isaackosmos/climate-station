# Estação Climática com Dashboard (Flask + Sensor DHT11)

Este projeto foi desenvolvido por mim **Isaac Kosmos** como uma aplicação para leitura e visualização de dados climáticos (temperatura e umidade) utilizando um **sensor DHT11** com **Raspberry Pi**, e exibindo os dados em um **dashboard com gráficos interativos** (Chart.js + Flask).
A coleta de dados é feita a cada 10 segundos, e os dados são armazenados em um banco de dados SQLite. O projeto é ideal para quem deseja aprender sobre automação, IoT e desenvolvimento web.

![image](https://github.com/user-attachments/assets/e725ccf6-0e2f-4bb8-bcb2-10b39f447e9f)

Você pode executar o projeto de duas formas:
- **Modo Simulado**: gera dados aleatórios para testes em qualquer computador, mesmo que você não tenha um Raspberry PI no momento.
- **Modo Real (Raspberry Pi)**: lê dados reais do sensor conectado via GPIO.

---

## Funcionalidades

- Coleta automática de temperatura e umidade
- Armazena os dados em um banco SQLite
- Exibe os dados em uma tabela HTML
- Gera gráficos interativos com Chart.js
- API para retornar os dados em JSON

---

## Tecnologias

- Python 3.10+
- Flask
- Chart.js
- Sensor DHT11 (modo real)
- SQLite
- Raspberry Pi GPIO (modo real)

---

## Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/isaackosmos/climate-state
cd climate-state
```
### 2. Crie o arquivo .env
Existe um arquivo de exemplo `.env.example` que você pode copiar e renomear para `.env`. O arquivo `.env` contém as variáveis de ambiente necessárias para o funcionamento do projeto.
```bash
SIMULATION_MODE=True
DHT_PIN=4
DEBUG=True
FLASK_RUN_PORT=5000
```
### 3. Instale as dependências

 Modo Simulado (sem sensor)
Ideal para desenvolvimento ou testes no PC:
```bash
pip install -r requirements.txt
```
 Modo Raspberry Pi (com sensor DHT11)
```bash
pip install -r requirements-rpi.txt
```
### 5. Execute a coleta de dados
```bash
python app/sensor.py
```
Isso inicia a leitura contínua (ou simulação) e salva os dados no banco.


### 6. Execute o servidor Flask
```bash
python app/web.py
```
Acesse: http://localhost:5000

### Dashboard
O dashboard exibe:

Últimos registros de temperatura e umidade

Gráfico de temperatura (linha)

Gráfico de umidade (linha)

Interface simples e responsiva

### Estrutura do Projeto
```bash
├── app/
│   ├── sensor.py         # Script que coleta e salva dados
│   ├── web.py            # Servidor Flask com rotas e dashboard
│   ├── database.py       # CRUD SQLite
│   └── templates/
│       └── dashboard.html
├── requirements.txt      # Dependências para modo simulado
├── requirements-rpi.txt  # Dependências para Raspberry Pi
├── .env
└── run.sh                # Script de inicialização (opcional)
```
### Executando com script .sh (Linux/macOS)
Se preferir, use o script start.sh para iniciar tudo:

```bash
./start.sh
```
Certifique-se de dar permissão de execução ao script:

```bash
chmod +x run.sh
```
### Autor
Feito com 💻 e ☕ por Isaac Kosmos


