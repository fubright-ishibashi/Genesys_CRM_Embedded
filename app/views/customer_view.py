from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models.customer_model import Customer
from app.models.history_model import History
from app.models.master import InquiryType1, InquiryType2, Staff, Status
from app.forms.customer_form import CustomerForm
from app.forms.history_form import HistoryForm
from datetime import datetime
from app import db

import uuid
customer_blueprint = Blueprint('customer', __name__)

# 特定のIDの顧客情報を表示するルート
@customer_blueprint.route('/customer/<string:id>', methods=['GET', 'POST'])
def show_customer(id):
    customer = Customer.query.get(id)
    # 問い合わせ分類1と担当者を取得
    inquiryType1_data = InquiryType1.query.all()
    inquiryType2_data = InquiryType2.query.all()
    staff_data = Staff.query.all()
    status_data = Status.query.all()
    if not customer:
        return "Customer not found", 404
    
    # クエリストリングからhistory_idを取得
    history_id = request.args.get('history_id')
    if not history_id:
        history_id = request.form.get('history_id')

    # 履歴を取得
    histories =  History.query.filter_by(customer_id=customer.id).order_by(History.createTime.desc()).all()

    # 履歴一覧表示用のデータでは inquiry_details を16文字で省略
    displayed_histories = []
    for history in histories:
        truncated_history = {
            "id": history.id,
            "date": history.date,
            "history_type1": history.type1.name,
            "history_type2": history.type2.name,
            "inquiry_details": history.inquiry_details[:16] + "..." if len(history.inquiry_details) > 16 else history.inquiry_details,
            "contact_person": history.contact_person_relation.name,
            "status": history.status_relation.name,
            "createTime": history.createTime
        }
        displayed_histories.append(truncated_history)

    # 履歴を取得するための変数
    selected_history = None

    if history_id:
        # history_idが存在すれば該当する問い合わせを取得
        selected_history = History.query.filter_by(id=history_id, customer_id=customer.id).first()

    # 履歴のフォームを準備
    form = HistoryForm()

    print(f"Form Data:", request.form, flush=True)
    print(f"selected_history:", selected_history, flush=True)
    print(f"Form Validation Errors: {selected_history}", flush=True)
    if form.validate_on_submit():
        print(f"Form Validation Errors: {selected_history}", flush=True)
        print(f"Form Data:", request.form, flush=True)
        if selected_history:
            # 既存の履歴を更新
            selected_history.history_type1 = form.history_type1.data
            selected_history.history_type2 = form.history_type2.data
            selected_history.inquiry_details = form.inquiry_details.data
            selected_history.contact_person = form.contact_person.data
            selected_history.status = form.status.data
            flash('History has been updated successfully!', 'success')
        else:
            # 新しい履歴を作成
            print(f"Form Data:", request.form, flush=True)
            print(f"Form Validation Errors: {form.errors}", flush=True)
            new_history = History(
                date=datetime.now().strftime('%Y-%m-%d'),
                history_type1=form.history_type1.data,
                history_type2=form.history_type2.data,
                inquiry_details=form.inquiry_details.data,
                contact_person=form.contact_person.data,
                status=form.status.data,
                customer_id=customer.id
            )
            db.session.add(new_history)
            flash('New history has been added successfully!', 'success')

        # データベースに変更をコミット
        db.session.commit()
        return redirect(url_for('customer.show_customer', id=customer.id))  # リダイレクトしてフォームをリセット
    else:
        # バリデーションエラーのデバッグ用出力
        print(f"Form Validation Errors: {form.errors}")

    return render_template('customer.html', customer=customer, histories=displayed_histories, form=form,
                                inquiryType1=inquiryType1_data, 
                                inquiryType2=inquiryType2_data, 
                                staff_data=staff_data,
                                status_data=status_data,
                                selected_history=selected_history
                                )

# 全顧客のリストを表示するルート
@customer_blueprint.route('/customers')
def list_customers():
    customers = Customer.query.all()
    print(f"Fetched customer: {customers}") 
    return render_template('customer_list.html', customers=customers)

@customer_blueprint.route('/customer/register', methods=['GET', 'POST'])
def register_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        # フォームのデータを使用して新しい Customer を作成
        new_customer = Customer(
            customer_name=form.customer_name.data, 
            division_name=form.division_name.data, 
            manager_name=form.manager_name.data, 
            post_code=form.post_code.data, 
            telephone_number=form.telephone_number.data, 
            cellphone_number=form.cellphone_number.data, 
            address=form.address.data, 
            fax_address=form.fax_address.data, 
            mail_address=form.mail_address.data, 
            customer_lank=form.customer_lank.data,
            memo=form.memo.data
        )
        db.session.add(new_customer)
        db.session.commit()

        flash(f'Customer {new_customer.customer_name} has been registered successfully!', 'success')
        return redirect(url_for('customer.show_customer', id=new_customer.id))  # 登録後に顧客リストページにリダイレクト

    return render_template('register_customer.html', form=form)

# 特定の履歴を削除するルート
@customer_blueprint.route('/customer/<string:customer_id>/history/<int:history_id>/delete', methods=['GET'])
def delete_history(customer_id, history_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        flash("Customer not found.", "error")
        return redirect(url_for('customer.show_customer', id=customer_id))

    history = History.query.filter_by(id=history_id, customer_id=customer_id).first()
    if history:
        db.session.delete(history)
        db.session.commit()
        flash("History has been deleted.", "success")
    else:
        flash("History not found.", "error")

    return redirect(url_for('customer.show_customer', id=customer_id))
