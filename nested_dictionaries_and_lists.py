
# 1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# TODO: 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x[1][0] = 15
print("x = ", x, "\n")

# TODO: 2. Change the last_name of the first student from 'Jordan' to 'Bryant'

students[0]['last_name'] = "Bryant"
print("students = \n", *students, sep = "\n"), "\n"

# TODO: 3. In the sports_directory, change 'Messi' to 'Andres'

sports_directory['soccer'][0] = 'Andres'
print("\n","soccer : ",sports_directory['soccer'],"\n")

# TODO: 4. Change the value 20 in z to 30

z[0]['y'] = 30
print("z = ",z)
print("\n")


# 2. Iterate Through a List of Dictionaries

# TODO: Create a function iterateDictionary(some_list) that,
# given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# * first_name - Michael, last_name - Jordan
# * first_name - John, last_name - Rosales
#* first_name - Mark, last_name - Guillen
# * first_name - KB, last_name - Tonel

def iterate_dictionary(list):
    print("students = ", "\n")
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val}"
        print(output)

iterate_dictionary(students)
print("\n")


# 3. Get Values From a List of Dictionaries

# TODO: Create a function iterateDictionary2(key_name, some_list) that,
# given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
# For example, iterateDictionary2('first_name', students) should output:

# * Michael
# * John
# * Mark
# * KB

# TODO: And iterateDictionary2('last_name', students) should output:

# * Jordan
# * Rosales
# * Guillen
# * Tonel

def iterate_dictionary2(key_name,some_list):
    for i in range(0, len(some_list)):

        for key,val in some_list[i].items():
            if key == key_name:
                print(val)
iterate_dictionary2('first_name', students)
print("\n")
iterate_dictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values

# TODO: Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
# prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    for key,val in some_dict.items():
        print("\n")
        print("--------------")
        print(f"{len(val)} {key.upper()}", ":","\n")
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)

# output:
# * 7 LOCATIONS
# * San Jose
# * Seattle
# * Dallas
# * Chicago
# * Tulsa
# * DC
# * Burbank

# 8 INSTRUCTORS
# * Michael
# * Amy
# * Eduardo
# * Josh
# * Graham
# * Patrick
# * Minh
# * Devon
