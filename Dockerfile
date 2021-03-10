FROM python:3.6-slim 
COPY as deploy ./app2.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./lr_reg.pkl /deploy/
COPY ./scaler_sel.pkl /deploy/
COPY ./templates /deploy/templates
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
