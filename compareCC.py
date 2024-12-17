import pandas as pd

file_to_check = 'lmu-users.xlsx'  # CHANGE: File with names to find
file_to_search = 'Fall 2024 Class Count.xlsx'  # CHANGE: File with "Instructor" column

sheet_to_check = 'User Information'  # CHANGE: Sheet with names to find
sheet_to_search = 'Class Counts by College - Busin'  # CHANGE: Sheet with Instructor column

df_to_check = pd.read_excel(file_to_check, sheet_name=sheet_to_check)
df_to_search = pd.read_excel(file_to_search, sheet_name=sheet_to_search)

df_to_search[['Last Name', 'First Name']] = df_to_search['INSTRUCTOR'].str.split(',', expand=True)

df_to_search['Last Name'] = df_to_search['Last Name'].str.strip().str.lower()
df_to_search['First Name'] = df_to_search['First Name'].str.strip().str.lower()

df_to_check_relevant = df_to_check.iloc[:, [1, 0]].copy() 
df_to_check_relevant.columns = ['First Name', 'Last Name']

df_to_check_relevant['First Name'] = df_to_check_relevant['First Name'].str.lower()
df_to_check_relevant['Last Name'] = df_to_check_relevant['Last Name'].str.lower()

names_set = set(zip(df_to_search['First Name'], df_to_search['Last Name']))

results = []
for _, row in df_to_check_relevant.iterrows():
    name_tuple = (row['First Name'], row['Last Name'])
    if name_tuple in names_set:
        results.append('x')  # Found
    else:
        results.append('0')  # Not found

# CHANGE: fill column with results
df_to_check['Fall 2024 CC'] = results

with pd.ExcelWriter(file_to_check, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df_to_check.to_excel(writer, sheet_name=sheet_to_check, index=False)

print(f"Process complete. '{sheet_to_check}' in '{file_to_check}' has been updated.")
