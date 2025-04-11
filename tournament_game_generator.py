# Tornament Game Generator 
# Schedule games that teams will play in an end of year tournament.
# Determine the games played in the first round of the tournament.

def get_team_info():
    # Get input of the number of teams
    # I may assume there are always an even number of teams
    # Asks for all team names and stores them
    teams_info = {}
    n_teams = 0
    while n_teams < 2:
        n_teams = input("Enter the number of teams in the tournament: ")
        if not n_teams.isdigit():
            print('Invalid input, try again. Enter an integer.')
            n_teams = 0
            continue

        n_teams = int(n_teams)
        if n_teams < 2:
            print('The minimum number of teams is 2, try again.')

    assert n_teams != 0
    assert n_teams % 2 == 0

    for i in range(n_teams):
        team_name = input(f'Enter the name for team #{i+1}: ')
        
        # Check num of chars in team name
        while len(team_name) < 2:
            print('Team names must have at least 2 characters, try again')
            team_name = input(f'Enter the name for team #{i+1}: ')

        # Check num of words in team name
        word_count = len(team_name.split())
        while word_count > 2:
            print('Team names may have have at most 2 words, try again.')
            team_name = input(f'Enter the name for team #{i+1}: ')
            word_count = len(team_name.split())

        # Check if team was already entered
        while team_name in teams_info:
            print(f'{team_name} is already in the tournament. Please enter a new team:')
            team_name = input(f'Enter the name for team #{i+1}: ')
        
        teams_info[team_name] = None
    
    return teams_info
        
def get_game_info(teams_info):
    n_teams = len(teams_info)

    # Check if each team at least pays each other once
    while True:
        n_games = input("Enter the number of games played by each team: ")
        
        # Check input is an integer
        while not n_games.isdigit():
            print('Invalid input, try again. Enter an integer.')
            n_games = input('Enter the number of games played by each team: ')
        
        n_games = int(n_games)
        if n_games < (n_teams-1):
            print('Invalid number of games. Each team plays each other a least once in the regular season, try again.')
        else:
            break

    assert n_games != 0

    return n_games


def get_regular_season_performance(teams_info, n_games):
    # Teams with the most regular season wins play the teams with thte least regular season wins.
    # If teams are tied in wins, the program can determine the matchup.
    # The team with less wins should be the home team.
    # If there is a tie in wins, the program can determine the home team.
    assert len(teams_info) > 0
    for team in teams_info.keys():
        while True:
            wins = input(f'Enter the number of wins Team {team} had: ')
            # Check if input is an integer
            while not (wins.isdigit() or (wins.startswith('-') and wins[1:].isdigit())):
                print('Invalid input, try again. Enter an integer.')
                wins = input(f'Enter the number of wins Team {team} had: ')
            
            wins = int(wins)
            # Check if wins in [0, n_games]
            if wins > n_games:
                print(f'The maximum number of wins is {n_games}, try again.')
            elif wins < 0:
                print('The minimum number of wins is 0, try again.')
            else:
                break
        
        teams_info[team] = wins
    return teams_info

def determine_matchups(teams_info):
    leaderboard = []
    for wins in teams_info.values():
        leaderboard.append(wins)
    
    # Bubble sort
    for i in range(len(leaderboard) - 1):
        already_sorted = True
        for j in range(len(leaderboard) - 1 - i):
            if leaderboard[j] < leaderboard[j+1]:
                leaderboard[j], leaderboard[j+1] = leaderboard[j+1], leaderboard[j]
                already_sorted = False
        if already_sorted:
            break
    # print(f'leaderboard: {leaderboard}')
    return leaderboard

def generate_first_round(teams_info, leaderboard):
    first_round = []
    n_first_round_games = int(len(teams_info) / 2)

    # Inverted_teams_info to index by wins and get team name {win_count: [team1, team2, ..., teamN]}
    inverted_teams_info = {}
    for team_name, win_count in teams_info.items():
        teams = []
        if win_count in inverted_teams_info:
            inverted_teams_info[win_count].append(team_name)
        else:
            teams.append(team_name)
            inverted_teams_info[win_count] = teams  

    # inverted_teams_info = {value: key for key, value in teams_info.items()} # to index by wins and get team_name
    # print(f'inverted teams info: {inverted_teams_info}')
    for i in range(n_first_round_games):
        match_up = None
        stronger_team = inverted_teams_info[leaderboard[i]].pop()
        weaker_team = inverted_teams_info[leaderboard[-(i+1)]].pop()

        match_up = [stronger_team, weaker_team]
        first_round.append(match_up)
    
    # print(f'first round matches: {first_round}')
    print('Generating the games to be played in the first round of the tournament...')
    for match_up in first_round:
        stronger_team = match_up[0]
        weaker_team = match_up[1]
        print(f'Home: {weaker_team} VS Away: {stronger_team}')

if __name__ == '__main__':
    teams_info = get_team_info()
    n_games = get_game_info(teams_info)
    teams_info = get_regular_season_performance(teams_info, n_games)
    leaderboard = determine_matchups(teams_info)
    generate_first_round(teams_info, leaderboard)
    
    