class DemoClass:
    def __init__(self) -> None:
        print("Called")

    def studentDetails(self, name, course, grade):
        self.name = name
        self.course = course
        self.grade = grade

        msg = f'STUDENT NAME: {self.name} \nSTUDENT COURSE: {self.course} \nGRADE: {self.grade}'
        print(msg)



classV1 = DemoClass()
classV2 = DemoClass()

classV1.studentDetails("Gem Rey", "BSIT", 98)
classV2.studentDetails("Menard", "BSIT", 89)


object_list = []
object_list.append(classV1)