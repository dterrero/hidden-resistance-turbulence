# Copyright (c) 2025 Dickson A. Terrero
# 
# This script is licensed for non-commercial research and academic use only.
# Redistribution, modification, or commercial use is strictly prohibited
# without prior written permission.



import numpy as np
import h5py
from scipy.ndimage import gaussian_filter, laplace
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from numpy import gradient

# Load velocity data
with h5py.File('isotropic1024coarse_block2.h5', 'r') as f:
    velocity = f['Velocity_0001'][:]  # shape: (16, 16, 16, 3)

u = velocity[..., 0]
v = velocity[..., 1]
w = velocity[..., 2]

# Compute kinetic energy
E = 0.5 * (u**2 + v**2 + w**2)
E_smoothed = gaussian_filter(E, sigma=2)
laplacian_E = laplace(E_smoothed)

# Invert gamma field
with np.errstate(divide='ignore', invalid='ignore'):
    gamma_field = -laplacian_E / (E_smoothed + 1e-8)
    gamma_field = np.clip(gamma_field, 0, np.percentile(gamma_field, 99))

# Compute vorticity components
du_dy, du_dz = gradient(u, axis=1), gradient(u, axis=2)
dv_dx, dv_dz = gradient(v, axis=0), gradient(v, axis=2)
dw_dx, dw_dy = gradient(w, axis=0), gradient(w, axis=1)

omega_x = dw_dy - dv_dz
omega_y = du_dz - dw_dx
omega_z = dv_dx - du_dy

vorticity_mag = np.sqrt(omega_x**2 + omega_y**2 + omega_z**2)

# Visualize
mid_z = gamma_field.shape[2] // 2
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

im0 = axs[0].imshow(gamma_field[:, :, mid_z], cmap='inferno')
axs[0].set_title('γ-Field (Mid-Z Slice)')
plt.colorbar(im0, ax=axs[0])

im1 = axs[1].imshow(vorticity_mag[:, :, mid_z], cmap='viridis')
axs[1].set_title('Vorticity Magnitude (Mid-Z Slice)')
plt.colorbar(im1, ax=axs[1])

plt.tight_layout()
plt.savefig("y_field_vorticity_magnitude.png")
plt.show()

# Correlation
corr = pearsonr(gamma_field.flatten(), vorticity_mag.flatten())
print(f"Pearson correlation between γ and vorticity magnitude: {corr[0]:.4f}")
