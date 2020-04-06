# -*- coding: utf-8 -*-
'''
Задание 3.3

Создать класс User, который представляет пользователя.
При создании экземпляра класса, как аргумент передается строка с именем пользователя.

Пример создания экземпляра класса:

In [3]: nata = User('nata')

После этого, должна быть доступна переменная username:
In [4]: nata.username
Out[4]: 'nata'

Переменная username должна быть доступна только для чтения:

In [5]: nata.username = 'user'
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-5-eba76ef1ed86> in <module>
----> 1 nata.username = 'user'

AttributeError: can't set attribute


Также в экземпляре должа быть создана переменная password, но
пока пользователь не установил пароль, при обращении к переменной должно
генерироваться исключение ValueError:

In [6]: nata.password
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-6-7527817bf03d> in <module>
----> 1 nata.password
...
ValueError: Надо установить пароль!

При установке пароля должны выполняться проверки:

* длины пароля - минимальная разрешенная длина пароля 8 символов
* содержится ли имя пользователя в пароле

Если проверки не прошли, надо вывести сообщение об ошибке и запросить пароль еще раз:
(Эта часть задания не тестируется, но ее все равно надо реализовать!)

In [7]: nata.password = 'sadf'
Пароль слишком короткий. Введите пароль еще раз: sdlkjfksnatasdfsd
Пароль содержит имя пользователя. Введите пароль еще раз: asdfkpeorti2435
Пароль установлен

Если пароль прошел проверки, должно выводиться сообщение "Пароль установлен"

In [8]: nata.password = 'sadfsadfsadf'
Пароль установлен
'''


'''
# Написал int вместо init на стеке нашел такую же ошибку. Было: TypeError: User() takes no arguments
class User:
    def __init__(self, name):
        #self.username = self.set_name(name)
        self._name = name

    @property
    def set_name(self, name):
        return self._name
'''



class User:
    def __init__(self, name):
        self._name = name
        self._password = None

    def set_name(self, name):
        return self._name

    @property
    def username(self):
        return self._name

    @property
    def password(self):
        if not self._password:
            raise ValueError('Надо установить пароль!')
        return self._password

    @password.setter
    def password(self, value):
        while True:
            if len(value) < 8:
                value = input('Пароль слишком короткий. Введите пароль еще раз: ')
                continue
            elif self._name in value:
                value = input('Пароль содержит имя пользователя. Введите пароль еще раз: ')
                continue
            else:
                self._password = value
                print('Пароль установлен')
                break
        return self._password


if __name__ == '__main__':
    nata = User('nata')

    print(nata.username)
    #nata.username = 'user'

    #print(nata.password)
    #nata.password = 'sadf'

    nata.password = 'sadfsadfsadf'
    print(nata.password)

    del nata