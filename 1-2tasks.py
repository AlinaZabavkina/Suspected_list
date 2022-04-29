incorrect_symbols = ['+', '-', '.', ')', '(']


def normalize_number(call):
    """Removes incorrect symbols from numbers and limits numbers length by 10 symbols"""
    for symbol in incorrect_symbols:
        call['caller'] = call['caller'].replace(symbol, '')
        call['recipient'] = call['recipient'].replace(symbol, '')
    if 'x' in call['caller']:
        split_list = call['caller'].split('x')
        call['caller'] = split_list[0]
    if len(call['caller']) > 10:
        call['caller'] = call['caller'][-10:]

    if 'x' in call['recipient']:
        split_list = call['recipient'].split('x')
        call['recipient'] = split_list[0]
    if len(call['recipient']) > 10:
        call['recipient'] = call['recipient'][-10:]
    return call

calls = []
with open('C:/Users/Acer/Desktop/calls.txt', 'r') as file:
    for line in file:
        line = line.split('|')
        current_call = {}
        for i in line:
            i = i.replace('\n', '')
            k, v = i.split(':')
            current_call[k] = v
        if int(current_call['duration_s']) > 120:
            current_call = normalize_number(current_call)
            calls.append(current_call)
print(*calls, sep='\n')
print(len(calls))

initial_suspects = []
with open('C:/Users/Acer/Desktop/suspects.txt', 'r') as file_suspects:
    for line in file_suspects:
        line = line.replace('\n', '')
        for symbol in incorrect_symbols:
            line = line.replace(symbol, '')
        if 'x' in line:
            line = line.split('x')[0]
        if len(line) > 10:
            line = line[-10:]
        initial_suspects.append(line)
print(initial_suspects)


with open('new_suspects.txt', 'w') as new_suspects:
    for number in initial_suspects:
        new_suspects.write(number + '\n')
    new_suspects.write('----------' + '\n')
    new_suspects_set = set()
    for call in calls:
        number_recipient = call['recipient']
        if number_recipient in initial_suspects:
            new_suspects_set.add(call['caller'])
    for number in new_suspects_set:
        new_suspects.write(number + '\n')
