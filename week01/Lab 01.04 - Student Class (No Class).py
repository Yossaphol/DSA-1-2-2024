"""student class"""
def main():
    """main"""
    name = []
    sex = []
    age = []
    id = []
    score = []
    for _ in range(3):
        name.append(input())
        sex.append(input())
        age.append(int(input()))
        id.append(input())
        score.append(float(input()))
    known = input()
    if not(known in id):
        print("Student not found")
    else:
        index = id.index(known)
        if sex[index] == 'Male':
            gender = 'Mr'
        else:
            gender = 'Miss'
        if len(str(score[index])) != 3:
            print(gender+' '+name[index]+' ('+str(age[index])+') '+'ID: '+id[index]+' GPA ' + str(score[index]))
        else:
            print(gender+' '+name[index]+' ('+str(age[index])+') '+'ID: '+id[index]+' GPA ' + str(score[index])+'0')
main()
