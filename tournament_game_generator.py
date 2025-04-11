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


def determine_matchups():
    # Teams with the most regular season wins play the teams with thte least regular season wins.
    # If teams are tied in wins, the program can determine the matchup.
    # The team with less wins should be the home team.
    # If there is a tie in wins, the program can determine the home team.
    pass

def first_round_games():
    pass


if __name__ == '__main__':
    teams_info = get_team_info()
    n_games = get_game_info(teams_info)