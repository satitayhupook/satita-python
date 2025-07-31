"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Toey", 19, "Chonburi", "Thailand")  # name, age, city, country
    hobbies = []

    # Your code here
    print("1 Display into, 2 Add hobby, 3 Remove, 4 Edit age, 5 Exit")
    choice = input("What do you want to do?: ")

    if choice == "1":
      print("name: ",person[0])
      print("age: ",person[1])
      print("city: ",person[2])
      print("country: ",person[3])
      print("hobbies: ",hobbies)

    elif choice == "2":
      hobby = input("insert new hobbies: ")
      hobbies.append(hobby)

    elif choice == "3":
      del hobbies[0]
    
    elif choice == "4":
      age = input("insert new age: ")
      person_list = list(person)
      person_list[1] = age
      person = tuple(person_list)
    
    elif choice == "5":
      exit(0)
    
    pass

if __name__ == "__main__":
    personal_info_manager()