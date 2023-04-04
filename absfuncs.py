import math
import constants as cts


"""
This set of functions are used in computing the Bethe-Block equation.
"""


gamma = lambda beta: (1-beta**2)**(-0.5)  #divide by the charge of the electron e to convert from Joule to eV
eta = lambda beta: beta * gamma(beta)
W_max = lambda beta: (2 * cts.M_E * cts.C **2 / cts.Q_E) * (eta(beta))**2 / (1 + 2 * cts.S * (1 + (eta(beta))**2)**0.5 + cts.S**2 )
Fn = lambda beta: math.log((2 * cts.M_E * cts.C**2/cts.Q_E) * (eta(beta))**2*W_max(beta)/(cts.I_P**2))
dbeta = lambda x, beta: (-cts.K * cts.RHO * (cts.Z / cts.A ) * cts.ZE**2/(cts.M_ALPHA * cts.C**2/cts.Q_E)) * eta(beta)**(-3)*(Fn(beta)-2*beta**2)
