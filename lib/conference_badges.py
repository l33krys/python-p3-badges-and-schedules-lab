def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    list = []
    i = 1
    while i <= len(names):
        for name in names:
            list.append(f"Hello, {name}! You'll be assigned to room {i}!")
            i += 1
    return list

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for assignment in assign_rooms(names):
        print(assignment)