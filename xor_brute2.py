
# 4e



def decode(data):
    value=""
    str_final=""
    print data
    data = data.split()

    search = ["Pas", "pas"]

    for i in search:
        one = ord(i[0])
        two = ord(i[1])
        three = ord(i[2])
        print "Search for ", i,"\n"

        for i in range(0,len(data)-1):
            #This is value xor value subtract value (decode)
            for x in range (0,127):
                for y in range (0,127):
                    if ((int(data[i],16) ^ x) - y) == one:
                        if ((int(data[i+1],16) ^ x) - y) == two:
                            if ((int(data[i+2],16) ^ x) - y) == three:
                                for z in data:
                                    if ((int(z,16) ^ x) - y) > 0:
                                        str_final+=(chr((int(z,16) ^ x) - y))
                                print "Found " + hex(x) + " and " + hex(y) + " that equals: " + str_final
                                str_final = ""
        print "Done with xor subtract; moving to next\n"

        for i in range(0,len(data)-1):
            #This is value xor value add value (decode)
            for x in range (0,127):
                for y in range (0,127):
                    if ((int(data[i],16) ^ x) + y) == one:
                        if ((int(data[i+1],16) ^ x) + y) == two:
                           if ((int(data[i+2],16) ^ x) + y) == two:
                                for z in data:
                                    if ((int(z,16) ^ x) + y) > 0:
                                        str_final+=(chr((int(z,16) ^ x) + y))
                                print "Found " + hex(x) + " and " + hex(y) + " that equals: " + str_final
                                str_final = ""
        print "Done with xor addition; ending\n"

  


def encode(data):
    enc_final = ""

    type1 = input("1 = Single xor or 2 = Add/Sub xor? ")

    if type1 == 1:
        xor1 = input("Enter xor value (decimal): ")
        for i in data:
            enc_final += hex(ord(i) ^ xor1)
        print enc_final.replace("0x", " ")

    if type1 == 2:
        xor1 = input("Enter 1st xor value (decimal): ")
        xor2 = input("Enter 2nd xor value (decimal): ")
        for i in data:
            enc_final += hex(((ord(i) + xor1) ^ xor2))
        print enc_final.replace("0x", " ")

def tester(data):
    for i in data:
        print i
        print hex((ord(i) ^ 36)-103)


def main():
    data = "Htuo<qyoo}{y<uo<zsn<X}yx}pio<_snlsn}husr<srpe2<Sin<~piylnurho<zsn<hty<_e~sn{<}ny<lnshyhyx<kuht<}<l}ooksnx2<Ht}h<l}ooksnx<uo</$,y}xz,~}~~/~z~}}*%zx.y$y}yx"
    #data = "43 de 4b 43 43 4d 43 43 43 9e e8 fd f9 f4 ee e8 a3 93 ec ee f6 a3 bf"
    #data = "77 41 56 52 4d 47 41 4 74 45 47 4f 4 10"
    #data = "10 26 31 35 2a 20 26 63 13 22 20 28 63 77"
    
    #encode(data)
    #tester()
    #decode(data)

    choice = ""

    while choice != 0:

        print "\n"
        print "XOR Brute Forcer v1"
        print "1 - Encode"
        print "2 - Test"
        print "3 - Decode"
        print "0 - Exit"

        choice = input("Please enter a number: ")

        if choice == 1:
            encode(data)
        elif choice == 2:
            tester(data)
        elif choice == 3:
            decode(data)

main()
