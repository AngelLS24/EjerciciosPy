file = open("/home/angel/pass.txt", "w")

max = 9999999

for n in range(max):
    cad = str(n)
    long = len(cad)
    if long < 7:
        num = ""
        ran = 7 - long
        for r in range(ran):
            num += "0"
        num += cad
        file.write(num + '\n')
    else:
        file.write(cad + '\n')

file.close()