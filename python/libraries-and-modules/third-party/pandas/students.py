import pandas



################
### PANDAS 2 ###
################


# DATAFRAMES + MANIPULATION # 

# Relative path:
filename = r'C:\Users\University\Dropbox\code\uni + references\python\data analysis (pandas)\studentdataperformance.csv'

# Read the CSV into the DataFrame:
print("\n\n")
df = pandas.read_csv(filename)
print(type(df))

# Show the first 5 rows:
print("\nThe first 5 rows:")
print(df.head())

# Show the first 15 rows:
print("\nThe first 15 rows:")
print(df.head(15))

# Show all column names:
print("\nShow column names")
print(df.columns)

print("\nShow file info")
df.info()

# Returns a new DataFrame removing all NaN values:
print("\nRemove missing values and store in new_df")
new_df = df.dropna()
new_df.info()

# Rename columns:
print("\nRenamed columns")
df = df.rename(columns={'test preparation course': 'tpc',
                        'math score': 'math',
                        'writing score': 'writing',
                        'reading score': 'reading'})

# Display new info:
print()
df.info()

# Simple description:
print("\nAnalysis:")
print(df.describe().T)      # "T" options transposes the rows into columns.

# Short summary:
print("\nCorrelation between math, reading and writing:")
corr_matrix = df[['math', 'writing', 'reading']].corr()
print(corr_matrix)

# Column selection:
print('\nDisplaying the math column:')
print(df['math'])

# Select multiple columns:
print("\nCreated data set with multiple columns and display:")
new_df = df[['tpc', 'writing']]
print(new_df.head)

# Create a new column:
print("\nLiteracy score = writing + reading:")
df['literacy'] = (df['writing'] + df['reading']) / 2
print(df.head())
print(len(df))
print()

# Create a new column of 000's:
print("\nAdd a new column of 0s")
df['new'] = [0] * len(df)
print(df.head())
print()

# Locate by index using df.iloc:
print(df.iloc[0])               # Row 0 only.
print(df.iloc[:10])             # First 10.
print(df.iloc[-10:])            # Last 10.
print(df.iloc[20:45])           # Rows 20 to 45.
print(df.iloc[::10])            # All rows, in the 10's w/ column selection.
print(df.iloc[10, 2])           # Row 10, column 2.
print(df.iloc[:10, -1])         # First 10 rows last column only.
print(df.iloc[-100:, [0, 2, 4]])# Last 100 rows, columns 0 2 & 4.
print()

# Use cases:
print("\nAverage reading score:")
average_reading = df['reading'].mean()
print(average_reading)
print()

print("\nTake math score over 70 and store in a new DataFrame")
df_math = df.loc[df.math > 70]
df_math.to_csv('highestmathers.csv', index=False)
df.math.info()
print()

# Analysis
print("MEAN AVERAGES:")
print("Mean math score:", round(df['math'].mean(), 2))
print("Mean writing score:", round(df['writing'].mean(), 2))
print("Mean reading score:", round(df['reading'].mean(), 2))
print()

print("STANDARD DEVIATIONS:")
print("Math:", df['math'].std())
print("Writing:", df['writing'].std())
print("Reading:", df['reading'].std())


