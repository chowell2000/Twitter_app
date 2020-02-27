import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    """Twitter Users we will analyze

    Arguments:
        DB {string} -- User name
    """
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(20), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Tweet(DB.Model):
    """Tweets we pull to analyze

    Arguments:
        DB {string} -- Tweet text
    """
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'),
                        nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
