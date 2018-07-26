# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from flask import flash, current_app
from flask_login import current_user
from functools import wraps


def flash_errors(form, category='warning'):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash('{0} - {1}'.format(getattr(form, field).label.text, error), category)


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin:
            flash("This page is for admins only!", "danger")
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)
    return decorated_view
