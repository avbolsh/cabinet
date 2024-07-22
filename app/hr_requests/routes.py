from flask import render_template, request, redirect, url_for
from app.hr_requests import bp
from .forms import HrRequestForm
from app.models.hr_request import Hr_Request
from app import db



@bp.route("/create/", methods=['GET', 'POST'])
def create():
    
    form = HrRequestForm()

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body'] 

        try:
            hr_request = Hr_Request(title=title, body=body)
            db.session.add(hr_request)
            db.session.commit()
        except:
            pass
    else:
        return render_template('hr_requests/create.html', form=form)
    
    return redirect(url_for('hr_requests.index'))

@bp.route("/")
def index():
    
    q = request.args.get("q")

    if q:
        hr_r = Hr_Request.query.filter(Hr_Request.title.contains(q) | 
                                  Hr_Request.body.contains(q))
    else:
        hr_r = Hr_Request.query.order_by(Hr_Request.created.desc())
    
    return render_template("hr_requests/index.html", hr_r=hr_r)
