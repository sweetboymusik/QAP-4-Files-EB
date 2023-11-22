# Program to plot a graph of total monthly sales for a year
# Dates written: November 18, 2023 -
# Author: Elliott Butt

# import libraries
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# define constants
MAX_COLOR = "green"
MIN_COLOR = "red"
REG_COLOR = "blue"

# define lists
x_months_list = ["Jan", "Feb", "Mar", "Apr", "May",
                 "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
label_list = ["MAX", "MIN", "REG"]
y_sales_list = []
colors_list = []

# inputs
for month in x_months_list:
    try:
        total_sales = float(
            input(f"Enter total amount of sales for the month of {month}: "))
    except:
        print("Total sales must be a valid number. Please re-enter.")
    else:
        y_sales_list.append(total_sales)

# calculations
amt_max = max(y_sales_list)
amt_min = min(y_sales_list)

for amt in y_sales_list:
    if amt == amt_max:
        colors_list.append(MAX_COLOR)
    elif amt == amt_min:
        colors_list.append(MIN_COLOR)
    else:
        colors_list.append(REG_COLOR)


# output
fig, ax = plt.subplots()

graph = ax.bar(x_months_list, y_sales_list, color=colors_list,
               label=colors_list, edgecolor="black", width=0.75, linewidth=1.0)

ax.bar_label(graph, fmt="$%.2f")

plt.title("Total Monthly Sales")
# plt.legend(["MAX", "MIN", "REG"], loc="upper left", frameon="fancy") TODO: figure this out
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('${x:,.2f}'))
plt.ylabel("Total Sales ($)")
plt.show()
