from model.classes import Call, PhoneNumber


def write_evidence_list(calls, suspects, lap_number):
    with open('evidence4.txt', 'a') as evidence_file:
        for call in calls:
            if call.suspected.number.number in suspects:
                evidence_file.write(str(call) + '\n')
        evidence_file.write(str(lap_number) + ' lap\n')


def check_count(number, new_suspect_list):
    count = 0
    for suspect in new_suspect_list:
        if suspect.number == number.number:
            count += 1
            if count >= 3:
                return True
    return False


def iterate_suspects(list_of_initial_suspects, lap_number):
    with open('new_suspects_task4.txt', 'a') as new_suspects:
        new_suspects.write(str(lap_number) + ' lap\n')
        current_calls = []
        new_suspects_set = set()
        new_suspect_list = []
        for call in long_calls:
            number_recipient = call.recipient.number
            if number_recipient in list_of_initial_suspects:
                call.suspected.level = lap_number
                new_suspect_list.append(call.suspected.number)
                current_calls.append(call)
        for number in new_suspect_list:
            if check_count(number, new_suspect_list):
                new_suspects_set.add(number.number)
        for number in new_suspects_set:
            new_suspects.write(number + '\n')
        write_evidence_list(current_calls, new_suspects_set, lap_number)
        return new_suspects_set


long_calls = []
with open('calls.txt', 'r') as file:
    for line in file:
        call = Call.parse_line_to_call(line)
        if call.duration > 120:
            long_calls.append(call)


initial_suspects = []
with open('suspects.txt', 'r') as file_suspects:
    for line in file_suspects:
        line = line.replace('\n', '')
        suspected_number = PhoneNumber(line).normalize()
        initial_suspects.append(suspected_number)

with open('new_suspects_task4.txt', 'a') as new_suspects:
    for number in initial_suspects:
        new_suspects.write(number + '\n')

suspects_lap1 = iterate_suspects(initial_suspects, 1)
suspects_lap2 = iterate_suspects(suspects_lap1, 2)
suspects_lap3 = iterate_suspects(suspects_lap2, 3)
suspects_lap4 = iterate_suspects(suspects_lap3, 4)
suspects_lap5 = iterate_suspects(suspects_lap4, 5)
 