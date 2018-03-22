from . import db


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    biography = db.Column(db.String(1024))
    upload = db.Column(db.String(80))
    userid = db.Column(db.String(80))
    created_on = db.Column(db.String(80))
    
    
    def __init__(self, firstname, lastname, email, location, gender, biography, upload, userid, created_on):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.gender = gender
        self.biography = biography
        self.upload = upload
        self.userid = userid
        self.created_on = created_on
        
    

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)