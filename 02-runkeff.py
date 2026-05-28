import openmc
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

tem_structre = 600
tem_coolant = 900
tem_fuel = 900

# Structure材料
zr_4 = openmc.Material(name="Zr-4",material_id=1)
zr_4.add_nuclide('Cr50', 3.29620E-06, 'ao')
zr_4.add_nuclide('Cr52', 6.35640E-05, 'ao')
zr_4.add_nuclide('Cr53', 7.20760E-06, 'ao')
zr_4.add_nuclide('Cr54', 1.79410E-06, 'ao')
zr_4.add_nuclide('Fe54', 8.66980E-06, 'ao')
zr_4.add_nuclide('Fe56', 1.36100E-04, 'ao')
zr_4.add_nuclide('Fe57', 3.14310E-06, 'ao')
zr_4.add_nuclide('Fe58', 4.18290E-07, 'ao')
zr_4.add_nuclide('O16', 3.07440E-04, 'ao')
zr_4.add_nuclide('O17', 1.16800E-07, 'ao')
zr_4.add_nuclide('Sn112', 4.67350E-06, 'ao')
zr_4.add_nuclide('Sn114', 3.17990E-06, 'ao')
zr_4.add_nuclide('Sn115', 1.63810E-06, 'ao')
zr_4.add_nuclide('Sn116', 7.00550E-05, 'ao')
zr_4.add_nuclide('Sn117', 3.70030E-05, 'ao')
zr_4.add_nuclide('Sn118', 1.16690E-04, 'ao')
zr_4.add_nuclide('Sn119', 4.13870E-05, 'ao')
zr_4.add_nuclide('Sn120', 1.56970E-04, 'ao')
zr_4.add_nuclide('Sn122', 2.23080E-05, 'ao')
zr_4.add_nuclide('Sn124', 2.78970E-05, 'ao')
zr_4.add_nuclide('Zr90', 2.18280E-02, 'ao')
zr_4.add_nuclide('Zr91', 4.76010E-03, 'ao')
zr_4.add_nuclide('Zr92', 7.27590E-03, 'ao')
zr_4.add_nuclide('Zr94', 7.37340E-03, 'ao')
zr_4.add_nuclide('Zr96', 1.18790E-03, 'ao')
zr_4.set_density('atom/b-cm', 4.343885E-02)


# Inconel
inconel = openmc.Material(name="Inconel",material_id=2)
inconel.add_nuclide('Cr50', 7.82390E-04, 'ao')
inconel.add_nuclide('Cr52', 1.50880E-02, 'ao')
inconel.add_nuclide('Cr53', 1.71080E-03, 'ao')
inconel.add_nuclide('Cr54', 4.25860E-04, 'ao')
inconel.add_nuclide('Fe54', 1.47970E-03, 'ao')
inconel.add_nuclide('Fe56', 2.32290E-02, 'ao')
inconel.add_nuclide('Fe57', 5.36450E-04, 'ao')
inconel.add_nuclide('Fe58', 7.13920E-05, 'ao')
inconel.add_nuclide('Mn55', 7.82010E-04, 'ao')
inconel.add_nuclide('Ni58', 2.93200E-02, 'ao')
inconel.add_nuclide('Ni60', 1.12940E-02, 'ao')
inconel.add_nuclide('Ni61', 4.90940E-04, 'ao')
inconel.add_nuclide('Ni62', 1.56530E-03, 'ao')
inconel.add_nuclide('Ni64', 3.98640E-04, 'ao')
inconel.add_nuclide('Si28', 5.67570E-04, 'ao')
inconel.add_nuclide('Si29', 2.88200E-05, 'ao')
inconel.add_nuclide('Si30', 1.89980E-05, 'ao')
inconel.set_density('atom/b-cm', 8.778987E-02)

# 304L SS
ss_304l = openmc.Material(name="304L SS")
ss_304l.add_nuclide('Cr50', 7.67780E-04, 'ao')
ss_304l.add_nuclide('Cr52', 1.48060E-02, 'ao')
ss_304l.add_nuclide('Cr53', 1.67890E-03, 'ao')
ss_304l.add_nuclide('Cr54', 4.17910E-04, 'ao')
ss_304l.add_nuclide('Fe54', 3.46200E-03, 'ao')
ss_304l.add_nuclide('Fe56', 5.43450E-02, 'ao')
ss_304l.add_nuclide('Fe57', 1.25510E-03, 'ao')
ss_304l.add_nuclide('Fe58', 1.67030E-04, 'ao')
ss_304l.add_nuclide('Mn55', 1.76040E-03, 'ao')
ss_304l.add_nuclide('Ni58', 5.60890E-03, 'ao')
ss_304l.add_nuclide('Ni60', 2.16050E-03, 'ao')
ss_304l.add_nuclide('Ni61', 9.39170E-05, 'ao')
ss_304l.add_nuclide('Ni62', 2.99450E-04, 'ao')
ss_304l.add_nuclide('Ni64', 7.62610E-05, 'ao')
ss_304l.add_nuclide('Si28', 9.52810E-04, 'ao')
ss_304l.add_nuclide('Si29', 4.83810E-05, 'ao')
ss_304l.add_nuclide('Si30', 3.18930E-05, 'ao')
ss_304l.set_density('atom/b-cm', 8.793223E-02)

ss_304l.temperature = tem_structre
inconel.temperature = tem_structre
zr_4.temperature = tem_structre
# Fuel
# AIC (80-15-5)
aic = openmc.Material(name="AIC (80-15-5)")
aic.add_nuclide('Ag107', 2.35230E-02, 'ao')
aic.add_nuclide('Ag109', 2.18540E-02, 'ao')
aic.add_nuclide('Cd106', 3.38820E-05, 'ao')
aic.add_nuclide('Cd108', 2.41660E-05, 'ao')
aic.add_nuclide('Cd110', 3.39360E-04, 'ao')
aic.add_nuclide('Cd111', 3.48210E-04, 'ao')
aic.add_nuclide('Cd112', 6.56110E-04, 'ao')
aic.add_nuclide('Cd113', 3.32750E-04, 'ao')
aic.add_nuclide('Cd114', 7.82520E-04, 'ao')
aic.add_nuclide('Cd116', 2.04430E-04, 'ao')
aic.add_nuclide('In113', 3.42190E-04, 'ao')
aic.add_nuclide('In115', 7.65110E-03, 'ao')
aic.set_density('atom/b-cm', 5.609172E-02)

# B4C
b4c = openmc.Material(name="B4C")
b4c.add_nuclide('B10', 1.52060E-02, 'ao')
b4c.add_nuclide('B11', 6.15140E-02, 'ao')
# b4c.add_nuclide('C12', 1.89720E-02, 'ao')
# b4c.add_nuclide('C13', 2.12520E-04, 'ao')
b4c.add_nuclide('C0', 1.89720E-02+2.12520E-04, 'ao')
b4c.set_density('atom/b-cm', 9.590452E-02)

