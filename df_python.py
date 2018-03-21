

"""Pandas using Python dictionary"""

	Employee_Data = {
	'EmployeeName' : ['Kumar'],
	'EmployeeId' : ['1023218797'],
	'Address' : ['161 Tanglewood Dr. Illnois'],
	'Zipcode': ['08817']
}
df = pd.DataFrame(Employee_Data)
df	
Pandas using List

	Student_Data = [
	('Sandeep', 'Kumar', '5472'),
	('Yugi', 'Rao', '1234'),
	('Santosh', 'Reddy', '3497'),
	('Deep', 'Gowda', '1899')
]
df = pd.DataFrame(Student_Data, columns = ['FirstName', 'LastName', 'Social'])
df


"""Pandas using Dictionary """
Salary_Data = [
	{'EmployeeId' : '5472', 'Name' : 'Sudeep', 'last' : 'Kumar', 'AnnualIncome' : 60000},
	{'EmployeeId' : '1234', 'Name' : 'Yugi', 'last' : 'Rao', 'AnnualIncome' : 60001},
	{'EmployeeId' : '3497', 'Name' : 'Santosh', 'last' : 'Reddy', 'AnnualIncome' : 60002},
	{'EmployeeId' : '1899', 'Name' : 'Deepu', 'last' : 'Gowda', 'AnnualIncome' : 60003}
]
df = pd.DataFrame(Salary_Data)
df

"""pandas reading a file"""

import pandas as pd
df = pd.read_csv('path')
df

df.column.values
df.describe()
df.head()


df = pd.read_csv('path', headers = none, names = ['Temp', 'Windspeed', 'max', 'min')
df

df = ['temp', 'windspeed'].max()
df = ['temp', 'windspeed'].min()
df = ['temp', 'windspeed'].mean()
df = ['temp', 'windspeed'].median()
df = ['temp', 'windspeed'].mod()
df = ['temp', 'windspeed'].head(20)

df = pd.read_csv('path', na_values = ['Not available', 'n.a.')


df.to_csv('filename')
df.to_csv('filename', columns = ['name', place', 'animal', 'total']

import pandas as pd
def convert_people_cell(cell):
	if cell=='n.a.'
	return 'sam walton'
	return cell
	
df = pd.read_excel('filename.xlsx', 'sheet', converters = {
		'people' : convert_peopel_cell
		})
df


