import os
import json

from services.food_service import search_food
from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def understand_request(message):

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=f"""
        Understand the customer's food request.

        Extract:
        - ingredients
        - price preference
        - food category

        Customer request:
        {message}
        """,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": {
                "type": "object",
                "properties": {
                    "ingredients": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "price_preference": {
                        "type": ["string", "null"]
                    },
                    "category": {
                        "type": ["string", "null"]
                    }
                },
                "required": [
                    "ingredients",
                    "price_preference",
                    "category"
                ]
            }
        }
    )

    return json.loads(interaction.output_text)
    

def find_foods_from_request(message):

    request = understand_request(message)

    results = []

    for ingredient in request["ingredients"]:
        foods = search_food(ingredient)
        results.extend(foods)

    return results