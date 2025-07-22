balance =1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        if choice == "1":
            print("Your balance :",balance)        
        elif choice == "2": # ถอนเงิน
            print("Withdraw") 
            if(balance == 0): # ถ้ายอดเงิน น้อยกว่า 0 ก็จะถอนไม่ได้ ซึ่งก็ไป เมนู 3 เพื่อฝากเพิ่มก็ได้
                print("Your balance is can't Withdraw")
            else: # ถ้ายอดเงิน มากกว่า 0 ก็จะถอนเงินได้ปกติ เพราะค่า มากกว่า 0 ครับ
                amount = int(input("Enter amount to Withdraw: "))
                if(amount > 0): # ไม่ควรจะน้อยกว่า 0 หรือ ติดลบ เพราะมันจะไป ลบ กับ ลบ อีก จะเป็น บวก
                    balance -= amount
                    print("you balance ",balance)
                else: # enter ค่าลบมา ก็จะdisplay นี้
                    print("Sorry you can't enter negative number")
        elif choice == "3":
            print("Deposit")        
            amount = int(input("Enter amount to Deposit: "))
            if(amount > 0): # เหมือนกันคือค่าต้องมากกว่า 0 เพราะไม่งั้น มันจะไปลบ กับยอดเงินเดิม
                balance += amount
                print("you balance ",balance)
            else: # enter ค่าลบมา ก็จะdisplay นี้
                print("Sorry you can't enter negative number")
        elif choice == "4": # ออก break this loop
            print("--exit--")
            break
        else: # check ว่าค่าต้องเป็น 1,2,3,4 menu ต้องเป็นนี้ ถ้านอกนั้นเป็น จะdisplay นี้มา
            print("Invalid option")
else: # อันนี้เช็ค pin ถูกไหม
    print("Invalid PIN")
