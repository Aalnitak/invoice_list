# Invoice List
### Interview Project

This is a Interview Proyect made for PENTA FINANCIERO. To make this I used python - Django

# Running the project

To successfully run the proyect you have to:

- make a virtual enviroment (you can use anaconda3, miniconda3 or virtualenv)

- the enviroment should have 
  - python 3.7+ 
  - sqlite 3.25.3+ 
  - django 2.2

- after setting your inviroment go to the terminal , activate it and navigate to folder "Invoices" (parent folder, where manage.py dwells)

- run one of the commands
```bash
manage runserver
```
```bash
manage.py runserver
```
```bash
python manage.py runserver
```



Now the proyect should be running on http://127.0.0.1:8000/ on your internet browser


# some insights

The user story states: "As a company executive, I want to see a list of all the invoices I have sent to my customers ordered by emission dates descending, so that I have a clear understanding of my accounts receivable."

# requirements

- The Software MUST be accesible from desktop browser

- The software CAN NOT directly access the invoice files, as this files are securely stored in a backup tape, but the software CAN preprocess the invoice files and store metadata in any way you see fit.

# process

To handle the access to the XML files I coded "tree.py" an algorithm to extract the information of the XML files. To do this i had to unzip, read, write into database, delete the unzziped XML file. After this I used the django Framework and bootstrap to show this information on the browser
