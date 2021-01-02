card_pk = 9033205
door_pk = 9281649

found_card, found_door = False, False
i = 1
value = 1
subject = 7
door_loop, card_loop = None, None
while True:
    value *= subject
    value %= 20201227
    if value  == card_pk:
        card_loop = i
        found_card = True
    if value == door_pk:
        door_loop = i
        found_door = True
    if found_door and found_card:
        break
    i += 1

def trans(subject, l_size):
    value = 1
    for _ in range(l_size):
        value *= subject
        value %= 20201227
    return value

print("encryption key=", trans(door_pk, card_loop))
print("encryption key=", trans(card_pk, door_loop))
