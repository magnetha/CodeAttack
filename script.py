import subprocess

for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                subprocess.run('./program-x86 ' + str(a) + str(b) + str(c) + str(d), shell=True)
