import psycopg2
import os


conn = psycopg2.connect(database="d2kca9k4ga3sc",
 user = "llzutrwvpgezqo", password = "a5d9584ecbf382d446d607c4830b8c797a34422e468d78ef519fadcd3bb0c600",
  host = "ec2-54-235-242-63.compute-1.amazonaws.com", port = "5432")
cur = conn.cursor()