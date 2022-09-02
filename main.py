import statistics
import math as M
import random

def Question1():
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    ages.sort() #using sort method to sort
    min = ages[0]
    max = ages[-1]
    print("max",max)
    print("min",min)
    ages.append(min)#append min value
    ages.append(max) # append the max value again
    print("median",statistics.median(ages))
    print("Average",sum(ages)/len(ages))
    print("Range",max-min)

def Question2():
    dog={}# creating new dictionary
    dog = {"name", "color", "breed", "legs", "age"} # taking values to the set
    student = {"first_name":[], "last_name":[], "gender":[], "age":[], "marital status":[],
           "skills":[], "country":[], "city":[] , "address":[]}
    print(len(student))
    # appending new values in the set
    student["skills"].append("Python")
    student["skills"].append("Java")
    # converting and printing the values using list function
    keysList = list(student.keys())
    valueList = list(student.values())
    print(keysList)
    print(valueList)

def Question3():
    #creating new tuple
    myBrothers = ("John", "Oman")
    mySysters = ("Bonny", "Cherry")
    # adding two tuples
    mySiblings = myBrothers+mySysters
    print(len(mySiblings))
    # added the name Father and the Mother in the new tuple . these are imaginary names
    myfamily_member = mySiblings+("Father","Mother")
    print(myfamily_member)


def Question4():
    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    age = [22, 19, 24, 25, 26, 24, 25, 24]
    print(len(it_companies))
    it_companies.add("Twitter")
    # adding two new name to new set
    it_companies2 = {"TCS","Databricks"}
    it_companies.update(it_companies2)
    # remove by the element
    it_companies.remove("TCS")
    it_companies.discard("Google")
    # The remove() method will raise an error if the specified item does not exist but  the discard() method will not.
    C = A.union(B)
    print(A.intersection(B))
    print(A.intersection(B))
    print(A.issubset(B))
    print(A.isdisjoint(B))
    #deleting the A set
    A.clear()
    set_age = set(age)
    print("Set Length: ", len(set_age)," List Length:  ", len(age))


def Question5():
    radius = 30
    #imported the math as M to get the pi value
    _area_of_circle_ = M.pi * radius* radius
    _circum_of_circle_ = 2 * M.pi * radius
    #user input to a new radius
    r = input("Enter Radius:")
    area = M.pi * float(r) * float(r)
    print("Area with user input",area )

def Question6():
    st = "I am a teacher and I love to inspire and teach people"
    unique = {" "}
    words = st.split(" ")
    #created for lopp to get the values and the add to the set
    for word in words:
        if word not in unique:
            unique.add(word)
    print(len(unique)) # only printing the length of the unique words

def Question7():
    #used \t and the \n to saperate tab and the new line respectively
    print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
def Question8():
    radius = 10
    area = 3.14 * radius ** 2
    txt = "For only {radius:.2f} dollars!""For only {price:.2f} dollars!"
    txt = "The area of a circle with radius {radius: d} is {area:.2f} meters square"
    #used the .format method to formating
    print(txt.format(radius = radius, area = area))

def Question9():
    #taking 0  and X values as classes
    class_1 = "O"
    class_2 = "X"
    result = []
    K = 3
    # makeing feture values with class 0 and X
    feature = [(1, class_1), (2, class_1), (3, class_2), (6, class_2), (6, class_2), (7, class_1), (10, class_1),
                     (11, class_1)]
    # taking random mathod to make machine suflle all the data and devide then into test and train data
    random.shuffle(feature)
    n = len(feature)


    train = feature[:n // 2]
    test = feature[n // 2:]

    for _feature, _class in test:
        distance = []
        for _f, _c in train:
            distance.append((abs(_feature - _f), _c))

        nearest_neighbors = sorted(distance)[:K]

        count_X = 0
        count_O = 0
        for _, _cls in nearest_neighbors:
            if _cls == class_2:
                count_X += 1
            else:
                count_O += 1

        if count_X > count_O:
            result.append((_feature, class_2))
        else:
            result.append((_feature, class_1))

    print(result)
    # creating confution matix Part 2 question
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for i in range(len(result)):
        if result[i][1] == "O":
            if result[i][1] == test[i][1]:
                TP += 1
            else:
                FP += 1
        elif result[i][1] == "X":
            if result[i][1] == test[i][1]:
                TN += 1
            else:
                FN += 1

    # printing confution matrix
    matrix = [[TP, FN], [FP, TN]]
    print(matrix)

    # calculate accuracy, sensitivity and specificity values
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    sensitivity = TP / (TP + FN)
    specificity = TN / (TN + FP)






if __name__ == '__main__':
    Question1()
    Question2()
    Question3()
    Question4()
    Question5()
    Question6()
    Question7()
    Question8()
    Question9()