# Coolant
# H2O + 1000 ppm boron
h2o_boron = openmc.Material(name="H2O + 1000 ppm boron")
h2o_boron.add_nuclide('B10', 8.33778E-06, 'ao')
h2o_boron.add_nuclide('B11', 3.35608E-05, 'ao')
h2o_boron.add_nuclide('O16', 2.51573E-02, 'ao')
h2o_boron.add_nuclide('H1', 5.02932E-02, 'ao')
h2o_boron.set_density('atom/b-cm', 7.549240E-02)
h2o_boron.temperature = tem_coolant

# helium (structure or fuel?)
helium = openmc.Material(name = "Helium")
helium.add_nuclide('He3', 4.80890E-10, 'ao')
helium.add_nuclide('He4',2.40440E-04, 'ao')
helium.set_density('atom/b-cm', 2.404405E-04)


# uo2_A1
uo2_A1 = openmc.Material(name="uo2_A1")
uo2_A1.add_nuclide('U235', 3.56456E-04, 'ao')
uo2_A1.add_nuclide('U238', 2.31116E-02, 'ao')
uo2_A1.add_nuclide('O16', 4.69361E-02, 'ao')
uo2_A1.set_density('atom/b-cm', 7.040416E-02)

# uo2_A2
uo2_A2 = openmc.Material(name="uo2_A2")
uo2_A2.add_nuclide('U235', 3.80219E-04, 'ao')
uo2_A2.add_nuclide('U238', 2.30881E-02, 'ao')
uo2_A2.add_nuclide('O16', 4.69367E-02, 'ao')
uo2_A2.set_density('atom/b-cm', 7.040502E-02)

# uo2_B1
uo2_B1 = openmc.Material(name="uo2_B1")
uo2_B1.add_nuclide('U235', 5.94084E-04, 'ao')
uo2_B1.add_nuclide('U238', 2.28766E-02, 'ao')
uo2_B1.add_nuclide('O16', 4.69414E-02, 'ao')
uo2_B1.set_density('atom/b-cm', 7.041208E-02)

# uo2_B2_C3
uo2_B2_C3 = openmc.Material(name="uo2_B2_C3")
uo2_B2_C3.add_nuclide('U235', 6.17846E-04, 'ao')
uo2_B2_C3.add_nuclide('U238', 2.28531E-02, 'ao')
uo2_B2_C3.add_nuclide('O16', 4.69419E-02, 'ao')
uo2_B2_C3.set_density('atom/b-cm', 7.041285E-02)

# uo2_C1
uo2_C1 = openmc.Material(name="uo2_C1")
uo2_C1.add_nuclide('U235', 9.62391E-04, 'ao')
uo2_C1.add_nuclide('U238', 2.25123E-02, 'ao')
uo2_C1.add_nuclide('O16', 4.69495E-02, 'ao')
uo2_C1.set_density('atom/b-cm', 7.042419E-02)

# uo2_C2
uo2_C2 = openmc.Material(name="uo2_C2")
uo2_C2.add_nuclide('U235', 9.61347E-04, 'ao')
uo2_C2.add_nuclide('U238', 1.99124E-02, 'ao')
uo2_C2.add_nuclide('O16', 4.58016E-02, 'ao')
uo2_C2.set_density('atom/b-cm', 6.937805E-02)

# uo2_C2_with_Gd2O3
uo2_C2_with_Gd2O3 = openmc.Material(name="uo2_C2_with_Gd2O3")
uo2_C2_with_Gd2O3.add_nuclide('U235', 1.08120E-03, 'ao')
uo2_C2_with_Gd2O3.add_nuclide('U238', 2.23948E-02, 'ao')
uo2_C2_with_Gd2O3.add_nuclide('O16', 4.69521E-02, 'ao')
uo2_C2_with_Gd2O3.add_nuclide('Gd152', 5.40541E-06, 'ao')
uo2_C2_with_Gd2O3.add_nuclide('Gd154', 5.89189E-05, 'ao')
uo2_C2_with_Gd2O3.add_nuclide('Gd155', 4.00000E-04, 'ao')
uo2_C2_with_Gd2O3.add_nuclide('Gd156', 5.53243E-04, 'ao')
uo2_C2_with_Gd2O3.add_nuclide('Gd157', 4.22973E-04, 'ao')
uo2_C2_with_Gd2O3.add_nuclide('Gd158', 6.71352E-04, 'ao')
uo2_C2_with_Gd2O3.add_nuclide('Gd160', 5.90811E-04, 'ao')
uo2_C2_with_Gd2O3.set_density('atom/b-cm', 7.042810E-02)

uo2_A2.temperature = tem_fuel
uo2_A1.temperature = tem_fuel
uo2_B1.temperature = tem_fuel
uo2_B2_C3.temperature = tem_fuel
uo2_C1.temperature = tem_fuel
uo2_C2.temperature = tem_fuel
uo2_C2_with_Gd2O3.temperature = tem_fuel

# 材料混合物
mat_hv = openmc.Material.mix_materials([ss_304l, h2o_boron], [0.956, 0.044], 'vo')
mat_bn = openmc.Material.mix_materials([ss_304l, h2o_boron], [0.172, 0.828], 'vo')
mat_tn = openmc.Material.mix_materials([ss_304l, h2o_boron], [0.177, 0.823], 'vo')

materials = openmc.Materials([uo2_A1, uo2_A2, uo2_B1, uo2_B2_C3, uo2_C1, uo2_C2, uo2_C2_with_Gd2O3]+[helium, h2o_boron, b4c, aic, ss_304l, inconel, zr_4]+[mat_hv,mat_bn,mat_tn])

# 几何CSG-base
tran_z = 243.561/2
fuel_r1 = openmc.ZCylinder(r=0.4058)
fuel_r2 = openmc.ZCylinder(r=0.4140)
fuel_r3 = openmc.ZCylinder(r=0.4750)
pitch = 1.2598
grid_pitch = 1.2242

leftX = openmc.XPlane(-pitch/2)
rightX = openmc.XPlane(pitch/2)
leftY = openmc.YPlane(-pitch/2)
rightY = openmc.YPlane(pitch/2)
grid_leftX = openmc.XPlane(-grid_pitch/2)
grid_rightX = openmc.XPlane(grid_pitch/2)
grid_leftY = openmc.YPlane(-grid_pitch/2)
grid_rightY = openmc.YPlane(grid_pitch/2)
bottomZ = openmc.ZPlane(z0=0-tran_z,boundary_type='vacuum')
topZ = openmc.ZPlane(z0=243.561-tran_z,boundary_type='vacuum')

rect = +leftX & -rightX & +leftY & -rightY
inner_rect = +grid_leftX & -grid_rightX & +grid_leftY & -grid_rightY


div12 = openmc.ZPlane(243.561 - 9.020 -tran_z)
div23 = openmc.ZPlane(243.561 - 9.020 - 8.481-tran_z)
div34 = openmc.ZPlane(243.561 - 9.020 - 8.481 - 1.205-tran_z)
div45 = openmc.ZPlane(243.561 - 9.020 - 8.481 - 1.205 - 13.490-tran_z)
div56 = openmc.ZPlane(10.160 + 1.205 - tran_z)
div67 = openmc.ZPlane(10.160 - tran_z)

GT_r1 = openmc.ZCylinder(r=0.5715)
GT_r2 = openmc.ZCylinder(r=0.6121)
GT_cr11 = openmc.ZCylinder(r=0.4267)
GT_cr12 = openmc.ZCylinder(r=0.4369)
GT_cr2 = openmc.ZCylinder(r=0.4369)
GT_cr3 = openmc.ZCylinder(r=0.4839)

