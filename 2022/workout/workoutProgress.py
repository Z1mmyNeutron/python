## 2-8 7 pages
### 2-9 8 pages 
##total: fifteen pages


daysWorkedOut = {str : int}
bodyParts = {str : int}

daysWorkedOut = {
        "2.8" : 1,
        "2.9" : 2,
        "2.10" : 3
        } 
bodyParts = {
    "Arms" : 5,
    "Butt" : 15,
    "Cardio" : 25,
}


def askUser(day, number):
    number = int(number)
    return day, number

def addDay(daysWorkedOut, day, number):
    askUser(day, number)
    daysWorkedOut.update({day : number})


#how many days did you write
def howManyDays(daysWorkedOut, bodyParts):
    print("You wrote for: ")
    print(len(daysWorkedOut), " days")
    print("in each story, you wrote: ")
    print(bodyParts)
        


def main():
   print("You've written: ")
   howManyDays(daysWorkedOut, bodyParts) 
   day = input("Enter the date as a decimal number" )
   number = input("Enter the number of pages you wrote: ")
   addDay(daysWorkedOut, day, number)
   print(bodyParts)
   
   
main()
