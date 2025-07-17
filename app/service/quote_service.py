import httpx

async def search_dollar_quote():
    try:
        async with httpx.AsyncClient() as client:
            print('test')


    except Exception as e:
        print(f'Error in dollar search request: {e}')