import pexpect
from pexpect import pxssh

ssh = pexpect.spawn('ssh p326jin@login01.plsi.or.kr')

PROMPT = ['#:','$:']

try:
    i = ssh.expect([ '[P|p]assword(OTP)', 'Are you sure you want to continue connecting (yes/no)?'], timeout=5)

    if i == 0:
        ssh.expect(['[P|p]assword(OTP):'])
        otp = raw_input('insert OTP: ')
        ssh.sendline(str(otp))
        ssh.expect(['[P|p]assword:'])
        ps = raw_input('insert password: ')
        ssh.sendline(ps)
        print("login success!")

    elif i == 1:
        print 'Are you sure you want to continue connecting (yes/no)?'
        ssh.sendline('yes')
        ssh.expect(['[P|p]assword(OTP):'])
        otp = raw_input('insert OTP: ')
        ssh.sendline(str(otp))
        ssh.expect(['[P|p]assword:'])
        ps = raw_input('insert password: ')
        ssh.sendline(ps)
        print("login success!")

except pexpect.EOF:
    print "EOF"
    ssh.close()

except pexpect.TIMEOUT:
    print "timeout"
    ssh.close()

ssh.close()
