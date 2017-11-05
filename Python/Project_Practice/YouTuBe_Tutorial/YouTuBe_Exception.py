def testException():
    while True:
        try:
            number = int(input("What's your fav number? \n"))
            print(10/number)
            break
        except ValueError:
            print("Make sure and input the number!!")
        except ZeroDivisionError:
            print("Can not divide zero")
        except:
            break
        finally:
            print("loop complete")

testException()