import pytest
from app.db_queries import *

def test_remove_staff():
	staffs = staff_query()
	#staff_list = list()
	for staff in staffs:
		#staff_list.append(staff.name)
		db.session.delete(staff)
	db.session.commit()	
