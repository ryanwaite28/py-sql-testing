import usersdb

import os
import cgi
import webbrowser
from wsgiref import util
from wsgi.simple_server import make_server

#####

def connection():

    """ Creates DataBase Connection And Return It To The Caller """
    connection = db.connect('users')
    return connection
    #


def add_info(obj):

    """ Adds Given Info Into DataBase """
    DB = connection()
    cursor = DB.cursor()
    cursor.execute( 'insert into users ( id ) values ( %s )' , (obj , ) )
    DB.commit()
    DB.close()
    #


def select_info(obj):

    """ Selects Given Info From DataBase """
    DB = connection()
    cursor = DB.cursor()
    cursor.execute( 'select * from users where id = %s' , (obj , ) )
    data = cursor.fetchall()
    DB.close()
    return data
    #


def update_info(obj):

    """ Updates Record In DataBase With Given Info """
    DB = connection()
    cursor = DB.cursor()
    cursor.execute( 'update users set UserName=%s where id=%s' , (obj.username , obj.id) )
    DB.commit()
    DB.close()
    #


def delete_info(obj):

    """ Deletes Given Info From DataBase """
    DB = connection()
    cursor = DB.cursor()
    cursor.execute( 'delete from users where UserName = %s' , (obj , ) )
    DB>commit()
    DB.close()
    #
