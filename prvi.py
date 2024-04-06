import pandas as pd

# Load the Titanic dataset
titanic_data = pd.read_csv("titanic.csv")

# Task 1: Find the minimum and maximum values for a specific column
def find_min_max(column_name):
    min_val = titanic_data[column_name].min()
    max_val = titanic_data[column_name].max()
    return min_val, max_val

# Example usage
min_age, max_age = find_min_max('Age')
print(f"Minimum Age: {min_age}, Maximum Age: {max_age}")

# Task 2: Calculate the average value for each column
def calculate_column_average(column_name):
    return titanic_data[column_name].mean()

# Task 3: Calculate the percentage difference between the average and maximum value
def calculate_percentage_difference(column_name):
    avg_value = calculate_column_average(column_name)
    max_value = titanic_data[column_name].max()
    percentage_difference = ((max_value - avg_value) / avg_value) * 100
    return percentage_difference

# Task 4: Normalize values in a numerical column between 0 and 1
def normalize_column(column_name):
    min_val = titanic_data[column_name].min()
    max_val = titanic_data[column_name].max()
    titanic_data[column_name] = (titanic_data[column_name] - min_val) / (max_val - min_val)

    # Save the updated DataFrame back to CSV
    titanic_data.to_csv("titanic.csv", index=False)

# Task 5: Find columns with highest positive and negative correlation
# Skripta računa koeficijente korelacije za sve parove numeričkih kolona u skupu podataka. Na kraju vraća kolone između kojih postoji najveće poklapanje vrijednosti
def find_correlation():
    corr_matrix = titanic_data.corr()

    # Filter out entries with correlation coefficient of 1 (columns with themselves)
    corr_matrix_filtered = corr_matrix[corr_matrix < 1]

    # Find maximum positive correlation
    max_positive_corr = corr_matrix_filtered.stack().max()

    # Find minimum negative correlation
    max_negative_corr = corr_matrix_filtered.stack().min()

    # Get the column names for highest positive and negative correlation
    max_pos_corr_cols = corr_matrix[corr_matrix == max_positive_corr].stack().index.tolist()
    max_neg_corr_cols = corr_matrix[corr_matrix == max_negative_corr].stack().index.tolist()

    return max_pos_corr_cols, max_neg_corr_cols



# Example usage
avg_age = calculate_column_average('Age')
print(f"Average Age: {avg_age}")

percentage_difference_age = calculate_percentage_difference('Age')
print(f"Percentage Difference for Age: {percentage_difference_age}%")

normalize_column('Age')  # Normalize Age column between 0 and 1

# Example usage
max_pos_corr_cols, max_neg_corr_cols = find_correlation()
print(f"Columns with highest positive correlation: {max_pos_corr_cols}")
print(f"Columns with highest negative correlation: {max_neg_corr_cols}")