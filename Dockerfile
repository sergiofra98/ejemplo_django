
FROM python:3.9.2-buster

ADD super_heroes/requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt

ADD super_heroes /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "backend_heroes.wsgi:application"]