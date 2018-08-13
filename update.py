# Perform match update

def run():
    import os
    import pandas as pd
    from datetime import datetime
    from datetime import timedelta

    today = datetime.today().date()
    tomorrow = today + timedelta(days=1)

    # Load matches data
    if not os.path.isfile('/home/FifaTracker/labtracker/static/data/matches.csv'):
        os.system('python3 /home/FifaTracker/labtracker/matches.py')

    matches = pd.read_csv('/home/FifaTracker/labtracker/static/data/matches.csv')
    matches['Date'] = pd.to_datetime(matches['Date'])

    remaining = pd.read_csv('/home/FifaTracker/labtracker/static/data/PlayerTeams.csv')
    remaining.columns = ['Player','Team','Code','Rank','Remaining']

    previous = matches[matches['Date'] < today].sort_values('Date',ascending=False)[['Team A', 'Player A', 'Score', 'Player B', 'Team B']].head(5).to_html(index=False, classes="table table-striped table-dark")
    current = matches[matches['Date'].dt.date == today][['Team A', 'Player A', 'Time', 'Player B', 'Team B']].rename(columns={'Time':'UK Time'}).to_html(index=False, classes="table table-striped table-dark")
    future = matches[matches['Date'] >= tomorrow][['Team A', 'Player A', 'Date', 'Player B', 'Team B']].head(5).to_html(index=False, classes="table table-striped table-dark")

    remaining = remaining[['Player','Team','Rank']].sort_values('Rank').to_html(classes="table table-striped table-dark", index=False)

    return previous, current, future, remaining