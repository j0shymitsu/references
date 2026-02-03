import pandas


##############
### PANDAS ###
##############



lst = [["Tom", 61], ["Sam", 63], ["Nick", ], ["Julie", 72], ["Fred", ], ["Alice", 68]]

# Read the CSV into DataFrame:
df1 = pandas.DataFrame(lst, columns=["Name", "Age"])
print("Print out the DataFrame\n")
print((df1))
print()

# Show information:
print("\nInformation about the DataFrame")
df1.info()
print()

# Remove rows where there is no number (NaN value):
print("\nRemove rows where there is no number")
df1.dropna(inplace=True)    # Replaced with boolean value.
print(df1)
print()

# Calculate averages and standard deviation:
print(f"Mean score: {df1['Age'].mean()}")
print(f"Standard deviation:", df1['Age'].std())
print()

# Select a row:
print("Showing Sam's data:")
print(df1.loc[df1.Name=='Sam'])
print()

# Select a column:
print("Showing the list of names:")
print(df1["Name"])
print()

# Select a row and a column:
print("Showing Sam's score:")
score = int(df1['Age'].loc[df1.Name=='Sam'])
print(score)
print()

# Output to a CSV file:
df1.to_csv("mydata.csv", index=False)