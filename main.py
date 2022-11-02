from sys import argv, exit
from copy import deepcopy


def read_from_csv(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split(",")
            f_row = []
            for i in row:
                # removing white space
                f_row.append(i.strip())
            data.append(f_row)
        file.close()
    return data


def write_to_csv(arr, filename):
    data = ""
    for line in arr:
        row = ", ".join(line)
        data += row + "\n"

    with open(filename, 'w') as file:
        file.write(data)


def subject_analyze(arr):
    compulsory = []
    optional = []
    for sub in arr:
        if sub[1] == "c":
            compulsory.append(sub)
        elif sub[1] == "o":
            optional.append(sub)
    return compulsory, optional


# backtracking algorithm implementation
def backtracking_algo(result, slots, depth):
    global sub_data, rooms
    n = len(result)

    if depth == n:
        return True

    sub, sub_type, available_time_slot = sub_data[depth][0], sub_data[depth][1], sub_data[depth][2:]
    # optional
    if sub_type == 'o':
        for slot in available_time_slot:
            if type(slots[slot]) == list:
                _rooms = slots[slot]
                t_copy = deepcopy(_rooms)
                if len(_rooms) == len(rooms):
                    continue

                _rooms.append(rooms[len(_rooms)])
                result[depth], slots[slot] = [
                    sub, slot, _rooms[-1]], slots[slot]

                if backtracking_algo(result, slots, depth+1):
                    return True

                else:
                    slots[slot] = t_copy
                    result[depth] = [sub, False, False]

            elif not slots[slot]:
                t1 = [sub, slot, rooms[0]]
                result[depth], slots[slot] = t1, [rooms[0]]
                if backtracking_algo(result, slots, depth+1):
                    return True
                else:
                    slots[slot] = False
                    t2 = [sub, False, False]
                    result[depth] = t2
        else:
            return False
    # compulsory
    elif sub_type == "c":
        for slot in available_time_slot:
            if not slots[slot]:
                result[depth], slots[slot] = [sub, slot, rooms[0]], rooms[0]
                if backtracking_algo(result, slots, depth+1):
                    return True
                else:
                    slots[slot] = False
                    result[depth] = [sub, False, False]
        else:
            return False


if __name__ == "__main__":
    try:
        # input_file, output_file = argv[1], argv[2]
        input_file, output_file = "Input.csv", "Output.csv"
        sub_data = read_from_csv(input_file)
        rooms = sub_data.pop()
        time_slots = {}
        result = []

        for sub in sub_data:
            for slot in sub[2:]:
                if slot != '' and slot not in time_slots:
                    time_slots[slot] = False
            result.append([sub[0], False, False])
        backtracking_algo(result, time_slots, 0)
        write_to_csv(result, output_file)

    except IndexError:
        print("Invalid input!")
        exit(1)
