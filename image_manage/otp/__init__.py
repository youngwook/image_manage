# -*- coding: utf-8 -*-
from sys import platform as pf
import pexpect
if pf == 'win32':
    from pexpect.popen_spawn import PopenSpawn

def sshConnect(account, ps, otp):
#    ssh = pexpect.spawn('ssh p326jin@login01.plsi.or.kr')
    if pf == 'win32':
        ssh = PopenSpawn(('ssh %s' % account))
    else:
        ssh = pexpect.spawn(('ssh %s' % account))
    PROMPT = ['#:','$:']

    try:
        i = ssh.expect([ '[P|p]assword\(OTP\)\:', 'Are you sure you want to continue connecting \(yes\/no\)\?'], timeout=5)

        if i == 0:
            ssh.sendline(str(otp))
            ssh.expect(['[P|p]assword\:'])
            ssh.sendline(ps)
            return ssh

        elif i == 1:

            ssh.sendline('yes')
            ssh.expect(['[P|p]assword\(OTP\)\:'])
            ssh.sendline(str(otp))
            ssh.expect(['[P|p]assword\:'])
            ssh.sendline(ps)
            return ssh

    except pexpect.EOF:
        print "EOF"
        return None

    except pexpect.TIMEOUT:
        print "timeout"
        return None

    return None