from Decompose import *

def MolarMass(molecule):
    '''Calculates the molar mass of a given molecule.

            The calculation is done summing the multiples of the coefficients in the compound's
            dictionnary (-> Decompose function) with the element's molar mass.
            * Requires: Decompose

            Args:
                molecule (str) : molecule of which one wants to know the molar mass

            Returns:
                M (float) :  molecule's molar mass'''

    d_atomic_masses = {'H' : 1.0080,
                       'He' : 4.00260,
                       'Li': 7.0,
                       'Be': 9.012183,
                       'B': 10.81,
                       'C': 12.011,
                       'N': 14.007,
                       'O': 15.999,
                       'F': 18.99840316,
                       'Ne': 20.180,
                       'Na': 22.9897693,
                       'Mg': 24.305,
                       'Al': 26.981538,
                       'Si': 28.085,
                       'P': 30.97376200,
                       'S': 32.07,
                       'Cl': 35.45,
                       'Ar': 39.9,
                       'K': 39.0983,
                       'Ca': 40.08,
                       'Sc': 44.95591,
                       'Ti': 47.867,
                       'V': 50.9415,
                       'Cr': 51.996,
                       'Mn': 54.93804,
                       'Fe': 55.84,
                       'Co': 58.93319,
                       'Ni': 58.693,
                       'Cu': 63.55,
                       'Zn': 65.4,
                       'Ga': 69.723,
                       'Ge': 72.63,
                       'As': 74.92159,
                       'Se': 78.97,
                       'Br': 79.90,
                       'Kr': 83.80,
                       'Rb': 85.468,
                       'Sr': 87.62,
                       'Y': 88.90584,
                       'Zr': 91.22,
                       'Nb': 92.90637,
                       'Mo': 95.95,
                       'Tc': 96.90636,
                       'Ru': 101.1,
                       'Rh': 102.9055,
                       'Pd': 106.42,
                       'Ag': 107.868,
                       'Cd': 112.41,
                       'In': 114.818,
                       'Sn': 118.71,
                       'Sb': 121.760,
                       'Te': 127.6,
                       'I': 126.9045,
                       'Xe': 131.29,
                       'Cs': 132.9054520,
                       'Ba': 137.33,
                       'La': 138.9055,
                       'Ce': 140.116,
                       'Pr': 140.90766,
                       'Nd': 144.24,
                       'Pm': 144.91276,
                       'Sm': 150.4,
                       'Eu': 151.964,
                       'Gd': 157.2,
                       'Tb': 158.92535,
                       'Dy': 162.500,
                       'Ho': 164.93033,
                       'Er': 167.26,
                       'Tm': 168.93422,
                       'Yb': 173.05,
                       'Lu': 174.9668,
                       'Hf': 178.49,
                       'Ta': 180.9479,
                       'W': 183.84,
                       'Re': 186.207,
                       'Os': 190.2,
                       'Ir': 192.22,
                       'Pt': 195.08,
                       'Au': 196.96657,
                       'Hg': 200.59,
                       'Tl': 204.383,
                       'Pb': 207,
                       'Bi': 208.98040,
                       'Po': 208.98243,
                       'At': 209.98715,
                       'Rn': 222.01758,
                       'Fr': 223.01973,
                       'Ra': 226.02541,
                       'Ac': 227.02775,
                       'Th': 232.038,
                       'Pa': 231.03588,
                       'U': 238.0289,
                       'Np': 237.048172,
                       'Pu': 244.06420,
                       'Am': 243.061380,
                       'Cm': 247.07035,
                       'Bk': 247.07031,
                       'Cf': 251.07959,
                       'Es': 252.0830,
                       'Fm': 257.09511,
                       'Md': 258.09843,
                       'No': 259.10100,
                       'Lr': 266.120,
                       'Rf': 267.122,
                       'Db': 268.126,
                       'Sg': 269.128,
                       'Bh': 270.133,
                       'Hs': 269.1336,
                       'Mt': 277.154,
                       'Ds': 282.166,
                       'Rg': 282.169,
                       'Cn': 286.179,
                       'Nh': 286.182,
                       'Fl': 290.192,
                       'Mc': 290.196,
                       'Lv': 293.205,
                       'Ts': 294.211,
                       'Og': 295.216}

    d_elements_molecule = Decompose([molecule])[0]
    molar_mass = 0

    for element, occurrence in d_elements_molecule.items():
        molar_mass = molar_mass + occurrence*(d_atomic_masses[element])

    return molar_mass

def MolarMassUI():
    '''User interface for the evaluation of a molecule's molar mass.

            Facilitates the input of parameters and only accepts valid one.
            Prints the molar mass
            * Requires: MolarMass'''
    
    while True:
        try:
            molecule = str(input(("\033[1m" + "\nPlease enter the chemical formula: " + "\033[0m")))
            M = round(MolarMass(molecule), 3)
            print(f"\033[1m" + f"{molecule} has a molar mass of {M} gmol⁻¹." + "\033[0m")
            break
        except:
            print(f"\033[1m" + "Invalid chemical formula!" + "\033[0m")

