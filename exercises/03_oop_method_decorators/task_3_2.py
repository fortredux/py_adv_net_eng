# -*- coding: utf-8 -*-
'''
Задание 3.2

Скопировать класс PingNetwork из задания 1.2.
Один из методов класса зависит только от значения аргумента и не зависит
от значений переменных экземпляра или другого состояния объекта.

Сделать этот метод статическим и проверить работу метода.

'''


import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.append('../01_oop_basics/')

from task_1_1 import IPv4Network


class PingNetwork:
    def __init__(self, ipv4network):
        self._ipv4network = ipv4network

    @staticmethod
    def _ping(ip):
        ping = subprocess.run(f'ping -c 3 {ip}', stdout=subprocess.DEVNULL, shell=True)
        return ping.returncode

    def scan(self, workers=5, include_unassigned=False):
        if include_unassigned:
            ips = self._ipv4network.hosts()
        else:
            ips = self._ipv4network.allocated

        reachable = []
        unreachable = []
        with ThreadPoolExecutor(max_workers=workers) as executor:
            result = executor.map(self._ping, ips)
            temp = list(zip(ips, result))
            for item in temp:
                if item[1] == 0:
                    reachable.append(item[0])
                elif item[1] != 0:
                    unreachable.append(item[0])
        return (reachable, unreachable)


if __name__ == "__main__":
    net1 = IPv4Network('8.8.4.0/29')

    net1.allocate('8.8.4.2')
    net1.allocate('8.8.4.4')
    net1.allocate('8.8.4.6')
    print(net1.allocated)
    print(net1.hosts())

    ping_net = PingNetwork(net1)
    print(ping_net.scan(include_unassigned=True))

    del net1