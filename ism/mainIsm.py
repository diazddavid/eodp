
# MAIN FUNCTION TO CALL THE ISM MODULE
import sys, os
# path = Path(os.path.realpath(__file__))
# sys.path.insert(0, path.parent.parent)
# print(sys.path)
from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
