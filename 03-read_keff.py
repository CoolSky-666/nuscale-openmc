import openmc
import re
from pathlib import Path
import pandas as pd

ref_xlsx = Path("ref/02-Reference_Solution_v3.xlsx")
df_ref = pd.read_excel(ref_xlsx, sheet_name="k-eff + CRW")
df_ref = df_ref[["Unnamed: 0", "k-eff"]].dropna()
ref_map = dict(zip(df_ref["Unnamed: 0"].astype(str), df_ref["k-eff"].astype(float)))

dir_to_case = {
    "Reference": "All rods out (ARO)",
    "RE1in": "RE1 in",
    "RE2in": "RE2 in",
    "SH3in": "SH3 in",
    "SH4in": "SH4 in",
    "SCRAM": "All rods in (ARI)",
}

run_dirs = [
    Path("data/Reference"),
    Path("data/RE1in"),
    Path("data/RE2in"),
    Path("data/SH3in"),
    Path("data/SH4in"),
    Path("data/SCRAM"),]

headers = ["case", "statepoint", "k-eff", "ref_k-eff", "rel_err(%)"]
rows = []

for d in run_dirs:
    files = list(d.glob("statepoint.*.h5"))
    if not files:
        case_label = dir_to_case.get(d.name, d.name)
        rows.append([case_label, "N/A", "N/A", "N/A", "N/A"])
        continue

    parsed = []
    for p in files:
        m = re.match(r"statepoint\.(\d+)\.h5$", p.name)
        if m:
            parsed.append((int(m.group(1)), p))

    if parsed:
        sp_path = max(parsed, key=lambda x: x[0])[1]
    else:
        sp_path = max(files, key=lambda p: p.stat().st_mtime)

    case_label = dir_to_case.get(d.name, d.name)
    ref_keff = ref_map.get(case_label)

    with openmc.StatePoint(str(sp_path)) as sp:
        k = float(sp.keff.n)

    if ref_keff is None or ref_keff == 0:
        rel_err = None
    else:
        rel_err = (k - float(ref_keff)) / float(ref_keff) * 100.0

    k_str = f"{k:.5f}"
    ref_str = f"{float(ref_keff):.5f}" if ref_keff is not None else "N/A"
    err_str = f"{rel_err:.5f}" if rel_err is not None else "N/A"

    rows.append([case_label, sp_path.name, k_str, ref_str, err_str])

widths = []
for i, h in enumerate(headers):
    widths.append(max(len(h), *(len(r[i]) for r in rows)))

fmt = "  ".join([f"{{:<{w}}}" for w in widths])
print(fmt.format(*headers))
print(fmt.format(*["-" * w for w in widths]))
for r in rows:
    print(fmt.format(*r))
