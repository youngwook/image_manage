# -*- coding: utf-8 -*-
import pexpect
from pexpect import pxssh

def sshConnect(account, ps, otp):
#    ssh = pexpect.spawn('ssh p326jin@login01.plsi.or.kr')

    ssh = pexpect.spawn('ssh {}'.format(account))
    PROMPT = ['#:','$:']

    try:
        i = ssh.expect([ '[P|p]assword\(OTP\)', 'Are you sure you want to continue connecting \(yes\/no\)\?'], timeout=5)

        if i == 0:
            ssh.expect(['[P|p]assword\(OTP\)\:'])
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
        ssh.close()
        return None

    except pexpect.TIMEOUT:
        print "timeout"
        ssh.close()
        return None

    ssh.close()
    return ssh