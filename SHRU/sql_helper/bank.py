from sqlalchemy import Column, String, UnicodeText, Integer, desc, delete
from sqlalchemy import asc, desc
from . import BASE, SESSION
from sqlalchemy import delete


class bankc(BASE):
    __tablename__ = "bank"
    user_id = Column(String(14), primary_key=True)
    first_name = Column(UnicodeText)
    balance = Column(Integer)
    bank = Column(UnicodeText)

    def __init__(self, user_id, first_name, balance, bank):
        self.user_id = str(user_id)
        self.first_name = first_name
        self.balance = int(balance)
        self.bank = bank


bankc.__table__.create(checkfirst=True)


def add_bank(
    user_id,
    first_name,
    balance,
    bank,
):
    
    to_check = get_bank(user_id)
    if not to_check:
        user = bankc(str(user_id), first_name, int(balance), bank)
        SESSION.add(user)
        SESSION.commit()
        return True
    user = bankc(str(user_id), first_name, int(balance), bank)
    SESSION.add(user)
    SESSION.commit()
    SESSION.close()
    return True

def update_bank(user_id, money):
    
    to_check = get_bank(user_id)
    if not to_check:
        return False
    rem = SESSION.query(bankc).filter(bankc.user_id == str(user_id)).first()
    rem.balance = int(money)
    SESSION.commit()
    SESSION.close()
    return True

def des_bank():
    
    ba = SESSION.query(bankc).order_by(desc(bankc.balance)).limit(10).all()
    SESSION.close()
    return ba

def del_bank(user_id):
    
    to_check = get_bank(user_id)
    if not to_check:
        return False
    stmt = delete(bankc).where(bankc.user_id == str(user_id)).execution_options(synchronize_SESSION='evaluate')
    SESSION.execute(stmt)
    SESSION.commit()
    SESSION.close()
    return True

def get_bank(user_id):
    try:
        if _result := SESSION.query(bankc).get(str(user_id)):
            return _result
        return None
    finally:
        SESSION.close()

def get_all_bank():
    try:
        return SESSION.query(bankc).all()
    except BaseException:
        SESSION.close()
        return None
    finally:
        SESSION.close()
