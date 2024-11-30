readFile = open('input.txt','r')
result = 0

def Get_Range(line):
    line = line.split(",")
    a = line[0].split("-")
    b = line[1].split("-")
    Elves = {"first": a,
             "second": b}
    return Elves

for line in readFile:
    dane = (Get_Range(line.rstrip()))
    if int(dane['first'][0]) <= int(dane['second'][0]) and int(dane['second'][1]) <= int(dane['first'][1]):
        result+=1
    elif int(dane['first'][0]) >= int(dane['second'][0]) and int(dane['second'][1]) >= int(dane['first'][1]):
        result += 1
print(result)