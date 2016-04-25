# -*- coding: utf-8 -*-

def bash_history_description():
   """
   The history of recently executed commands.
   
   The numpy array of recently executed commands.
   Each element of the numpy array consists of command's name and command's arguments separated with a space.
   """

   print("""The history of recently executed commands.
   
The numpy array of recently executed commands.
Each element of the numpy array consists of command's name and command's arguments separated with a space.""")


def employees_description():
   """
   The database with employees of Faculty of Electronics and Information Technology of Warsaw University of Technology.
   
   The pandas DataFrame describing names, surnames and faculty employees' logins.
   Note that it is an artificial dataset that imitates real database.
   The subsequent columns in this pandas DataFrame describe:
      - name - The name of an employee.
      - surname - The surname of an employee.
      - login - The login of an employee on the Proton server.
   """

   print("""The database with employees of Faculty of Electronics and Information Technology of Warsaw University of Technology.
   
The pandas DataFrame describing names, surnames and faculty employees' logins.
Note that it is an artificial dataset that imitates real database.
The subsequent columns in this pandas DataFrame describe:
   - name - The name of an employee.
   - surname - The surname of an employee.
   - login - The login of an employee on the Proton server.""")


def logs_description():
   """
   The history of logs into the Proton server.
   
   The pandas DataFrame describing the history of logs: who, from where and when logged into the Proton server.
   The subsequent columns in this pandas DataFrame describe:
      - login - The login of the user which logs into the Proton server. 
      - host - The IP address of the computer, from which the log into the Proton server was detected.
      - date - The date of log into the Proton server. Rows are sorted by this column.
   """

   print("""The history of logs into the Proton server
   
The pandas DataFrame describing the history of logs: who, from where and when logged into the Proton server.
The subsequent columns in this pandas DataFrame describe:
   - login - The login of the user which logs into the Proton server. 
   - host - The IP address of the computer, from which the log into the Proton server was detected.
   - date - The date of log into the Proton server. Rows are sorted by this column.""")


def top1000passwords_description():
   """
   The top 1000 most popular passwords.
   
   The numpy array of 1000 most commonly used passwords.
   It is sorted by the frequency of password's usage. First passwords in the numpy array are the most frequently used.
   """

   print("""The vector of 1000 most popular passwords.
   
The numpy array of 1000 most commonly used passwords.
It is sorted by the frequency of password's usage. First passwords in the numpy array are the most frequently used.""")