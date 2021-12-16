FROM python:3.6.4-alpine3.7
RUN pip install pymongo
COPY MongoSeeder.py .
CMD python MongoSeeder.py


