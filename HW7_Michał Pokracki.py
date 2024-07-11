# Homework for Topic 7

import heapq

def minimum_cost_to_connect_cables(cables):
    """Oblicza minimalny koszt połączenia kabli sieciowych.

    Args:
        cables: Lista długości kabli sieciowych.

    Returns:
        Minimalny całkowity koszt połączenia wszystkich kabli.

    Raises:
        ValueError: Jeśli którykolwiek z kabli ma długość niedodatnią.
    """

    if not cables:  # Obsługa pustej listy
        return 0

    # Sprawdzenie, czy wszystkie kable mają dodatnią długość
    if any(cable <= 0 for cable in cables):
        raise ValueError("Długości kabli muszą być liczbami dodatnimi.")

    # Utworzenie kopca minimalnego (min-heap) z listy kabli
    heapq.heapify(cables)

    total_cost = 0

    # Dopóki w kopcu jest więcej niż jeden kabel
    while len(cables) > 1:
        # Wyciągnięcie dwóch najkrótszych kabli
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Koszt połączenia tych dwóch kabli
        cost = first + second

        # Dodanie nowego kabla (połączonego) z powrotem do kopca
        heapq.heappush(cables, cost)

        # Akumulacja całkowitego kosztu
        total_cost += cost

    return total_cost

# Przykładowe użycie:
cables = [4, 3, 2, 6, 10, 15]
print(minimum_cost_to_connect_cables(cables))  
