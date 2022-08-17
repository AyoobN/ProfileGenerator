from initial import DOB, firstName, lastName, li
import pandas as pd

# print(li)
# print(DOB)
# print(firstName)
# print(lastName)

df = pd.DataFrame({'First Name':firstName, 'Last Name':lastName, 'Gender':li, 'DOB':DOB})
print(df)

df.to_csv('export.csv', encoding='utf-8', index=False)
