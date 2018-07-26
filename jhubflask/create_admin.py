#!/usr/bin/env python

from getpass import getpass
import sys

from user.models import User
from autoapp import app


def main():
    print("Create Admin User")

    with app.app_context():
        print('USER NAME')
        user_name = raw_input()

        print('ENTER EMAIL')
        email = raw_input()

        print('ENTER PASSWORD')
        password = getpass()
        assert password == getpass('Password again:')

        user = User(user_name, email, password, is_admin=True)
        user.save()


if __name__ == '__main__':
    sys.exit(main())
