import asyncio
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.service.quote_service import search_dollar_quote



def lambda_handler(event, context):
    asyncio.run(search_dollar_quote())
    return {
       "statusCode": 200,
       "body": "Quot sent!"
    }

if __name__ == "__main__":
  lambda_handler(None,None)