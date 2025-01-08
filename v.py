import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Créer une grille de valeurs x et y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Définir les fonctions
z_sin = np.sin(np.sqrt(x**2 + y**2))
z_cos = np.cos(np.sqrt(x**2 + y**2))
z_exp = np.exp(-np.sqrt(x**2 + y**2))

# Initialiser la figure
fig = plt.figure(figsize=(15, 15))

# Tracer sin(sqrt(x^2 + y^2))
ax1 = fig.add_subplot(311, projection='3d')
ax1.plot_surface(x, y, z_sin, cmap='viridis', edgecolor='none')
ax1.set_title('Surface de z = sin(sqrt(x^2 + y^2))')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.view_init(30, 30)  # Ajuster l'angle de vue

# Tracer cos(sqrt(x^2 + y^2))
ax2 = fig.add_subplot(312, projection='3d')
ax2.plot_surface(x, y, z_cos, cmap='plasma', edgecolor='none')
ax2.set_title('Surface de z = cos(sqrt(x^2 + y^2))')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.view_init(30, 30)  # Ajuster l'angle de vue

# Tracer exp(-sqrt(x^2 + y^2))
ax3 = fig.add_subplot(313, projection='3d')
ax3.plot_surface(x, y, z_exp, cmap='inferno', edgecolor='none')
ax3.set_title('Surface de z = exp(-sqrt(x^2 + y^2))')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
ax3.view_init(30, 30)  # Ajuster l'angle de vue

# Afficher le graphique
plt.tight_layout()
plt.show()
