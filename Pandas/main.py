import pandas as pd
df=pd.read_csv ("diabetes.csv") # first import the file in a dataframe just like a file object
print(df.head(15)) #allows to read first n rows of the data (5 is default)
# first row is represented by index 0
print(df.tail(10)) # reads the bottom 5 elements


temp_dict={'col1': [1, 2, 3], 'col2': [4, 5, 6]} # created a dictionary as data
dictdf=pd.DataFrame.from_dict(temp_dict) # creates a dataframe out of the dictionary
#now we can apply same functions in this dictionary same as in a csv file.
print(dictdf.head()) # will access the data of dictionary


print(df.columns) # gives all the column headings in a list
print(df.dtypes) # gives the datatype of columns

# summary statistics
print(df.describe) # only gives the summary of int and float column datatype
#print(df.describe (include="object"), errors ='ignore')  will also include object datatype
 

 #filtering columns
print(df.Glucose) # to access one column of the data
# print (df.['name of column']) this is used to access that column which has space in its name
print(df[["Outcome","SkinThickness","BloodPressure","Glucose"]]) # to access multiple columns at the same time
print(df.Outcome.unique()) # to print the unique values present in the valence column in the form of a list