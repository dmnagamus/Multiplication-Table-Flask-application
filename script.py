from flask import *
app = Flask(__name__)

@app.router('/table/<int:num>')
def table(num):
	return render_tenplate('print-table.html',n=num)
if__name__ == '__main__' :
app.run(debug = True)
