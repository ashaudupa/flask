from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,validators,IntegerField
from wtforms.validators import DataRequired

class StaffForm(Form):
	name = StringField(label="Name", validators=[validators.Length(max=64),DataRequired()])
	skill = StringField(label = "Skill", validators = [validators.Length(max=20),DataRequired()])
	submit = SubmitField("send")

class TaskForm(Form):
	name = StringField("name",validators=[validators.Length(max=64),DataRequired()])
	client = StringField("client",validators=[validators.Length(max=20),DataRequired()])
	capabilities = StringField("capabilities",validators=[validators.Length(max=40),DataRequired()])
	duration = IntegerField("duration",validators=[validators.NumberRange(min=0,max=100),DataRequired()])
	submit = SubmitField("send")

class SkilledstaffForm(Form):
	task_name = StringField("task_name",validators = [validators.Length(max=64),DataRequired()])
	assign = SubmitField("assign")
