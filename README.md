# espn-ffb-schedule-analysis

## Overview

The *headtohead.py* function creates spreadsheets containing information about matchups in an ESPN fantasy football league. The two sheets created are a HeadToHead excel file that details what each team's record would be if it went up against another team in the league *every* week of the season (Team A's record if it faced Team B every week) and a SameSchedule excel file that details what each team's record would be if it went up against another team's opponents every week (Team A's record if it had Team B's schedule).

### Getting Started

#### Command Line Arguments

Four command line arguments are needed for the *draftresults.py* function. The first two are cookies, which are required to access information for private leagues.

To access the cookies, in Chrome go to Settings -> Privacy and Security -> Site Settings -> Cookies and site data -> See all cookies and site data -> espn.com. Find the *espn_s2* and *SWID* cookies. These are the first two command line arguments.

The third command line argument is the League ID, which can be found simply by going to your league from the [ESPN Fantasy homepage](https://www.espn.com/fantasy/football/). From any page in your league, the url should have a *leagueId* value included within the url.

The fourth command line argument is Season ID, which is the year of the fantasy season that will be analyzed. Note that the season must be completed. Also it appears that there is no longer player information available for years before 2018, so the code will only work using 2018 or later.

The final function call will be in the form: python draftresults.py [*espn_s2 HERE*] [*SWID HERE*] [*LEAGUEID HERE*] [*SEASONID HERE*]

*Example:* python headtohead.py ABCDEFGHIJKLMNOPQRSTUVWXYZ%1%2%3%4%5%6%7%8%9%0 ABCD-EFG-HIJ-KLMN 12345 2019

#### Additional Setup

I recommend creating and activating a Python virtual environment.

Install the necessary libraries by running *pip install -r requirements.txt* in the terminal.