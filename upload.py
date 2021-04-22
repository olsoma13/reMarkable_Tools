from rmapy.api import Client

rmapy = Client()

def upload():
    if rmapy.renew_token():
        return True
    else:
        rmapy.log.error("Rmarkable token renew failed:")
        