# grid region
SG_region = rect & (~inner_rect)
SG5_region = SG_region & -openmc.ZPlane(223.581-tran_z) & +openmc.ZPlane(219.136-tran_z)
SG4_region = SG_region & -openmc.ZPlane(172.527-tran_z) & +openmc.ZPlane(168.082-tran_z)
SG3_region = SG_region & -openmc.ZPlane(121.473-tran_z) & +openmc.ZPlane(117.028-tran_z)
SG2_region = SG_region & -openmc.ZPlane(70.419-tran_z) & +openmc.ZPlane(65.974-tran_z)
SG1_region = SG_region & -openmc.ZPlane(19.365-tran_z) & +openmc.ZPlane(14.920-tran_z)
SG1234_region = SG1_region | SG2_region | SG3_region | SG4_region 
SG12345_region = SG1_region | SG2_region | SG3_region | SG4_region | SG5_region 
SG2345_region = SG2_region | SG3_region | SG4_region | SG5_region

# 1.1 燃料棒A1

HTPs_A1 = openmc.Cell(fill=zr_4, region=SG2345_region)
HMPs_A1 = openmc.Cell(fill=inconel,region=SG1_region)
# coolant
top_coolant_A1 = openmc.Cell(fill=h2o_boron, region=-div12 & +div23 & rect)
# nozzle
top_nozzle_A1 = openmc.Cell(fill=mat_tn,region= rect &-topZ & +div12)
bot_nozzle_A1 = openmc.Cell(fill=mat_bn,region= rect & +bottomZ & -div67)

# top endcap
top_endcap_A1 = openmc.Cell(fill=zr_4, region=-div23 & +div34 & -fuel_r3)
top_endcap_coolant_A1 = openmc.Cell(fill=h2o_boron, region=-div23 & +div34 & rect & +fuel_r3)

# Plenum spring 
spring_A1 = openmc.Cell(fill=inconel, region=-div34 & +div45 & -openmc.ZCylinder(r=0.0646))
spring_gap_A1 = openmc.Cell(fill=helium, region=-div34 & +div45 & +openmc.ZCylinder(r=0.0646) & -fuel_r2)
spring_clad_A1 = openmc.Cell(fill=zr_4, region=-div34 & +div45 & -fuel_r3 & +fuel_r2)
spring_coolant_A1 = openmc.Cell(fill=h2o_boron, region=-div34 & +div45 & +fuel_r3 & rect & ~SG5_region)

# UOX
fuel_A1 = openmc.Cell(fill=uo2_A1, region=-div45 & +div56 & -fuel_r1)
UOX_airgap_A1 = openmc.Cell(fill=helium, region=-div45 & +div56 & +fuel_r1 & -fuel_r2)
UOX_clad_A1 = openmc.Cell(fill=zr_4, region=-div45 & +div56 & +fuel_r2 & -fuel_r3)
UOX_coolant_A1 = openmc.Cell(fill=h2o_boron, region=-div45 & +div56 & +fuel_r3 & rect & ~SG1234_region)

# endcap
bot_endcap_A1 = openmc.Cell(fill=zr_4, region=-div56 & +div67 & -fuel_r3)
bot_endcap_coolant_A1 = openmc.Cell(fill=h2o_boron, region=-div56 & +div67 & rect & +fuel_r3)

u_A1 = openmc.Universe(cells=(top_coolant_A1,top_endcap_A1,top_endcap_coolant_A1,
                              spring_A1,spring_clad_A1,spring_coolant_A1,spring_gap_A1,
                              UOX_airgap_A1,UOX_clad_A1,UOX_coolant_A1,fuel_A1,
                              bot_endcap_A1,bot_endcap_coolant_A1,
                              HMPs_A1,HTPs_A1,top_nozzle_A1,bot_nozzle_A1))


# 1.2 燃料棒A2
top_nozzle_A2 = openmc.Cell(fill=mat_tn,region= rect &-topZ & +div12)
bot_nozzle_A2 = openmc.Cell(fill=mat_bn,region= rect & +bottomZ & -div67)
HTPs_A2 = openmc.Cell(fill=zr_4, region=SG2345_region)
HMPs_A2 = openmc.Cell(fill=inconel,region=SG1_region)
top_coolant_A2 = openmc.Cell(fill=h2o_boron, region=-div12 & +div23 & rect)
top_endcap_A2 = openmc.Cell(fill=zr_4, region=-div23 & +div34 & -fuel_r3)
top_endcap_coolant_A2 = openmc.Cell(fill=h2o_boron, region=-div23 & +div34 & rect & +fuel_r3)
spring_A2 = openmc.Cell(fill=inconel, region=-div34 & +div45 & -openmc.ZCylinder(r=0.0646))
spring_gap_A2 = openmc.Cell(fill=helium, region=-div34 & +div45 & +openmc.ZCylinder(r=0.0646) & -fuel_r2)
spring_clad_A2 = openmc.Cell(fill=zr_4, region=-div34 & +div45 & -fuel_r3 & +fuel_r2)
spring_coolant_A2 = openmc.Cell(fill=h2o_boron, region=-div34 & +div45 & +fuel_r3 & rect & ~SG5_region)
fuel_A2 = openmc.Cell(fill=uo2_A2, region=-div45 & +div56 & -fuel_r1)
UOX_airgap_A2 = openmc.Cell(fill=helium, region=-div45 & +div56 & +fuel_r1 & -fuel_r2)
UOX_clad_A2 = openmc.Cell(fill=zr_4, region=-div45 & +div56 & +fuel_r2 & -fuel_r3)
UOX_coolant_A2 = openmc.Cell(fill=h2o_boron, region=-div45 & +div56 & +fuel_r3 & rect & ~SG1234_region)
bot_endcap_A2 = openmc.Cell(fill=zr_4, region=-div56 & +div67 & -fuel_r3)
bot_endcap_coolant_A2 = openmc.Cell(fill=h2o_boron, region=-div56 & +div67 & rect & +fuel_r3)

u_A2 = openmc.Universe(cells=(top_coolant_A2,top_endcap_A2,top_endcap_coolant_A2,
                              spring_A2,spring_clad_A2,spring_coolant_A2,spring_gap_A2,
                              UOX_airgap_A2,UOX_clad_A2,UOX_coolant_A2,fuel_A2,
                              bot_endcap_A2,bot_endcap_coolant_A2,HMPs_A2,HTPs_A2,
                              top_nozzle_A2,bot_nozzle_A2))

