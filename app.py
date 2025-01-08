import numpy as np
import matplotlib.pyplot as plt

def holomorphic_functions():
    return {
        "f(z) = z^2": lambda z: z**2,
        "f(z) = exp(z)": lambda z: np.exp(z),
        "f(z) = sin(z)": lambda z: np.sin(z),
        "f(z) = cos(z)": lambda z: np.cos(z),
        "f(z) = 1/z": lambda z: 1 / z,
    }

def plot_function(selected_function):
    functions = holomorphic_functions()

    if selected_function not in functions:
        raise ValueError("Invalid function selected")

    # Créer un plan complexe
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Appliquer la fonction choisie
    W = functions[selected_function](Z)

    # Dessiner le résultat
    plt.figure(figsize=(6, 6))
    plt.imshow(np.angle(W), extent=(-2, 2, -2, 2), origin="lower", cmap="hsv")
    plt.colorbar(label="Argument of f(z)")
    plt.title(f"{selected_function}")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.show()

if __name__ == "__main__":
    print("Available functions:")
    for func in holomorphic_functions().keys():
        print(f"- {func}")

    selected_function = input("\nSelect a function to plot: ")

    try:
        plot_function(selected_function)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
