import subprocess
import sys
import getpass
import json
import log

# Constants
CUR_USER = getpass.getuser()
PLATFORM = sys.platform

if PLATFORM == "darwin":
    PRIV_SSH_DIR = "/Users/%s/.ssh" % (CUR_USER)
elif PLATFORM == "linux":
    PRIV_SSH_DIR = "/home/%s/.ssh" % (CUR_USER)

KNOWN_HOSTS = PRIV_SSH_DIR + "/known_hosts"

# Start logging stuff
logger = log.setup_logger(__name__)

# load config file
try:
    config = json.load(open("config.json"))
except IOError:
    logger.critical("failed to open the file")
    sys.exit()
except TypeError:
    logger.critical("failed to parse json")
    sys.exit()

# Query a host key and checks for a match in the host key 
def validate_key(host):
    try:
        logger.debug("Starting ssh-keyscan to check for '%s' in existing fingerprints." % host)
        host_key = subprocess.run(["ssh-keyscan", host], capture_output=True, text=True)
        #check if host exists in file
        if host_key.returncode == 0:
            with open(KNOWN_HOSTS) as f:
                if host_key.stdout in f.read():
                    return True
        else:
            logger.info("For host: '%q' ssh-keyscan subprocess returned the following stderr: %s" % host, host_key.stderr)
            return False           
    except:
        e = sys.exc_info()[0]
        logger.critical("Exception occurred when validating host key: %s" % e)
        return False
    else:
        return False

# Add Fingerprint to known_hosts file
def add_fingerprint(host):
    try:
        logger.debug("Starting ssh-keyscan to add '%s' fingerprint to known_hosts." % (host))
        host_key = subprocess.run(["ssh-keyscan", host], capture_output=True, text=True)
        #check if host exists in file
        if host_key.returncode == 0:
            with open(KNOWN_HOSTS, "a") as f:
                if f.write(host_key.stdout):
                    f.close
                    return True
        else:
            logger.info("For host: '%q' ssh-keyscan subprocess returned the following stderr: %s" % host, host_key.stderr)
            return False
    except:
        e = sys.exc_info()[0]
        logger.critical("Exception occurred when adding key fingerprint to known_hosts: %s" % e)
        return False
    else:
        return False

# todo: Change this to an execution with argparse to pass in a specific IP
if __name__ == "__main__":
    def check_and_add (nuhost):
        if validate_key(nuhost) is True:
            logger.info("No change needed. '%s' exists in known_hosts." % nuhost)
            return True
        else:
            # todo: Clean up this logic so I don't keep adding IP addresses :)
            if add_fingerprint(nuhost) is True:
                logger.info("Added fingerprint for '%s' to known_hosts" % nuhost)
                return True
            else:
                logger.info("Could not add '%s' as an entry in known_hosts." % nuhost)
                return False
    if check_and_add("reMarkable") is not True:
        logger.info("Not able to use hostname, falling back to IP address defined in config.json.")
        myIP = config["RM_customize"]["address"] 
        check_and_add(myIP)