# 1.3 燃料棒B1
top_nozzle_B1 = openmc.Cell(fill=mat_tn,region= rect &-topZ & +div12)
bot_nozzle_B1 = openmc.Cell(fill=mat_bn,region= rect & +bottomZ & -div67)
HTPs_B1 = openmc.Cell(fill=zr_4, region=SG2345_region)
HMPs_B1 = openmc.Cell(fill=inconel,region=SG1_region)
top_coolant_B1 = openmc.Cell(fill=h2o_boron, region=-div12 & +div23 & rect)
top_endcap_B1 = openmc.Cell(fill=zr_4, region=-div23 & +div34 & -fuel_r3)
top_endcap_coolant_B1 = openmc.Cell(fill=h2o_boron, region=-div23 & +div34 & rect & +fuel_r3)
spring_B1 = openmc.Cell(fill=inconel, region=-div34 & +div45 & -openmc.ZCylinder(r=0.0646))
spring_gap_B1 = openmc.Cell(fill=helium, region=-div34 & +div45 & +openmc.ZCylinder(r=0.0646) & -fuel_r2)
spring_clad_B1 = openmc.Cell(fill=zr_4, region=-div34 & +div45 & -fuel_r3 & +fuel_r2)
spring_coolant_B1 = openmc.Cell(fill=h2o_boron, region=-div34 & +div45 & +fuel_r3 & rect & ~SG5_region)
fuel_B1 = openmc.Cell(fill=uo2_B1, region=-div45 & +div56 & -fuel_r1)
UOX_airgap_B1 = openmc.Cell(fill=helium, region=-div45 & +div56 & +fuel_r1 & -fuel_r2)
UOX_clad_B1 = openmc.Cell(fill=zr_4, region=-div45 & +div56 & +fuel_r2 & -fuel_r3)
UOX_coolant_B1 = openmc.Cell(fill=h2o_boron, region=-div45 & +div56 & +fuel_r3 & rect & ~SG1234_region)
bot_endcap_B1 = openmc.Cell(fill=zr_4, region=-div56 & +div67 & -fuel_r3)
bot_endcap_coolant_B1 = openmc.Cell(fill=h2o_boron, region=-div56 & +div67 & rect & +fuel_r3)

u_B1 = openmc.Universe(cells=(top_coolant_B1,top_endcap_B1,top_endcap_coolant_B1,
                              spring_B1,spring_clad_B1,spring_coolant_B1, spring_gap_B1,
                              UOX_airgap_B1,UOX_clad_B1,UOX_coolant_B1,fuel_B1,
                              bot_endcap_B1,bot_endcap_coolant_B1,HMPs_B1,HTPs_B1,
                              top_nozzle_B1,bot_nozzle_B1))
# 1.4 燃料棒B2
top_nozzle_B2 = openmc.Cell(fill=mat_tn,region= rect &-topZ & +div12)
bot_nozzle_B2 = openmc.Cell(fill=mat_bn,region= rect & +bottomZ & -div67)
HTPs_B2 = openmc.Cell(fill=zr_4, region=SG2345_region)
HMPs_B2 = openmc.Cell(fill=inconel,region=SG1_region)
top_coolant_B2 = openmc.Cell(fill=h2o_boron, region=-div12 & +div23 & rect)
top_endcap_B2 = openmc.Cell(fill=zr_4, region=-div23 & +div34 & -fuel_r3)
top_endcap_coolant_B2 = openmc.Cell(fill=h2o_boron, region=-div23 & +div34 & rect & +fuel_r3)
spring_B2 = openmc.Cell(fill=inconel, region=-div34 & +div45 & -openmc.ZCylinder(r=0.0646))
spring_gap_B2 = openmc.Cell(fill=helium, region=-div34 & +div45 & +openmc.ZCylinder(r=0.0646) & -fuel_r2)
spring_clad_B2 = openmc.Cell(fill=zr_4, region=-div34 & +div45 & -fuel_r3 & +fuel_r2)
spring_coolant_B2 = openmc.Cell(fill=h2o_boron, region=-div34 & +div45 & +fuel_r3 & rect & ~SG5_region)
fuel_B2 = openmc.Cell(fill=uo2_B2_C3, region=-div45 & +div56 & -fuel_r1)
UOX_airgap_B2 = openmc.Cell(fill=helium, region=-div45 & +div56 & +fuel_r1 & -fuel_r2)
UOX_clad_B2 = openmc.Cell(fill=zr_4, region=-div45 & +div56 & +fuel_r2 & -fuel_r3)
UOX_coolant_B2 = openmc.Cell(fill=h2o_boron, region=-div45 & +div56 & +fuel_r3 & rect & ~SG1234_region)
bot_endcap_B2 = openmc.Cell(fill=zr_4, region=-div56 & +div67 & -fuel_r3)
bot_endcap_coolant_B2 = openmc.Cell(fill=h2o_boron, region=-div56 & +div67 & rect & +fuel_r3)

u_B2 = openmc.Universe(cells=(top_coolant_B2,top_endcap_B2,top_endcap_coolant_B2,
                              spring_B2,spring_clad_B2,spring_coolant_B2,spring_gap_B2,
                              UOX_airgap_B2,UOX_clad_B2,UOX_coolant_B2,fuel_B2,
                              bot_endcap_B2,bot_endcap_coolant_B2,HMPs_B2,HTPs_B2,top_nozzle_B2,bot_nozzle_B2))

# 1.5 燃料棒C1
top_nozzle_C1 = openmc.Cell(fill=mat_tn,region= rect &-topZ & +div12)
bot_nozzle_C1 = openmc.Cell(fill=mat_bn,region= rect & +bottomZ & -div67)
HTPs_C1 = openmc.Cell(fill=zr_4, region=SG2345_region)
HMPs_C1 = openmc.Cell(fill=inconel,region=SG1_region)
top_coolant_C1 = openmc.Cell(fill=h2o_boron, region=-div12 & +div23 & rect)
top_endcap_C1 = openmc.Cell(fill=zr_4, region=-div23 & +div34 & -fuel_r3)
top_endcap_coolant_C1 = openmc.Cell(fill=h2o_boron, region=-div23 & +div34 & rect & +fuel_r3)
spring_C1 = openmc.Cell(fill=inconel, region=-div34 & +div45 & -openmc.ZCylinder(r=0.0646))
spring_gap_C1 = openmc.Cell(fill=helium, region=-div34 & +div45 & +openmc.ZCylinder(r=0.0646) & -fuel_r2)
spring_clad_C1 = openmc.Cell(fill=zr_4, region=-div34 & +div45 & -fuel_r3 & +fuel_r2)
spring_coolant_C1 = openmc.Cell(fill=h2o_boron, region=-div34 & +div45 & +fuel_r3 & rect & ~SG5_region)
fuel_C1 = openmc.Cell(fill=uo2_C1, region=-div45 & +div56 & -fuel_r1)
UOX_airgap_C1 = openmc.Cell(fill=helium, region=-div45 & +div56 & +fuel_r1 & -fuel_r2)
UOX_clad_C1 = openmc.Cell(fill=zr_4, region=-div45 & +div56 & +fuel_r2 & -fuel_r3)
UOX_coolant_C1 = openmc.Cell(fill=h2o_boron, region=-div45 & +div56 & +fuel_r3 & rect & ~SG1234_region)
bot_endcap_C1 = openmc.Cell(fill=zr_4, region=-div56 & +div67 & -fuel_r3)
bot_endcap_coolant_C1 = openmc.Cell(fill=h2o_boron, region=-div56 & +div67 & rect & +fuel_r3)

u_C1 = openmc.Universe(cells=(top_coolant_C1,top_endcap_C1,top_endcap_coolant_C1,
                              spring_C1,spring_clad_C1,spring_coolant_C1,spring_gap_C1,
                              UOX_airgap_C1,UOX_clad_C1,UOX_coolant_C1,fuel_C1,
                              bot_endcap_C1,bot_endcap_coolant_C1,HMPs_C1,HTPs_C1,top_nozzle_C1,bot_nozzle_C1))
