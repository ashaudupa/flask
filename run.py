#!flask/bin/python
from factory import app

#create application
#app = create_app('BaseConfigeration')

from app.views import home,staff_blue,task_blue,result

app.register_blueprint(home)
app.register_blueprint(staff_blue)
app.register_blueprint(task_blue)
app.register_blueprint(result)


app.run(debug=True)
