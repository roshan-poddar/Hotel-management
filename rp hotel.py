def rrp():
    print("Welcome To Hotel Transylvania")
    print("""1. You want to book the room
2. You want to see the records""")
    a = input("Choose your option:")
    if a == "1":
        X = input("""please tell us your name for better communication:""")  
        def rp():
            b = input(X+" Which type of room you want:\n1.single  2.couple:")
            if "single" in b or "1" in b:
                print(X+" We have room in range 3000 to 10000")
                c = input(X+" in which range you want the room:")
                if int(c) in range(9000,10001):
                    print(X+" We have five star room,")
                    print("Which cost 10000 for one day")
                    d = input(X+" you want to book the room:")
                    if "yes"in d or "y" in d:
                        e = input(X+" For how many days you want to book the room:")
                        if int(e) in range(4,6):
                            print(X+ "For every extra day it charge 5000 extra")
                            print("and after giving 10% discount")
                            print("Your total bill become of 31500")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes?")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                   
                        elif int(e) in range(2,4):
                            print(X+" for every extra day we charge 5000 extra")
                            print("and after giving 10% discount")
                            print(" your total bill become of 22500")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        elif e == "1":
                            print(X+" After giving 10% discount")
                            print("Than your total bill become of 9000")
                            x= input(X+" you want to book the room:")
                            if "yes" in x or "y" in x:
                                y = input(X+" you want to make any changes:")
                                if "yes" in y or "y" in y:
                                    print(rp())
                                else:
                                    print (X+" your room is booked")
                                    print("enjoy your day")
                                    o = input(X+" you want to reuse:")
                                    if "yes" in o or "y" in o:
                                        print(rp())
                                    else:
                                        print(X+" Thanking you for using our program")
                                        print("goodbye")
                            else:
                                k = input(X+" you don't want to book the room:")
                                if "yes" in k or "y" in k:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    l = input(X+" you want to reuse:")
                                    if "yes" in l or "y" in l :
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        else:
                            print(X+" you can book room for only five days")
                            print("please book room carefully")
                            print(rp())            
        
                        
                        
                                        
                        
                    else:
                        j = input(X+" you want to rebook:")
                        if "yes" in j or "y" in j:
                            print(rp())
                        else:
                            print("goodbye")
                            h = input(X+" you want to reuse:")
                            if "yes" in h or "y" in h:
                                print(rp())
                            else:
                                print(X+" Thank you for using our program")
                                print("goodbye")        
                elif int(c) in range(7000,9000):
                    
                    print(X+" we have four star room")
                    print("which cost 8000 for one day")
                    d = input(X+" you want to book the room:")
                    if "yes"in d or "y" in d:
                        e = input(X+" for how many days you want to book the room:")
                        if int(e) in range(4,6):
                            print(X+" for every extra day it will charge 4000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 25200")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                   
                        elif int(e) in range(2,4):
                            print(X+" for every extra day it will charge 4000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 18000")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        elif e == "1":
                            print(X+" After giving 10% discount")
                            print(" your total bill become of 7200")
                            x= input(X+" you want to book the room:")
                            if "yes" in x or "y" in x:
                                y = input(X+" you want to make any changes:")
                                if "yes" in y or "y" in y:
                                    print(rp())
                                else:
                                    print (X+" your room is booked")
                                    print("enjoy your day")
                                    o = input(X+" you want to reuse:")
                                    if "yes" in o or "y" in o:
                                        print(rp())
                                    else:
                                        print(X+" Thanking you for using our program")
                                        print("goodbye")
                            else:
                                k = input(X+" you don't want to book the room:")
                                if "yes" in k or "y" in k:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    l = input(X+" you want to reuse:")
                                    if "yes" in l or "y" in l :
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        else:
                            print(X+" you can book room for only five days")
                            print("please book room carefully")
                            print(rp())            
        
                        
                        
                                        
                        
                    else:
                        j = input(X+" you want to rebook:")
                        if "yes" in j or "y" in j:
                            print(rp())
                        else:
                            print("goodbye")
                            h = input(X+" you want to reuse:")
                            if "yes" in h or "y" in h:
                                print(rp())
                            else:
                                print(X+" Thank you for using our program")
                                print("goodbye")        
                elif int(c) in range(5000,7000):
                    print(X+" we have Three star room")
                    print("which cost 6000 for one day")
                    d = input(X+" you want to book the room:")
                    if "yes"in d or "y" in d:
                        e = input(X+" for how many days you want to book the room:")
                        if int(e) in range(4,6):
                            print(X+" for every extra day it will charge 3000 extra")
                            print("and after giving 10% discount")
                            print(" your total bill become of 18900")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                   
                        elif int(e) in range(2,4):
                            print(X+" for every extra day it will charge 3000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 13500")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        elif e == "1":
                            print(X+" After giving 10% discount")
                            print("your total bill become of 5400")
                            x= input(X+" you want to book the room:")
                            if "yes" in x or "y" in x:
                                y = input(X+" you want to make any changes:")
                                if "yes" in y or "y" in y:
                                    print(rp())
                                else:
                                    print (X+" your room is booked")
                                    print("enjoy your day")
                                    o = input(X+" you want to reuse:")
                                    if "yes" in o or "y" in o:
                                        print(rp())
                                    else:
                                        print(X+" Thanking you for using our program")
                                        print("goodbye")
                            else:
                                k = input(X+" you don't want to book the room:")
                                if "yes" in k or "y" in k:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    l = input(X+" you want to reuse:")
                                    if "yes" in l or "y" in l :
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        else:
                            print(X+" you can book room for only five days")
                            print("please book room carefully")
                            print(rp())            
        
                        
                        
                                        
                        
                    else:
                        j = input(X+" you want to rebook:")
                        if "yes" in j or "y" in j:
                            print(rp())
                        else:
                            print("goodbye")
                            h = input(X+" you want to reuse:")
                            if "yes" in h or "y" in h:
                                print(rp())
                            else:
                                print(X+" Thank you for using our program")
                                print("goodbye")        
                elif int(c) in range(3000,5000):
                    print(X+" we have two star room")
                    print("which cost 4000 for one day")
                    d = input(X+" you want to book the room:")
                    if "yes"in d or "y" in d:
                        e = input(X+" for how many days you want to book the room:")
                        if int(e) in range(4,6):
                            print(X+" for every extra day it will charge 2000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 12600")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                   
                        elif int(e) in range(2,4):
                            print(X+" for every extra day it will charge 2000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 9000")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        elif e == "1":
                            print(X+" After giving 10% discount")
                            print(" your total bill become of 3600")
                            x= input(X+" you want to book the room:")
                            if "yes" in x or "y" in x:
                                y = input(X+" you want to make any changes:")
                                if "yes" in y or "y" in y:
                                    print(rp())
                                else:
                                    print (X+" your room is booked")
                                    print("enjoy your day")
                                    o = input(X+" you want to reuse:")
                                    if "yes" in o or "y" in o:
                                        print(rp())
                                    else:
                                        print(X+" Thanking you for using our program")
                                        print("goodbye")
                            else:
                                k = input(X+" you don't want to book the room:")
                                if "yes" in k or "y" in k:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    l = input(X+" you want to reuse:")
                                    if "yes" in l or "y" in l :
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        else:
                            print(X+" you can book room for only five days")
                            print("please book room carefully")
                            print(rp())            
        
                        
                        
                                        
                        
                    else:
                        j = input(X+" you want to rebook:")
                        if "yes" in j or "y" in j:
                            print(rp())
                        else:
                            print("goodbye")
                            h = input(X+" you want to reuse:")
                            if "yes" in h or "y" in h:
                                print(rp())
                            else:
                                print(X+"Thank you for using our program")
                                print("goodbye")        
                else:
                    print(X+" we do not have room in this range")
                    x = input("so you want to rebook:")
                    if "yes" in x or "y" in x:
                        print(rp())
                    else:
                        print("goodbye")
            elif "2" in b or "couple" in b:
                print(X+" we have room in range 15000 to 22000")
                c = input(X+" in which range you want the room:")
                if int(c) in range(21000,22001):
                    print(X+" we have five star room")
                    print("which cost 22000 for one day")
                    d = input(X+" you want to book the room:")
                    if "yes"in d or "y" in d:
                        e = input(X+" for how many days you want to book the room:")
                        if int(e) in range(4,6):
                            print(X+" for every extra day it will charge 11000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 69300")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                   
                        elif int(e) in range(2,4):
                            print(X+" for every extra day it will charge 11000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 49500")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        elif e == "1":
                            print(X+" After giving 10% discount")
                            print("your total bill become of 19800")
                            x= input(X+" you want to book the room:")
                            if "yes" in x or "y" in x:
                                y = input(X+" you want to make any changes:")
                                if "yes" in y or "y" in y:
                                    print(rp())
                                else:
                                    print (X+" your room is booked")
                                    print("enjoy your day")
                                    o = input(X+" you want to reuse:")
                                    if "yes" in o or "y" in o:
                                        print(rp())
                                    else:
                                        print(X+" Thanking you for using our program")
                                        print("goodbye")
                            else:
                                k = input(X+" you don't want to book the room:")
                                if "yes" in k or "y" in k:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    l = input(X+" you want to reuse:")
                                    if "yes" in l or "y" in l :
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        else:
                            print(X+" you can book room for only five days")
                            print("please book room carefully")
                            print(rp())            
        
                        
                        
                                        
                        
                    else:
                        j = input(X+" you want to rebook:")
                        if "yes" in j or "y" in j:
                            print(rp())
                        else:
                            print("goodbye")
                            h = input(X+" you want to reuse:")
                            if "yes" in h or "y" in h:
                                print(rp())
                            else:
                                print(X+" Thank you for using our program")
                                print("goodbye")        
                elif int(c) in range(19000,21000):
                    
                    print(X+" we have four star room")
                    print("which cost 20000 for one day")
                    d = input(X+" you want to book the room:")
                    if "yes"in d or "y" in d:
                        e = input(X+" for how many days you want to book the room:")
                        if int(e) in range(4,6):
                            print(X+" for every extra day it will charge 10000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 63000")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+"Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                   
                        elif int(e) in range(2,4):
                            print(X+" for every extra day it will charge 10000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 45000")
                            f = input(X+" so you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        elif e == "1":
                            print(X+" After giving 10% discount")
                            print("your total bill become of 18000")
                            x= input(X+" you want to book the room:")
                            if "yes" in x or "y" in x:
                                y = input(X+" you want to make any changes:")
                                if "yes" in y or "y" in y:
                                    print(rp())
                                else:
                                    print (X+" your room is booked")
                                    print("enjoy your day")
                                    o = input(X+" you want to reuse:")
                                    if "yes" in o or "y" in o:
                                        print(rp())
                                    else:
                                        print(X+" Thanking you for using our program")
                                        print("goodbye")
                            else:
                                k = input(X+" you don't want to book the room:")
                                if "yes" in k or "y" in k:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    l = input(X+" you want to reuse:")
                                    if "yes" in l or "y" in l :
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        else:
                            print(X+" you can book room for only five days")
                            print("please book room carefully")
                            print(rp())            
        
                        
                        
                                        
                        
                    else:
                        j = input(X+" you want to rebook:")
                        if "yes" in j or "y" in j:
                            print(rp())
                        else:
                            print("goodbye")
                            h = input(X+" you want to reuse:")
                            if "yes" in h or "y" in h:
                                print(rp())
                            else:
                                print(X+" Thank you for using our program")
                                print("goodbye")        
                elif int(c) in range(17000,19000):
                    print(X+" we have Three star room")
                    print("which cost 18000 for one day")
                    d = input(X+" you want to book the room:")
                    if "yes"in d or "y" in d:
                        e = input(X+" for how many days you want to book the room:")
                        if int(e) in range(4,6):
                            print(X+" for every extra day it will charge 9000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 56700")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                   
                        elif int(e) in range(2,4):
                            print(X+" for every extra day it will charge 9000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 40500")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        elif e == "1":
                            print(X+" After giving 10% discount")
                            print("your total bill become of 16200")
                            x= input(X+" you want to book the room:")
                            if "yes" in x or "y" in x:
                                y = input(X+" you want to make any changes:")
                                if "yes" in y or "y" in y:
                                    print(rp())
                                else:
                                    print (X+" your room is booked")
                                    print("enjoy your day")
                                    o = input(X+" you want to reuse:")
                                    if "yes" in o or "y" in o:
                                        print(rp())
                                    else:
                                        print(X+" Thanking you for using our program")
                                        print("goodbye")
                            else:
                                k = input(X+" you don't want to book the room:")
                                if "yes" in k or "y" in k:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    l = input(X+" you want to reuse:")
                                    if "yes" in l or "y" in l :
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        else:
                            print(X+" you can book room for only five days")
                            print("please book room carefully")
                            print(rp())            
        
                        
                        
                                        
                        
                    else:
                        j = input(X+" you want to rebook:")
                        if "yes" in j or "y" in j:
                            print(rp())
                        else:
                            print("goodbye")
                            h = input(X+" you want to reuse:")
                            if "yes" in h or "y" in h:
                                print(rp())
                            else:
                                print(X+" Thank you for using our program")
                                print("goodbye")        
                elif int(c) in range(15000,17000):
                    print(X+" we have two star room")
                    print("which cost 16000 for one day")
                    d = input(X+" you want to book the room:")
                    if "yes"in d or "y" in d:
                        e = input(X+" for how many days you want to book the room:")
                        if int(e) in range(4,6):
                            print(X+(" for every extra day it will charge 8000 extra"))
                            print("and after giving 10% discount")
                            print("your total bill become of 50400")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+" your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                   
                        elif int(e) in range(2,4):
                            print(X+" for every extra day it will charge 8000 extra")
                            print("and after giving 10% discount")
                            print("your total bill become of 36000")
                            f = input(X+" you want to book the room:")
                            if "yes" in f or "y" in f:
                                g = input(X+" you want to make any changes:")
                                if "yes" in g or "y" in g:
                                    print(rp())
                                    
                                else:
                                    print(X+"your room is booked")
                                    print("enjoy your day")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                            else:
                                i = input(X+" you don't want to book the room:")
                                if "yes" in i or "y" in i:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        elif e == "1":
                            print(X+" After giving 10% discount")
                            print(" your total bill become of 14400")
                            x= input(X+" you want to book the room:")
                            if "yes" in x or "y" in x:
                                y = input(X+" you want to make any changes:")
                                if "yes" in y or "y" in y:
                                    print(rp())
                                else:
                                    print (X+" your room is booked")
                                    print("enjoy your day")
                                    o = input(X+" you want to reuse:")
                                    if "yes" in o or "y" in o:
                                        print(rp())
                                    else:
                                        print(X+" Thanking you for using our program")
                                        print("goodbye")
                            else:
                                k = input(X+" you don't want to book the room:")
                                if "yes" in k or "y" in k:
                                    print(X+" Thank you for coming")
                                    print("goodbye")
                                    l = input(X+" you want to reuse:")
                                    if "yes" in l or "y" in l :
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                                else:
                                    print("goodbye")
                                    h = input(X+" you want to reuse:")
                                    if "yes" in h or "y" in h:
                                        print(rp())
                                    else:
                                        print(X+" Thank you for using our program")
                                        print("goodbye")
                        else:
                            print(X+" you can book room for only five days")
                            print("please book room carefully")
                            print(rp())            
        
                        
                        
                                        
                        
                    else:
                        j = input(X+" you want to rebook:")
                        if "yes" in j or "y" in j:
                            print(rp())
                        else:
                            print("goodbye")
                            h = input(X+" you want to reuse:")
                            if "yes" in h or "y" in h:
                                print(rp())
                            else:
                                print(X+" Thank you for using our program")
                                print("goodbye")        
                else:
                    print(X+" we do not have room in this range")
                    x = input("so you want to rebook:")
                    if "yes" in x or "y" in x:
                        print(rp())
                    else:
                        print("goodbye")
        
            else:
                print(X+" you choose wrong one ")
                print("please choose correctly")
                print(rp())
            file = open("records.txt","a+")
            file.write(X+'\n')
            file.write(b+'\n')
            file.write(c+'\n')
            file.write(e+'\n')
            file.close()    
    
        rp()  
    if a == "2":
        z = input("Enter your name:")
        if z == ("roshan"):
            print("Welcome sir")
            t = input("You want to see records:")
            if "yes" in t or "y" in t or "Y" in t:
                def pa():
                    o = input("Enter the password:")
                    if o == "rp the great":
                        fobj = open("records.txt","r")
                        data = fobj.read()
                        print(data)
                        q = input("You want to reuse:")
                        if "yes" in q or "y" in q or "Yes" in q:
                            print(rrp())
                        else:
                            print(exit())
                    else:
                        print("You enter wrong password:")
                        print("try again")
                        print(pa())
                        q = input("You want to reuse:")
                        if "yes" in q or "y" in q or "Yes" in q:
                            print(rrp())
                        else:
                            print(exit())
                pa()
            else:
                print(exit())
                q = input("You want to reuse:")
                if "yes" in q or "y" in q or "Yes" in q:
                    print(rrp())
                else:
                    print(exit())
        else:
            print("Sorry, we can't show you records")
            print("You are not the authorized person")
            q = input("You want to reuse:")
            if "yes" in q or "y" in q or "Yes" in q:
                print(rrp())
            else:
                print(exit())
    else:
        print("You choose wrong one:")
        q = input("You want to reuse:")
        if "yes" in q or "y" in q or "Yes" in q:
            print(rrp())
        else:
            print(exit())
rrp()