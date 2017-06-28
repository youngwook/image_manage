# -*- coding: utf-8 -*-
from sys import platform as pf
import pexpect
if pf == 'win32':
    from pexpect.popen_spawn import PopenSpawn

class Connection:

    def sshLogin(self, account, ps, otp):
        self.ssh = None

        try:
            if pf == 'win32':
                self.ssh = pexpect.popen_spawn.PopenSpawn(('ssh %s' % account))
            else:
                self.ssh = pexpect.spawn(('ssh %s' % account))

            for n in range(3):

                i = self.ssh.expect(['Are you sure you want to continue connecting \(yes\/no\)\?', '[P|p]assword\(OTP\)', '[P|p]assword\:'], timeout=5)

                if i == 0:
                    self.ssh.sendline('yes')

                if i == 1:
                    self.ssh.sendline(otp)

                if i == 2:
                    self.ssh.sendline(ps)
                    return self.ssh


        except pexpect.EOF:
            return self.ssh

        except pexpect.TIMEOUT:
            return self.ssh

    def command(self, user):

        try :
            self.ssh.sendline("ls")
            self.ssh.expect(('%s@' % user))

        except pexpect.EOF:
            return None

        except pexpect.TIMEOUT:
            return None

        return self.ssh.before