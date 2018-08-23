import psycopg2
import os


conn = psycopg2.connect(host="localhost",database="stackoverflow_lite", user="postgres", password="root")
cur = conn.cursor()