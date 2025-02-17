"""
Autor: Professor Sandeco
GitHub: https://github.com/sandeco
YouTube: https://www.youtube.com/@canalsandeco
Data de Criação: 2024

Descrição:
    Este módulo implementa a classe MessageSender para envio de mensagens de texto
    através da Evolution API. O código carrega as variáveis de ambiente necessárias,
    inicializa o cliente da API e define métodos para enviar mensagens.

Uso:
    1. Crie um arquivo ".env" na raiz do projeto contendo as seguintes variáveis:
       - EVO_API_TOKEN: Token de autenticação da API Evolution.
       - EVO_INSTANCE_NAME: Nome da instância a ser utilizada.
       - EVO_INSTANCE_TOKEN: Token específico da instância.
       - EVO_BASE_URL: URL base para conexão com a API.
    2. Instale as dependências necessárias:
       - python-dotenv: Para carregar as variáveis de ambiente.
       - evolutionapi: Cliente para interação com a Evolution API.
    3. Importe e utilize a classe MessageSender para enviar mensagens de texto.
"""

import os
from dotenv import load_dotenv
from evolutionapi.client import EvolutionClient
from evolutionapi.models.message import TextMessage, MediaMessage

class MessageSender:
    """
    Classe responsável por enviar mensagens através da Evolution API.
    
    Ao ser instanciada, a classe carrega as variáveis de ambiente e inicializa
    o cliente da API para realizar o envio das mensagens.
    """

    def __init__(self) -> None:
        """
        Inicializa a instância de MessageSender.

        Executa o carregamento das variáveis de ambiente e configura o cliente
        da Evolution API com os parâmetros necessários.
        """
        load_dotenv()

        # Carregar variáveis de ambiente necessárias
        self.evo_api_token = os.getenv("EVO_API_TOKEN")
        self.evo_instanse_id = os.getenv("EVO_INSTANCE_NAME")
        self.evo_instanse_token = os.getenv("EVO_INSTANCE_TOKEN")
        self.evo_base_url = os.getenv("EVO_BASE_URL")

        # Inicializar o cliente da Evolution API
        self.client = EvolutionClient(
            base_url=self.evo_base_url,
            api_token=self.evo_api_token
        )

    def textMessage(self, number, msg):
        """
        Envia uma mensagem de texto para um número específico utilizando a Evolution API.

        Parâmetros:
            number (str): Número de telefone do destinatário.
            msg (str): Conteúdo da mensagem a ser enviada.

        Retorna:
            Response: Objeto de resposta retornado pela Evolution API após o envio da mensagem.
        """
        # Criar objeto de mensagem de texto
        self.text_message = TextMessage(
            number=number,
            text=msg
        )

        # Enviar a mensagem utilizando o cliente da API e retornar a resposta
        response = self.client.messages.send_text(
            self.evo_instanse_id,
            self.text_message,
            self.evo_instanse_token
        )
        return response
