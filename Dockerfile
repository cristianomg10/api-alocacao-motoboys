FROM edwintye/sklearn-service

RUN mkdir ./alocacao-motoboy
WORKDIR ./alocacao-motoboy
COPY . .

RUN pip install --upgrade pip
RUN pip install flask==0.12.2
RUN pip install flask-ngrok
RUN pip install pandas

EXPOSE 5000

CMD python cluster.py

