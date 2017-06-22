# -*- coding: utf-8 -*-
from sys import platform as pf
import pexpect
from pexpect.popen_spawn import PopenSpawn

class Connection:

    def sshLogin(self, account, ps):
        self.ssh = None

        try:
            if pf == 'win32':
                self.ssh = pexpect.popen_spawn.PopenSpawn(('ssh %s' % account))
            else:
                self.ssh = pexpect.spawn(('ssh %s' % account))

            i = self.ssh.expect(['[P|p]assword\:', 'Are you sure you want to continue connecting \(yes\/no\)\?'], timeout=5)

            if i == 0:
                '''ps = raw_input('[P|p]assword:')'''
                self.ssh.sendline(ps)
                return self.ssh

            elif i == 1:
                self.ssh.sendline('yes')
                self.ssh.expect(['[P|p]assword\:'])
                '''ps = raw_input('[P|p]assword:')'''
                self.ssh.sendline(ps)
                return self.ssh

        except pexpect.EOF:
            return self.ssh

        except pexpect.TIMEOUT:
            return self.ssh

    def command(self):

        try :
            self.ssh.sendline("ls")
            self.ssh.expect("root@sdn")

        except pexpect.EOF:
            return None

        except pexpect.TIMEOUT:
            return None

        return self.ssh.before


