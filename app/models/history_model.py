from app import db
from datetime import datetime
from sqlalchemy_utils import UUIDType

import uuid

class History(db.Model):
    __tablename__ = 'histories'
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(255), primary_key=True, nullable=False)
    
    # 問い合わせ分類1と2のマスターリレーションを追加
    history_type1 = db.Column(db.Integer, db.ForeignKey('inquiry_type1.id'), nullable=False)
    history_type2 = db.Column(db.Integer, db.ForeignKey('inquiry_type2.id'), nullable=False)
    
    inquiry_details = db.Column(db.String(255), nullable=False)

    # 正しく外部キー制約を設定
    contact_person = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    status = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    
    createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    # 外部キーでcustomerとリレーション
    customer_id = db.Column(UUIDType(binary=False), db.ForeignKey('customers.id'), nullable=False)
    
    # 双方向リレーション
    customer = db.relationship('Customer', back_populates='customer_histories')
    
    # マスターとのリレーション
    type1 = db.relationship('InquiryType1', backref='histories')
    type2 = db.relationship('InquiryType2', backref='histories')

    # 'primaryjoin' を使用して明示的にリレーションを定義
    contact_person_relation = db.relationship('Staff', backref='histories', primaryjoin="History.contact_person == Staff.id")
    status_relation = db.relationship('Status', backref='histories', primaryjoin="History.status == Status.id")