# 1.6 燃料棒C2
top_nozzle_C2 = openmc.Cell(fill=mat_tn,region= rect &-topZ & +div12)
bot_nozzle_C2 = openmc.Cell(fill=mat_bn,region= rect & +bottomZ & -div67)
HTPs_C2 = openmc.Cell(fill=zr_4, region=SG2345_region)
HMPs_C2 = openmc.Cell(fill=inconel,region=SG1_region)
top_coolant_C2 = openmc.Cell(fill=h2o_boron, region=-div12 & +div23 & rect)
top_endcap_C2 = openmc.Cell(fill=zr_4, region=-div23 & +div34 & -fuel_r3)
top_endcap_coolant_C2 = openmc.Cell(fill=h2o_boron, region=-div23 & +div34 & rect & +fuel_r3)
spring_C2 = openmc.Cell(fill=inconel, region=-div34 & +div45 & -openmc.ZCylinder(r=0.0646))
spring_gap_C2 = openmc.Cell(fill=helium, region=-div34 & +div45 & +openmc.ZCylinder(r=0.0646) & -fuel_r2)
spring_clad_C2 = openmc.Cell(fill=zr_4, region=-div34 & +div45 & -fuel_r3 & +fuel_r2)
spring_coolant_C2 = openmc.Cell(fill=h2o_boron, region=-div34 & +div45 & +fuel_r3 & rect & ~SG5_region)
fuel_C2 = openmc.Cell(fill=uo2_C2, region=-div45 & +div56 & -fuel_r1)
UOX_airgap_C2 = openmc.Cell(fill=helium, region=-div45 & +div56 & +fuel_r1 & -fuel_r2)
UOX_clad_C2 = openmc.Cell(fill=zr_4, region=-div45 & +div56 & +fuel_r2 & -fuel_r3)
UOX_coolant_C2 = openmc.Cell(fill=h2o_boron, region=-div45 & +div56 & +fuel_r3 & rect & ~SG1234_region)
bot_endcap_C2 = openmc.Cell(fill=zr_4, region=-div56 & +div67 & -fuel_r3)
bot_endcap_coolant_C2 = openmc.Cell(fill=h2o_boron, region=-div56 & +div67 & rect & +fuel_r3)

u_C2 = openmc.Universe(cells=(top_coolant_C2,top_endcap_C2,top_endcap_coolant_C2,
                              spring_C2,spring_clad_C2,spring_coolant_C2,spring_gap_C2,
                              UOX_airgap_C2,UOX_clad_C2,UOX_coolant_C2,fuel_C2,
                              bot_endcap_C2,bot_endcap_coolant_C2,HMPs_C2,HTPs_C2,
                              top_nozzle_C2,bot_nozzle_C2))

# 1.7 燃料棒C3
top_nozzle_C3 = openmc.Cell(fill=mat_tn,region= rect &-topZ & +div12)
bot_nozzle_C3 = openmc.Cell(fill=mat_bn,region= rect & +bottomZ & -div67)
HTPs_C3 = openmc.Cell(fill=zr_4, region=SG2345_region)
HMPs_C3 = openmc.Cell(fill=inconel,region=SG1_region)
top_coolant_C3 = openmc.Cell(fill=h2o_boron, region=-div12 & +div23 & rect)
top_endcap_C3 = openmc.Cell(fill=zr_4, region=-div23 & +div34 & -fuel_r3)
top_endcap_coolant_C3 = openmc.Cell(fill=h2o_boron, region=-div23 & +div34 & rect & +fuel_r3)
spring_C3 = openmc.Cell(fill=inconel, region=-div34 & +div45 & -openmc.ZCylinder(r=0.0646))
spring_gap_C3 = openmc.Cell(fill=helium, region=-div34 & +div45 & +openmc.ZCylinder(r=0.0646) & -fuel_r2)
spring_clad_C3 = openmc.Cell(fill=zr_4, region=-div34 & +div45 & -fuel_r3 & +fuel_r2)
spring_coolant_C3 = openmc.Cell(fill=h2o_boron, region=-div34 & +div45 & +fuel_r3 & rect & ~SG5_region)
fuel_C3 = openmc.Cell(fill=uo2_B2_C3, region=-div45 & +div56 & -fuel_r1)
UOX_airgap_C3 = openmc.Cell(fill=helium, region=-div45 & +div56 & +fuel_r1 & -fuel_r2)
UOX_clad_C3 = openmc.Cell(fill=zr_4, region=-div45 & +div56 & +fuel_r2 & -fuel_r3)
UOX_coolant_C3 = openmc.Cell(fill=h2o_boron, region=-div45 & +div56 & +fuel_r3 & rect & ~SG1234_region)
bot_endcap_C3 = openmc.Cell(fill=zr_4, region=-div56 & +div67 & -fuel_r3)
bot_endcap_coolant_C3 = openmc.Cell(fill=h2o_boron, region=-div56 & +div67 & rect & +fuel_r3)

u_C3 = openmc.Universe(cells=(top_coolant_C3,top_endcap_C3,top_endcap_coolant_C3,
                              spring_C3,spring_clad_C3,spring_coolant_C3,spring_gap_C3,
                              UOX_airgap_C3,UOX_clad_C3,UOX_coolant_C3,fuel_C3,
                              bot_endcap_C3,bot_endcap_coolant_C3,HMPs_C3,HTPs_C3,top_nozzle_C3,bot_nozzle_C3))

# 1.8 毒物棒gC2
top_nozzle_gC2 = openmc.Cell(fill=mat_tn,region= rect &-topZ & +div12)
bot_nozzle_gC2 = openmc.Cell(fill=mat_bn,region= rect & +bottomZ & -div67)
HTPs_gC2 = openmc.Cell(fill=zr_4, region=SG2345_region)
HMPs_gC2 = openmc.Cell(fill=inconel,region=SG1_region)
top_coolant_gC2 = openmc.Cell(fill=h2o_boron, region=-div12 & +div23 & rect)
top_endcap_gC2 = openmc.Cell(fill=zr_4, region=-div23 & +div34 & -fuel_r3)
top_endcap_coolant_gC2 = openmc.Cell(fill=h2o_boron, region=-div23 & +div34 & rect & +fuel_r3)
spring_gC2 = openmc.Cell(fill=inconel, region=-div34 & +div45 & -openmc.ZCylinder(r=0.0646))
spring_gap_gC2 = openmc.Cell(fill=helium, region=-div34 & +div45 & +openmc.ZCylinder(r=0.0646) & -fuel_r2)
spring_clad_gC2 = openmc.Cell(fill=zr_4, region=-div34 & +div45 & -fuel_r3 & +fuel_r2)
spring_coolant_gC2 = openmc.Cell(fill=h2o_boron, region=-div34 & +div45 & +fuel_r3 & rect & ~SG5_region)
fuel_gC2 = openmc.Cell(fill=uo2_C2_with_Gd2O3, region=-div45 & +div56 & -fuel_r1)
UOX_airgap_gC2 = openmc.Cell(fill=helium, region=-div45 & +div56 & +fuel_r1 & -fuel_r2)
UOX_clad_gC2 = openmc.Cell(fill=zr_4, region=-div45 & +div56 & +fuel_r2 & -fuel_r3)
UOX_coolant_gC2 = openmc.Cell(fill=h2o_boron, region=-div45 & +div56 & +fuel_r3 & rect & ~SG1234_region)
bot_endcap_gC2 = openmc.Cell(fill=zr_4, region=-div56 & +div67 & -fuel_r3)
bot_endcap_coolant_gC2 = openmc.Cell(fill=h2o_boron, region=-div56 & +div67 & rect & +fuel_r3)

