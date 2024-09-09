from app import db
from datetime import datetime
from sqlalchemy_utils import UUIDType

import uuid
import sqlalchemy_utils

class Customer(db.Model):
    __tablename__ = 'customers'
    __table_args__ = {'mysql_charset': 'utf8mb4'}
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    customer_name = db.Column(db.String(255), nullable=False)
    division_name = db.Column(db.String(255), nullable=False)
    manager_name = db.Column(db.String(255), nullable=False)
    post_code = db.Column(db.String(255), nullable=False)
    telephone_number = db.Column(db.String(255), nullable=False)
    cellphone_number = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    fax_address = db.Column(db.String(255), nullable=False)
    mail_address = db.Column(db.String(255), nullable=False)
    customer_lank = db.Column(db.String(255), nullable=False)
    memo = db.Column(db.String(255), nullable=False)
    
    createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    # 双方向リレーションを 'back_populates' でリンク
    customer_histories = db.relationship('History', back_populates='customer')
