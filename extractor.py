class Extractor:
    def __init__(self, name: str):
        self.energy_points: list = [0]
        self.name: str = name

    def extract_max(self, energy_field_points: int) -> int:
        """Spielstrategie aus Aufgabe 2"""
        if energy_field_points >= 3:
            self.energy_points.append(max(self.energy_points) + 3)
            return energy_field_points - 3

        elif energy_field_points <= 2:
            self.energy_points.append(max(self.energy_points) + energy_field_points)
            return 0

    def skip_round(self):
        self.energy_points.append(max(self.energy_points))
