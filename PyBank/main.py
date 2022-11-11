## Challenge 1: PyBank

#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 

#* Your task is to create a Python script that analyzes the records to calculate each of the following:
#       1.	The total number of months included in the dataset
#       2.	The total net amount of "Profit/Losses" over the entire period
#       3.	The changes in "Profit/Losses" over the entire period, and then the average of those changes
#       4.	The greatest increase in profits (date and amount) over the entire period
#       5.	The greatest decrease in losses (date and amount) over the entire period
#* Your analysis should align with the following results:

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)
 
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#-----------------------------------------------------------------------------------------------------------------------

# ----------------------------
#    SOLUTION
# ----------------------------



# I: Import os and csv.

import os
import csv

# II: Set path for the CSV file in 'budget_data_csv'


os.chdir(os.path.dirname(__file__))
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# III: Create lists to store data. 

date = []
profit = []
change = []


# IV: Initialization.
 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# V: Using 'budget_data_csv', complete the needed calculations.

with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Ask
    for row in csvreader:    
      # Count to count the number months
      count = count + 1 

      # To help collect the greatest increase and decrease in profits
      date.append(row[0])

      # Append profit information appending, total profit total profit calculation
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      # Average change in profits month to month + average change in profits
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      # Store  monthly_changes in list
      change.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      # Average change in profits
      average_change_profits = (total_change_profits/count)
      
      # Min/Max change in profits
      greatest_decrease_profits = min(change)
      greatest_increase_profits = max(change)

      # Dates of observation
      increase_date = date[change.index(greatest_increase_profits)]
      decrease_date = date[change.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

# VI: Write results to a separate .txt file.
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")

# Fin.