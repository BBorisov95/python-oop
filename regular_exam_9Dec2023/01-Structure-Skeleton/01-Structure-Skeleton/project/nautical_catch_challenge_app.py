from project.divers.base_diver import BaseDiver
from project.divers.scuba_diver import ScubaDiver
from project.divers.free_diver import FreeDiver
from project.fish.base_fish import BaseFish
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish
from typing import List


class NauticalCatchChallengeApp:
    VALID_DIVERS = {'ScubaDiver': ScubaDiver,
                    'FreeDiver': FreeDiver}

    VALID_FISHES = {'PredatoryFish': PredatoryFish,
                    'DeepSeaFish': DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVERS:
            return f"{diver_type} is not allowed in our competition."
        try:
            diver = any([d for d in self.divers if d.name == diver_name])
            if diver:
                return f"{diver_name} is already a participant."
        except IndexError:
            pass
        new_diver = self.VALID_DIVERS[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISHES:
            return f"{fish_type} is forbidden for chasing in our competition."
        try:
            fish = any([f for f in self.fish_list if f.name == fish_name])
            if fish:
                return f"{fish_name} is already permitted."
        except IndexError:
            pass
        new_fish = self.VALID_FISHES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = [d for d in self.divers if d.name == diver_name][0]
        except IndexError:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = [f for f in self.fish_list if f.name == fish_name][0]
        except IndexError:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish.name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = [d for d in self.divers if d.name == diver_name][0]
        result = [f'**{diver_name} Catch Report**']
        for f in diver.catch:
            result.append(f.fish_details())
        return '\n'.join(result)

    def competition_statistics(self):
       # filtered_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(self.divers, key=lambda diver: (-diver.competition_points, -len(diver.catch), diver.name))
        result = ['**Nautical Catch Challenge Statistics**']
        for d in sorted_divers:
            if not d.has_health_issue:
                result.append(str(d))
        return '\n'.join(result)
