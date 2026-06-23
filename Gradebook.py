#From Codecademy's Learn Python 3 course in Lists Section

last_semester_gradebook = [["Politics", 80], ["Latin", 96], ["Dance", 97], ["Architecture", 65]]

# Your code below: 
subjects= ["Physics","Calculus","Poetry","History"]
grades= [98,97,85,88] #grades for each class in subjects list above

#created full gradebook list that includes sublists of said subjects
gradebook= [
  ["Physics",98],
  ["Calculus",97],
  ["Poetry",85],
  ["History",88]
]

#modifying sublists
gradebook.append(["Computer Science",100]) #added sublist w/ computer science & 100
gradebook.append(["Visual Arts",93]) #added sublist w/ visual arts & 93
gradebook[5][1]= 98 #changed value of visual arts to 98
gradebook[2].remove(85) #removed 85 value in poetry class
gradebook[2].append("Pass") #added Pass string to poetry class

#combines two different lists to gradebook list to create a full gradebook
full_gradebook= last_semester_gradebook + gradebook
print(full_gradebook)