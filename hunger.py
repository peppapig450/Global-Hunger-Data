# Actual data for global hunger crisis
# get rid of countries dict we dont need it
years = [2018, 2019, 2020, 2021, 2022]
hunger_data = {
    "India": [
        14.5,
        14.0,
        13.7,
        13.2,
        13.0,
    ],  # Hypothetical data in percentage of population suffering from hunger
    "Nigeria": [10.9, 11.1, 11.5, 11.8, 12.0],
    "Yemen": [16.1, 16.5, 17.0, 17.3, 17.5],
    "Democratic Republic of the Congo": [13.7, 13.9, 14.2, 14.5, 14.7],
    "Afghanistan": [13.8, 14.0, 14.2, 14.4, 14.6],
}
countries = hunger_data.keys()  # create countries list from the keys

# Print the data
print("Hunger Data (percentage of population suffering from hunger):")
for country, data in hunger_data.items():
    print(f"{country}: {data}")

# Calculate average hunger rate for each country
# initialize all the variables that will be modified when we loop through hunger_data
average_hunger_rate = {}
highest_hunger_country = None
lowest_hunger_country = None
max_rate = float(
    "-inf"
)  # starting at negative infinity ('-inf') ensures the first encountered rate (even if a low value) will be considered the maximum initially.
min_rate = float(
    "inf"
)  # starting at positive infinity ('inf') guarantees that the first encountered rate (even if a high value) will be correctly identified as the minimum so far

# Dictionary to store the plot lines per country
plot_lines = {}

for country, data in hunger_data.items():
    avg_rate = sum(data) / len(
        data
    )  # set avg_rate to a variable so we can use it elsewhere in loop
    average_hunger_rate[country] = avg_rate

    if avg_rate > max_rate:
        max_rate = avg_rate
        highest_hunger_country = country

    if avg_rate < min_rate:
        min_rate = avg_rate
        lowest_hunger_country = country

    # Prepare plot line for each country using list comprehension
    plot_line = [f"{'█' * int(value)}" for value in data]
    plot_lines[country] = plot_line

# Print the average hunger rates
print("\nAverage Hunger Rate (2018-2022):")
for country, avg_rate in average_hunger_rate.items():
    print(f"{country}: {avg_rate:.2f}%")

print(
    f"\nCountry with the highest average hunger rate: {highest_hunger_country} ({average_hunger_rate[highest_hunger_country]:.2f}%)"
)
print(
    f"Country with the lowest average hunger rate: {lowest_hunger_country} ({average_hunger_rate[lowest_hunger_country]:.2f}%)"
)


# Print plot lines from dictionary
print("\nHunger Data Over Years (Text-based Plot):")
for country in countries:
    plot_line = f"{country}: " + " ".join(plot_lines[country])
    print(plot_line)


# without .items() a loop over a dictionary iterates over it's keys which is a shortcut for
# .keys()
"""
dict = {
    "hi": "there",
    "hello": "buddy",
}

for key in dict:
    print(key)
    
returns "hi" and "hello"

for key in dict.keys():
    print(key)
    
returns "hi" and "hello"

"""
# more at https://docs.python.org/3/library/stdtypes.html#dict-views

# Yearly changes in hunger rates using dictionary comprehension
yearly_changes_1 = {
    year: {country: hunger_data[country][years.index(year)] for country in countries}
    for year in years
}

# enumerate(years) does the same as range(len(years))
# https://docs.python.org/3/library/functions.html#enumerate
# for year_index in range(len(years)):
#    for country in countries:
#        yearly_changes[years[year_index]][country] = hunger_data[country][year_index]

# Yearly changes in hunger rates without dict comprehension and using enumerate
"""
yearly_changes = {}

for i, year in enumerate(years):
    yearly_changes[year] = {}  # you can also use a dictionary comprehension here
    for country, data in hunger_data.items():
        yearly_changes[year][country] = data[i]
"""

print("\nYearly Changes in Hunger Rates:")
for year, data in yearly_changes_1.items():
    print(f"{year}: {data}")
