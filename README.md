# 🔬 Hidden Resistance in Turbulence

This repository documents the results of a novel method to **infer internal dissipation structures** (γ-field) directly from observed 3D turbulent velocity fields.

📅 **Date of experiment:** June 23, 2025  
🧠 **Theory author:** Dickson A. Terrero  
📂 **Status:** Preliminary results (data-driven inversion only)

---

## 📌 Project Summary

Using smoothed kinetic energy and its Laplacian, we invert for a scalar dissipation field \( γ(x,y,z) \), which reflects **internal resistance to transformation** in turbulent flows. This field is not assumed but **inferred** directly from velocity data.

We then compare this inferred field against:
- ✅ Strain rate magnitude
- ✅ Vorticity magnitude

This serves as a **validation layer** for the γ-inversion methodology.

---

## 📁 Contents

- `gamma_inversion_64cube.py`: core script for energy Laplacian-based γ inversion
- `strain_and_vorticity_analysis.py`: correlation tests with physical observables
- `figures/`: visualizations of the inferred γ-field and comparisons

---

## 🧪 Key Result (June 23)

- Inverted γ-field shows strong coherent structures
- Qualitative match with energetic regions
- Pearson correlation with strain: **-0.25**
- Pearson correlation with vorticity: **-0.13**

While not highly correlated, γ identifies **energy-centric features** distinct from traditional fields — offering a complementary perspective on turbulence.

---

## ⚠️ License and Use

This repository is shared **for academic non-commercial use only**.  
Please see the [LICENSE](LICENSE) for full terms.

- ❌ Do not use for machine learning model training.
- ❌ Do not derive or publish the theory behind the code.
- ✅ Academic replication and peer review is allowed.

For questions, contact the author: **dicksont@gmail.com**

---

## 📊 Screenshot

![γ-field slice vs vorticity](figures/y_field_vorticity_magnitude_mid_z_slice.png)

---

## 🧭 Next Steps

- Extend to full-resolution DNS data (e.g., JHTDB)
- Explore correlations with dissipation ε if available
- Develop formal theory documentation

---

> This repository represents the beginning of a broader theoretical framework. The code alone is **not sufficient** to reconstruct the full theory.
