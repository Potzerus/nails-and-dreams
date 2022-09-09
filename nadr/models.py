class Weapon:
    dance_service: DanceService
    base_damage: int
    actions: list[str]


class Inventory:
    unique: set[Item]


class Player:
    weapon: Weapon
    inventory: Inventory
    flores: int  # Currency
