def team_message(team):
    if team.lower() == "arsenal":
        return "Trust the process! Big season ahead 🔴"
    else:
        return "Every season is a new opportunity ⚽"


if __name__ == "__main__":
    team = input("Enter your team: ")
    print(team_message(team))
