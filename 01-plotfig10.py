import pandas as pd
import matplotlib.pyplot as plt

xlsx_path = "./ref/02-Reference_Solution_v3.xlsx"
out_png = "./figs/fig10-pow_ax.png"

df = pd.read_excel(xlsx_path, sheet_name="pow_ax")

lower = pd.to_numeric(df["Lower boundary, cm"], errors="coerce")
upper = pd.to_numeric(df["Upper boundary, cm"], errors="coerce")
power = pd.to_numeric(df["Power, MW"], errors="coerce")

data = pd.DataFrame({"lower": lower, "upper": upper, "power": power}).dropna()
data = data.sort_values(["lower", "upper"]).reset_index(drop=True)
print(data)

x = []
y = []
for _, r in data.iterrows():
    h0 = float(r["lower"])
    h1 = float(r["upper"])
    p = float(r["power"])
    x.extend([h0, h1])
    y.extend([p, p])

y_max = float(data["power"].max()) if data["power"].notna().any() else 1.0
y_min = 0.0
y_pad = 0.5

fig = plt.figure(figsize=(12, 6))
plt.plot(x, y, color="blue", linewidth=2.0)

x_grid = [14.92,19.365,65.974,70.419,117.028,121.473,168.082,172.527]
plt.vlines(
    x_grid,
    ymin=y_min,
    ymax=y_max + y_pad,
    colors="red",
    linestyles=(0, (6, 4)),
    linewidth=1.5,
    label="Spacer grid")

plt.xlabel("Height (cm)")
plt.ylabel("Power (MW)")
plt.xlim(float(data["lower"].min()), float(data["upper"].max()))
plt.ylim(y_min, y_max + y_pad)
plt.grid(True, alpha=0.5)
plt.legend(loc="upper right")
fig.savefig(out_png, dpi=200)
plt.close(fig)
print(out_png)
