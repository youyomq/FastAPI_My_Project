from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.students import StudentsTeachersRepository
from src.repositories.students import StudentsRepository
from src.repositories.teachers import TeachersRepository
from src.schemas.students import Student, Students
from src.schemas.students_teachers import StudentsTeachers
from src.schemas.teachers import Teacher, Teachers
from src.repositories.mappers.mappers import StudentWithTeachersDataMapper, \
    TeacherWithStudentsDataMapper
from src.schemas.students import StudentCreate
from src.schemas.students_teachers import StudentTeacherCreateRequest, StudentTeacherJoinCreate, \
    StudentsWithTeachersLists, StudentTeacherListsJoinCreate
from src.schemas.teachers import TeacherCreate
from src.services.base import BaseService

class StudentTeacherService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(db)
        self.students_repository = StudentsRepository(db)
        self.teachers_repository = TeachersRepository(db)
        self.students_teachers_repository = StudentsTeachersRepository(db)
    
    async def get_students_teachers(self, students_ids: list[UUID], teachers_ids: list[UUID]):
        if students_ids and teachers_ids:
            student_with_teachers_models = await self.students_repository.get_student_with_teachers(student_ids=students_ids)
            student_with_teachers = list(map(StudentWithTeachersDataMapper.map_to_domain_entity, student_with_teachers_models))

            teacher_with_students_models = await self.teachers_repository.get_teacher_with_students(teachers_ids=teachers_ids)
            teacher_with_students = list(map(TeacherWithStudentsDataMapper.map_to_domain_entity, teacher_with_students_models))

            teachers_with_students_lists = StudentsWithTeachersLists(students=student_with_teachers, teachers=teacher_with_students)

            await self.db.commit()
            return teachers_with_students_lists
        elif students_ids:
            student_with_teachers_models = await self.students_repository.get_student_with_teachers(student_ids=students_ids)
            student_with_teachers = list(map(StudentWithTeachersDataMapper.map_to_domain_entity, student_with_teachers_models))

            teachers_with_students_lists = StudentsWithTeachersLists(students=student_with_teachers)

            await self.db.commit()
            return teachers_with_students_lists
        elif teachers_ids:
            teacher_with_students_models = await self.teachers_repository.get_teacher_with_students(teachers_ids=teachers_ids)
            teacher_with_students = list(map(TeacherWithStudentsDataMapper.map_to_domain_entity, teacher_with_students_models))

            teachers_with_students_lists = StudentsWithTeachersLists(teachers=teacher_with_students)

            await self.db.commit()
            return teachers_with_students_lists

    async def create_student_teacher(self, student_teacher_data: StudentTeacherCreateRequest):
        student_to_add = StudentCreate(**student_teacher_data.student.model_dump(exclude_unset=True))
        created_student_model = await self.students_repository.create(data=student_to_add)
        created_student = Student.model_validate(created_student_model, from_attributes=True)

        teacher_to_add = TeacherCreate(**student_teacher_data.teacher.model_dump(exclude_unset=True))
        created_teacher_model = await self.teachers_repository.create(data=teacher_to_add)
        created_teacher = Teacher.model_validate(created_teacher_model, from_attributes=True)

        student_teacher_to_add = StudentTeacherJoinCreate(teacher_id=created_teacher_model.id, student_id=created_student.id)
        await self.students_teachers_repository.create(data=student_teacher_to_add)

        students_list = student_teacher_data.teacher.students
        teachers_list = student_teacher_data.student.teachers

        created_students_teachers_from_lists = []

        if teachers_list:
            for teacher_id in teachers_list:
                teacher_model = await self.teachers_repository.get_one_or_none(id=teacher_id)

                if teacher_model:
                    student_teacher = StudentTeacherJoinCreate(student_id=created_student.id, teacher_id=teacher_id)
                    await self.students_teachers_repository.create(student_teacher)

                    created_students_teachers_from_lists.append(student_teacher)

        if students_list:
            for student_id in students_list:
                student_model = await self.students_repository.get_one_or_none(id=student_id)

                if student_model:
                    student_teacher = StudentTeacherJoinCreate(student_id=student_id, teacher_id=created_teacher.id)
                    await self.students_teachers_repository.create(student_teacher)

                    created_students_teachers_from_lists.append(student_teacher)

        created_students_with_teachers = StudentTeacherListsJoinCreate(student=created_student.model_dump(), teacher=created_teacher.model_dump(), students_teachers=created_students_teachers_from_lists)

        await self.db.commit()
        return created_students_with_teachers

    async def edit_student_teacher(self, student_teacher_data: StudentTeacherCreateRequest, teacher_id: UUID, student_id: UUID):
        await self.students_teachers_repository.delete_by_fks(students_ids=[student_id], teachers_ids=[teacher_id])

        student_to_update = StudentCreate(**student_teacher_data.student.model_dump(exclude_unset=True))
        updated_student_model = await self.students_repository.edit_one(data=student_to_update, id=student_id)
        updated_student = Student.model_validate(updated_student_model, from_attributes=True)

        teacher_to_update = TeacherCreate(**student_teacher_data.teacher.model_dump(exclude_unset=True))
        updated_teacher_model = await self.teachers_repository.edit_one(data=teacher_to_update, id=teacher_id)
        updated_teacher = Teacher.model_validate(updated_teacher_model, from_attributes=True)


        students_list = student_teacher_data.teacher.students
        teachers_list = student_teacher_data.student.teachers

        created_students_teachers_from_lists = []

        if students_list:
            for s_id in students_list:
                student_model = await self.students_repository.get_one_or_none(id=s_id)

                if student_model:
                    student_teacher = StudentTeacherJoinCreate(student_id=s_id, teacher_id=teacher_id)
                    await self.students_teachers_repository.create(student_teacher)

                    created_students_teachers_from_lists.append(student_teacher)

        if teachers_list:
            for t_id in teachers_list:
                teacher_model = await self.teachers_repository.get_one_or_none(id=t_id)

                if teacher_model:
                    student_teacher = StudentTeacherJoinCreate(student_id=student_id, teacher_id=t_id)
                    await self.students_teachers_repository.create(student_teacher)

                    created_students_teachers_from_lists.append(student_teacher)


        updated_students_with_teachers = StudentTeacherListsJoinCreate(student=updated_student.model_dump(),
                                                                       teacher=updated_teacher.model_dump(),
                                                                       students_teachers=created_students_teachers_from_lists)

        await self.db.commit()
        return updated_students_with_teachers

    async def delete_students_teachers(self, students_ids: list[UUID], teachers_ids: list[UUID]):
        deleted_students_model = await self.students_repository.delete_all_in_list(students_ids)
        deleted_students_schema = Students(students=deleted_students_model)

        deleted_students = Students.model_validate(deleted_students_schema, from_attributes=True)

        for student in deleted_students.students:
            await self.students_teachers_repository.delete_all(student_id=student.id)

        deleted_teachers_model = await self.teachers_repository.delete_all_in_list(teachers_ids)
        deleted_teachers_schema = Teachers(teachers=deleted_teachers_model)

        deleted_teachers = Teachers.model_validate(deleted_teachers_schema, from_attributes=True)

        for teacher in deleted_teachers.teachers:
            await self.students_teachers_repository.delete_all(student_id=teacher.id)

        deleted_students_teachers = StudentsTeachers(students=deleted_students.model_dump(), teachers=deleted_teachers.model_dump())

        await self.db.commit()
        return deleted_students_teachers
