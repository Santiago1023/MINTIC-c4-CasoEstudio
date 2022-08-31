from models.student_model import StudentModel

class StudentController():
    def __init__(self):
        self.students = {
            "1": StudentModel(
                {
                    "id": "1",
                    "name": "Sebas",
                    "lastname": "Guti"
                }
            ),
            "2": StudentModel(
                {
                    "id": "2",
                    "name": "Jairo",
                    "lastname": "Ochoa"
                }
            )
        }
    def get(self):
        values = []
        for v in self.students.values():
            values.append(v.__dict__)
        return values
        
    def getById(self,id):
        #return filter(lambda x: x.id == id, students)   # filtreme el/los estudiantes que cumple con que x.id == id , le mandamos la lista
        return self.students.get(id, StudentModel({}))

    def create(self,data):
        #students.append(StudentModel(data))
        self.students[data['id']] = StudentModel(data)
        return self.students[data['id']]

    def update(self, id, data):
        student = self.students[id]
        for key, value in data.items():
            setattr(student, key, value)
            #student[key] = value 
    
    def delete(self,id):
        del self.students[id]

