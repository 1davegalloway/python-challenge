# create a Python script that analyzes the records 
# to calculate each of the following

# Dependencies and import csv file
import os
import csv

file_to_load = os.path.join("..", "PyBank","budget_data.csv")


csvPath = "budget_data.csv"
with open(csvPath, 'r', newline = '') as csvfile:
    csv_reader = csv.reader(csvfile)

    print("Financial Analysis")
    print("------------------") #prints a separator line between the above and below print commands.
#Count Months and print total
    next(csv_reader) #next goes down one row to avoid printing the 'Date' and counting it as a valid month.
    monthcount = sum(1 for line in csvfile) # the value of 1 is given to the first line in the csv file, the months
    print("Total Months: ", monthcount) # prints phrase and prints total number of months included in the dataset (count)


# Count total net amount of "Profit/Losses" over the entire period and print
numtotalRevenue = 0
avgchangerev = 0
maxincreaseprofits = 0 #date and amount
maxdecreaseprofits = 0 #date and amount
priorrevenue = 0
numtotalmonths = 0
monthgreatincrease = ""
greatincrease = 0
monthgreatdecrease = ""
greatdecrease = 0

with open(csvPath, 'r', newline = '') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    
    for row in csv_reader:
        numtotalmonths += 1
        thismonth = row[0]
        thisrevenue = int(row[1])

        revchange = thisrevenue - priorrevenue
        
# greatest increase in profits (date and amount) over the entire period

        if revchange > maxincreaseprofits:
            monthgreatincrease = thismonth
            maxincreaseprofits = revchange            
 # greatest decrease in losses (date and amount) over the entire period    
        if revchange < greatdecrease:
            monthgreatdecrease = thismonth
            Greatdecrease = revchange

        priorrevenue = thisrevenue

        numtotalRevenue += thisrevenue
# average change in "Profit/Losses" between months over the entire period

        avgchangerev = numtotalRevenue / numtotalmonths

        Avgrev2= round(avgchangerev,2)

print("Total: $", numtotalRevenue)

print("Average Change: $", Avgrev2)

print("Greatest Increase in Profits: $", monthgreatincrease, maxincreaseprofits)

print("Greatest Decrease in Profits: $", monthgreatdecrease, Greatdecrease)


output = (  
    f"\nTotal Number of Months: {monthcount} + months\n"
    f"\nTotal Revenue: $ {numtotalRevenue}\n"
    f"\nAverage Change: $ {Avgrev2} \n"
    f"\nGreatest Increase in Revenue: {monthgreatincrease} ${greatincrease}\n"
    f"\nGreatest Decrease in Revenue: {monthgreatdecrease} ${greatdecrease}\n"
    f"\n------------------------------------------------\n")


with open("analysis.txt", "w") as txt_file:
    print("Financial Analysis", file=txt_file)
    print("------------------", file=txt_file)
    print("Total Months: ", monthcount, file=txt_file)
    print("Total: $", numtotalRevenue, file=txt_file)

    print("Average Change: $", Avgrev2, file=txt_file)

    print("Greatest Increase in Profits: $", monthgreatincrease, maxincreaseprofits, file=txt_file)

    print("Greatest Decrease in Profits: $", monthgreatdecrease, Greatdecrease, file=txt_file)