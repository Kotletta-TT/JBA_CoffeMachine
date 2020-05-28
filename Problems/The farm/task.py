CHIKEN_PRICE = 23
GOAT_PRICE = 678
PIG_PRICE = 1296
COW_PRICE = 3848
SHEEP_PRICE = 6769

user_money = int(input())

if user_money < CHIKEN_PRICE:
    print("None")

if user_money >= SHEEP_PRICE:
    print(f"{user_money // SHEEP_PRICE} sheep")
elif user_money >= COW_PRICE:
    print(f"{user_money // COW_PRICE} cow")
elif user_money >= PIG_PRICE:
    if user_money // PIG_PRICE > 1:
        print(f"{user_money // PIG_PRICE} pigs")
    else:
        print(f"{user_money // PIG_PRICE} pig")
elif user_money >= GOAT_PRICE:
    if user_money // GOAT_PRICE > 1:
        print(f"{user_money // GOAT_PRICE} goats")
    else:
        print(f"{user_money // GOAT_PRICE} goat")
elif user_money >= CHIKEN_PRICE:
    if user_money // CHIKEN_PRICE > 1:
        print(f"{user_money // CHIKEN_PRICE} chickens")
    else:
        print(f"{user_money // CHIKEN_PRICE} chicken")
