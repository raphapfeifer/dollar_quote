import os
import httpx
if os.getenv('AWS_EXECUTION_ENV') is None:
    from dotenv import load_dotenv
    load_dotenv()


QUOTE_API_URL_DOLLAR = os.getenv('QUOTE_API_URL_DOLLAR')

async def search_dollar_quote():
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(QUOTE_API_URL_DOLLAR)
            response.raise_for_status()
            data = response.json()
            print(data['USDBRL']['bid'])


    except Exception as e:
        print(f'Error in dollar search request: {e}')