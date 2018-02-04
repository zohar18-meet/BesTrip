from init import *
from flask import Flask, request, url_for, render_template, redirect

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
#heroku = Heroku(app)


# #access data
# trips=db.session.query(Trip).all()  #filter_by(area='golan').filter_by(difficulty=2).all()
# for trip in trips:
#     print(trip.area)
#     print(trip.difficulty)

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trips/<trips>')
@app.route('/trips')
def trips(trips=None):
    print(trips)
    return render_template('trips.html',trips=trips)

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/results/<trip_id>')
def results(trip_id):
    trip = Trip.query.filter_by(id=trip_id).first()
    return render_template('results.html',trip=trip)

@app.route('/filter', methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        area=request.form['area']
        difficulty=request.form['difficulty']
        trips = Trip.query.filter_by(area=area, difficulty=difficulty).all()
        return render_template('trips.html', trips=trips)

@app.route('/trip/<trip_id>')
def trip(trip_id):
    trip1=db.session.query(Trip).filter_by(id=trip_id).all()
    return render_template('trip.html')

# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    #app.debug = True
    app.run(debug=True)