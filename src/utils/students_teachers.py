async def get_student_with_teachers_utils():
    student_with_teachers_models = await db.students.get_student_with_teachers(student_ids=students_ids)
    student_with_teachers = list(map(StudentWithTeachersDataMapper.map_to_domain_entity, student_with_teachers_models))