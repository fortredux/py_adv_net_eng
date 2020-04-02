# -*- coding: utf-8 -*-
'''
Задание 3.1a

Скопировать класс IPv4Network из задания 3.1.
Добавить метод from_tuple, который позволяет создать экземпляр класса IPv4Network
из кортежа вида ('10.1.1.0', 29).

Пример создания экземпляра класса:

In [3]: net2 = IPv4Network.from_tuple(('10.1.1.0', 29))

In [4]: net2
Out[4]: IPv4Network(10.1.1.0/29)

'''


import ipaddress


class IPv4Network:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self._hosts = [str(host) for host in subnet.hosts()]
        self.address = str(subnet.network_address)
        self.mask = int(subnet.prefixlen)
        self.broadcast = str(subnet.broadcast_address)
        self.allocated = ()

    @property
    def hosts(self):
        return tuple(self._hosts)

    def allocate(self, ip):
        if ip in self._hosts:
            allocated = [i for i in self.allocated]
            allocated.append(ip)
            self.allocated = tuple(allocated)

    @property
    def unassigned(self):
        return tuple(set(self._hosts) - set(self.allocated))

    @classmethod
    def from_tuple(cls, ip_and_mask):
        ip, mask = ip_and_mask
        return cls(f'{ip}/{mask}')


if __name__ == '__main__':
    net2 = IPv4Network.from_tuple(('10.1.1.0', 29))
    print(net2.unassigned)
    del net2