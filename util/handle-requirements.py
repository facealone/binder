import sys
import subprocess

if __name__ == "__main__":
    commands = [["pip", "install", "-r", "requirements.txt"],
                ["/home/main/anaconda/envs/python3/bin/pip", "install", "-r", "requirements.txt"]]
    errors = 0
    for cmd in commands:
        try:
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError as e:
            print("installation command failed: {}".format(e))
            errors += 1
            continue
    if errors >= len(commands): 
        raise Exception("All installation commands failed")
