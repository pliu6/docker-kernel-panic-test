import time
import os
import subprocess


def main():
    print 'start testing...'

    cmd = ['docker', 'logs', '-f', '-t', 'docker-test']
    print "Calling: {}".format(" ".join(cmd))
    env = {
        "PATH": os.environ.get("PATH", "/bin")
    }
    env['PATH'] += ':' + '/snap/bin'
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=True, env=env)

    time.sleep(300)

if __name__ == "__main__":
    main()
