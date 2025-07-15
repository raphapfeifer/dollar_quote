import asyncio
from service.quote_service import search_dollar_quote


def lambda_handler(event, context):
    asyncio.run(search_dollar_quote())

if __name__ == "__main__":
    lambda_handler(None,None)    