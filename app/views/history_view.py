from flask import Blueprint, render_template
from app.models.history_model import History

# Blueprint の作成
history_blueprint = Blueprint('history', __name__)

# 全対応履歴を表示するルート
@history_blueprint.route('/histories')
def list_histories():
    histories = History.query.all()

    # 履歴一覧表示用のデータでは inquiry_details を16文字で省略
    displayed_histories = []
    for history in histories:
        truncated_history = {
            "id": history.id,
            "date": history.date,
            "history_type1": history.type1.name,
            "history_type2": history.type2.name,
            "inquiry_details": history.inquiry_details[:16] + "..." if len(history.inquiry_details) > 21 else history.inquiry_details,
            "contact_person": history.contact_person_relation.name,
            "status": history.status_relation.name,
            "createTime": history.createTime,
            "customer_id": history.customer_id
        }
        displayed_histories.append(truncated_history)


    return render_template('histories.html', histories=displayed_histories)

# 特定のユーザーの対応履歴を表示するルート
@history_blueprint.route('/customer/<int:customer_id>/histories')
def show_customer_histories(customer_id):
    histories = History.query.filter_by(customer_id=customer_id).all()
    return render_template('customer_histories.html', histories=histories)
