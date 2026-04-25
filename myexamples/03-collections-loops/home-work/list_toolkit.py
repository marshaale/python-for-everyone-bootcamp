premier_league_teams = ["Liverpool","West Ham","Man U","Man City","Everton"]

# Printing the first and last team
print("First team:",premier_league_teams[0])
print("Last team:",premier_league_teams[-1])

# Adding new team
premier_league_teams.append("Bottle Fc")
print(premier_league_teams)

# Removing team by name
premier_league_teams.remove("Man U")

# Display number of teams
print(len(premier_league_teams))