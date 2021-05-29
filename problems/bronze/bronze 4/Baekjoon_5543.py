# https://www.acmicpc.net/problem/5543

# answer

SangDuck_Burger_price = int(input())
JungDuck_Burger_price = int(input())
HaDuck_Burger_price = int(input())
Coke_price = int(input())
Sprite_price = int(input())

Burger_list = [SangDuck_Burger_price, JungDuck_Burger_price, HaDuck_Burger_price]
Beverage_list = [Coke_price, Sprite_price]

price = min(Burger_list) + min(Beverage_list) - 50
print(price)