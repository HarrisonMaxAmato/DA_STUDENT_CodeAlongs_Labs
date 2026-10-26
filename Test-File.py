









from itertools import count


with open("Users/Marcy_Student/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/rec_center_signups.txt") as f:
    signups = [line for line in f.read().splitlines()
               if line and not line.startswith("#")]

def total_sessions(records):
    # TODO: add up the sessions column across every record in `records`
    # TODO: hand the total back to whoever called this. Do not print it.
    pass

swim_only = []
for signup in signups:
    class_name = signup.split(",")[1]
    if class_name == "Swim":
        swim_only.append(signup)

print("every class:", total_sessions(signups))
print("swim only:  ", total_sessions(swim_only))





















def count_long_bookings(records, minimum):
    count = 0
    for record in records:
        if int(record.split(",")[2]) >= minimum:
            count += 1
    return count

def show_long_bookings(records, minimum):
    # TODO: print a sentence with the same count in it. Only print.
    count = count_long_bookings(records, minimum)
    print(f"There are {count} long bookings with a minimum of {minimum} sessions.")

print("returned:", count_long_bookings(signups, 4))
print("returned:", count_long_bookings(signups, 2))

handed_back = show_long_bookings(signups, 4)
print("what show_long_bookings handed back:", handed_back)