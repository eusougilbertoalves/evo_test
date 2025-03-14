# WhatsApp Message Sender com Evolution API

Este projeto implementa uma interface para envio de mensagens WhatsApp utilizando a Evolution API. A aplicação permite enviar mensagens de texto para números de WhatsApp através de uma interface amigável construída com Streamlit.

## 📋 Requisitos

- Python 3.8+
- Evolution API (Docker)
- Credenciais de acesso à Evolution API

## 🚀 Instalação

### Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/eusougilbertoalves/evo_test.git
   cd evo_test
   ```

2. Inicialize o projeto com uv:
   ```bash
   uv init
   ```

3. Instale as dependências:
   ```bash
   uv pip install -r requirements.txt
   ```

### Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
EVO_API_TOKEN=seu_token_api
EVO_INSTANCE_NAME=nome_instancia
EVO_INSTANCE_TOKEN=token_instancia
EVO_BASE_URL=url_base_api
```

Você pode usar o arquivo `.env.exemple` como modelo.

### Configuração da Evolution API

É necessário ter a Evolution API em execução. Você pode implantá-la usando Docker:

```bash
# Containers necessários: Evo2, Redis, PostgreSQL
# Consulte a documentação da Evolution API para mais detalhes sobre a implantação
```

## 🎮 Uso

### Execução do Script de Teste

```bash
uv run evo_msgsender_test.py
```

### Execução da Interface Streamlit

```bash
streamlit run st_evo_msgsender.py
```

ou

```bash
streamlit run app.py
```

## 🌟 Funcionalidades

- Envio de mensagens de texto para números de WhatsApp
- Interface amigável com Streamlit
- Configurações avançadas para personalização do envio
- Suporte para envio de arquivos (em desenvolvimento)

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Contribuição

Contribuições são bem-vindas! Veja o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para instruções sobre como contribuir para este projeto.

---

### Notas Adicionais

Para desenvolvedores que preferem o método tradicional de ambiente virtual:

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Desativar ambiente virtual
deactivate
```
