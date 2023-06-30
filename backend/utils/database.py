from sqlalchemy.exc import IntegrityError

from app import db


def try_save(object):
    try:
        if object.id is None:
            db.session.add(object)
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False


def try_delete(object):
    try:
        db.session.delete(object)
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False
