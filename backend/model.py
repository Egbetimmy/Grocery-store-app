from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

class Products(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    unom_id = db.Column(db.Integer, db.ForeignKey('uom.unom_id'), nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)


class Order_details(db.Model):
    __tablename__ = 'order_details'

    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    unom_id = db.Column(db.Integer, db.ForeignKey('uom.unom_id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)


class uom(db.Model):
    __tablename__ = 'uom'

    uom_id = db.Column(db.Integer, primary_key=True, nullable=False)
    uom_name = db.Column(db.String, nullable=False)


class Orders(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    total = db.Column(db.Float, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Show id={self.id} artist_id={self.artist_id} venue_id={self.venue_id} start_time={self.start_time}"
