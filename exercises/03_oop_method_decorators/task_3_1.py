# -*- coding: utf-8 -*-
'''
Задание 3.1

Скопировать класс IPv4Network из задания 1.1.
Переделать класс таким образом, чтобы методы hosts и unassigned
стали переменными, но при этом значение переменной экземпляра вычислялось
каждый раз при обращении и запись переменной была запрещена.


Пример создания экземпляра класса:
In [1]: net1 = IPv4Network('8.8.4.0/29')

In [2]: net1.hosts
Out[2]: ('8.8.4.1', '8.8.4.2', '8.8.4.3', '8.8.4.4', '8.8.4.5', '8.8.4.6')

In [3]: net1.allocate('8.8.4.2')

In [4]: net1.allocate('8.8.4.3')

In [5]: net1.unassigned
Out[5]: ('8.8.4.1', '8.8.4.4', '8.8.4.5', '8.8.4.6')

Запись переменной:

In [6]: net1.unassigned = 'test'
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-c98e898835e1> in <module>
----> 1 net1.unassigned = 'test'

AttributeError: can't set attribute

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


if __name__ == '__main__':
    net1 = IPv4Network('10.1.1.0/29')

    print('net1')
    print(net1.address)
    print(net1.hosts)
    print(net1.broadcast)

    print(net1.allocated)
    net1.allocate('10.1.1.4')
    net1.allocate('10.1.1.6')
    print(net1.allocated)

    print(net1.unassigned)
    #net1.unassigned = 'test'

    del net1