# python-challenge
Projext Name: PyBank and PyPoll

#Description 
 1. PyBank:
    In this project, the Python scripting is used to analyze the financial record of PyBank from Jan-10 to Feb-17. 
    The script calculates total profit and loss and average monthly change of the dataset. Also,the months with 
    greatest profit increase and decrease are showed for reference.
  
 2. PyPoll:
    In this project, the Python scripting is used to help a small, rural town modernize its vote counting process.
    The script calculates total votes and analyze the vote counts for each candidate, then announce the winner.

#Date: 06.29.2022 #Author: I Ju Su selina.iju@gmail.com #How to start working with this?
 1. There are two folders - PyBank and Pypoll, each folder has it's script file main.py, analysis folder and resource folder respectively
 2. The analysis file was created and written by the main.py based on dataset (in resource folder) and saved in analysis folder.
 
#coding:
 1. PyBank:
    With budgetdataCSV (os path budget_data.csv) open as sourcefile and csvreader
    * Total Month: set variable totalmonths=0 and use for loop to count (increment) the total months (rows except header)
    * Total Profit and loss: set variable net_total=0 and loop through to sumup from fist row (skip header)
    * Average monthly change: initialize the list of monthlychanges =[], set the initial 'previous profit and loss' to the first row index 1, calculate the monthly changes by deduct 'previous profit and loss' from current profit and loss, then update the previouse profit and loss when looping throgh the rows. Add on to the monthly changes and devided by len of 'monthlychanges' to get the averge monthly changes.
    * Greatest increase and decrease in profit: set variables to hold the greatest increase and decrease month and value, use for loop and if to loop through and compare the changes, update the new greatest month and value.
    * Print and write all the results (output) above to Pybank_analysis.txt

 2. Pypoll:
