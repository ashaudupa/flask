import pytest
from app.db_queries import *
def test_task(app):
	t = task_insert('testing','acd','python',5)
	
	
