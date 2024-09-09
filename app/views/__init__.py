def init_views(app):
    from app.views.customer_view import customer_blueprint
    app.register_blueprint(customer_blueprint)
    