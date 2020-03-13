from flask import Flask
import os
import subprocess

app = Flask(__name__)

def os_launch(proc, arg):
    return str(subprocess.Popen([proc, arg], stdout=subprocess.PIPE).communicate()[0])[2:-3]


@app.route('/')
def task():
    string = 'Python version: %s' % os_launch('python3', '-V').split()[1] + '\n'
    string += 'Flask version: %s' % os_launch('flask', '--version').split('\\n')[1].split()[1] + '\n'
    string += 'OS Name: %s' % os_launch('cat', '/etc/os-release').split('\\n')[0].split('=')[1] + '\n'
    string += 'OS Release: %s' % os_launch('cat', '/etc/os-release').split('\\n')[1].split('=')[1] + '\n'
    string += 'OS Family: %s' % os_launch('cat', '/etc/os-release').split('\\n')[3].split('=')[1] + '\n'
    string += 'Kernel version: %s' % os_launch('uname', '-r') + '\n'
    string += 'Hostname: %s' % os_launch('hostname', '-s') + '\n'
    string += 'IP: %s' % os_launch('hostname', '-i') + '\n'
    string += 'Container build date: %s' % os.environ.get('BUILD_DATE') + '\n'
    string += 'Student Name: %s' % os.environ.get('STUDENT_NAME') + '\n'
    string += 'HOMEDIR: %s' % os.environ.get('HOME')
    return string

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
