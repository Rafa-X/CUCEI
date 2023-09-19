import sys
import psutil

# psutil - Library for retreiving information on running processes and system utilization,
#          also provides an interface for setting up, monitoring, profiling and management.
# Documentation - https://code.google.com/p/psutil/wiki/Documentation

#Checks if the given argument is valid
def check_arguments():
    if len(sys.argv) == 1:
    	print('Este programa no funciona sin argumentos')
    	sys.exit(0)

#Gets the objective processes arguments and cancates the .exe if don't have in it
def get_targets():
    targets = sys.argv[1:]

    i = 0
    while i < len(targets):
    	if not targets[i].endswith('.exe'):
    		targets[i] = targets[i] + '.exe'
    	i += 1
    return targets

#Gets the opened process and checks if it's and objective to block (and kill) or just some other process
def lock_proc(target):
    for proc in psutil.process_iter():
    	if proc.name().lower() == target.lower():
            print(f'!La aplicacion {target} esta bloqueada!')
    		proc.kill()


if __name__ == '__main__':

    check_arguments()
    targets = get_targets()

    #While the service is running it will check all the processes that are opening
    while True:
    	for target in targets:
    		lock_proc(target)