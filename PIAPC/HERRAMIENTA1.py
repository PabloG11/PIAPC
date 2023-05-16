import subprocess, sys

p = subprocess.Popen(["powershell.exe", "C:\\Users\elcha\Desktop\PIAPC\HERRAMIENTA1.ps1"], stdout=sys.stdout)
p.communicate()
