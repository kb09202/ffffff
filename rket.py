import time
import matplotlib.pyplot as plt

# Constantes
GRAVITY = 9.81  # Accélération gravitationnelle (m/s^2)
THRUST = 30.0   # Poussée de la fusée (m/s^2)
MASS = 500.0    # Masse de la fusée (kg)
BURN_RATE = 1.0 # Taux de combustion du carburant (kg/s)
INITIAL_FUEL = 100.0 # Quantité initiale de carburant (kg)

def launch_rocket():
    # Initialisation des paramètres
    altitude = 0.0  # Altitude (m)
    velocity = 0.0  # Vitesse (m/s)
    fuel = INITIAL_FUEL  # Quantité de carburant (kg)
    time_step = 0.1  # Pas de temps (s)

    # Listes pour la visualisation
    time_data = []
    altitude_data = []
    velocity_data = []
    fuel_data = []

    print("\n--- Lancement de la fusée ---\n")
    print(f"{'Temps (s)':<10} {'Altitude (m)':<15} {'Vitesse (m/s)':<15} {'Carburant (kg)':<15}")

    time_elapsed = 0.0

    while altitude >= 0:
        # Calcul de la poussée actuelle
        if fuel > 0:
            thrust_force = THRUST * fuel / MASS
            fuel -= BURN_RATE * time_step
        else:
            thrust_force = 0.0

        # Mise à jour des paramètres
        acceleration = thrust_force - GRAVITY
        velocity += acceleration * time_step
        altitude += velocity * time_step
        time_elapsed += time_step

        # Enregistrement des données pour la visualisation
        time_data.append(time_elapsed)
        altitude_data.append(max(altitude, 0))
        velocity_data.append(velocity)
        fuel_data.append(max(fuel, 0))

        # Affichage des résultats en temps réel
        print(f"{time_elapsed:<10.1f} {altitude:<15.2f} {velocity:<15.2f} {max(fuel, 0):<15.2f}")

        # Arrêt de la boucle si la fusée touche le sol
        if altitude <= 0 and velocity <= 0:
            break

        time.sleep(time_step)

    print("\n--- La fusée a terminé son vol ---\n")

    # Visualisation des résultats
    plt.figure(figsize=(10, 6))

    # Altitude
    plt.subplot(3, 1, 1)
    plt.plot(time_data, altitude_data, label="Altitude (m)", color="blue")
    plt.xlabel("Temps (s)")
    plt.ylabel("Altitude (m)")
    plt.grid(True)
    plt.legend()

    # Vitesse
    plt.subplot(3, 1, 2)
    plt.plot(time_data, velocity_data, label="Vitesse (m/s)", color="green")
    plt.xlabel("Temps (s)")
    plt.ylabel("Vitesse (m/s)")
    plt.grid(True)
    plt.legend()

    # Carburant
    plt.subplot(3, 1, 3)
    plt.plot(time_data, fuel_data, label="Carburant (kg)", color="red")
    plt.xlabel("Temps (s)")
    plt.ylabel("Carburant (kg)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    launch_rocket()
