import csv
from collections import defaultdict

FILE= "expenses.csv"

try:
   open(FILE ,"x").close()
except:
    pass

print(" Welcome to Expense Tracker")
def add_expense():
   amount=float(input("Enter The Amount: "))
   category=input("Enter Category (Food,Transportation,etc..):")
   date=input("Enter Date[YYYY-MM-DD]:")


   with open(FILE,"a", newline="") as f:
          writer=csv.writer(f)
          writer.writerow([amount,category,date])


   print("Expenses Added")

def report():
   total=0
   categories= defaultdict(float)
    
   with open(FILE,"r") as f:
      reader=csv.reader(f)


      for row in reader:
         if row:
            amount=float(row[0])
            category=row[1]

            total+=amount
            categories[category]+=amount

   print( " \n ==REPORT== ")
   print("Total Spent= ",total)


   if categories:
      TopCategory=max(categories, key=categories.get)
      print(f" Top Category:{TopCategory}-> {categories[TopCategory]}")

while True:
   print("\n1- Add expenses")
   print("2- Show Report")
   print("3- Exit")

   choice= input("Enter Your choice: ")
   if choice=="1":
      add_expense()
   elif choice=="2":
      report()
   elif choice=="3":
      break
   else:
      print("Invalid Choice!!!")

                            
