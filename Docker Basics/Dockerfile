FROM python:3
#copy all the content in the dir specified - ". /"
COPY . /usr/src/app
COPY requeriments.txt /usr/src/app/requeriments.txt
WORKDIR /usr/src/app
#install the requeriments specified
RUN pip install -r requeriments.txt 
#default command to run when container deployed - CMD ["<executable", "<param>"] 
CMD ["python3","faker-service.py"]