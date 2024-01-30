import os
import psutil

l1, l2, l3 = psutil.getloadavg()
CPU_use = (l3 / os.cpu_count()) * 100

print(CPU_use)