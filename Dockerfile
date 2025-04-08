
# استخدم Python الرسمي
FROM python:3.10-slim

# إعداد مجلد العمل
WORKDIR /app

# نسخ الملفات
COPY . .

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# تحديد المنفذ
EXPOSE 8080

# أمر التشغيل
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
