from typing import List
from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH = {"PredatoryFish": PredatoryFish,"DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVERS:
            return f"{diver_type} is not allowed in our competition."

        diver = next(filter(lambda d: d.name == diver_name, self.divers), None)
        if diver:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVERS[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = next(filter(lambda f: f.name == fish_name, self.fish_list), None)
        if fish:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISH[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next(filter(lambda d: d.name == diver_name, self.divers), None)
        if diver is None:
            return f"{diver_name} is not registered for the competition."

        fish = next(filter(lambda f: f.name == fish_name, self.fish_list), None)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            message = f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                message = f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                message = f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            message = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level == 0:
            diver.has_health_issue = True

        return message

    def health_recovery(self):
        divers_recovered = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.renew_oxy()
                diver.has_health_issue = False
                divers_recovered += 1
        return f"Divers recovered: {divers_recovered}"

    def diver_catch_report(self, diver_name: str):
        diver = next(filter(lambda d: d.name == diver_name, self.divers))
        message = [f"**{diver_name} Catch Report**"]

        for fish in diver.catch:
            message.append(f"{fish.fish_details()}")

        return "\n".join(message)

    def competition_statistics(self):
        good_health_divers = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(good_health_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        message = ["**Nautical Catch Challenge Statistics**"]

        for diver in sorted_divers:
            message.append(diver.__str__())

        return "\n".join(message)
