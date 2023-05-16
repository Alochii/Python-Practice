student_scores = {
    "Harry" : 81,
    "Ron" : 1,
    "Hemione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}
student_marks = {}
gradelist = [0,60,70,80,90]
marklist = ["F","D","C","B","A"]
for _ in student_scores:
    for rank in range(5):
        if student_scores[_] > gradelist[rank]:
            temp = marklist[rank]
    student_marks[_] = temp   


for _ in student_marks:
    print (_)
    print(student_marks[_])
    
