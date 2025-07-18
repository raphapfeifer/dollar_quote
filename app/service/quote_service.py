import httpx

async def search_dollar_quote():
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            print(data['USDBRL']['bid'])


    except Exception as e:
        print(f'Error in dollar search request: {e}')