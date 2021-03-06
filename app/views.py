from app.models import Staff,Task,db
from app.db_queries import *
from flask import render_template,request,flash,jsonify,current_app,Blueprint
from forms import StaffForm,TaskForm,SkilledstaffForm
#from factory import db

home = Blueprint('Home',__name__,template_folder = 'templates')
@home.route('/')


def index():
	return render_template('index.html',title='home')


staff_blue = Blueprint('staff_blue',__name__,template_folder = 'templates')
@staff_blue.route('/staff',methods = ['GET','POST'])	

def staff():
	form = StaffForm()
	if request.method == 'POST':
		if form.validate()== False:
			flash("All fields are required ")
			return render_template("details.html",form=form)	
		else:
			
			insert_msg = staff_insert(form.name.data,form.skill.data)
			return jsonify(name = form.name.data,skill = form.skill.data,result = insert_msg)
			#return render_template("success.html",form=form)
	elif request.method == 'GET':
		return render_template('details.html',form=form)
		

#blueprint for Task
task_blue = Blueprint('task_blue',__name__,template_folder='templates')
@task_blue.route('/task',methods=['GET','POST']) 
#@flask_obj.route('/task',methods = ['GET','POST'])

def task():
	form = TaskForm()
	if request.method == "POST":
		if form.validate() == False:
			flash("All fields are required")
			return render_template("task.html",form=form)
		else:
			
			task_name = form.name.data
			task_client = form.client.data
			task_capabilities = form.capabilities.data
			task_duration = int(form.duration.data)
			#insert values to Task table
				
			task_msg = task_insert(task_name,task_client,task_capabilities,task_duration)
				
                         
			
			return jsonify(name =task_name,
					client=task_client, 
					capabilities=task_capabilities,
					duration=task_duration,result = task_msg)
			#return render_template("success.html",form=form)
	elif request.method == 'GET':
		return render_template("task.html",form=form)
		

#Blueprint for result form
result = Blueprint('result',__name__,template_folder='templates')
@result.route('/skilled_staff',methods = ['GET','POST'])
#@flask_obj.route('/skilled_staff',methods = ['GET','POST'])

def skilled_staff():
	form = SkilledstaffForm()
	staff_list = list()
	task_list = list()
	tasks = task_query()
	if tasks is None:
		flash ("Task table is Empty")
	for task in tasks:
		task_list.append(task.name)

	if request.method == 'POST':
		if form.validate() == False:
			flash('Please provide the task name from the list below')
			return render_template("result.html",form=form,task_list=task_list)
		else:
			task_name = form.task_name.data

			if task_name not in task_list:
				flash('Task name not included in the list')
				return jsonify(requested_task_name=task_name,status=False,message = "Task not in list",task_list=task_list)         
				#return render_template("result.html",form=form,task_list=task_list)      
				   
			skill_needed = task_filter_query(Task.name,task_name)[0].capabilities
			
			working_staffs = staff_filter_query(Staff.skill,skill_needed)
			
			if working_staffs == []:
				flash('No skilled staff for this Task!')
			
			for staff in working_staffs:
				staff_list.append(staff.name)
			return jsonify(requested_task_name=task_name,status = True,message = '',staff_list=staff_list)
			#return render_template("result.html",form=form,staff_list=staff_list,task_name=task_name)
	elif request.method =='GET':
		task_list = list()
		tasks = task_query()
		for task in tasks:
			task_list.append(task.name)
		return render_template("result.html",form=form,task_list = task_list)
    		


		


