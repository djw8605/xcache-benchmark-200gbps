import sys
from multiprocessing import Pool
import subprocess
import os

def process(filename):
    os.environ["XRD_LOGLEVEL"] = "Dump"
    converted_file = "root://xcache.cmsaf-dev.flatiron.hollandhpc.org:1094/" + filename.strip()
    command = ["xrdcp", "--debug", "3", "-f", converted_file, "/dev/null"]
    print(f'Running command: {command}')
    command_output = subprocess.run(command)
    print(f'Exit code of command {command}: {command_output.returncode}')
    
    #print(filename)

def main():
    # Get a few of the files
    pool = Pool(10)
    files = []
    with open('files.txt', 'r') as file_list:
        files = file_list.readlines()

    # Get the argument, multiply by 100, and that's our start index
    start_index = int(sys.argv[1]) * 100
    files = files[start_index:start_index+100]
    #files = files[:10]
    pool.imap(process, files)
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
