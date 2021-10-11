import re

def sanitize(text):
    return re.sub("[^a-zA-Z0-9_ ]", '', text).replace(" ", "_")
