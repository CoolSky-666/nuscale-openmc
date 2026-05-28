import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

xlsx_path = "./ref/02-Reference_Solution_v3.xlsx"
out_png = "./figs/fig11-pinpower-ref.png"

df_ref = pd.read_excel(
    xlsx_path,
    sheet_name="pin_pow_ref",
    header=None,
    usecols="B:DP",
    nrows=119,
)

df_CR = pd.read_excel(
    xlsx_path,
    sheet_name="pin_pow_CR",
    header=None,
    usecols="B:DP",
    nrows=119,
)

mat_ref = df_ref.to_numpy(dtype=float)
mat_cr = df_CR.to_numpy(dtype=float)

masked_ref = np.ma.masked_invalid(mat_ref)
masked_cr = np.ma.masked_invalid(mat_cr)

vmin_ref = float(np.nanmin(mat_ref))
vmax_ref = float(np.nanmax(mat_ref))
vmin_cr = float(np.nanmin(mat_cr))
vmax_cr = float(np.nanmax(mat_cr))

fig, axes = plt.subplots(1, 2, figsize=(12, 6), constrained_layout=True)

im0 = axes[0].imshow(masked_ref, cmap="jet", vmin=vmin_ref, vmax=vmax_ref, interpolation="nearest")
im1 = axes[1].imshow(masked_cr, cmap="jet", vmin=vmin_cr, vmax=vmax_cr, interpolation="nearest")

for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")

axes[0].set_title("Reference state (all rods out)", y=-0.08)
axes[1].set_title("Asymmetric insertion of a single RE1 CR at D5", y=-0.08)

cb0 = fig.colorbar(im0, ax=axes[0], fraction=0.046, pad=0.04)
fmt0 = ScalarFormatter(useMathText=True)
fmt0.set_powerlimits((4, 4))
cb0.formatter = fmt0
cb0.update_ticks()

cb1 = fig.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)
fmt1 = ScalarFormatter(useMathText=True)
fmt1.set_powerlimits((4, 4))
cb1.formatter = fmt1
cb1.update_ticks()
fig.savefig(out_png, dpi=200)
plt.close(fig)
print(out_png)
