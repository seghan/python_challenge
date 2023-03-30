#import modules
import os
import csv

#set path for file
budget_data_csv = os.path.join('.', "Resources", "budget_data.csv")

#set the output for text file
text_path = "output.txt"

#set variables
total_months = 0 
total_revenue = 0 
revenue = []
previous_revenue = 0
month_of_change = 0
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0

#open the csv file
with open(budget_data_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #loop through to find total months
    for row in csvreader:

        #count the total of months
        total_months += 1

        #calculate the total revenue over the entire period
        total_revenue = total_revenue + int(row[1])

        #calculate the average change in revenue between months over the entire period
        revenue_change = float(row[1]) - previous_revenue
        revenue_change_list.append(revenue_change)
        previous_revenue = float(row[1])
        month_of_change = [month_of_change] + [row[0]]

        #The greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row[0]

        #The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row[0]
    revenue_change_list.pop(0)
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)
    print("financial Analysis\n")
    print("---------------------\n")
    print("Total Months: %d\n" % total_months)
    print("Total Revenue: $%d\n" % total_revenue)
    print("Average Revenue: $%s\n" % revenue_average) 
    print("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    print("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))

    #write changes to csv
    with open(text_path, 'w') as file:
        file.write("financial Analysis\n")
        file.write("---------------------\n")
        file.write("Total Months: %d\n" % total_months)
        file.write("Total Revenue: $%d\n" % total_revenue)
        file.write("Average Revenue: $%s\n" % revenue_average) 
        file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
        file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))