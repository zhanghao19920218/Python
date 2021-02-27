guests = ['taylor', 'emma', 'bieber', 'tom', 'john']

cannot_guest = guests[2]
print(f"{cannot_guest} can not come in")
guests[2] = 'brain'
print(f"{guests[2]} will come instead")

for guest in guests:
    print(f"Hello {guest.title()}, I invite you to my party!")

print("------- I  FOUND A BIGGER TABLE ---------")
guests.insert(0, 'amy')
guests.insert(3, 'justin')
guests.append('james')
for guest in guests:
    print(f"Hello {guest.title()}, I invite you to my party!")

print('---------------------- I can only invite 2 -------------')
while len(guests) > 2:
    username = guests.pop()
    print(f"Sorry, {username}, I cannot invite you")

for guest in guests:
    print(f"Hello {guest.title()}, I invite you to my party!")

del guests[0]
del guests[0]
print(guests)