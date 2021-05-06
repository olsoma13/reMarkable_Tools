# Push new templates your your ReMarkable Tablet. Need to deploy after RM software updates as well. 
import asyncio
import json
import sys

import asyncssh #https://asyncssh.readthedocs.io/en/latest/

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
        dest = config["RM_customize"]["address"] 
        my_user = "root"
        my_pw = config["RM_customize"]["pw"]

        #Upload Templates
        try:
            origin_templates = ["Templates/*.png", "Templates/*.svg", "Templates/*.json"]
            dest_ssh_templates = dest + ":" + "/usr/share/remarkable/templates/"
            await asyncssh.scp(origin_templates, dest_ssh_templates, username=my_user, password=my_pw)
            logger.debug("Completed update of remote Templates.")
        except (OSError, asyncssh.Error) as template_exc:
            logger.warning("Template uploads failed", template_exc)

        #Upload Splash Screens
        try:
            origin_splashscreens = "Splashscreens/*.png"
            dest_ssh_splashscreen = dest + ":" + "/usr/share/remarkable/"
            await asyncssh.scp(origin_splashscreens, dest_ssh_splashscreen, username=my_user, password=my_pw)
            logger.debug("Completed update of remote ReMarkable files. Sending restart command to RM")
        except (OSError, asyncssh.Error) as splashscreen_exc:
            logger.warning("Splashscreen uploads failed", splashscreen_exc)

        #Restart
        async with asyncssh.connect('reMarkable', username=my_user, password=my_pw) as conn:
            # Had to hack a method to ensure the shell gives a prompt back: https://stackoverflow.com/a/26119118/15725505
            logger.warning("Uploads completed successfully. Restarting reMarkable for changes to take effect.")
            result = await conn.run('/sbin/reboot -f > /dev/null 2>&1 &', check=True)
            print(result.stdout, end='')

    try:
        asyncio.get_event_loop().run_until_complete(run_client())
    except (OSError, asyncssh.Error) as exc:
        logger.warning("SCP operation failed:", exc)
        sys.exit()
