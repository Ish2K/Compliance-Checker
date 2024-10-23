import requests
from bs4 import BeautifulSoup
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def extract_compliance(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        all_text = soup.get_text(separator='\n')

        # Print or copy the content (this prints all the text)
        print(all_text)

        # remove redundant whitespaces but not newlines
        all_text = '\n'.join([line.strip() for line in all_text.split('\n') if line.strip()])
        # Optionally, you can save the content to a file for easy access later
        # with open("compliance.txt", "w", encoding="utf-8") as file:
        #     file.write(all_text)
        
        return all_text
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"

def extract_product(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        all_text = soup.get_text(separator='\n')

        # Print or copy the content (this prints all the text)
        print(all_text)

        # remove redundant whitespaces but not newlines
        all_text = '\n'.join([line.strip() for line in all_text.split('\n') if line.strip()])
        # with open("product.txt", "w", encoding="utf-8") as file:
        #     file.write(all_text)
        return all_text
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"

def get_compliance(compliance_text, product_text):
    """
    Check the product text against the compliance rules.
    :param compliance_text: The compliance rules
    :param product_text: The product text
    :return: Result of compliance check (which rules passed or failed)
    """
    messages = [
        {"role": "system", "content": "You are a compliance assistant that checks if product content follows specific compliance rules."},
        {"role": "user", "content": f"Compliance Rules:\n{compliance_text}\n\nProduct Content:\n{product_text}"},
    ]

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0,
        max_tokens=3000
    )
    
    return response.choices[0].message.content

# compliance_text = (extract_compliance("https://docs.stripe.com/treasury/marketing-treasury"))
# product_text = (extract_product("https://mercury.com/"))

# result = check_compliance(compliance_text, product_text)

# print(result)