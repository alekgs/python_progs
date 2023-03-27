import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Course(Base):
    __tablename__ = "course"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):
        return f'Course {self.id}: {self.name}'


class Homework(Base):
    __tablename__ = "homework"

    id = sq.Column(sq.Integer, primary_key=True)
    number = sq.Column(sq.Integer, nullable=False)
    description = sq.Column(sq.Text, nullable=False)
    course_id = sq.Column(sq.Integer, sq.ForeignKey("course.id"), nullable=False)

    # связь с таблицей course по ForeignKey course.id и id в course
    course = relationship(Course, backref='homework')

    def __str__(self):
        return f'Homework {self.id}: ({self.description}, {self.course})'

def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
