FROM python:3

# set a directory for the app
WORKDIR /Users/jackdiamond/Desktop/blackjack

# copy all the files to the container
COPY . .

# install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# run the command
CMD ["python", "./table.py"]