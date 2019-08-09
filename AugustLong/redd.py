def flip(number):
    order, next_card_higher = [], False
    for index, num in enumerate(number):
        print(order, next_card_higher, index, num)
        order.append(index) if next_card_higher else order.insert(0, index)
        next_card_higher ^= num=="1"
    return "WIN" if next_card_higher else "LOSE"


print(flip("1001"))