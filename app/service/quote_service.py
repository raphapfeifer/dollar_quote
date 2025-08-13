from datetime import datetime
import os
import httpx
import boto3
import json
from botocore.exceptions import ClientError

#if os.getenv('AWS_EXECUTION_ENV') is None:
#    from dotenv import load_dotenv
 #   load_dotenv()

async def get_secrets(secret_name: str, region_name: str = "us-east-2"):
    client = boto3.client("secretsmanager", region_name=region_name)
    try:
        response = client.get_secret_value(SecretId=secret_name)
        secret = json.loads(response["SecretString"])
        return secret
    except ClientError as e:
        print(f"Unable to retrieve secret {e}")
        return None

secrets = get_secrets("whatsapp/credentials")

QUOTE_API_URL_DOLLAR = os.getenv('QUOTE_API_URL_DOLLAR')
META_GRAPH_API_URL = os.getenv("META_GRAPH_API_URL")
PHONE_ID = secrets.getenv('PHONE_ID')
TOKEN = secrets.getenv('TOKEN')
PHONE_NUMBER_DESTINATION = secrets.getenv('PHONE_NUMBER_DESTINATION')


async def search_dollar_quote():
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(QUOTE_API_URL_DOLLAR)
            response.raise_for_status()
            data = response.json()

            quote = data['USDBRL']['bid']
            date = datetime.strptime(data['USDBRL']['create_date'], "%Y-%m-%d %H:%M:%S").strftime("%d %b %Y at %H:%M")
            message = f'The dollar exchange rate on {date} is : R$ {float(quote):.2f}'
            
            await send_to_whatsapp(message)

    except Exception as e:
        print(f'Error in dollar search request: {e}')

async def send_to_whatsapp(message: str):
    url = f"{META_GRAPH_API_URL}/{PHONE_ID}/messages"
    headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
    }
    payload = {
            "messaging_product": "whatsapp",
            "to": PHONE_NUMBER_DESTINATION,
            "type": "text",
            "text": {"body": message}
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
         