from typing import Callable, Enum, Iterable

import tomli


class ActionType(Enum):
    attack = "attack"
    buff = "buff"
    heal = "heal"


class DanceService:
    def __init__(self, filepath):
        self.moves = {
            move["label"]: self.actionify(move)
            for move in tomli.loads(open(filepath, "r").read())
        }

    def actionify(move: dict) -> Callable:

        a_type = ActionType(move["type"])

        def predicate(player, target, weapon) -> Iterable[Callable]:
            for event in move["events"]:
                who, what, value = event.split("|")

    def parse(self, action: str):
        return self.moves[action]
