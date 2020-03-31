# -*- coding: utf-8 -*-
'''
Задание 2.2

Скопировать класс PingNetwork из задания 1.2 и изменить его таким образом,
чтобы адреса пинговались не при вызове метода scan, а при вызове экземпляра.

Вся функциональность метода scan должна быть перенесена в метод, который отвечает
за вызов экземпляра.

Пример работы с классом PingNetwork. Сначала создаем сеть:
In [2]: net1 = IPv4Network('8.8.4.0/29')

И выделяем несколько адресов:
In [3]: net1.allocate('8.8.4.2')
   ...: net1.allocate('8.8.4.4')
   ...: net1.allocate('8.8.4.6')
   ...:

Затем создается экземпляр класса PingNetwork, сеть передается как аргумент:
In [6]: ping_net = PingNetwork(net1)

После этого экземпляр должен быть вызываемым объектом (callable):

In [7]: ping_net()
Out[7]: (['8.8.4.4'], ['8.8.4.2', '8.8.4.6'])

In [8]: ping_net(include_unassigned=True)
Out[8]: (['8.8.4.4'], ['8.8.4.2', '8.8.4.6', '8.8.4.1', '8.8.4.3', '8.8.4.5'])


'''


import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

from task_2_1 import IPv4Network


class PingNetwork:
    def __init__(self, ipv4network, workers=4):
        self._ipv4network = ipv4network

        ips = self._ipv4network.hosts()

        self._reachable = []
        self._unreachable = []
        self._reachable_unassigned = []
        self._unreachable_unassigned = []

        with ThreadPoolExecutor(max_workers=workers) as executor:
            result = executor.map(self._ping, ips)
            temp = list(zip(ips, result))

            for item in temp:
                if item[1] == 0:
                    self._reachable_unassigned.append(item[0])
                    if item[0] in self._ipv4network.allocated:
                        self._reachable.append(item[0])

                elif item[1] != 0:
                    self._unreachable_unassigned.append(item[0])
                    if item[0] in self._ipv4network.allocated:
                        self._unreachable.append(item[0])

    def __call__(self, include_unassigned=False):
        if include_unassigned:
            return (self._reachable_unassigned, self._unreachable_unassigned)
        else:
            return (self._reachable, self._unreachable)

    def _ping(self, ip):
        ping = subprocess.run(f'ping -c 3 {ip}', stdout=subprocess.DEVNULL, shell=True)
        return ping.returncode


if __name__ == "__main__":
    net1 = IPv4Network('8.8.4.0/29')

    net1.allocate('8.8.4.2')
    net1.allocate('8.8.4.4')
    net1.allocate('8.8.4.6')
    print(net1.allocated)
    print(net1.hosts())

    ping_net = PingNetwork(net1)
    print(ping_net())
    print(ping_net(include_unassigned=True))

    del net1