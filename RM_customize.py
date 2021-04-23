# Push new templates your your ReMarkable Tablet. Need to deploy after RM software updates as well. 
import asyncio
import json
import sys

import asyncssh #https://asyncssh.readthedocs.io/en/latest/#optional-extras

import log

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

if __name__ == "__main__":
    async def run_client():
        put_files = ["Templates/*.png", "Templates/*.svg", "Templates/*.json"]
        dest = config["RM_customize"]["address"] 
        ssh_string = dest + ":" + "/usr/share/remarkable/templates/"
        my_user = "root"
        my_pw = config["RM_customize"]["pw"]
        await asyncssh.scp(put_files, ssh_string, username=my_user, password=my_pw)
        logger.warning("Completed update of remote ReMarkable files. Sending restart command to RM")
        async with asyncssh.connect('reMarkable', username=my_user, password=my_pw) as conn:
            # Had to hack a method to ensure the shell gives a prompt back: https://stackoverflow.com/a/26119118/15725505
            result = await conn.run('/sbin/reboot -f > /dev/null 2>&1 &', check=True)
            print(result.stdout, end='')
    try:
        asyncio.get_event_loop().run_until_complete(run_client())
    except (OSError, asyncssh.Error) as exc:
        logger.warning("SCP operation failed:", exc)
        sys.exit()
