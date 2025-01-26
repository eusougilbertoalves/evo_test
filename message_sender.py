import os
from dotenv import load_dotenv
from evolutionapi.client import EvolutionClient
from evolutionapi.models.message import TextMessage, MediaMessage

class MessageSender:

    def __init__(self) -> None:

        load_dotenv()

        # Carregar variávies de ambiente
        self.evo_api_token = os.getenv("EVO_API_TOKEN")
        self.evo_instanse_id = os.getenv("EVO_INSTANCE_NAME")
        self.evo_instanse_token = os.getenv("EVO_INSTANCE_TOKEN")
        self.evo_base_url = os.getenv("EVO_BASE_URL")

        self.client = EvolutionClient(
            base_url=self.evo_base_url,
            api_token=self.evo_api_token
        )

    def textMessage(self, number, msg):

        self.text_message = TextMessage(
            number=number,
            text=msg
        )

        response = self.client.messages.send_text(
                    self.evo_instanse_id,
                    self.text_message,
                    self.evo_instanse_token
        )
        return(response)
        #return()