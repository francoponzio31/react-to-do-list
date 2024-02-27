FROM python:latest

WORKDIR /app

COPY ./backend/requirements.txt /app
COPY ./backend/src /app
COPY ./frontend/dist /app/static

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]
# CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "main:app"]
