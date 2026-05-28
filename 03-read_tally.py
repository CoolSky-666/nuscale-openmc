import openmc
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

statepoint_filename = 'data/Reference/statepoint.300.h5' # Reference state
statepoint_filename = 'data/RE1d5in/statepoint.300.h5' # Reference state
sp = openmc.StatePoint(statepoint_filename)

power_w = 160e6
t1 = sp.get_tally(name='rad_pow')
t2 = sp.get_tally(name='pin_pow')
t3 = sp.get_tally(name='pow_ax')

t1_mean = t1.mean*37 / np.sum(t1.mean)
t2_mean = t2.mean*power_w / np.sum(t2.mean) # Transfer to W
t3_mean = t3.mean*160 / np.sum(t3.mean)

rad_mean = t1_mean.reshape((7,7))[::-1]
pin_mean = t2_mean.reshape((7*17,7*17))[::-1]
ax_mean = np.squeeze(t3_mean)

rad_mean[rad_mean == 0] = np.nan
pin_mean[pin_mean == 0] = np.nan

fig, ax = plt.subplots(figsize=(10, 8), constrained_layout=True)
masked_rad = np.ma.masked_invalid(rad_mean)
im = ax.imshow(masked_rad, cmap="jet", interpolation="nearest")
ax.set_xticks(np.arange(7))
ax.set_yticks(np.arange(7))
ax.set_xticklabels(list("ABCDEFG"), fontsize=14)
ax.set_yticklabels(list("1234567"), fontsize=14)
ax.tick_params(axis="x", which="both", length=0)
ax.tick_params(axis="y", which="both", length=0)
for i in range(7):
    for j in range(7):
        v = rad_mean[i, j]
        if np.isfinite(v):
            c = plt.get_cmap("jet")(im.norm(v))
            lum = 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
            ax.text(
                j,
                i,
                f"{v:.3f}",
                ha="center",
                va="center",
                fontsize=14,
                color="black" if lum > 0.6 else "white",
            )
fig.colorbar(im, ax=ax)
fig.savefig("./figs/t1-ref-rad_pow.png", dpi=300)
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 8), constrained_layout=True)
masked_pin = np.ma.masked_invalid(pin_mean)
im = ax.imshow(masked_pin, cmap="jet", interpolation="nearest")
ax.set_xticks([])
ax.set_yticks([])
cb = fig.colorbar(im, ax=ax)
fmt = ScalarFormatter(useMathText=True)
fmt.set_powerlimits((4, 4))
cb.formatter = fmt
cb.update_ticks()
fig.savefig("./figs/t2-ref-pin_pow.png", dpi=300)
plt.close(fig)

height = np.array([11.365,14.920,19.365,31.017,42.670,54.322,65.974,70.419,82.071,93.724,105.376,117.028,121.473,133.125,144.778,156.430,168.082,172.527,182.236,191.946,201.656,211.365])
power_mw = np.append(ax_mean, ax_mean[-1])
fig = plt.figure(figsize=(16, 9))
plt.xticks(height, height)
plt.step(height, power_mw, where='post', linewidth=1, label='Axis power', color='blue')
grid_x = [168.082,121.473,117.028,70.419,65.974,19.365,14.92]
plt.axvline(x=172.527, color='red', linestyle='--', linewidth=1, label='Spacer grid')
for pos in grid_x:
    plt.axvline(x=pos, color='red', linestyle='--', linewidth=1)
plt.xlabel('Height (cm)')
plt.ylabel('Power (MW)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.xlim(float(height.min()), float(height.max()))
plt.savefig('./figs/t3-refax_pow.png', format='png', dpi=300)
plt.close(fig)
