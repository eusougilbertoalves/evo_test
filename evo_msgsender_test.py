import os
from dotenv import load_dotenv
from evolutionapi.client import EvolutionClient
from evolutionapi.models.message import TextMessage, MediaMessage

load_dotenv()
evo_api_token = os.getenv("EVO_API_TOKEN")
evo_instanse_id = os.getenv("EVO_INSTANCE_NAME")
evo_instanse_token = os.getenv("EVO_INSTANCE_TOKEN")
evo_base_url = os.getenv("EVO_BASE_URL")

client = EvolutionClient(
    base_url=evo_base_url,
    api_token=evo_api_token
)

text_message = TextMessage(
    number="5561992793401",
    text="Esta mensagem é para testes do EvolutionAPI v2!"
)

response = client.messages.send_text(
    evo_instanse_id,
    text_message,
    evo_instanse_token
)

print(response)