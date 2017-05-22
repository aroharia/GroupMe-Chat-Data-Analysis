
[![Build Status](https://travis-ci.org/aroharia/GroupMe-Chat-Data-Analysis.png?branch=master)](https://travis-ci.org/aroharia/GroupMe-Chat-Data-Analysis)
[![Python Status](https://img.shields.io/badge/python-2.6%2C%202.7-blue.svg)](https://www.python.org/downloads/release/python-2713/)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/aroharia/GroupMe-Chat-Data-Analysis/issues)
[![](https://github.com/aroharia/GroupMe-Chat-Data-Analysis/blob/master/images/groupme_chat_data_analysis_logo.jpg)](https://aroharia.github.io/GroupMe-Chat-Data-Analysis/)

Tools to fetch the complete history of a GroupMe group chat and analyze it.

`fetch.py` allows you to grab the entire transcript for one of your groups and save it as JSON for backup and analysis. It is documented.

`analyze.py` allows you to take the JSON file created by `fetch.py` and display multiple stats.

## Statistics Displayed
1) Message count by member

2) Message count by month

3) Message count by time of day

4) Like count by member

5) Like to post ratio by member

6) Any messages with a specified number of likes

7) Any messages that contain a specified word.



## Tutorial with Images
[fetch.py](https://github.com/aroharia/GroupMe-Chat-Data-Analysis/wiki/fetch)

[analysis.py](https://github.com/aroharia/GroupMe-Chat-Data-Analysis/wiki/analysis)

## Finding your Access Token

Log into [GroupMe's web interface](https://dev.groupme.com/) and login on the top right of the page. Once you login, there should be a tab called "Access Token" in the top right where you will be able to retrieve your token for the `fetch.py` GUI

## Finding your Group ID

In `fetch.py`, enter your access token for ACCESS TOKEN and 'help' in the groupID textbox.

## Requirements/Dependencies/Python

This was written and tested on Python 2.7 I suspect this script will break if you run it with Python 3, because Unicode.

Another dependency is [Requests](http://docs.python-requests.org/en/latest/). `pip install requests` at (Python27/Scripts directory). Download pip from (https://bootstrap.pypa.io/get-pip.py). Current version will probably vary from the version I used when writing this.

The final dependency is [Gooey](https://github.com/chriskiehl/Gooey). (the tool used to implement the GUI)

## Stress Testing and Performance

These tools have been tested with a transcript containing ~16,000 messages. It works fine.

