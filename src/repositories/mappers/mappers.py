from src.schemas.customers_orders import CustomerOrdersGet
from src.schemas.students_teachers import StudentTeacherJoin, StudentWithTeachers, TeacherWithStudents
from src.schemas.orders import Order
from src.models.orders import OrdersOrm
from src.schemas.customers import Customer
from src.models.customers import CustomersOrm
from src.models.students import StudentsOrm, StudentsTeachersOrm
from src.schemas.students import Student
from src.models.teachers import TeachersOrm
from src.models.drivers import DriversOrm
from src.models.licenses import LicensesOrm
from src.schemas.teachers import Teacher
from src.schemas.licenses import LicenseAdd
from src.repositories.mappers.base import DataMapper
from src.schemas.drivers import DriverAdd


class DriverDataMapper(DataMapper):
    db_model = DriversOrm
    schema = DriverAdd

class LicenseDataMapper(DataMapper):
    db_model = LicensesOrm
    schema = LicenseAdd

class TeacherDataMapper(DataMapper):
    db_model = TeachersOrm
    schema = Teacher

class StudentDataMapper(DataMapper):
    db_model = StudentsOrm
    schema = Student

class StudentTeacherJoinDataMapper(DataMapper):
    db_model = StudentsTeachersOrm
    schema = StudentTeacherJoin

class StudentWithTeachersDataMapper(DataMapper):
    db_model = StudentsOrm
    schema = StudentWithTeachers

class TeacherWithStudentsDataMapper(DataMapper):
    db_model = TeachersOrm
    schema = TeacherWithStudents

class CustomerDataMapper(DataMapper):
    db_model = CustomersOrm
    schema = Customer

class OrderDataMapper(DataMapper):
    db_model = OrdersOrm
    schema = Order

class CustomerOrdersDataMapper(DataMapper):
    db_model = CustomersOrm
    schema = CustomerOrdersGet

