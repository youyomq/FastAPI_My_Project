from uuid import UUID

from src.repositories.mappers.mappers import StudentDataMapper, TeacherDataMapper, StudentWithTeachersDataMapper, \
    TeacherWithStudentsDataMapper
from src.schemas.students import StudentAdd
from src.schemas.students_teachers import StudentTeacherRequestAdd, StudentTeacherJoinAdd, StudentsWithTeachersLists
from src.schemas.teachers import TeacherAdd
from src.services.base import BaseService

class StudentTeacherService(BaseService):
    async def get_students_teachers(self, students_ids: list[UUID], teachers_ids: list[UUID]):
        if students_ids:
            student_with_teachers_models = await self.db.students.get_student_with_teachers(student_ids=students_ids)
            student_with_teachers = list(map(StudentWithTeachersDataMapper.map_to_domain_entity, student_with_teachers_models))

        if teachers_ids:
            teacher_with_students_models = await self.db.teachers.get_teacher_with_students(teachers_ids=teachers_ids)
            teacher_with_students = list(map(TeacherWithStudentsDataMapper.map_to_domain_entity, teacher_with_students_models))

        teachers_with_students_lists = StudentsWithTeachersLists(students=student_with_teachers, teachers=teacher_with_students)

        return teachers_with_students_lists

    async def add_student_teacher(self, student_teacher_data: StudentTeacherRequestAdd):
        student_to_add = StudentAdd(**student_teacher_data.student.model_dump(exclude_unset=True))
        added_student = await self.db.students.add(data=student_to_add)
        mapped_student = StudentDataMapper.map_to_domain_entity(added_student)

        teacher_to_add = TeacherAdd(**student_teacher_data.teacher.model_dump(exclude_unset=True))
        added_teacher = await self.db.teachers.add(data=teacher_to_add)
        mapped_teacher = TeacherDataMapper.map_to_domain_entity(added_teacher)

        student_teacher_added = StudentTeacherJoinAdd(teacher_id=mapped_teacher.id, student_id=mapped_student.id)
        print(student_teacher_added)
        await self.db.students_teachers.add(data=student_teacher_added)

        students_list = student_teacher_data.teacher.students
        teachers_list = student_teacher_data.student.teachers

        if teachers_list:
            for teacher_id in teachers_list:
                print(teachers_list, teacher_id)
                student_teacher = StudentTeacherJoinAdd(student_id=mapped_student.id, teacher_id=teacher_id)
                await self.db.students_teachers.add(student_teacher)

        if students_list:
            for student_id in students_list:
                student_teacher = StudentTeacherJoinAdd(student_id=student_id, teacher_id=mapped_teacher.id)
                await self.db.students_teachers.add(student_teacher)

    async def edit_student_teacher(self, student_teacher_data: StudentTeacherRequestAdd, record_child_id: int):
        ...

    async def delete_students_teachers(self, students_ids: list[UUID], teachers_ids: list[UUID]):
        ...