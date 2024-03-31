from school import School,ClassRoom, Subject
from persons import Student, Teacher


def main():
    school = School("ESS","DMD")

    seven = ClassRoom('seven')
    school.add_classroom(seven)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # print(school)

    # add students
    abul = Student('Abul Khan', seven)
    school.student_admission(abul)
    babul = Student('Babul Khan', seven)
    school.student_admission(babul)
    kabul = Student('kabul Khan', seven)
    school.student_admission(kabul)

    # subjects
    physics_teacher = Teacher('Shahjahan Tapon Rana')
    physics = Subject('physics', physics_teacher)
    seven.add_subject(physics)

    chemistry_teacher = Teacher('Haradon Nag')
    chemistry = Subject('chemistry', chemistry_teacher)
    seven.add_subject(chemistry)
    
    biology_teacher = Teacher('Azmal Sir')
    biology = Subject('biology', biology_teacher)
    seven.add_subject(biology)

    seven.take_semester_final()


    print(school)

if __name__ == "__main__":
    main()