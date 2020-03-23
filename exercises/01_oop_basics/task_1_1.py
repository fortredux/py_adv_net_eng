# -*- coding: utf-8 -*-
'''
Задание 1.1

Создать класс IPv4Network, который представляет сеть.
При создании экземпляра класса, как аргумент передается строка с адресом сети.

Пример создания экземпляра класса:

In [3]: net1 = IPv4Network('10.1.1.0/29')

После этого, должны быть доступны переменные address и mask:
In [5]: net1.address
Out[5]: '10.1.1.0'

In [6]: net1.mask
Out[6]: 29


Broadcast адрес должен быть записан в атрибуте broadcast:

In [7]: net1.broadcast
Out[7]: '10.1.1.7'

Также должен быть создан атрибут allocated в котором будет
храниться кортеж с адресами, которые назначены на каком-то
устройстве/хосте. Изначально атрибут равен пустому кортежу:

In [8]: print(net1.allocated)
()


Метод hosts должен возвращать кортеж IP-адресов, которые входят в сеть,
не включая адрес сети и broadcast:

In [9]: net1.hosts()
Out[9]: ('10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5', '10.1.1.6')

Метод allocate ожидает как аргумент IP-адрес. Указанный адрес
должен быть записан в кортеж в атрибуте net1.allocated:

In [10]: net1 = IPv4Network('10.1.1.0/29')

In [11]: print(net1.allocated)
()

In [12]: net1.allocate('10.1.1.6')

In [13]: net1.allocate('10.1.1.3')

In [14]: print(net1.allocated)
('10.1.1.6', '10.1.1.3')


Метод unassigned возвращает возвращает кортеж со свободными адресами:

In [15]: net1 = IPv4Network('10.1.1.0/29')

In [16]: net1.allocate('10.1.1.4')
    ...: net1.allocate('10.1.1.6')
    ...:

In [17]: net1.unassigned()
Out[17]: ('10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.5')

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


if __name__ == '__main__':
    net1 = IPv4Network('10.1.1.0/29')
    net2 = IPv4Network('100.7.1.0/26')

    print('net1')
    print(net1.address)
    print(net1.hosts())
    print(net1.broadcast)

    print(net1.allocated)
    net1.allocate('10.1.1.4')
    net1.allocate('10.1.1.6')
    print(net1.allocated)

    print(net1.unassigned())

    print('\nnet2')
    print(len(net2.hosts()))
    print(net2.broadcast)

    del net1