from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        try:
            new_equipment = self.VALID_EQUIPMENT[equipment_type]()
        except KeyError:
            raise Exception("Invalid equipment type!")

        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        try:
            team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        except KeyError:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = next(filter(lambda x: x.__class__.__name__ == equipment_type, reversed(self.equipment)), None)
        team = next(filter(lambda x: x.name == team_name, self.teams), None)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        team.budget -= equipment.price
        team.equipment.append(equipment)
        self.equipment.remove(equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda x: x.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        affected_equipment = [x for x in self.equipment if x.__class__.__name__ == equipment_type]

        for equipment in affected_equipment:
            equipment.increase_price()

        return f"Successfully changed {len(affected_equipment)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next(filter(lambda x: x.name == team_name1, self.teams))
        team2 = next(filter(lambda x: x.name == team_name2, self.teams))

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_total = sum(x.protection for x in team1.equipment) + team1.advantage
        team2_total = sum(x.protection for x in team2.equipment) + team2.advantage

        if team1_total > team2_total:
            team1.win()
            return f"The winner is {team1.name}."
        elif team2_total > team1_total:
            team2.win()
            return f"The winner is {team2.name}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)

        message = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", f"Teams:"]

        for team in sorted_teams:
            message.append(team.get_statistics())

        return "\n".join(message)
