 from rmapy.api import Client

rmapy = Client()
# Should return False
rmapy.is_auth()
# This registers the client as a new device. The received device token is
# stored in the users directory in the file ~/.rmapi, the same as with the
# go rmapi client.
# todo: build out registration as commdand prompt
rmapy.register_device("fkgzzklrs")
# It's always a good idea to renew the user token every time you start
# a new session.
rmapy.renew_token()
# Should return True
rmapy.is_auth()