import subprocess 
ob = subprocess.call('start', shell = True)
if ob:
    subprocess.call('echo hi', shell = True)