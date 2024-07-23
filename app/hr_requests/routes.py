from flask import render_template, request, redirect, url_for
from app.hr_requests import bp
from .forms import HrRequestForm
from app.models.hr_request import Hr_Request
from app import db
from flask_login import current_user
from flask_login import login_required


@bp.route("/create/", methods=['GET', 'POST'])
@login_required
def create():
    
    form = HrRequestForm()

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body'] 

        try:
            hr_request = Hr_Request(title=title, body=body, author=current_user)
            db.session.add(hr_request)
            db.session.commit()
        except:
            pass
    else:
        return render_template('hr_requests/create.html', form=form)
    
    return redirect(url_for('hr_requests.index'))

@bp.route("/")
@login_required
def index():
    
    hr_r = Hr_Request.query.filter_by(author=current_user).order_by(Hr_Request.created.desc())
    return render_template("hr_requests/index.html", hr_r=hr_r)
