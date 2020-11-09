from common.io.l1cProduct import readL1c
from common.plot.plotF import plotF
import sys, os
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# Directory - this is the common directory for the execution of the E2E, all modules

# Initialise the ISM

def compare_L1C(ref_dir, gen_dir, name_file):
    ref_L1C = readL1c(ref_dir, name_file)[1]
    generated_L1C = readL1c(gen_dir, name_file)[1]

    diff_L1C = np.abs((generated_L1C-ref_L1C)/generated_L1C)

    print("Maximum Difference: " + str(np.max(diff_L1C)*100) + "%")

    title_str = name_file.replace(".nc", "") + " Difference"
    xlabel_str=''
    ylabel_str=''
    out_dir = os.path.join(gen_dir, "test")
    idalt = int(diff_L1C.shape[0]/2)
    plotF([], diff_L1C, title_str, xlabel_str, ylabel_str, out_dir, name_file.replace(".nc", ".png"))


path = Path(os.path.realpath(__file__))
parent_path = path.parent.parent
project_path = parent_path.parent.parent
auxdir = str(os.path.join(parent_path, 'auxiliary'))
provided_dir = str(os.path.join(project_path, 'eodp_data', 'EODP-TS-L1C', 'output'))
generated_dir = str(os.path.join(parent_path, 'output', 'l1c'))

print("L1C auxdir: " + auxdir)
print("L1C provided dir: " + provided_dir)
print("L1C generated dir: " + generated_dir)

provided_L1Cs = [f for f in os.listdir(provided_dir) if os.path.isfile(os.path.join(provided_dir, f))]
provided_L1Cs_path = []
for file in provided_L1Cs:
    provided_L1Cs_path.append(os.path.join(provided_dir, file))

generated_L1Cs = [f for f in provided_L1Cs if os.path.isfile(os.path.join(generated_dir, f))]
generated_L1Cs_path = []
for file in generated_L1Cs:
    generated_L1Cs_path.append(os.path.join(generated_dir, file))

print("CHECK if there are the same generated L1C than provided: ")
print("Generated: " + str(len(generated_L1Cs)))
print("Provided: " + str(len(provided_L1Cs)))

for name_file in generated_L1Cs:
    print("\n\nComparing " + name_file + ":\n")
    compare_L1C(provided_dir, generated_dir, name_file)
