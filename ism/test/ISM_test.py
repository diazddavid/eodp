from common.io.writeToa import readToa
from common.plot.plotF import plotF
import sys, os
import numpy as np
from pathlib import Path
from ism.src.ism import ism
import matplotlib.pyplot as plt

# Directory - this is the common directory for the execution of the E2E, all modules

# Initialise the ISM

def compare_toa(ref_dir, gen_dir, name_file):
    ref_toa = readToa(ref_dir, name_file)
    generated_toa = readToa(gen_dir, name_file)

    diff_toa = np.abs((generated_toa-ref_toa)/generated_toa)

    print("Maximum Difference: " + str(np.max(diff_toa)*100) + "%")

    title_str = name_file.replace(".nc", "") + " Difference"
    xlabel_str=''
    ylabel_str=''
    out_dir = os.path.join(gen_dir, "test")
    idalt = int(diff_toa.shape[0]/2)
    plotF([], diff_toa[idalt,:], title_str, xlabel_str, ylabel_str, out_dir, name_file.replace(".nc", ".png"))


path = Path(os.path.realpath(__file__))
parent_path = path.parent.parent
project_path = parent_path.parent.parent
auxdir = str(os.path.join(parent_path, 'auxiliary'))
provided_dir = str(os.path.join(project_path, 'eodp_data', 'EODP-TS-ISM', 'output'))
generated_dir = str(os.path.join(parent_path, 'output', 'ism'))

print("ISM auxdir: " + auxdir)
print("ISM provided dir: " + provided_dir)
print("ISM generated dir: " + generated_dir)

provided_toas = [f for f in os.listdir(provided_dir) if os.path.isfile(os.path.join(provided_dir, f))]
provided_toas_path = []
for file in provided_toas:
    provided_toas_path.append(os.path.join(provided_dir, file))

generated_toas = [f for f in provided_toas if os.path.isfile(os.path.join(generated_dir, f))]
generated_toas_path = []
for file in generated_toas:
    generated_toas_path.append(os.path.join(generated_dir, file))

print("CHECK if there are the same generated TOA than provided: ")
print("Generated: " + str(len(generated_toas)))
print("Provided: " + str(len(provided_toas)))

for name_file in generated_toas:
    if "detec" in name_file:
        print("\n\nComparing " + name_file + ":\n")
        compare_toa(provided_dir, generated_dir, name_file)
