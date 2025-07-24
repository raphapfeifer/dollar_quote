import os
import httpx
if os.getenv('AWS_EXECUTION_ENV') is None:
    from dotenv import load_dotenv
    load_dotenv()


QUOTE_API_URL_DOLLAR = os.getenv('QUOTE_API_URL_DOLLAR')
PHONE_ID = os.getenv('PHONE_ID')
TOKEN = os.getenv('TOKEN')
PHONE_NUMBER_DESTINATION = os.getenv('PHONE_NUMBER_DESTINATION')


async def search_dollar_quote():
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(QUOTE_API_URL_DOLLAR)
            response.raise_for_status()
            data = response.json()

            quote = data['USDBRL']['bid']
            date = data['USDBRL']['create_date']
            message = f'The dollar exchange rate in {date} is : R$ {quote}'

            await send_to_whatsapp(message)

    except Exception as e:
        print(f'Error in dollar search request: {e}')

async def send_to_whatsapp(message: str):
    url = f"https://graph.facebook.com/v22.0/{PHONE_ID}/messages"
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