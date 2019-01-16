# -*- coding: utf-8 -*-
# Author: LDD
# Time: 2018/12/8 14:36
# File: base.py.py
from .. import basedir

import sys
from ..common import log

import logging
logger = logging.getLogger(__name__)

if sys.version_info < (3, 6):
    import MySQLdb
    import MySQLdb.cursors
else:
    import pymysql


class Model(object):

    def __init__(self, table_name):
        if sys.version_info < (3, 6):
            db = MySQLdb.connect("localhost", "root", "b5059507-7ab9-4e3d-963b-901ddd114e1b", "db_blog", charset="utf8", cursorclass=MySQLdb.cursors.DictCursor)
        else:
            db = pymysql.connect("localhost", "root", "root", "db_blog", charset="utf8", cursorclass=pymysql.cursors.DictCursor)
        self.conn = db
        self.logger = log.Logs()
        self.sql = ''

        self.tb_field = '*'
        self.tb_name = table_name
        self.tb_join = ''
        self.tb_where = ''
        self.tb_limit = ''
        self.tb_order = ''
        self.tb_group = ''

    @staticmethod
    def connect(self):
        if sys.version_info < (3, 6):
            db = MySQLdb.connect("localhost", "root", "b5059507-7ab9-4e3d-963b-901ddd114e1b", "db_blog", charset="utf8", cursorclass=MySQLdb.cursors.DictCursor)
        else:
            db = pymysql.connect("localhost", "root", "root", "db_blog", charset="utf8", cursorclass=pymysql.cursors.DictCursor)
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
            sql = "INSERT INTO %s(%s) VALUES (%s)" % (self.tb_name, key_word, value_word)
            try:
                self.cursor().execute(sql)
                self.commit()
                self.logger.info(sql)
            except Exception as e:
                self.rollback()
                self.logger.error("Insert into %s failed, %s, %s" % (self.tb_name, e, sql))

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
                (self.tb_name, mk_key, mk_val)
        try:
            self.cursor().execute(sql)
            self.commit()
            self.logger.info(sql)
        except Exception as e:
            self.rollback()
            # LOG.error("delete data from %s failed, %s" % (self.table_name, e))
            self.logger.error("delete data from %s failed, %s, %s" % (self.tb_name, e, sql))
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
                  (self.tb_name, key_word, mk_key, mk_val)
            try:
                self.cursor().execute(sql)
                self.commit()
                self.logger.info(sql)
            except Exception as e:
                self.rollback()
                # LOG.error("Update data from %s failed, %s" % (self.table_name, e))
                self.logger.error("Update data from %s failed, %s, %s" % (self.tb_name, e, sql))
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

            sql = "SELECT * FROM %s WHERE %s='%s'" % (self.tb_name, mk_key, mk_val)
        else:
            sql = "SELECT * FROM %s" % self.tb_name

        try:
            c = self.cursor()
            c.execute(sql)
            results = c.fetchall()
            self.logger.info(sql)
        except Exception as e:
            # LOG.error("Select data from %s failed, %s" % (self.table_name, e))
            self.logger.error("Select data from %s failed, %s, %s" % (self.tb_name, e, sql))
            return output
        output["valid"] = True
        output["detail"] = results
        return output

    def query(self, sql):
        """
        直接根据sql语句查询数据
        :param sql:
        :return:
        """
        output = {
            "valid": False,
            "detail": {}
        }
        try:
            c = self.cursor()
            c.execute(sql)
            results = c.fetchall()
            self.logger.info(sql)
        except Exception as e:
            self.logger.error("Select data from %s failed, %s, %s" % (self.tb_name, e, sql))
            return output
        output["valid"] = True
        output["detail"] = results
        return output

    def get(self):
        """
        获取多条数据
        :return:
        """
        output = {
            "valid": False,
            "detail": {}
        }
        try:
            self.sql = self.get_sql()
            c = self.cursor()
            c.execute(self.sql)
            results = c.fetchall()
            self.logger.info(self.sql)
        except Exception as e:
            self.logger.error("Select data from %s failed, %s, %s" % (self.tb_name, e, self.sql))
            return output
        output["valid"] = True
        output["detail"] = results
        return output

    def first(self):
        """
        获取一条数据
        :return:
        """
        output = {
            "valid": False,
            "detail": {}
        }
        try:
            self.sql = self.get_sql()
            c = self.cursor()
            c.execute(self.sql)
            results = c.fetchone()
            self.logger.info(self.sql)
        except Exception as e:
            self.logger.error("Select data from %s failed, %s, %s" % (self.tb_name, e, self.sql))
            return output
        output["valid"] = True
        output["detail"] = results
        return output

    def get_sql(self):
        sql = 'SELECT %s FROM %s %s %s %s %s' % (self.tb_field, self.tb_name, self.tb_join, self.tb_where, self.tb_limit, self.tb_group)
        return sql

    def field(self, field='*'):
        self.tb_field = field
        # self.sql = 'SELECT %s FROM %s ' % (field, self.table_name)
        return self

    def join(self, join_table, field1, field2, join_type='LEFT'):
        self.tb_join += ' %s JOIN %s ON %s = %s' % (join_type, join_table, field1, field2)

        return self

    def where(self, map):
        # map = {'uid': ['=', '1'], 'article_title': ['LIKE', 'test']}
        if not map:
            return self

        where = ''
        if map:
            for key in map:
                val = map[key]
                if type(val) == list:
                    where += ' %s %s "%s" AND ' % (key, val[0], val[1])
                else:
                    where += ' %s = "%s" AND ' % (key, val)
        if where:
            if self.tb_where:
                self.tb_where = self.tb_where.strip(' WHERE ')
                self.tb_where += ' WHERE ' + where.strip('AND ')
            else:
                self.tb_where = ' WHERE ' + where.strip('AND ')

        return self

    def limit(self, offset=0, limit=10):
        self.tb_limit = ' LIMIT %s, %s' % (offset, limit)

        return self

    def order(self, order='id ASC'):
        self.tb_order = ' ORDER BY %s' % (order)

        return self

    def group(self, group):
        self.tb_group = ' GROUP BY %s' % (group)

        return self

    def close(self):
        return self.conn.close()

    def cursor(self):
        return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def rollback(self):
        return self.conn.rollback()

    def __del__(self):
        return self.close()

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