import os
import csv

budgetdataCSV=os.path.join("python-challenge/PyBank","Resources","budget_data.csv")

outputfile=os.path.join("python-challenge/PyBank","analysis","Pybank_analysis.txt")

totalmonths =0
net_total =0
monthlychanges =[]
months =[]


with open(budgetdataCSV,"r", encoding="utf-8") as sourcefile:
    csvreader = csv.reader(sourcefile)
    header = next(csvreader)
    
    firstRow= next(csvreader)
    totalmonths +=1
    net_total += int(firstRow[1])
    previouspandl= int(firstRow[1])


    for row in csvreader:
        
        totalmonths +=1
        
        net_total += int(row[1])

        netchange= int(row[1])- previouspandl
        monthlychanges. append(netchange)
        months.append(row[0])
        previouspandl= int(row[1])
    
averagechange = sum(monthlychanges)/len(monthlychanges)

greatestincrease=[months[0],monthlychanges[0]]
greatestdecrease=[months[0],monthlychanges[0]]

for m in range(len(monthlychanges)):
    if (monthlychanges[m] > greatestincrease[1]):
        greatestincrease[1]= monthlychanges[m]
        greatestincrease[0]= months[m]

    if (monthlychanges[m] < greatestdecrease[1]):
        greatestdecrease[1]= monthlychanges[m]
        greatestdecrease[0]= months[m]

output=(
    f"Financial Analysis\n"
    f"------------------------------------------\n"
    f"Total Months: {totalmonths}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${averagechange:,.2f}\n"
    f"Greatest Increase in Profits: {greatestincrease[0]} (${greatestincrease[1]})\n"
    f"Greatest Decrease in Profits: {greatestdecrease[0]} (${greatestdecrease[1]})\n"
    )
print(output) 

with open(outputfile,"w") as textfile:
    textfile.write(output)

     


 
       
