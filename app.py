from constants import PLAYERS
from constants import TEAMS


def clean_data(original_list):
    #create new list
    new_player_list = []
    #create empty dictionary for each player, within new list
    for item in original_list:
        new_player_list.append({})
    #add cleaned data to each player's dictionary
    for item in original_list:
        index = original_list.index(item)
        new_player_list[index]['name'] = item['name']
        new_player_list[index]['guardians'] = item['guardians'].split(' and ')
        if item['experience'] == "YES":
            new_player_list[index]['experience'] = True
        else:
            new_player_list[index]['experience'] = False
        new_player_list[index]['height'] = int(item['height'][0:2])
    # return cleaned player data list
    return new_player_list


def divide_players(player_list, team_list):
    num_per_team = len(player_list) // len(team_list)
    players_on_team = [player_list[i:i+num_per_team] for i in range(0,len(player_list),num_per_team)]
    return players_on_team


def balance_teams(player_list, team_list):
    experienced_players = []
    inexperienced_players = []
    for item in player_list:
        if item['experience']:
            experienced_players.append(item['name'])
        else:
            inexperienced_players.append(item['name'])
    #Divide experienced and inexperienced players into teams using sublists 
    experienced_by_team = divide_players(experienced_players, team_list)
    inexperienced_by_team = divide_players(inexperienced_players, team_list)
    #Add 'Team':Team Name to each player's dictionary
    for team in team_list:
        players_by_team = experienced_by_team[team_list.index(team)] + inexperienced_by_team[team_list.index(team)]
        for item in player_list:
            if item['name'] in players_by_team:
                item['team'] = team


def players_by_team_data(player_list, team_list):
    players_by_team_data = []
    for team in team_list:
        players_by_team_data.append([])
    for team in team_list:
        for item in player_list:
            if item['team'] == team:
                players_by_team_data[team_list.index(team)].append(item)
    return players_by_team_data
                                    

def menu_selection():
    print("\n-----------MENU-----------")
    print("""\nHere are your choices:
      1) Display Team Stats
      2) Quit""")
    while True:
        try:
            menu_choice = int(input("Enter your choice here: "))
            while menu_choice > 2 or menu_choice < 1:
                menu_choice = int(input("\nInvalid entry, outside of the range. \nEnter a number between 1 and 2: "))
            return menu_choice
        except ValueError:
            print("\nInvalid entry. Please use a numeral.")


def team_selection():
    while True:
            try:
                team_choice = int(input("Enter your choice here: "))
                while team_choice > 3 or team_choice < 1:
                    team_choice = int(input("\nInvalid entry, outside of the range. \nEnter a number between 1 and 3: "))
                if team_choice <= 3 and team_choice >= 1:
                    return run_team_stats(team_choice)
            except ValueError:
                print("\nInvalid entry. Please use a numeral.")    
    
    
def run_team_stats(team):
    index = int(team) - 1
    experience_count = 0
    total_height = 0
    player_list = []
    guardian_list = []
    #Total Player Count
    player_count = len(players_by_team[index])
    #Loop through players and update Experience Count, Total Height, Player List, & Guardian List
    for player in players_by_team[index]:
        #Experienced Player Count
        if player['experience'] == True:
            experience_count += 1
        #Total Height
        total_height += player['height']
        #Players List
        player_list.append(player['name'])
        #Guardians List
        for guardian in player['guardians']:
            guardian_list.append(guardian)
    #Print Stats
    print("\n{} Stats".format(TEAMS[index]))
    print("---------------")
    print("Total Players:", player_count)
    print("  Experienced Players:", experience_count)
    print("  Inexperienced Players:", player_count - experience_count)
    average_height = total_height / player_count
    print("\nAverage Player Height:", average_height)
    player_names = ", ".join(player_list)
    print("\nPlayers:\n  {}".format(player_names)) 
    guardian_names = ", ".join(guardian_list)
    print("\nGuardians:\n  {}".format(guardian_names))
    

if __name__ == '__main__': 
    
    clean_players_list = clean_data(PLAYERS)
    balance_teams(clean_players_list, TEAMS)
    players_by_team = players_by_team_data(clean_players_list, TEAMS)
    
    print("--------------------------")
    print("BASKETBALL TEAM STATS TOOL")
    print("--------------------------")
    
    menu_num = menu_selection()
    
    while menu_num == 1:
        print("""\nWhich team's stats would you like to see? Here are your choices:
        1) Panthers
        2) Bandits
        3) Warriors""")
        
        team_selection()
        continue_tool = input("\nPress ENTER to continue...")
        menu_num = menu_selection()
        
    else:
        print("\nThanks for using the Basketball Team Stats Tool. Have a great day!")
    


   
