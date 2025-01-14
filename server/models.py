from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Metadata for table reflection
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

# Define Earthquake model
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"  # Table name should be lowercase and consistent

    # Define columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String, nullable=False)  # Fix typo in 'location'
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
