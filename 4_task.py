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
with open('calls.txt', 'r') as file:
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
with open('suspects.txt', 'r') as file_suspects:
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


def write_evidence_list(calls, suspects, lap_number):
    with open('evidence4.txt', 'a') as evidence_file:
        for call in calls:
            if call['caller'] in suspects:
                evidence_file.write(str(call) + '\n')
        evidence_file.write(str(lap_number) + ' lap\n')


calls_list = []
def iterate_suspects(list_of_initial_suspects, lap_number):
    with open('new_suspects_task4.txt', 'a') as new_suspects:
        new_suspects.write(str(lap_number) + ' lap\n')
        current_calls = []
        new_suspects_set = set()
        new_suspect_list = []
        for call in calls:
            number_recipient = call['recipient']
            if number_recipient in list_of_initial_suspects:
                new_suspect_list.append(call['caller'])
                current_calls.append(call)
        for number in new_suspect_list:
            if new_suspect_list.count(number) >= 3:
                new_suspects_set.add(number)
        for number in new_suspects_set:
            new_suspects.write(number + '\n')
        write_evidence_list(current_calls, new_suspects_set, lap_number)
        return new_suspects_set


with open('new_suspects_task4.txt', 'a') as new_suspects:
    for number in initial_suspects:
        new_suspects.write(number + '\n')

suspects_lap1 = iterate_suspects(initial_suspects, 1)
suspects_lap2 = iterate_suspects(suspects_lap1, 2)
suspects_lap3 = iterate_suspects(suspects_lap2, 3)
suspects_lap4 = iterate_suspects(suspects_lap3, 4)
suspects_lap5 = iterate_suspects(suspects_lap4, 5)