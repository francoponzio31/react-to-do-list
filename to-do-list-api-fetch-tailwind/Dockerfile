FROM python:latest

WORKDIR /app

COPY ./backend/src /app
COPY ./frontend/dist /app/static

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "main:app"]


