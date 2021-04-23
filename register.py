import os
import sys

from rmapy.api import Client

import log

# Start logging stuff
logger = log.setup_logger(__name__)

rmapy = Client()
# This registers the client as a new device. The received device token is
# stored in the users directory in the file ~/.rmapi, the same as with the
# go rmapi client.
home = os.path.expanduser("~")
if os.path.exists(home + "/.rmapi"):
    if rmapy.is_auth():
        print("Your Device is already authorized. If you believe this is incorrect, delete ~/.rmapi in your home directory and try to register again.")
    elif rmapy.renew_token():
        print("Token renewed!")
    else:
        logger.warning("error occured while registering. ~./rmapi token exists, but another token is not able to renew.")
else:
    print("Go to my reMarkable (https://my.remarkable.com/connect/desktop) to register a new device and enter the code returned after registering:")
    rmapy.register_device(input())
    # It's always a good idea to renew the user token every time you start
    # a new session.
    rmapy.renew_token()
    if rmapy.is_auth():
        logger.warning("Registration completed successfully.")
