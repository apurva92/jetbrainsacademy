from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()
engine = create_engine('sqlite:///todo.db?check_same_thread=False')


class ToDoList(Base):
	__tablename__ = 'task'
	id = Column(Integer, primary_key=True)
	task = Column(String, default='default_task')
	deadline = Column(Date, default=datetime.today().date())

	def __repr__(self):
		return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def todaystasks():
	todays_date = datetime.today().date()
	count = 1
	rows = session.query(ToDoList).filter(ToDoList.deadline == todays_date).all()
	print(todays_date.strftime('%A %d %B'))
	if len(rows) > 0:
		for row in rows:
			print(f'{count}. {row.task}')
			count += 1
	else:
		print('Nothing to do!')


def weektask():
	for i in range(7):
		count = 1
		todays_date = datetime.today().date()
		new_date = todays_date + timedelta(days=i)
		print(new_date.strftime('%A %d %B') + ':')
		rows = session.query(ToDoList).filter(ToDoList.deadline == new_date).all()
		if len(rows) > 0:
			for row in rows:
				print(f'{count}. {row.task}')
				count += 1
		else:
			print('Nothing to do!')
		print()


def alltasks():
	count = 1
	print('All tasks:')
	rows = session.query(ToDoList).order_by(ToDoList.deadline).all()
	if len(rows) > 0:
		for row in rows:
			d = row.deadline.strftime('%d %b')
			print(f'{count}. {row.task}. {d}')
			count += 1
	else:
		print('Nothing to do!')


def missedtasks():
	count = 1
	todays_date = datetime.today().date()
	print('Missed tasks:')
	rows = session.query(ToDoList).filter(ToDoList.deadline < todays_date).order_by(ToDoList.deadline).all()
	if len(rows) > 0:
		for row in rows:
			d = row.deadline.strftime('%d %b')
			print(f'{count}. {row.task}. {d}')
			count += 1
	else:
		print('Nothing to do!')


def addtask():
	print('Enter task')
	new_task = input()
	print('Enter deadline')
	new_deadline = input()
	new_row = ToDoList(task=new_task, deadline=datetime.fromisoformat(new_deadline).date())
	session.add(new_row)
	session.commit()
	print('The task has been added!')


def deletetask():
	print('Chose the number of the task you want to delete:')
	rows = session.query(ToDoList).order_by(ToDoList.deadline).all()
	if len(rows) > 0:
		for row in rows:
			d = row.deadline.strftime('%d %b')
			print(f'{row.id}. {row.task}. {d}')
		c = int(input())
		session.query(ToDoList).filter(ToDoList.id == c).delete()
		print('The task has been deleted!')
		session.commit()
	else:
		print('Nothing to do!')


while True:
	print("1) Today's tasks")
	print("2) Week's tasks")
	print('3) All tasks')
	print('4) Missed tasks')
	print('5) Add task')
	print('6) Delete task')
	print('0) Exit')
	choice = int(input())
	if choice == 1:
		print()
		todaystasks()
		print()
	elif choice == 2:
		print()
		weektask()
	elif choice == 3:
		print()
		alltasks()
		print()
	elif choice == 4:
		print()
		missedtasks()
		print()
	elif choice == 5:
		print()
		addtask()
		print()
	elif choice == 6:
		print()
		deletetask()
		print()
	elif choice == 0:
		print('\nBye!')
		break
