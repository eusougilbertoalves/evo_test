"""
Autor: Professor Sandeco
GitHub: https://github.com/sandeco
YouTube: https://www.youtube.com/@canalsandeco
Data de Criação: 2024

Descrição:
    Este módulo implementa a classe MessageSender para envio de mensagens e arquivos
    através da Evolution API. O código carrega as variáveis de ambiente necessárias,
    inicializa o cliente da API e define métodos para enviar mensagens e diferentes tipos de mídia.

Uso:
    1. Crie um arquivo ".env" na raiz do projeto contendo as seguintes variáveis:
       - EVO_API_TOKEN: Token de autenticação da API Evolution.
       - EVO_INSTANCE_NAME: Nome da instância a ser utilizada.
       - EVO_INSTANCE_TOKEN: Token específico da instância.
       - EVO_BASE_URL: URL base para conexão com a API.
    2. Instale as dependências necessárias:
       - python-dotenv: Para carregar as variáveis de ambiente.
       - evolutionapi: Cliente para interação com a Evolution API.
    3. Importe e utilize a classe MessageSender para enviar mensagens e arquivos.
"""

import os
from dotenv import load_dotenv
from evolutionapi.client import EvolutionClient
from evolutionapi.models.message import TextMessage, MediaMessage

class MessageSender:
    """
    Classe responsável por enviar mensagens e arquivos através da Evolution API.
    
    Ao ser instanciada, a classe carrega as variáveis de ambiente e inicializa
    o cliente da API para realizar o envio das mensagens e diferentes tipos de mídia.
    """
    
    def __init__(self) -> None:
        """
        Inicializa a instância de MessageSender.

        Executa o carregamento das variáveis de ambiente e configura o cliente
        da Evolution API com os parâmetros necessários.
        """
        # Carregar variáveis de ambiente
        load_dotenv()
        self.evo_api_token = os.getenv("EVO_API_TOKEN")
        self.evo_instance_id = os.getenv("EVO_INSTANCE_NAME")
        self.evo_instance_token = os.getenv("EVO_INSTANCE_TOKEN")
        self.evo_base_url = os.getenv("EVO_BASE_URL")
        
        
        # Inicializar o cliente Evolution
        self.client = EvolutionClient(
            base_url=self.evo_base_url,
            api_token=self.evo_api_token
        )

    def textMessage(self, number, message, mentions=[]):
        """
        Envia uma mensagem de texto para um número específico utilizando a Evolution API.

        Parâmetros:
            number (str ou int): Número de telefone do destinatário.
            message (str): Conteúdo da mensagem a ser enviada.
            mentions (list, opcional): Lista de números a serem mencionados na mensagem.

        Retorna:
            Response: Objeto de resposta retornado pela Evolution API após o envio da mensagem.
        """
        # Enviar mensagem de texto
        text_message = TextMessage(
            number=str(number),
            text=message,
            mentioned=mentions
        )

        response = self.client.messages.send_text(
            self.evo_instance_id, 
            text_message, 
            self.evo_instance_token
        )
        return response

    def PDF(self, number, pdf_file, caption=""):
        """
        Envia um arquivo PDF para um número específico.

        Parâmetros:
            number (str): Número de telefone do destinatário.
            pdf_file (str): Caminho para o arquivo PDF a ser enviado.
            caption (str, opcional): Legenda a ser exibida junto com o arquivo.

        Raises:
            FileNotFoundError: Se o arquivo especificado não for encontrado.
        """
        # Enviar PDF
        if not os.path.exists(pdf_file):
            raise FileNotFoundError(f"Arquivo '{pdf_file}' não encontrado.")
        
        media_message = MediaMessage(
            number=number,
            mediatype="document",
            mimetype="application/pdf",
            caption=caption,
            fileName=os.path.basename(pdf_file),
            media=""
        )
        
        self.client.messages.send_media(
            self.evo_instance_id, 
            media_message, 
            self.evo_instance_token,
            pdf_file
        )

    def audio(self, number, audio_file):
        """
        Envia um arquivo de áudio para um número específico.

        Parâmetros:
            number (str): Número de telefone do destinatário.
            audio_file (str): Caminho para o arquivo de áudio a ser enviado.

        Raises:
            FileNotFoundError: Se o arquivo especificado não for encontrado.
            
        Retorna:
            str: Mensagem de confirmação após o envio bem-sucedido.
        """
        # Enviar áudio
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Arquivo '{audio_file}' não encontrado.")

        audio_message = {
            "number": number,
            "mediatype": "audio",
            "mimetype": "audio/mpeg",
            "caption": ""
        }
            
        self.client.messages.send_whatsapp_audio(
            self.evo_instance_id,
            audio_message,
            self.evo_instance_token,
            audio_file
        )
                    
        return "Áudio enviado"

    def image(self, number, image_file, caption=""):
        """
        Envia uma imagem para um número específico.

        Parâmetros:
            number (str): Número de telefone do destinatário.
            image_file (str): Caminho para o arquivo de imagem a ser enviado.
            caption (str, opcional): Legenda a ser exibida junto com a imagem.

        Raises:
            FileNotFoundError: Se o arquivo especificado não for encontrado.
            
        Retorna:
            str: Mensagem de confirmação após o envio bem-sucedido.
        """
        # Enviar imagem
        if not os.path.exists(image_file):
            raise FileNotFoundError(f"Arquivo '{image_file}' não encontrado.")

        media_message = MediaMessage(
            number=number,
            mediatype="image",
            mimetype="image/jpeg",
            caption=caption,
            fileName=os.path.basename(image_file),
            media=""
        )

        self.client.messages.send_media(
            self.evo_instance_id, 
            media_message, 
            self.evo_instance_token,
            image_file
        )
        
        return "Imagem enviada"

    def video(self, number, video_file, caption=""):
        """
        Envia um vídeo para um número específico.

        Parâmetros:
            number (str): Número de telefone do destinatário.
            video_file (str): Caminho para o arquivo de vídeo a ser enviado.
            caption (str, opcional): Legenda a ser exibida junto com o vídeo.

        Raises:
            FileNotFoundError: Se o arquivo especificado não for encontrado.
            
        Retorna:
            str: Mensagem de confirmação após o envio bem-sucedido.
        """
        # Enviar vídeo
        if not os.path.exists(video_file):
            raise FileNotFoundError(f"Arquivo '{video_file}' não encontrado.")

        media_message = MediaMessage(
            number=number,
            mediatype="video",
            mimetype="video/mp4",
            caption=caption,
            fileName=os.path.basename(video_file),
            media=""
        )

        self.client.messages.send_media(
            self.evo_instance_id, 
            media_message, 
            self.evo_instance_token,
            video_file
        )
        
        return "Vídeo enviado"

    def document(self, number, document_file, caption=""):
        """
        Envia um documento para um número específico.

        Parâmetros:
            number (str): Número de telefone do destinatário.
            document_file (str): Caminho para o arquivo de documento a ser enviado.
            caption (str, opcional): Legenda a ser exibida junto com o documento.

        Raises:
            FileNotFoundError: Se o arquivo especificado não for encontrado.
            
        Retorna:
            str: Mensagem de confirmação após o envio bem-sucedido.
        """
        # Enviar documento
        if not os.path.exists(document_file):
            raise FileNotFoundError(f"Arquivo '{document_file}' não encontrado.")

        media_message = MediaMessage(
            number=number,
            mediatype="document",
            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            caption=caption,
            fileName=os.path.basename(document_file),
            media=""
        )

        self.client.messages.send_media(
            self.evo_instance_id, 
            media_message, 
            self.evo_instance_token,
            document_file
        )
        
        return "Documento enviado"