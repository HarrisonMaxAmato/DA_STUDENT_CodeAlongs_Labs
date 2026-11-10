#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "/Users/Marcy_Student/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/validate-catch-keep-going/service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason
# TODO: assign `EXPECTED_FIELDS` to 5
# TODO: assign `ALLOWED_STATUS` to ["Open", "In Progress", "Closed"]
EXPECTED_FIELDS = 5
ALLOWED_STATUS = ["Open", "In Progress", "Closed"]

def validate_request(row):
    fields = row.split(",")
    # TODO: assign `fields` to `row` split on commas
    if len(fields) != EXPECTED_FIELDS:
        return False, "wrong number of fields: " + str(len(fields))
    # TODO: unpack `fields` into the five names in the CSV header
    request_id, request_type, borough, days_open, status = fields
    # TODO: if `borough` is empty, return False and "borough is empty"
    if borough == "":
        return False, "borough is empty"
    # TODO: if `status` is not in ALLOWED_STATUS, return False and a reason
    if status not in ALLOWED_STATUS:
        return False, "status not allowed " + status
    # TODO: make that reason "status not allowed: " plus `status`
    
    
    return True, "ok"
    # TODO: return True and "ok"
    for row in rows:
        ok, reason = validate_request(row)
        if not ok:
            print(row.split(",")[0], "REJECTED -", reason)
        else:
            print(row.split(",")[0], "ACCEPTED -", reason)



    for row in rows:
        ok, reason = validate_request(row)
        if not ok:
            print(row.split(",")[0], "REJECTED -", reason)
        else:
            print(row.split(",")[0], "ACCEPTED -", reason)
    
print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# # Step 1, answer 1:
# # what is in the file is a single string, and the function is expecting a row of data that has been split into fields. The function is trying to unpack the string into five variables, but since it is not split, it raises a ValueError because there are not enough values to unpack.
# # Step 1, answer 2:
# # The caller takes two returned values apart in one line through the comma. The function is really handing back a single tuple that contains two values, which is the boolean and the string.

for row in rows:
    ok, reason = validate_request(row)
    if not ok:
        print(row.split(",")[0], "REJECTED -",)
    
# # Step 2: Run All 15 Rows Through the Validator and Report Each Rejection
# # TODO: assign `valid` to 0
# # TODO: loop over `rows`; unpack validate_request(row) into ok, reason
# # TODO: if `ok`, add 1 to `valid`
# # TODO: else print row.split(",")[0], "REJECTED -" and `reason`

# print("header:", header)
# print("rows read:", len(rows))
# print("passed Day 1 validation:", valid)

# # Step 2, answer 1:
# # SR-1004 has no borough, SR-1009 has the status escalated and SR-1011 is
# # missing a field. 
# # Step 2, answer 2:
# #


# # ===== Day 2 =====

# # Step 3: Build the Days-Open Report With No Protection and Watch It Crash
# # TODO: assign `total_days` and `counted` to 0
# # TODO: loop over `rows`; `continue` past any row validate_request() rejects
# # TODO: assign `days_open` to int() of the row's fourth field
# # TODO: add `days_open` to `total_days` and 1 to `counted`
# # TODO: print the row's ID, "days open:" and `days_open`
# # TODO: after your answers, comment out this step so Step 4 can run
total_days = 0
counted = 0
for row in rows:
    ok, reason = validate_request(row)
    if not ok:
        continue
    days_open = int(row.split(",")[3])
    total_days += days_open
    counted += 1
    print(row.split(",")[0], "days open:", days_open)
# # Step 3, answer 1:
# # 5 report lines print before it crashes. SR-1007 stops it.
# # Step 3, answer 2:
# # ValueError: invalid literal for int() with base 10: '3 days'
# 5 rows were counted before the crash.
# # Step 3, answer 3:
# # SR-1008 through SR-1015 are never reached, so they aren't checked or counted, and the average never prints.


# # Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    try:
        days = int(value)   
    except ValueError:
        return False, "days_open is not a number: " + value
    if days < 0:   
        return False, "days_open is negative: " + value
    return True, "ok"
#     # TODO: in a try, assign `days` to int(value)
#     # TODO: in except ValueError, return False and a reason
#     # TODO: make that reason "days_open is not a number: " plus `value`
#     # TODO: if `days` is below 0, return False and a reason
#     # TODO: make that reason "days_open is negative: " plus `value`
#     # TODO: return True and "ok"
#     pass


# # TODO: assign `total_days`, `counted` and `skipped` to 0
# # TODO: loop over `rows`; unpack validate_request(row) into ok, reason
# # TODO: if ok, unpack check_days_open() of the fourth field into ok, reason
# # TODO: if still ok, add the days to `total_days` and 1 to `counted`
# # TODO: else add 1 to `skipped`; print the ID, "SKIPPED -" and `reason`
def check_days_open(value):
    try:
        days = int(value)
    except ValueError:
        return False, "days_open is not a number: " + value
    if days < 0:
        return False, "days_open is negative: " + value
    return True, "ok"
# print("counted:", counted, "| skipped:", skipped)
# print("average days open:", round(total_days / counted, 1))

# # Step 4, answer 1:
# #5 rows get skipped: SR-1004, SR-1007, SR-1009, SR-1011, and SR-1013. The Day 1
# # validator let SR-1007 and SR-1013 through.
# # Step 4, answer 2:
# #A try caught "3 days" because int() raises ValueError on it. An if could also
# catch it by checking the text first. An if caught -3. A try alone could not,
# because int("-3") works and raises no error.
# # Step 4, answer 3:
# # Yes. 10 counted + 5 skipped = 15 rows.
