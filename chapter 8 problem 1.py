def data_entrie():
    global months
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    global data
    data = []

    count = 0
    while count < 12:
        rainfalls = int(input('Enter total number of rainfalls for %s.\n' % months[count]))
        data.append(rainfalls)
        count += 1

    return data

def statistics_rainfall():
    print('Total rainfall: %d\n' % sum(data))
    average = sum(data)/12
    print('Average monthly rainfall: %d\n' % average)
    dictionary = dict(zip(months, data))
    value = list(dictionary.values())
    key = list(dictionary.keys())
    print("Highest amount of rainfall was in %s.\n" % key[value.index(max(value))])
    print("Lowest amount of rainfall was in %s." % key[value.index(min(value))])
    return


data_entrie()
statistics_rainfall()