g_C2 = openmc.Universe(cells=(top_coolant_gC2,top_endcap_gC2,top_endcap_coolant_gC2,
                              spring_gC2,spring_clad_gC2,spring_coolant_gC2,spring_gap_gC2,
                              UOX_airgap_gC2,UOX_clad_gC2,UOX_coolant_gC2,fuel_gC2,
                              bot_endcap_gC2,bot_endcap_coolant_gC2,HMPs_gC2,HTPs_gC2,
                              top_nozzle_gC2,bot_nozzle_gC2))

# 2.1 空导向管 empty guide tube
top_nozzle_GT = openmc.Cell(fill=mat_tn,region= rect &-topZ & +div12)
bot_nozzle_GT = openmc.Cell(fill=mat_bn,region= rect & +bottomZ & -div67)
HTPs_GT = openmc.Cell(fill=zr_4, region=SG2345_region)
HMPs_GT = openmc.Cell(fill=inconel,region=SG1_region)
GT_inner_coolant = openmc.Cell(fill=h2o_boron, region=+div67 & -div12 & -GT_r1)
GT_clad = openmc.Cell(fill=zr_4, region=+div67 & -div12 & +GT_r1 & -GT_r2)
GT_coolant = openmc.Cell(fill=h2o_boron,region=+div67 & -div12 & +GT_r2 & rect & ~SG12345_region)
gt = openmc.Universe(cells=(top_nozzle_GT,bot_nozzle_GT,GT_inner_coolant,GT_clad,GT_coolant,HMPs_GT,HTPs_GT))

# 3.1 0% 控制棒完全抽出的导向管---------------------------------------
top_nozzle_GTcr0 = openmc.Cell(fill=mat_tn,region= rect &-topZ & +div12)
bot_nozzle_GTcr0 = openmc.Cell(fill=mat_bn,region= rect & +bottomZ & -div67)
# GT region 没加中间的控制棒
HTPs_GTcr0 = openmc.Cell(fill=zr_4, region=SG2345_region)
HMPs_GTcr0 = openmc.Cell(fill=inconel,region=SG1_region)
GT_outer_coolant = openmc.Cell(fill=h2o_boron, region=rect & +GT_r2 & -div12 & +div67 & ~SG12345_region)
GT_clad = openmc.Cell(fill=zr_4, region=+div67 & -div12 & +GT_r1 & -GT_r2)
GT_coolant_gap = openmc.Cell(fill=h2o_boron, region=+GT_cr3 & -GT_r1 & -div12 & +div67)
# CR region 控制棒区域
# Upper CR B4C
Upper_CR_b4c_clad = openmc.Cell(fill=ss_304l, region=+GT_cr2 & -GT_cr3 & -div12 & +openmc.ZPlane(211.365 + 3.758 - tran_z))
Upper_CR_b4c_airgap = openmc.Cell(fill=helium, region=+GT_cr12 & -GT_cr2 & -div12 & +openmc.ZPlane(211.365 + 3.758 - tran_z))
Upper_CR_b4c_fuel = openmc.Cell(fill=b4c, region=-GT_cr12 & -div12 & +openmc.ZPlane(211.365 + 3.758 - tran_z))

# Upper CR AIC
Upper_CR_aic_clad = openmc.Cell(fill=ss_304l, region=+GT_cr2 & -GT_cr3 & +div45 & -openmc.ZPlane(211.365 + 3.758 - tran_z))
Upper_CR_aic_airgap = openmc.Cell(fill=helium, region=+GT_cr11 & -GT_cr2 & +div45 & -openmc.ZPlane(211.365 + 3.758 - tran_z))
Upper_CR_aic_fuel = openmc.Cell(fill=aic, region=-GT_cr11 & +div45 & -openmc.ZPlane(211.365 + 3.758 - tran_z))

# CR End Plug
Withdrawn_CR_endplug_clad = openmc.Cell(fill=ss_304l, region=-GT_cr3 & -openmc.ZPlane(211.365 - tran_z) & +openmc.ZPlane(211.365 - 4.859 - tran_z))

# CR Empty Guide Tube
Withdrawn_CR_empty = openmc.Cell(fill=h2o_boron, region=-GT_cr3 & -openmc.ZPlane(211.365 - 4.859 - tran_z) & +div67)

CR_tuple = (Upper_CR_b4c_fuel, Upper_CR_b4c_airgap, Upper_CR_b4c_clad,
            Upper_CR_aic_airgap, Upper_CR_aic_clad, Upper_CR_aic_fuel,
            Withdrawn_CR_endplug_clad, Withdrawn_CR_empty, 
            GT_outer_coolant, GT_clad, GT_coolant_gap,HMPs_GTcr0,HTPs_GTcr0,
            top_nozzle_GTcr0,bot_nozzle_GTcr0)
gtcr0 = openmc.Universe(cells=CR_tuple)

# 3.2 100% 控制棒完全插入的导向管---------------------------------------
top_nozzle_GTcr1 = openmc.Cell(fill=mat_tn,region= rect &-topZ & +div12)
bot_nozzle_GTcr1 = openmc.Cell(fill=mat_bn,region= rect & +bottomZ & -div67)
# GT cells 加了个1避免变量一样自动消除了
HTPs_GTcr1 = openmc.Cell(fill=zr_4, region=SG2345_region)
HMPs_GTcr1 = openmc.Cell(fill=inconel,region=SG1_region)
GT1_outer_coolant = openmc.Cell(fill=h2o_boron, region=rect & +GT_r2 & -div12 & +div67 & ~SG12345_region)
GT1_clad = openmc.Cell(fill=zr_4, region= +div67 & -div12 & +GT_r1 & -GT_r2)
GT1_coolant_gap = openmc.Cell(fill=h2o_boron, region=+GT_cr3 & -GT_r1 & -div12 & +div67)

# Upper plenum
CR_plenum_air = openmc.Cell(fill=helium, region=-GT_cr2 & -div12 & +div45)
CR_plenum_clad = openmc.Cell(fill=ss_304l, region=+GT_cr2 & -GT_cr3 & -div12 & +div45)

# CR B4C
CR_b4c_clad = openmc.Cell(fill=ss_304l, region=+GT_cr2 & -GT_cr3 & -div45 & +openmc.ZPlane(211.365 - 157.480 - tran_z))
CR_b4c_airgap = openmc.Cell(fill=helium, region=+GT_cr12 & -GT_cr2 & -div45 & +openmc.ZPlane(211.365 - 157.480 - tran_z))
CR_b4c_fuel = openmc.Cell(fill=b4c, region=-GT_cr12 & -div45 & +openmc.ZPlane(211.365 - 157.480 - tran_z))

