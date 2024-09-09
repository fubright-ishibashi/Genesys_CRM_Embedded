from app import db
from app.master import InquiryType1, InquiryType2, Staff

# 担当者データの登録
def seed_staff():
    staff_members = [
        Staff(name='山本', department='営業'),
        Staff(name='石田', department='サポート'),
        Staff(name='斎藤', department='開発'),
        Staff(name='佐藤', department='サポート'),
        Staff(name='高橋', department='営業'),
        Staff(name='加藤', department='マーケティング'),
        Staff(name='鈴木', department='開発'),
        Staff(name='伊藤', department='サポート')
    ]
    for staff in staff_members:
        db.session.add(staff)
    db.session.commit()

# 問い合わせ分類データの登録
def seed_inquiry_types():
    inquiry_type1 = [
        InquiryType1(name='操作問い合わせ'),
        InquiryType1(name='不具合問い合わせ'),
        InquiryType1(name='要望')
    ]

    inquiry_type2 = [
        InquiryType2(name='Windows', parent_id=1),  # 操作問い合わせに関連
        InquiryType2(name='Office365', parent_id=1),
        InquiryType2(name='スマートフォン', parent_id=1),
        InquiryType2(name='その他', parent_id=1),
        InquiryType2(name='PC不具合', parent_id=2),  # 不具合問い合わせに関連
        InquiryType2(name='Windows不具合', parent_id=2),
        InquiryType2(name='スマートフォン不具合', parent_id=2),
        InquiryType2(name='その他', parent_id=2),
        InquiryType2(name='PC交換', parent_id=3),  # 要望に関連
        InquiryType2(name='Windowsアップグレード', parent_id=3),
        InquiryType2(name='スマートフォン交換', parent_id=3),
        InquiryType2(name='その他', parent_id=3)
    ]

    for it1 in inquiry_type1:
        db.session.add(it1)

    for it2 in inquiry_type2:
        db.session.add(it2)

    db.session.commit()

# 実行用関数
def seed_all():
    seed_staff()
    seed_inquiry_types()

if __name__ == '__main__':
    seed_all()
