import matplotlib.pyplot as plt
import numpy as np

from energy_field import EnergyField
from extractor import Extractor


def game(rounds: int):
    energy_field = EnergyField()
    extractor_one = Extractor("A")
    extractor_two = Extractor("B")
    extractor_three = Extractor("C")
    extractors = [extractor_one, extractor_two, extractor_three]

    current_round = 1
    energy_field_points_over_time = [20]
    current_extractor = 0

    def rotate_extractor(current_extractor: int):
        if current_extractor + 1 == len(extractors):
            return 0
        else:
            return current_extractor + 1

    while current_round <= rounds:
        if energy_field.energy_points > 0:
            energy_field.energy_points = extractors[current_extractor].extract_max(energy_field.energy_points)
            for index, extractor in enumerate(extractors):
                if current_extractor == index:
                    continue
                extractor.skip_round()

            energy_field_points_over_time.append(energy_field.energy_points)
            if energy_field.energy_points > 0:
                energy_field.energy_points = min(energy_field.energy_points + 1, 30)

            current_round += 1
            current_extractor = rotate_extractor(current_extractor)
        else:
            for i in range(3):
                energy_field_points_over_time.append(energy_field.energy_points)
                for extractor in extractors:
                    extractor.skip_round()
                current_round += 1
                if current_round > rounds:
                    break

            energy_field.energy_points = 1

    results = {
        extractor_one.name: extractor_one.energy_points,
        extractor_two.name: extractor_two.energy_points,
        extractor_three.name: extractor_three.energy_points,
        "energy_field_points_over_time": energy_field_points_over_time,
    }
    return results


def plot_results(results, rounds):
    # Akkumulierte Energiepunkte für jeden Extraktor berechnen
    extractor_a_accumulated = results.get("A")
    extractor_b_accumulated = results.get("B")
    extractor_c_accumulated = results.get("C")

    # Plotten
    plt.figure(figsize=(10, 6))
    plt.plot(range(0, len(results.get("energy_field_points_over_time"))), results.get("energy_field_points_over_time"), label='Energiepunkte', marker='^')
    plt.plot(range(0, len(extractor_a_accumulated) ), extractor_a_accumulated, label='Extractor A', marker='o')
    plt.plot(range(0, len(extractor_b_accumulated) ), extractor_b_accumulated, label='Extractor B', marker='s')
    plt.plot(range(0, len(extractor_c_accumulated) ), extractor_c_accumulated, label='Extractor C', marker='^')

    plt.xlabel('Runde')
    plt.ylabel('Akkumulierte Energiepunkte')
    plt.title('Akkumulierte Energiepunkte der Extraktoren über die Runden')
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    rounds = 50
    results = game(rounds)
    plot_results(results, rounds)
