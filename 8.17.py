
count = 1
stats = {}

num = []
rat = []
while count <= 5:
    stat1 = int(input('Enter player %d\'s jersey number:\n' % count))
    stat2 = int(input('Enter player %d\'s rating:\n' % count))
    stats.update({stat1:stat2})

    num.append(stat1)
    rat.append(stat2)

    count += 1






Print('ROSTER')
roster1 = num.sort()

