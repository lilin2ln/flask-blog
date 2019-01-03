# -*- coding: utf-8 -*-
# Author: LDD
# Time: 2018/12/8 14:36
# File: base.py.py

from babyshell.common import log
from babyshell import conf
import MySQLdb

CONF = conf.CONF
LOG = log.create_logger(conf.DEFAULT_LOG)

class Base(object):

    def __init__(self, table_name):
        self.table_name = table_name

    def connect(self, db_name="babyshell"):
        db = MySQLdb.connect(
            "localhost",
            "root",
            CONF.babyshell_database_passwd,
            db_name,
            charset="utf8"
        )
        self.conn = db

    def insert(self, data):
        """插入数据
        :param data: dict {}
        :return: True/False
        """
        key_word = ""
        value_word = ""
        if data:
            for key in data:
                if key_word:
                    key_word += ","
                if value_word:
                    value_word += ","
                key_word += key
                value_word += "'"+data[key]+"'"
            sql = "INSERT INTO %s(%s) VALUES (%s)" % (self.table_name, key_word, value_word)
            try:
                self.cursor().execute(sql)
                self.commit()
            except Exception as e:
                self.rollback()
                LOG.error("Insert into %s failed, %s" % (self.table_name, e))
                return False
        return True

    def delete(self, main_key):
        """删除数据(根据main_key删除)
        :param main_key: data: dict {}
        :return: True/False
        """
        mk_key = ""
        mk_val = ""
        for mk in main_key:
            mk_key = mk
            mk_val = main_key[mk_key]

        sql = "DELETE FROM %s WHERE %s='%s'" % \
                (self.table_name, mk_key, mk_val)
        try:
            self.cursor().execute(sql)
            self.commit()
        except Exception as e:
            self.rollback()
            LOG.error("delete data from %s failed, %s" %
                        (self.table_name, e))
            return False
        return True

    def update(self, main_key, data):
        """更新数据(根据main_key更新)
        :param data: dict {}
        :return: True/False
        """
        key_word = ""
        mk_key = ""
        mk_val = ""
        for mk in main_key:
            mk_key = mk
            mk_val = main_key[mk_key]

        if data:
            for key in data:
                if key_word:
                    key_word += ","
                key_word += key + "=" + "'"+data[key]+"'"
            sql = "UPDATE %s SET %s WHERE %s='%s'" % \
                  (self.table_name, key_word, mk_key, mk_val)
            try:
                self.cursor().execute(sql)
                self.commit()
            except Exception as e:
                self.rollback()
                LOG.error("Update data from %s failed, %s" %
                (self.table_name, e))
                return False
        return True

    def show(self, main_key={}):
        """查询数据(根据main_key查询)
        :param main_key: dict {}
        :return: {"valid": True/False, "detail": {}}
        """
        mk_key = ""
        mk_val = ""
        output = {
            "valid": False,
            "detail": {}
        }
        if main_key:
            for mk in main_key:
                mk_key = mk
                mk_val = main_key[mk_key]

            sql = "SELECT * FROM %s WHERE %s='%s'" % \
                  (self.table_name, mk_key, mk_val)
        else:
            sql = "SELECT * FROM %s" % self.table_name

        try:
            c = self.cursor()
            c.execute(sql)
            results = c.fetchall()
        except Exception as e:
            LOG.error("Select data from %s failed, %s" %
                      (self.table_name, e))
            return output
        output["valid"] = True
        output["detail"] = results
        return output

    def close(self):
        return self.conn.close()

    def cursor(self):
        return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def rollback(self):
        return self.conn.rollback()

if __name__ == "__main__":
    pass
    # ut = Base("user")
    # data = {"bs_id": "dfasfd124", "name": "ldd", "password": "xx123", "mobilephone": "12311111", "home_id": "dsfa", "enable_home": "1"}
    # ut.connect()
    # data = {"enable_home": "0", "name": "ldd23"}
    # res = ut.insert(data)
    # res = ut.update({"bs_id":"dfasfd124"}, data)
    # res = ut.delete({"bs_id":"dfasfd124"})
    # res = ut.show()
    # ut.close()
    # print res