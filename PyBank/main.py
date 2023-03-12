import csv
import os

#Find directory for input and output
FILE_PATH_INPUT = os.path.join("Resources", "budget_data.csv")
FILE_PATH_OUTPUT = os.path.join("analysis", "Results.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Initalize Variables
output = ""
month_count = 0
profit_change = {}
prev_amount = None

#Initalize csv file
with open(FILE_PATH_INPUT) as csvfile:
    file_reader = csv.reader(csvfile, delimiter=",")
    next(file_reader)  #Skip Header

    for row in file_reader:
        month_count += 1

        #Check if there is a previous amount (Don't run calculation for first month.)
        if prev_amount is None:
            prev_amount = float(row[1])
            continue
        
        #Find the amount for the current month
        curr_amount = float(row[1])

        #Find the difference
        diff = curr_amount - prev_amount
        
        #Store the month and difference to a dictionary
        profit_change[row[0]] = diff
        
        #Reset previous value to the current one for next iteration
        prev_amount = curr_amount

#Find values using dictionary
net_total = sum(profit_change.values())
average_change = sum(profit_change.values())/len(profit_change)
max_increase = max(profit_change.values())
max_key = [key for key, value in profit_change.items() if value == max_increase][0]
min_decrease = min(profit_change.values())
min_key = [key for key, value in profit_change.items() if value == min_decrease][0]

#Create output for the results
output += "Financial Analysis\n"
output += "-"*40 + "\n"
output += "Total Months: " + str(month_count) +"\n"
output += "Total: " + str(net_total) + "\n"
output += "Average Change: " + str(average_change) +"\n"
output += "Greatest Increase in Profits: " + str(max_key) + " (" + str(max_increase) + ")" +"\n"
output += "Greatest Decrease in Profits: " + str(min_key) + " (" + str(min_decrease) + ")" + "\n"

#Print and Write Output
print(output)
with open(FILE_PATH_OUTPUT, "w") as output_file:
    print(output)
    output_file.write(output)

