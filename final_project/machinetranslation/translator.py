"""This package is to translate english to french and vice versa"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

"""This section is to create ibm-watson instance"""
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
                        version='2018-05-01',
                        authenticator=authenticator
                        )
language_translator.set_service_url(url)


def english_to_french(eng_text):
    """This function is to translate english to french"""
    frenchtranslation = language_translator.translate(
                        text=eng_text,
                        model_id='en-fr'
                        ).get_result()
    return frenchtranslation.get('translations')[0].get('translation')


def french_to_english(fre_text):
    """This function is to translate french to english"""
    englishtranslation = language_translator.translate(
                        text=fre_text,
                        model_id='fr-en'
                        ).get_result()
    return englishtranslation.get('translations')[0].get('translation')
