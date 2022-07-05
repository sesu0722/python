import os
import csv

#source file
budgetdataCSV=os.path.join("python-challenge/PyBank","Resources","budget_data.csv")
#output file
outputfile=os.path.join("python-challenge/PyBank","analysis","Pybank_analysis.txt")
#variables
totalmonths =0
net_total =0
monthlychanges =[]
months =[]

#read the csv file
with open(budgetdataCSV,"r", encoding="utf-8") as sourcefile:
    csvreader = csv.reader(sourcefile)
    #read the header row
    header = next(csvreader)
    #read the first row
    firstRow= next(csvreader)
    #add on the total months
    totalmonths +=1
    #add on to the total profit and loss
    net_total += int(firstRow[1])
    #set the previouse profit and loss to the value at first row index 1
    previouspandl= int(firstRow[1])


    for row in csvreader:
        #increment the count of total month
        totalmonths +=1
        #add on to the total
        net_total += int(row[1])
        #net change equal to current row - previouse row
        netchange= int(row[1])- previouspandl
        #update the list of monthly changes
        monthlychanges. append(netchange)
        #add the first month that a change occurred
        months.append(row[0])
        #update the previous profit and loss
        previouspandl= int(row[1])
#calculate the average change per month   
averagechange = sum(monthlychanges)/len(monthlychanges)

#variables to hold the month and monthly changes with greatest increase & decrease
greatestincrease=[months[0],monthlychanges[0]]
greatestdecrease=[months[0],monthlychanges[0]]

#calculate the greatest increase and decrease by loop
for m in range(len(monthlychanges)):
    if (monthlychanges[m] > greatestincrease[1]):
        #if the value is greater than greatestincrease, the value becomes the new greatest increase 
        greatestincrease[1]= monthlychanges[m]
        #update the month with the new greatest increase
        greatestincrease[0]= months[m]

    if (monthlychanges[m] < greatestdecrease[1]):
        #if the value is less than greatestdecrease, the value becomes the new greatest decrease
        greatestdecrease[1]= monthlychanges[m]
        #update the month with the greatest decrease
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

     


 
       
