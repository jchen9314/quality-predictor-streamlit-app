# adapt from https://github.com/srivatsan88/ContinousModelDeploy/

# lightweight python
FROM python:3.7-slim

RUN apt-get update

# copy local code to the container image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# check the contents in image
RUN ls -la $APP_HOME/

# install packages
RUN pip install -r requirements.txt

# run streamlit app in container
# disable CORS: secure, single-origin (resources from the same server)
CMD ["streamlit", "run", "--service.enableCORS", "false", "app.py"]