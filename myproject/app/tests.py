import os
import subprocess


def os_launch(proc, arg):
    return str(subprocess.Popen([proc, arg], stdout=subprocess.PIPE).communicate()[0])[2:-3]

if __name__ == '__main__':
    print('Python version: %s' % os_launch('python', '-V').split()[1])
    print('Flask version: %s' % os_launch(
        'flask', '--version').split('\\n')[1].split()[1])
    print('OS Name: %s' % os_launch(
        'cat', '/etc/os-release').split('\\n')[0].split('=')[1])
    print('OS Family: %s' % os_launch(
        'cat', '/etc/os-release').split('\\n')[1].split('=')[1])
    print('Release: %s' % os_launch(
        'cat', '/etc/os-release').split('\\n')[3].split('=')[1])
    print('Kernel version: %s' % os_launch('uname', '-r'))
    print('Hostname: %s' % os_launch('hostname', '-s'))
    print('IP: %s' % os_launch('hostname', '-i'))
    print('Container build date: %s' % os.environ['BUILD_DATE'])
    print('Student Name: %s' % os.environ['STUDENT_NAME'])
