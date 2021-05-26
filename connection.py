import paramiko

def connect_with_pi(ip = '192.168.178.207', username = 'pi', password = 'bierbier'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password)
    except:
        ssh=None
    return ssh

def execute_command(ssh, cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    return(resp)

