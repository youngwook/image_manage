# -*- coding: utf-8 -*-
from sys import platform as pf
import pexpect
from pexpect.popen_spawn import PopenSpawn

#    ssh = pexpect.spawn('ssh p326jin@login01.plsi.or.kr')

account = 'p326jin@login01.plsi.or.kr'




try:
    if pf == 'win32':
        ssh = pexpect.popen_spawn.PopenSpawn('ssh p326jin@login01.plsi.or.kr')
    else:
        ssh = pexpect.spawn('ssh {}'.format(account))
    i = ssh.expect([ '[P|p]assword\(OTP\)', 'Are you sure you want to continue connecting \(yes\/no\)\?'], timeout=5)

    if i == 0:
        ssh.expect(['[P|p]assword\(OTP\)\:'])
        otp = raw_input("[P|p]assword\(OTP\)\:")
        ssh.sendline(str(otp))
        ssh.expect(['[P|p]assword\:'])
        ps = raw_input('[P|p]assword\:')
        ssh.sendline(ps)

    elif i == 1:

        ssh.sendline('yes')
        otp = raw_input("[P|p]assword\(OTP\)\:")
        ssh.sendline(str(otp))
        ssh.expect(['[P|p]assword\:'])
        ps = raw_input('[P|p]assword\:')
        ssh.sendline(ps)

except pexpect.EOF:
    print "EOF"

except pexpect.TIMEOUT:
    print "timeout"
