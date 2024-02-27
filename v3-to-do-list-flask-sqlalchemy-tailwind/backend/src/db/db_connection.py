from flask_sqlalchemy import SQLAlchemy
import MySQLdb


conn = MySQLdb.connect(host="db", user="root", password="rootpassword")
conn.query("CREATE DATABASE IF NOT EXISTS to_do_list")

db = SQLAlchemy()