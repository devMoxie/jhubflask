# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required
from jhubflask.utils import admin_required

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@blueprint.route('/')
@login_required
def members():
    """List members."""
    return render_template('users/members.html')


@blueprint.route('/admin/')
@login_required
@admin_required
def admin():
    return render_template('users/admin.html')
