## 2-8 7 pages
### 2-9 8 pages 
##total: fifteen pages


pagesWritten = {str : int}

pagesWritten = {
        "2.8" : 7,
        "2.9" : 8
        }   

def askUser(day, number):
    number = int(number)
    return day, number

def addDay(pagesWritten, day, number):
    askUser(day, number)
    pagesWritten.update({day : number})


#how many days did you write
def howManyDays(pagesWritten):
    print(len(pagesWritten))

def main():
   print("You've written: ")
   howManyDays(pagesWritten) 
   day = input("Enter the date as a decimal number" )
   number = input("Enter the number of pages you wrote: ")
   addDay(pagesWritten, day, number)
   print(pagesWritten)
   
   
main()
