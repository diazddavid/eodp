
# MAIN FUNCTION TO CALL THE ISM MODULE
import sys, os
from pathlib import Path
from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules

# Initialise the ISM

path = Path(os.path.realpath(__file__))
parent_path = path.parent.parent
project_path = parent_path.parent
auxdir = str(os.path.join(parent_path, 'auxiliary'))
indir = str(os.path.join(project_path, 'eodp_data', 'EODP-TS-ISM', 'input', 'gradient_alt100_act150'))
outdir = str(os.path.join(parent_path, 'output', 'ism'))
print("ISM auxdir: " + auxdir)
print("ISM indir: " + indir)
print("ISM outdir: " + outdir)

myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
