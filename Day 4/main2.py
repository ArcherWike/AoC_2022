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
    if int(dane['first'][1]) <  int(dane['second'][0]) or int(dane['second'][1]) < int(dane['first'][0]):
        pass
    else:
        result += 1
print(result)