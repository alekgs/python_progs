import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from create_models import create_tables, Course, Homework

DSN = 'postgresql://postgres@localhost:5432/test'
engine = sq.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

#course1 = Course(name='PHP')
#session.add(course1)


#hw1 = Homework(number=1, description='Домашняя работа № 1', course_id=4)
#hw2 = Homework(number=2, description='Домашняя работа № 2', course_id=4)
#session.add_all([hw1, hw2])

for c in session.query(Course, Homework).join(Homework.course).filter(Course.name.like('Python')).all():
    print(*c)

# session.commit()
session.close()


