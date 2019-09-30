from . import db


class Marker(db.Model):
    """
    Model for Marker
    """
    __tablename__ = 'marker'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(64),
                     index=False,
                     unique=True,
                     nullable=False)
    latitude = db.Column(db.Float,
                         index=False,
                         nullable=False)
    longitude = db.Column(db.Float,
                          index=False,
                          nullable=False)

    @property
    def serialize(self):
        """
        Serializer for Marker method, returns JSON serialize able object
        :return:
        """
        return {
            'id': self.id,
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    def __repr__(self):
        return '<Marker name: {}, latitude: {}, longitude: {}'.format(self.name, self.latitude, self.longitude)