import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = "2018-05-01"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')


def englishToFrench(englishText):
    
    response = language_translator.translate(text = englishText,
    model_id = 'en-fr').get_result()
    #frenchText = json.dumps(response, indent=4, ensure_ascii=False)
    return response["translations"][0]["translation"]


def frenchToEnglish(frenchText):
    
    response = language_translator.translate(text = frenchText,
    model_id = 'fr-en').get_result()
    #englishText = json.dumps(response, indent=4, ensure_ascii=False)
    return response["translations"][0]["translation"]
