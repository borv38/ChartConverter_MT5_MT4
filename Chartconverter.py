import csv
from tkinter.filedialog import askopenfilename
filename = askopenfilename()
try:
 with open(filename, newline='', encoding ='UTF-16') as f:
    reader = csv.reader(f)
    with open(filename.replace(".csv", "_output.csv"), 'w', newline ='') as g:
     writer = csv.writer(g)
     for row in reader:
        if len(row[0]) == 10 and len(row) and len(row[1]) != 5:
          new_row = [' '.join([row[0],'00:00:00'])] + row[1:-1] #daily, weekly, monthly charts
          writer.writerow(new_row)
        elif len(row[0]) == 16 and len(row):
          new_row = row[:-1]                            #minutes, hours charts
          writer.writerow(new_row)
        else:
            print("You use wrong MT5 file format for convertation to MT4.")
            break
     print ("File was succesfully converted to MT4 format")
except UnicodeError:
  print("Source file has MT4 format, please verify output data after convertation")
  with open(filename, newline='', encoding ='UTF-8') as f:
    reader = csv.reader(f)
    with open(filename.replace(".csv", "_output.csv"), 'w', newline ='') as g:
     writer = csv.writer(g)
     for row in reader:
        if len(row[1]) == 5 and len(row):                       # from MT4 export to MT4 import format (works for all besides daily, weekly, months)
          new_row = [' '.join([row[0], row[1]])] + row[2:]
          writer.writerow(new_row)
        else:
            print("You use wrong MT4 file format for convertation to MT4.")
            break
     print ("MT4 file successfully converted to MT4 format available for import to MT4!")
