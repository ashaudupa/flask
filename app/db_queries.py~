#from factory import db
from app.models import db
from models import Staff,Task
from sqlalchemy.exc import IntegrityError

def staff_insert(name,skill):
	s = staff_query()
	s_id = 1
	if s != []:
		s.sort()
		s_id = s[-1].id + 1
	name_up = name.encode('ascii','ignore').upper()
	skill_up = skill.encode('ascii','ignore').upper()
	staff = Staff(s_id,name_up,skill_up)
	try:	
		db.session.add(staff)
		db.session.commit()
		db.session.flush()
		return "Staff is added successfully"
	except:
		db.session.rollback()
		return "Staff Name is already exists "
				
def staff_query():
	staff = Staff.query.all()
	return staff	
	

def staff_filter_query(skill):
	return Staff.query.filter(Staff.skill == skill).all()
			
def staff_delete():
	staffs = staff_query()
	if staffs == []:
		print "No items in the table"
	else:
		try:
			for staff in staffs:
				db.session.delete(staff)
			db.session.commit()	
		except:
			db.session.rollback()
			#raise:
		#finally:
		#	db.session.close()	
	
def task_insert(name,client,skill,duration):
	t = task_query()
	t_id = 1
	if t != []:
		t.sort()
		t_id = t[-1].id + 1
		
	task_name = name.encode('ascii','ignore').upper()
	task_client = client.encode('ascii','ignore').upper()
	task_capabilities = skill.encode('ascii','ignore').upper()
	task_duration = int(duration)	
	
	try:
		task = Task(t_id,task_name,task_client,task_capabilities,task_duration)
		db.session.add(task)
		db.session.commit()
		db.session.flush()
		return "Task Entry successfully done"
	except:
		db.session.rollback()
		return "Task name already exits"		
		
		
def task_query():
	tasks = Task.query.all()
	return tasks
		
def task_filter_query(task_name):
	task_name = task_name.encode('ascii','ignore')
	task_name = task_name.upper()
	return Task.query.filter(Task.name == task_name).all()
	
def task_delete():
	tasks = task_query()
	if tasks == []:
		print "Task table is empty "
	else:
		try:	
			for task in tasks:
				db.session.delete(task)
			db.session.commit()
		except:
			db.session.rollback()
	
					
		
	