# CR AIC
aic_regionZ = -openmc.ZPlane(211.365 - 157.480 - tran_z) & +openmc.ZPlane(211.365 - 157.480 - 30.480 - tran_z)
CR_aic_clad = openmc.Cell(fill=ss_304l, region=+GT_cr2 & -GT_cr3 & aic_regionZ)
CR_aic_airgap = openmc.Cell(fill=helium, region=+GT_cr11 & -GT_cr2 & aic_regionZ)
CR_aic_fuel = openmc.Cell(fill=aic, region=-GT_cr11 & aic_regionZ)

# CR End Plug
endplug_regionZ = -openmc.ZPlane(10.160 + 8.386 + 4.859 - tran_z) & +openmc.ZPlane(10.160 + 8.386 - tran_z)
CR_endplug_clad = openmc.Cell(fill=ss_304l, region=-GT_cr3 & endplug_regionZ)

# CR Empty Guide Tube
CR_empty = openmc.Cell(fill=h2o_boron, region=-GT_cr3 & -openmc.ZPlane(10.160 + 8.386 - tran_z) & +openmc.ZPlane(10.160 - tran_z))

# Combine all cells into a tuple
CR1_tuple = (GT1_outer_coolant, GT1_clad, GT1_coolant_gap,
             CR_plenum_clad, CR_plenum_air, CR_b4c_airgap, CR_b4c_clad, CR_b4c_fuel,CR_aic_airgap, CR_aic_clad, CR_aic_fuel, CR_endplug_clad, CR_empty,HMPs_GTcr1,HTPs_GTcr1,
             bot_nozzle_GTcr1,top_nozzle_GTcr1)

gtcr1 = openmc.Universe(cells=CR1_tuple)

# 矩形晶格网络
tube_x = np.array([5, 8, 11, 3, 13, 2, 5, 8, 11, 14, 2, 5, 8, 11, 14,
                    2, 5, 8, 11, 14, 3, 13, 5, 8, 11])
tube_y = np.array([2, 2, 2, 3, 3, 5, 5, 5, 5, 5, 8, 8, 8, 8, 8,
                    11, 11, 11, 11, 11, 13, 13, 14, 14, 14])
# 毒物棒位置
pos_x = np.array([2, 14, 7, 9, 6, 10, 3, 13, 3, 13, 6, 10, 7, 9, 2, 14])
pos_y = np.array([2, 2, 3, 3, 6, 6, 7, 7, 9, 9, 10, 10, 13, 13, 14, 14])

as_prism = openmc.model.RectangularPrism(width=pitch*17,height=pitch*17,axis='z')
lat_region = -as_prism & -topZ & +bottomZ

# B2 B1 部分的A1 含有控制棒组件
lat_A1 = openmc.RectLattice()
lat_A1.lower_left = (-pitch*8.5, -pitch*8.5)
lat_A1.pitch = (pitch, pitch)
lat_A1.universes = np.tile(u_A1, (17, 17))
lat_A1.universes[tube_x, tube_y] = gt
a1 = openmc.Universe()
a1.add_cell(openmc.Cell(fill=lat_A1,region=lat_region))

lat_A1cr = openmc.RectLattice()
lat_A1cr.lower_left = (-pitch*8.5, -pitch*8.5)
lat_A1cr.pitch = (pitch, pitch)
lat_A1cr.universes = np.tile(u_A1, (17, 17))
lat_A1cr.universes[tube_x, tube_y] = gtcr0
lat_A1cr.universes[8, 8] = gt
a1cr = openmc.Universe()
a1cr.add_cell(openmc.Cell(fill=lat_A1cr,region=lat_region))

lat_RE1cr = openmc.RectLattice()
lat_RE1cr.lower_left = (-pitch*8.5, -pitch*8.5)
lat_RE1cr.pitch = (pitch, pitch)
lat_RE1cr.universes = np.tile(u_A1, (17, 17))
lat_RE1cr.universes[tube_x, tube_y] = gtcr1
lat_RE1cr.universes[8, 8] = gt
re1 = openmc.Universe()
re1.add_cell(openmc.Cell(fill=lat_RE1cr,region=lat_region))

lat_A2 = openmc.RectLattice()
lat_A2.lower_left = (-pitch*8.5, -pitch*8.5)
lat_A2.pitch = (pitch, pitch)
lat_A2.universes = np.tile(u_A2, (17, 17))
lat_A2.universes[tube_x, tube_y] = gt
a2 = openmc.Universe()
a2.add_cell(openmc.Cell(fill=lat_A2,region=lat_region))

lat_B1 = openmc.RectLattice()
lat_B1.lower_left = (-pitch*8.5, -pitch*8.5)
lat_B1.pitch = (pitch, pitch)
lat_B1.universes = np.tile(u_B1, (17, 17))
lat_B1.universes[tube_x, tube_y] = gtcr0
lat_B1.universes[8, 8] = gt
b1 = openmc.Universe()
b1.add_cell(openmc.Cell(fill=lat_B1,region=lat_region))

lat_SH3 = openmc.RectLattice()
lat_SH3.lower_left = (-pitch*8.5, -pitch*8.5)
lat_SH3.pitch = (pitch, pitch)
lat_SH3.universes = np.tile(u_B1, (17, 17))
lat_SH3.universes[tube_x, tube_y] = gtcr1
lat_SH3.universes[8, 8] = gt
sh3 = openmc.Universe()
sh3.add_cell(openmc.Cell(fill=lat_SH3,region=lat_region))

lat_SH4 = openmc.RectLattice()
lat_SH4.lower_left = (-pitch*8.5, -pitch*8.5)
lat_SH4.pitch = (pitch, pitch)
lat_SH4.universes = np.tile(u_B1, (17, 17))
lat_SH4.universes[tube_x, tube_y] = gtcr1
lat_SH4.universes[8, 8] = gt
sh4 = openmc.Universe()
sh4.add_cell(openmc.Cell(fill=lat_SH4,region=lat_region))

lat_B2 = openmc.RectLattice()
lat_B2.lower_left = (-pitch*8.5, -pitch*8.5)
lat_B2.pitch = (pitch, pitch)
lat_B2.universes = np.tile(u_B2, (17, 17))
lat_B2.universes[tube_x, tube_y] = gtcr0
lat_B2.universes[8, 8] = gt
b2 = openmc.Universe()
b2.add_cell(openmc.Cell(fill=lat_B2,region=lat_region))

lat_RE2 = openmc.RectLattice()
lat_RE2.lower_left = (-pitch*8.5, -pitch*8.5)
lat_RE2.pitch = (pitch, pitch)
lat_RE2.universes = np.tile(u_B2, (17, 17))
lat_RE2.universes[tube_x, tube_y] = gtcr1
lat_RE2.universes[8, 8] = gt
re2 = openmc.Universe()
re2.add_cell(openmc.Cell(fill=lat_RE2,region=lat_region))

lat_C1 = openmc.RectLattice()
lat_C1.lower_left = (-pitch*8.5, -pitch*8.5)
lat_C1.pitch = (pitch, pitch)
lat_C1.universes = np.tile(u_C1, (17, 17))
lat_C1.universes[tube_x, tube_y] = gt
c1 = openmc.Universe()
c1.add_cell(openmc.Cell(fill=lat_C1,region=lat_region))

