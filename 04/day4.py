#!/home/rajivn/anaconda3/bin/python
import re

lines = None
with open("/home/rajivn/adventOfCode/04/input", "r") as input:
    lines = input.read().split("\n\n")
required = set(["byr","iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def parse(passport):
    p_fields = list()
    p_vals = list()
    for line in passport.split("\n"):
        fields = line.split(" ")
        for l2 in fields:
            key, val = l2.split(":")
            p_fields.append(key.strip())
            p_vals.append(val.strip())
    return p_fields, p_vals

def validbyr(val):
    val = int(val)
    return False if val < 1920 or val > 2002 else True

def validiyr(val):
    val = int(val)
    return False if val < 2010 or val > 2020 else True

def valideyr(val):
    val = int(val)
    return False if val < 2020 or val > 2030 else True

def validhgt(val):
    if val.find("cm") > 1:
        if 150 <= int(val[:val.find("cm")]) <= 193:
            return True
    elif val.find("in") > 1:
        if 59 <= int(val[:val.find("in")]) <= 76:
            return True
    return False

def validhcl(val):
    return re.match("^#[0-9 a-f]{6}$", val)

valid_ecl = set(["amb", "blu", "brn", "gry", "grn","hzl", "oth"])
def validecl(val):
    return val in valid_ecl

def validpid(val):
    return re.match("^[0-9]{9}$", val)

def validcid(val):
    return True

def isvalidp2(key, val):
    rules = {"byr": validbyr, "iyr": validiyr, "eyr": valideyr, "hgt": validhgt, "hcl":validhcl, "ecl": validecl, "pid": validpid, "cid": validcid}
    try:
        return rules[key](val)
    except:
        return False

valid_p1 = 0
valid_p2 = 0
for passport in lines:
    fields, vals = parse(passport)
    if len(required - set(fields) ) == 0:
        valid_p1 += 1
        for f, v in zip(fields, vals):
            if not isvalidp2(f, v):
                break
        else:
            valid_p2 += 1
print(valid_p1)
print(valid_p2)