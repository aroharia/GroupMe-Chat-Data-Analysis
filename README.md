# GroupMe Chat Data Analysis

Tools to fetch the complete history of a GroupMe group chat and analyze it.

`fetch.py` allows you to grab the entire transcript for one of your groups and save it as JSON for backup and analysis. It is documented.

`analyze.py` allows you to take the JSON file created by `fetch.py` and display multiple stats.


## Finding your access token

Log into [GroupMe's web interface](https://dev.groupme.com/) and login on the top right of the page. Once you login, there should be a tab called "Access Token" in the top right where you will be able to retrieve your token for the `fetch.py` GUI

## Finding your group ID

In `fetch.py`, enter your access token for ACCESS TOKEN and 'help' in the groupId textbox.

## Requirements/Dependencies/Python

This was written and tested on Python 2.7 I suspect this script will break if you run it with Python 3, because Unicode.

Another dependency is [Requests](http://docs.python-requests.org/en/latest/). `pip install requests` at (Python27/Scripts directory). Download pip from (https://bootstrap.pypa.io/get-pip.py). Current version will probably vary from the version I used when writing this.

The final dependency is [Gooey](https://github.com/chriskiehl/Gooey). (the tool used to implement the GUI)

## Stress testing/performance

These tools have been tested with a transcript containing ~16,000 messages. It works fine.

