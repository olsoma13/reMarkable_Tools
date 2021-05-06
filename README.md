# reMarkable Tools

This is a library of the personal tools I use to increase the productivity of my reMarkable Tablet. You'll find lots more info on the extensibility of the tablet here:  <https://remarkablewiki.com/tips/start>

**Prerequisites:** You should have working knowledge of Python, ssh, and *nix operating systems if using these tools. See LICENSE as there is no guarantee of any functionality.

**Note:** These tools are developed for use on an OSX python implementation using `pipenv` virtualization config. They certainly could be adapted to Windows or other python implementations, but they'll take a little work.

## Tools

### Customize reMarkable Templates

Set of Python scripts to automate the deployment of Templates and/or Splash Screens (TBD) to your reMarkable Tablet. Automates processes outlined here: <https://remarkablewiki.com/tips/templates> && <https://remarkablewiki.com/tips/splashscreens>
**Note:** Re-deploy with each ReMarkable software update.
_todo: add splash screen config. (Basically the same as Templates, just different files and paths!)_

- splashscreen scp: `scp root@remarkable:/usr/share/remarkable/\*.png ./`

1. Edit `config.json.template` to update the pertinent values in the `RM_customize` block. Rename as `config.json` in the same directory
2. Create PNG and SVG versions of the templates. Tablet native resolution: 1872x1404 @ 226dpi (Set palette size to that custom size and used 160 dpi in LucidChart<https://lucidchart.com> for export)
3. Save template files to `/Templates` directory
4. Modify the `templates.json` document in the same directory
5. Execute `RM_customize.py` in the virtualized environment

### REST-based push to RM

_todo: Build a REST API to convert a webpage to PDF using Python pdfkit <https://pypi.org/project/pdfkit/> & rmapy <https://rmapy.readthedocs.io/en/latest/quickstart.html>_

### Notes for Getting DRM protected ePub books on my ReMarkable

Download Calibre: <https://calibre-ebook.com/download_osx>
Download DeDRM plugin and install in Calibre: <https://github.com/apprenticeharper/DeDRM_tools/>

- Follow install instructions. Need a restart.
- Configure Plugin with Kindle Serial Number:
  - Can find SN in device summary here: <https://amazon.com/hz/mycd/digital-console/alldevices>
- Download a kindle book, use the USB delivery method, making sure to select the above registered device.
- Convert in Calibre > Copy to RM using app
