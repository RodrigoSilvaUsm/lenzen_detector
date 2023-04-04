from scipy import constants as cts


# Physical constants

PI = cts.pi
Q_E = cts.elementary_charge
M_E = cts.electron_mass
R_E = cts.physical_constants['classical electron radius'][0]
C = cts.c
N_A = cts.N_A
H = cts.h
K = 1000 * 2 * PI * N_A * R_E**2 * M_E * C**2 / Q_E #the factor 1000 is due to an imbalance in units, ideally to find anothe way to write this, N_A in mol and A in kg/kmol 


M_ALPHA = cts.physical_constants['alpha particle mass'][0]
S = M_E / M_ALPHA
#Properties of the absorving material (copper)
Z = 0.49919 #for dry air Z/A=0.499, so it is assumed A=1
A = 1
I_P = 85.7
RHO = 1.2048 #[kg/m^3], air density
ZE = 2          # charge of incident particle in units of e, for alpha particle z=2
