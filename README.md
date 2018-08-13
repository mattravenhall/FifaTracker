# FifaTracker
A FIFA 2018 match tracker designed for sweepstakes.

<img width="600" alt="example_screenshot" src="https://raw.githubusercontent.com/mattravenhall/FifaTracker/master/screenshot.png">

During the Fifa World Cup, this site was hosted on pythonanywhere.com so that people could check the latest scores and remember who had which team. I'm putting it up here in case I want to reuse the code in the future, or in case others want to make something similar.

## Requirements
- Python3
- Pandas
- BeautifulSoup
- Flask

## Main Functions
### main.py
Primary script for running the site.

### update.py
Run often to update the match data, daily should be fine.

### matches.py
Fetch and process match data from the FIFA website.
