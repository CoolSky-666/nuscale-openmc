import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

xlsx_path = "./ref/02-Reference_Solution_v3.xlsx"
out_png = "./figs/fig9-rppf_heatmap.png"

df_ref = pd.read_excel(
    xlsx_path,
    sheet_name="rad_pow_ref",
    header=None,
    usecols="A:G",
    nrows=7,
)

df_cr = pd.read_excel(
    xlsx_path,
    sheet_name="rad_pow_CR",
    header=None,
    usecols="A:G",
    nrows=7,
)

mat_ref = df_ref.to_numpy(dtype=float)
mat_cr = df_cr.to_numpy(dtype=float)

vmin_ref = float(np.nanmin(mat_ref))
vmax_ref = float(np.nanmax(mat_ref))
vmin_cr = float(np.nanmin(mat_cr))
vmax_cr = float(np.nanmax(mat_cr))

fig, axes = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)

masked_ref = np.ma.masked_invalid(mat_ref)
masked_cr = np.ma.masked_invalid(mat_cr)

im0 = axes[0].imshow(masked_ref, cmap="jet", vmin=vmin_ref, vmax=vmax_ref, interpolation="nearest")
im1 = axes[1].imshow(masked_cr, cmap="jet", vmin=vmin_cr, vmax=vmax_cr, interpolation="nearest")

axes[0].set_title("Ref state (all rods out)")
axes[1].set_title("Single RE1 CR")

for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])

cmap = plt.get_cmap("jet")
den_ref = vmax_ref - vmin_ref
den_cr = vmax_cr - vmin_cr
if den_ref == 0:
    den_ref = 1.0
if den_cr == 0:
    den_cr = 1.0
for i in range(mat_ref.shape[0]):
    for j in range(mat_ref.shape[1]):
        v = mat_ref[i, j]
        if np.isfinite(v):
            c = cmap((v - vmin_ref) / den_ref)
            lum = 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
            axes[0].text(j, i, f"{v:.3f}", ha="center", va="center", fontsize=9, color="black" if lum > 0.6 else "white")

for i in range(mat_cr.shape[0]):
    for j in range(mat_cr.shape[1]):
        v = mat_cr[i, j]
        if np.isfinite(v):
            c = cmap((v - vmin_cr) / den_cr)
            lum = 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
            axes[1].text(j, i, f"{v:.3f}", ha="center", va="center", fontsize=9, color="black" if lum > 0.6 else "white")

fig.colorbar(im0, ax=axes[0], fraction=0.046, pad=0.04)
fig.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)
fig.savefig(out_png, dpi=200)
plt.close(fig)
print(out_png)
