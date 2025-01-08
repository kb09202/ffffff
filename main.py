import requests
import time
import matplotlib.pyplot as plt

# Constantes API (vous devez configurer une API pour obtenir des données de devises en temps réel)
API_URL = "https://api.exchangerate-api.com/v4/latest/"
CURRENCIES = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY"]
BASE_CURRENCY = "USD"

# Fonction pour récupérer les taux de change
def get_exchange_rates(base_currency):
    response = requests.get(f"{API_URL}{base_currency}")
    if response.status_code == 200:
        data = response.json()
        return data["rates"]
    else:
        print("Erreur lors de la récupération des données.")
        return None

# Plateforme de trading
class TradingPlatform:
    def __init__(self, base_currency):
        self.base_currency = base_currency
        self.exchange_rates = {}
        self.history = {currency: [] for currency in CURRENCIES}
        self.time_data = []

    def update_rates(self):
        rates = get_exchange_rates(self.base_currency)
        if rates:
            self.exchange_rates = {currency: rates.get(currency, 0) for currency in CURRENCIES}
            return True
        return False

    def record_history(self, time_elapsed):
        for currency in CURRENCIES:
            self.history[currency].append(self.exchange_rates.get(currency, 0))
        self.time_data.append(time_elapsed)

    def display_rates(self):
        print(f"Taux de change basés sur {self.base_currency} :")
        for currency, rate in self.exchange_rates.items():
            print(f"1 {self.base_currency} = {rate:.2f} {currency}")

    def plot_history(self):
        plt.figure(figsize=(12, 8))

        for currency in CURRENCIES:
            plt.plot(self.time_data, self.history[currency], label=f"{self.base_currency}/{currency}")

        plt.xlabel("Temps (s)")
        plt.ylabel("Taux de change")
        plt.title("Évolution des taux de change")
        plt.legend()
        plt.grid()
        plt.show()

# Main
if __name__ == "__main__":
    platform = TradingPlatform(BASE_CURRENCY)
    simulation_time = 60  # Durée de la simulation en secondes
    interval = 5          # Intervalle de mise à jour en secondes

    start_time = time.time()
    while time.time() - start_time < simulation_time:
        if platform.update_rates():
            time_elapsed = int(time.time() - start_time)
            platform.record_history(time_elapsed)
            platform.display_rates()
        else:
            print("Erreur lors de la mise à jour des taux.")

        time.sleep(interval)

    # Afficher l'historique des taux de change
    platform.plot_history()