lat_C2 = openmc.RectLattice()
lat_C2.lower_left = (-pitch*8.5, -pitch*8.5)
lat_C2.pitch = (pitch, pitch)
lat_C2.universes = np.tile(u_C2, (17, 17))
lat_C2.universes[tube_x, tube_y] = gt
lat_C2.universes[pos_x, pos_y] = g_C2
c2 = openmc.Universe()
c2.add_cell(openmc.Cell(fill=lat_C2,region=lat_region))

lat_C3 = openmc.RectLattice()
lat_C3.lower_left = (-pitch*8.5, -pitch*8.5)
lat_C3.pitch = (pitch, pitch)
lat_C3.universes = np.tile(u_C3, (17, 17))
lat_C3.universes[tube_x, tube_y] = gt
c3 = openmc.Universe()
c3.add_cell(openmc.Cell(fill=lat_C3,region=lat_region))
              
lat_W = openmc.Cell(fill=mat_hv)
lat_W.region = -as_prism & -topZ & +bottomZ
w = openmc.Universe()
w.add_cell(lat_W)

# 定义堆芯！
core = openmc.RectLattice(name = "NuScale Core")
core.lower_left = (-(pitch*17)*3.5, -(pitch*17)*3.5)
core.pitch = (pitch*17, pitch*17)
cr1_lst =  [[w   , w   , c1  , re2 , c1  , w   , w   ],
            [w   , c2  , sh4 , a1  , sh3 , c2  , w   ],
            [c1  , sh3 , a2  , re1 , a2  , sh4 , c1  ],
            [re2 , a1  , re1 , c3  , re1 , a1  , re2 ],
            [c1  , sh4 , a2  , re1 , a2  , sh3 , c1  ],
            [w   , c2  , sh3 , a1  , sh4 , c2  , w   ],
            [w   , w   , c1  , re2 , c1  , w   , w   ]]

cr0_lst =  [[w   , w   , c1  , b2  , c1  , w   , w   ],
            [w   , c2  , b1  , a1  , b1  , c2  , w   ],
            [c1  , b1  , a2  , a1cr, a2  , b1  , c1  ],
            [b2  , a1  , a1cr, c3  , a1cr, a1  , b2  ],
            [c1  , b1  , a2  , a1cr, a2  , b1  , c1  ],
            [w   , c2  , b1  , a1  , b1  , c2  , w   ],
            [w   , w   , c1  , b2  , c1  , w   , w   ]]

scram =    [[0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]] # SCRAM: All rods in 

re1in = [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]] # RE1 in

re2in = [[0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]] # RE2 in

sh3in = [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]] # SH3 in

sh4in =    [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]] # SH4 in

ref =      [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]] # Ref: All rods out

re1d5in =    [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]] # Single RE1 D5 on 

core.universes = cr0_lst
all_water_cell = openmc.Cell(fill=mat_hv) # 不定义region就是全空间
outer_universe = openmc.Universe(cells=(all_water_cell,))
core.outer = outer_universe
R2_core = openmc.ZCylinder(r=99.0600, boundary_type='vacuum')
R1_core = openmc.ZCylinder(r=93.9800)

# 一、堆芯
core_cell = openmc.Cell(name='root cell', fill=core)
core_cell.region = -openmc.ZCylinder(r=93.9800) & -topZ & +bottomZ

# 二、钢制容器壁
barrel = openmc.Cell(fill=ss_304l, region=-R2_core & +R1_core & -topZ & +bottomZ)

# 三、Core方形之外的冷却水
rect_core = openmc.model.RectangularPrism(width=pitch*17*7,height=pitch*17*7,axis='z')
heavy_reflector = openmc.Cell(fill=mat_hv,region= -topZ & +bottomZ & +rect_core & -R1_core)

root_universe = openmc.Universe(cells=[core_cell,barrel,heavy_reflector])
geometry = openmc.Geometry(root_universe)

# ------------- Tally -------------

# FAs 功率密度
mesh1 = openmc.RegularMesh()
mesh1.dimension = [7, 7]
mesh1.lower_left = [-pitch*17*7/2, -pitch*17*7/2]
mesh1.upper_right = [+pitch*17*7/2, +pitch*17*7/2]
mesh_filter1 = openmc.MeshFilter(mesh1)
t1 = openmc.Tally(name='rad_pow')
t1.filters = [mesh_filter1]
t1.scores = ['fission']

# Fuel pins 功率密度
mesh2 = openmc.RegularMesh()
mesh2.dimension = [7*17, 7*17]
mesh2.lower_left = [-pitch*17*7/2, -pitch*17*7/2]
mesh2.upper_right = [+pitch*17*7/2, +pitch*17*7/2]
mesh_filter2 = openmc.MeshFilter(mesh2) # 网格过滤器
t2 = openmc.Tally(name='pin_pow') # 最后根据name来读取h5文件
t2.filters = [mesh_filter2]
t2.scores = ['fission']

# Rect
mesh3 = openmc.RectilinearMesh()
mesh3.x_grid = [-pitch*17*7/2, +pitch*17*7/2]
mesh3.y_grid = [-pitch*17*7/2, +pitch*17*7/2]
z_lst = [11.365,14.920,19.365,31.017,42.670,54.322,65.974,70.419,82.071,93.724,105.376,117.028,121.473,133.125,144.778,156.430,168.082,172.527,182.236,191.946,201.656,211.365]
mesh3.z_grid = [x - tran_z for x in z_lst]
mesh_filter3 = openmc.MeshFilter(mesh3)
t3 = openmc.Tally(name='pow_ax') # 最后根据name来读取h5文件
t3.filters = [mesh_filter3]
t3.scores = ['fission'] # 选择分数

tallies = openmc.Tallies([t1,t2,t3])
settings = openmc.Settings()

settings.batches = 300
settings.inactive = 100
settings.particles = 50000

# source = openmc.Source()
# source.space = openmc.stats.Box(lower_left=[-99.0600, -99.0600, 0-tran_z], upper_right=[99.0600, 99.0600,243.561-tran_z])
# settings.source = source

run_root = Path("data")
cases = [
    ("Reference", ref),
    ("RE1in", re1in),
    ("RE2in", re2in),
    ("SH3in", sh3in),
    ("SH4in", sh4in),
    ("SCRAM", scram),
    ("RE1d5in", re1d5in),
    ]

for case_name, case_mode in cases:
    run_dir = run_root / case_name
    run_dir.mkdir(parents=True, exist_ok=True)

    cr0_run = [row[:] for row in cr0_lst]
    for i in range(len(case_mode)):
        for j in range(len(case_mode[i])):
            if case_mode[i][j] == 1:
                cr0_run[i][j] = cr1_lst[i][j]
    core.universes = cr0_run

    materials.export_to_xml(path=run_dir / "materials.xml")
    geometry.export_to_xml(path=run_dir / "geometry.xml")
    tallies.export_to_xml(path=run_dir / "tallies.xml")
    settings.export_to_xml(path=run_dir / "settings.xml")

    print(run_dir)
    openmc.run(cwd=str(run_dir))