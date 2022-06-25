# Notas sobre Python

Dicas: Explicito é melhor do que Implicito

Exemplos:

Python é uma linguagem fortemente tipada, ou seja você tem que explicitar o tipo da variável na hora de uma conversão.

~~~python
>>> str(20) + 'batatinhas'
'20 batatinhas'
~~~

Python é orientado a objetos, ou seja os dados que são repassados para o python possuem metódos, eles não são simples dados, você consegue modificar os modificar.

~~~python
>>> 'batatatinha'.upper()
'BATATINHA'
~~~

Python possui atribuição multipla, ou seja, em outras linguagens, se eu obtivesse dois valores e quisesse inverter os valores das variáveis, eu teria que criar uma nova variável para isso, porém em python, eu não preciso disto.

~~~python
a = 3
b = 'batatinha'

a, b = b, a
~~~
~~~python
>>> a
'batatinha'

>>> b
3
~~~

~~~python
# Estou separando os valore por uma barra
>>> d, m, y = '25/6/2022'.split('/')

>>> d
25
>>> m
6
>>> y
2022
~~~

