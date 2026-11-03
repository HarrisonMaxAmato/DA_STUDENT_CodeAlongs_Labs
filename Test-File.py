









from itertools import count


with open("/Users/Marcy_Student/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/build-it-once/rec_center_signups.txt") as f:
    signups = [line for line in f.read().splitlines()
               if line and not line.startswith("#")]

def total_sessions(records):
    total = 0
    for record in records:
        total += int(record.split(",")[2])
    return total
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











def count_long_shifts(hours):
    count = 0
    for hour in hours:
        if hour >=4:
            count += 1
    return count
print(count_long_shifts([3,4,6,2,5]))






def count_reaching_outside(records):
    count = 0
    for record in records:
        if int(record.split(",")[2]) >= sessions_cutoff:
            count += 1
    return count


def sessions_in(record):
    pass


def signups_for(records, member):
    pass

def total_for(records, member):
    # This one should get its work done by calling the other two.
    pass

# TODO: an empty list
total_for([], "anyone")
# TODO: a list holding exactly one record
total_for([signups[0]], "Nia")
# TODO: a member name that is not in the file at all
total_for(signups, "Marco")
# TODO: a name that differs from a real member's only by capitalization
total_for(signups, "nia")
# TODO: then: do the per-member totals add up to the whole-file total?
members = ["Nia", "Omar", "Tess", "Rafi", "Gwen"]
total_sum = sum(total_for(signups, member) for member in members)
print("per-member totals add up to:", total_sum)
print("whole-file total is:", total_sessions(signups))