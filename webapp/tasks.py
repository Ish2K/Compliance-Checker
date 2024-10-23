from celery import Celery
import httpx
from .utils import *

celery = Celery(__name__, broker='redis://redis:6379/0')

@celery.task
def check_compliance(compliance_url: str, product_url: str):
    # Load compliance and product text from the URLs
    compliance_text = extract_compliance(compliance_url)
    product_text = extract_product(product_url)

    # Compliance checking logic goes here
    # Compare compliance with product and return results
    # This is a placeholder for the actual logic

    response = get_compliance(compliance_text, product_text)

    return {
        "result": response
    }