import pandas as pd

file_to_check = 'lmu-users.xlsx'  # CHANGE: File with names to check
file_to_search = 'Spring 2024 Scheduled Teaching.xlsx'  # CHANGE: File to compare against

sheet_to_check = 'User Information'  # CHANGE: Sheet with names to find
sheet_to_search = 'MyReport-20241122-123042-CST'  # CHANGE: Sheet to compare against

df_to_check = pd.read_excel(file_to_check, sheet_name=sheet_to_check)
df_to_search = pd.read_excel(file_to_search, sheet_name=sheet_to_search)

df_to_check_relevant = df_to_check.iloc[:, [1, 0]]  
df_to_search_relevant = df_to_search.iloc[:, [0, 1]]  

df_to_check_relevant = df_to_check_relevant.apply(lambda x: x.str.lower())
df_to_search_relevant = df_to_search_relevant.apply(lambda x: x.str.lower())

names_set = set(zip(df_to_search_relevant.iloc[:, 0], df_to_search_relevant.iloc[:, 1]))

results = []
for _, row in df_to_check_relevant.iterrows():
    name_tuple = (row.iloc[0], row.iloc[1])  
    if name_tuple in names_set:
        results.append('x')  # Found
    else:
        results.append('0')  # Not found

# CHANGE: fill column with results
df_to_check['Spring 2024 ST'] = results

with pd.ExcelWriter(file_to_check, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df_to_check.to_excel(writer, sheet_name=sheet_to_check, index=False)

print(f"Process complete. '{sheet_to_check}' in '{file_to_check}' has been updated.")
