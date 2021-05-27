'''TODO: Documentation'''

# System libraries
import os, time, sys, glob
from pathlib import Path
from datetime import date, datetime, timedelta

# API libraries
from dotenv import load_dotenv

# Twilio libraries
from twilio.rest import Client

twilio_account_sid = str()
twilio_auth_token = str()

def load_twilio_api(api_path : str = '../resources/api_keys.env',
                    debug : bool = False):
    '''Instantiates connection to Alpaca Trade API'''
    
    # load API keys
    load_dotenv(api_path)
    
    twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    
    if debug:
        print(f"Testing Twilio API key by data type:")
        print(f"TWILIO_ACCOUNT_SID: {type(twilio_account_sid)}")
        print(f"TWILIO_AUTH_TOKEN: {type(twilio_auth_token)}")


def send_message(message : str,
                 to_phone : str,
                 from_phone : str = '+12483852892'):
    
    client = Client(twilio_account_sid, twilio_auth_token)
    
    client = client.messages.create(body = message,
                                   from_ = from_phone,
                                   to = to_phone)