import os
import csv

budgetdataCSV=os.path.join("03 - Python/Module 03 Challenge - Due 07-05-2022/PyBank/Resources","budget_data.csv")

outputfile=os.path.join("03 - Python/Module 03 Challenge - Due 07-05-2022/PyBank/Resources","Pybank_analysis.txt")

totalmonths=0
net_total=0
change=[]

with open(budgetdataCSV,"r", encoding="utf-8") as file:
    csvreader=csv.reader(file,delimiter=",")
    header =next(csvreader)
    for row in csvreader:
        
        totalmonths +=1
        total=int(row[1])
        net_total += total
    


       

output=(
    f"Financial Analysis\n"
    f"------------------------------------------\n"
    f"Total Months: {totalmonths}\n"
    f"Total: ${net_total}"
    )
print(output) 

with open(outputfile,"w") as textfile:
    textfile.write(output)

     


 
       
