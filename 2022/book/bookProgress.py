## 2-8 7 pages
### 2-9 8 pages 
##total: fifteen pages


pagesWritten = {str : int}
wordsWritten = {str : int}

pagesWritten = {
        "11.11" : 4,
        "2.8" : 7,
        "2.9" : 8,
        } 
pagesInEachStory = {
    "Nikki" : 10,
    "James" : 4,
    "Christiana" : 2,
    "Khana" : 4
}


def askUser(day, number):
    number = int(number)
    return day, number

def addDay(pagesWritten, day, number):
    askUser(day, number)
    pagesWritten.update({day : number})


#how many days did you write
def howManyDays(pagesWritten, pagesInEachStory):
    print("You wrote for: ")
    print(len(pagesWritten), " days")
    print("in each story, you wrote: ")
    print(pagesInEachStory)
        


def main():
   print("You've written: ")
   howManyDays(pagesWritten, pagesInEachStory) 
   day = input("Enter the date as a decimal number" )
   number = input("Enter the number of pages you wrote: ")
   addDay(pagesWritten, day, number)
   print(pagesWritten)
   
   
main()
