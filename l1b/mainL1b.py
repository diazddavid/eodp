
# MAIN FUNCTION TO CALL THE L1B MODULE

import sys, os
from pathlib import Path
from l1b.src.l1b import l1b

# Directory - this is the common directory for the execution of the E2E, all modules
# auxdir = '/home/luss/EODP/eodp/auxiliary'
# indir = '/home/luss/EODP/eodp/ism/test/ut02/output'
# outdir = '/home/luss/EODP/eodp/l1b/test/ut02/output'

path = Path(os.path.realpath(__file__))
parent_path = path.parent.parent
project_path = parent_path.parent
auxdir = str(os.path.join(parent_path, 'auxiliary'))
indir = str(os.path.join(project_path, 'eodp_data', 'EODP-TS-L1B', 'input'))
outdir = str(os.path.join(project_path, 'output', 'l1b'))
print("L1B auxdir: " + auxdir)
print("L1B indir: " + indir)
print("L1B outdir: " + outdir)
# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
