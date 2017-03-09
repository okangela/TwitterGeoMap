import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt
import time
import os
import sys


consumer_key = 'CYt8uVj3H4hyOCPK5oz8iY1CY'
consumer_secret = 'xdI3TdTN9ruQVqu9jWzshqCN3UbPcllrhVtoEfwr1V75n3ix68'
access_token = '115414150-YRHkZ8fGnuCMnfZVoL2eDNtN7MVyRgyeX87scjsT'
access_secret = '2QFLNLQFVag8w7z6gtvvfoxIzmxRtRtY4dMbwPBH1haVm'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
