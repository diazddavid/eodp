
# MAIN FUNCTION TO CALL THE L1C MODULE
import sys, os
from pathlib import Path
from l1c.src.l1c import l1c

# Directory - this is the common directory for the execution of the E2E, all modules
# auxdir = '/home/luss/EODP/eodp/auxiliary'
# # GM dir + L1B dir
# indir = '/home/luss/my_shared_folder/gm_out/gm_alt100_act_150/,/home/luss/EODP/eodp/l1b/test/ut02/output'
# outdir = '/home/luss/EODP/eodp/l1c/test/ut01/output'

path = Path(os.path.realpath(__file__))
parent_path = path.parent.parent
project_path = parent_path.parent
auxdir = str(os.path.join(parent_path, 'auxiliary'))
indir_base = os.path.join(project_path, 'eodp_data', 'EODP-TS-L1C', 'input')
indir1 = str(os.path.join(indir_base, 'gm_alt100_act_150'))
indir2 = str(os.path.join(indir_base, 'l1b_output'))
indir = indir1 + ',' + indir2
outdir = (os.path.join(project_path, 'output', 'l1c'))
print("L1C auxdir: " + auxdir)
print("L1C indir: " + indir)
print("L1C outdir: " + outdir)


# Initialise the ISM
myL1c = l1c(auxdir, indir, outdir)
myL1c.processModule()
