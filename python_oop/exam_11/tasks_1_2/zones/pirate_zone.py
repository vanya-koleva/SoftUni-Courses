from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)
        self.zone_type = 'PirateZone'

    def zone_info(self):
        ships = self.get_ships()
        total_ships = len(ships)
        royal_ships = sum(1 for x in ships if x.ship_type == "RoyalBattleship")
        ship_names = ', '.join(x.name for x in ships) if ships else ""

        result = (f"@Pirate Zone Statistics@\n"
                  f"Code: {self.code}; Volume: {self.volume}\n"
                  f"Battleships currently in the Pirate Zone: {total_ships}, "
                  f"{royal_ships} out of them are Royal Battleships.")

        return result + f"\n#{ship_names}#" if ship_names else result
