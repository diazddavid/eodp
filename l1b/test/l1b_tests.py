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

def plot_isrf_vs_rest(generated_dir, isrf_file, rest_file, i):
    isrf_toa = readToa(generated_dir, isrf_file)
    rest_toa = readToa(generated_dir, rest_file)
    idalt = int(isrf_toa.shape[0]/2)

    fig = plt.figure(figsize=(10, 7))
    plt.plot(isrf_toa[idalt,:], 'b')
    plt.plot(rest_toa[idalt,:], 'r')
    plt.legend(["ISRF TOA", "Restored TOA"])
    plt.title("Restored VS ISRF TOA", fontsize=20)
    plt.xlabel("ACT_pixel [-]", fontsize=16)
    plt.ylabel("TOA", fontsize=16)
    plt.grid()
    savestr = os.path.join(generated_dir, "test", "restored_" + str(i) + ".png")
    plt.savefig(savestr)
    plt.close(fig)

def plot_isrf_vs_eq_vs_neq(generated_dir, isrf_file, eq_file, neq_file, i):
    isrf_toa = readToa(generated_dir, isrf_file)
    eq_toa = readToa(generated_dir, eq_file)
    neq_toa = readToa(generated_dir, neq_file)
    idalt = int(isrf_toa.shape[0]/2)

    fig = plt.figure(figsize=(10, 7))
    plt.plot(isrf_toa[idalt,:], 'blue')
    plt.plot(eq_toa[idalt,:], 'black')
    plt.plot(neq_toa[idalt,:], 'red')
    plt.legend(["ISRF TOA", "TOA 1LB with EQ", "TOA 1LB no EQ"])
    plt.title("Restored VS ISRF TOA VS NEQ", fontsize=20)
    plt.xlabel("ACT_pixel [-]", fontsize=16)
    plt.ylabel("TOA", fontsize=16)
    plt.grid()
    savestr = os.path.join(generated_dir, "test", "eq_vs_neq_" + str(i) + ".png")
    plt.savefig(savestr)
    plt.close(fig)


path = Path(os.path.realpath(__file__))
parent_path = path.parent.parent
project_path = parent_path.parent.parent
auxdir = str(os.path.join(parent_path, 'auxiliary'))
provided_dir = str(os.path.join(project_path, 'eodp_data', 'EODP-TS-L1B', 'output'))
generated_dir = str(os.path.join(parent_path, 'output', 'l1b'))

print("L1B auxdir: " + auxdir)
print("L1B provided dir: " + provided_dir)
print("L1B generated dir: " + generated_dir)

provided_toas = [f for f in os.listdir(provided_dir) if os.path.isfile(os.path.join(provided_dir, f))]
provided_toas_path = []
for file in provided_toas:
    provided_toas_path.append(os.path.join(provided_dir, file))

generated_toas = [f for f in  os.listdir(generated_dir)  if os.path.isfile(os.path.join(generated_dir, f))]
generated_toas_path = []
for file in generated_toas:
    generated_toas_path.append(os.path.join(generated_dir, file))

isrf_toas = [f for f in generated_toas if "isrf" in f]
restored_str = "l1b_toa_VN"
restored_toas = [f for f in generated_toas if restored_str in f]
eq_toas = [f for f in generated_toas if "_eq_" in f]
neq_toas = [f for f in generated_toas if "_neq_" in f]

print("CHECK if there are the same generated TOA than provided: ")
print("Generated: " + str(len(generated_toas)))
print("Provided: " + str(len(provided_toas)))

for name_file in provided_toas:
        print("\n\nComparing " + name_file + ":\n")
        compare_toa(provided_dir, generated_dir, name_file)

i = 0
for name_file in isrf_toas:
    isrf_file = name_file
    rest_file = restored_toas[i]
    i = i+1
    plot_isrf_vs_rest(generated_dir, isrf_file, rest_file, i)

i = 0
for name_file in isrf_toas:
    isrf_file = name_file
    eq_file = eq_toas[i]
    neq_file = neq_toas[i]
    i = i+1
    plot_isrf_vs_eq_vs_neq(generated_dir, isrf_file, eq_file, neq_file, i)
