import pytest
from app.db_queries import *

def test_staff(app):
	s = staff_insert('ganesh','c')
