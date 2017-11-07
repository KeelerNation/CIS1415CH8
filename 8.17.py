def output_roster():
    print('ROSTER')
    for key in sorted(stats):
        print('Jersey number: %d, Rating: %d' % (key, stats[key]))
    print('')
    return

def add_new_player():
    jersey_number = int(input("Enter a new player's jersey number:\n"))
    player_rating = int(input("Enter the player's rating:\n"))
    stats.update({jersey_number: player_rating})
    return

def delete_player():
    jersey_number = int(input("Enter a jersey number:\n"))
    stats.pop(jersey_number)
    return

def new_rating():
    jersey_number = int(input("Enter a jersey number:\n"))
    new_rating = int(input("Enter a new rating for player:\n"))
    stats.pop(jersey_number)
    stats.update({jersey_number: new_rating})
    return

def rating_above():
    rating = int(input('Enter a rating:\n'))
    print('ABOVE',rating)
    jersey = stats.items()
    for key, values in stats.items():
        if values > rating:
            print('Jersey number: %d, Rating: %d' % (key, values))
    print('')
    return

def print_menu():
    menuOp = ' '
    menuOp = input("MENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n\nChoose an option:\n")
    if menuOp == 'q':
        exit()
    elif menuOp == 'a':
        add_new_player()
        print_menu()
    elif menuOp == 'd':
        delete_player()
        print_menu()
    elif menuOp == 'u':
        new_rating()
        print_menu()
    elif menuOp == 'r':
         rating_above()
         print_menu()
    elif menuOp == 'o':
        output_roster()
        print_menu()
    else:
        print_menu()
    return



count = 1
stats = {}

while count <= 5:
    stat1 = int(input('Enter player %d\'s jersey number:\n' % count))
    stat2 = int(input('Enter player %d\'s rating:\n' % count))
    while stat2 > 9:
        stat2 = int(input('Enter player %d\'s rating:\n' % count))
    print('')
    stats.update({stat1:stat2})

    count += 1




print('ROSTER')

for key in sorted(stats):
    print('Jersey number: %d, Rating: %d' % (key, stats[key]))

print('')

print_menu()


