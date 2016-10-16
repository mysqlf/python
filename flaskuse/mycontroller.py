def valid_login(username, password):
    if len(username) > 0:
        return True
    else:
        return False


def log_the_user_in(username):
    return render_template('me.html')


def about():
    return 'About Us'


def this_is_never_executed():
    return '123'
