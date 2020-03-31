# -*- coding: utf-8 -*-
'''
Задание 2.1

Скопировать класс IPv4Network из задания 1.1 и добавить ему все методы,
которые необходимы для реализации протокола последовательности (sequence):
* __getitem__, __len__, __contains__, __iter__
* index, count - должны работать аналогично методам в списках и кортежах

И оба метода, которые отвечают за строковое представление экземпляров
класса IPv4Network.

Существующие методы и атрибуты (из задания 1.1) можно менять, при необходимости.

Пример создания экземпляра класса:

In [2]: net1 = IPv4Network('8.8.4.0/29')

Проверка методов:

In [3]: for ip in net1:
   ...:     print(ip)
   ...:
8.8.4.1
8.8.4.2
8.8.4.3
8.8.4.4
8.8.4.5
8.8.4.6

In [4]: net1[2]
Out[4]: '8.8.4.3'

In [5]: net1[-1]
Out[5]: '8.8.4.6'

In [6]: net1[1:4]
Out[6]: ('8.8.4.2', '8.8.4.3', '8.8.4.4')

In [7]: '8.8.4.4' in net1
Out[7]: True

In [8]: net1.index('8.8.4.4')
Out[8]: 3

In [9]: net1.count('8.8.4.4')
Out[9]: 1

In [10]: len(net1)
Out[10]: 6

Строковое представление:

In [13]: net1
Out[13]: IPv4Network(8.8.4.0/29)

In [14]: str(net1)
Out[14]: 'IPv4Network 8.8.4.0/29'

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

    def hosts(self):
        return tuple(self._hosts)

    def allocate(self, ip):
        if ip in self._hosts:
            allocated = [i for i in self.allocated]
            allocated.append(ip)
            self.allocated = tuple(allocated)

    def unassigned(self):
        return tuple(set(self._hosts) - set(self.allocated))

    def __len__(self):
        return len(self._hosts)

    def __iter__(self):
        return iter(self._hosts)

    def __getitem__(self, index):
        #print(type(index))
        if isinstance(index, slice):
            return tuple(self._hosts[index])
        elif isinstance(index, int):
            return self._hosts[index]

    def __contains__(self, item):
        return item in self._hosts

    def index(self, ip):
        return self._hosts.index(ip)

    def count(self, ip):
        return self._hosts.count(ip)


if __name__ == '__main__':
    net1 = IPv4Network('10.1.1.0/29')

    print(net1.allocated)
    net1.allocate('10.1.1.4')
    net1.allocate('10.1.1.6')
    print(net1.allocated)
    print(net1.unassigned())

    print(len(net1))

    for ip in net1:
        print(ip, end=" | ")
    print()

    print(net1[2])
    print(net1[-1])
    print(net1[1:4])

    print(net1.index('10.1.1.3'))
    print(net1.count('10.1.1.3'))

    del net1