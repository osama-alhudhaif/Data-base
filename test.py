import os
import pymysql
from dotenv import load_dotenv

# تحميل القيم من ملف .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# الاتصال بالسيرفر بدون تحديد قاعدة بيانات
conn = pymysql.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD # type: ignore
) # type: ignore

cursor = conn.cursor()

# التشييك على القاعدة
cursor.execute(f"SHOW DATABASES LIKE '{DB_NAME}';")
result = cursor.fetchone()

if result:
    print(f"✅ قاعدة البيانات '{DB_NAME}' موجودة.")
else:
    print(f"⚠️ قاعدة البيانات '{DB_NAME}' غير موجودة... جاري إنشاؤها.")
    cursor.execute(f"CREATE DATABASE `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    print(f"✅ تم إنشاء قاعدة البيانات '{DB_NAME}' بنجاح.")

cursor.close()
conn.close()
