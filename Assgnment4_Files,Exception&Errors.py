try:
    with open('sample.txt','rt') as file:
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        print(line1)
        print(line2)
        print(line3)

except FileNotFoundError as errormsg:
    print(errormsg)
