# Closed-Location
Vivek Gopalakrishnan | June 15, 2018

## Overview
This repository contains code for a tracking system that logs your location in a Google Spreadsheet. 

When run, the script fetches the user's information using the ipstack API. 
Relevant information from this request is parsed and subsequently stored on a Google Spreadsheet.
If the user wishes to check their location history, they merely need to access the spreadsheet to see where the device has been.

Motivated by my distaste for a laptop tracking system recommended by my university
([FrontDoorSoftware](https://frontdoorsoftware.com/) is a special kind of awful), I decided to write my own!
Thus, Closed-Location was born!

## To-Do
- Make script run on startup
- Run `update_sheet` function at a regular interval (probably every 15 minutes)

## APIs
If you wish to run this software on your machine, you will need API keys for the following:
- [ipstack](https://ipstack.com/)
- [Google Drive API](https://console.cloud.google.com/)
- [Google Sheets API](https://console.cloud.google.com/)

## User guide
1. Save your ipstack key as a string in a file named `config.py` with the following:
`ipstack_key = YOUR_KEY_HERE`

2. Save your Google Sheets/Drive credentials (they are the same thing) in a file called `client_secret.json`.

3. Share your target spreadsheet with the client_email listed in the `client_secret.json`.

4. Run `main.py`,
