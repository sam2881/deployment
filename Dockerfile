FROM python:3.9.4

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /house-prices-api

ARG PIP_EXTRA_INDEX_URL

# Install requirements, including from Gemfury
ADD ./house-prices-api /house-prices-api/
RUN pip install --upgrade pip
RUN pip install -r /house-prices-api/requirements.txt



USER ml-api-user

EXPOSE 8001

CMD ["python", "/house-prices-api/app/main.py"]
