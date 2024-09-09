from app import db

# 問い合わせ分類1のテーブル
class InquiryType1(db.Model):
    __tablename__ = 'inquiry_type1'
    __table_args__ = {'mysql_charset': 'utf8mb4'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    # 問い合わせ分類2とのリレーション
    types2 = db.relationship('InquiryType2', backref='type1', lazy=True)

# 問い合わせ分類2のテーブル
class InquiryType2(db.Model):
    __tablename__ = 'inquiry_type2'
    __table_args__ = {'mysql_charset': 'utf8mb4'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    type1_id = db.Column(db.Integer, db.ForeignKey('inquiry_type1.id'), nullable=False)

class Staff(db.Model):
    __tablename__ = 'staff'
    __table_args__ = {'mysql_charset': 'utf8mb4'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100))

class Status(db.Model):
    __tablename__ = 'status'
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True) 