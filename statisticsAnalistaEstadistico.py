import statistics
import csv

#leer los datos de ventas mensuales desde un archivo CSV
monthly_sales = {}
with open('monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales
    
sales = list(monthly_sales.values())
print(sales)

#--------------------------------------------------------------
#Hallar la media

mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

#--------------------------------------------------------------
#Hallar la mediana

mean_sales = statistics.median(sales)
print(f"La media es: {mean_sales}")

#--------------------------------------------------------------
#Hallar la moda

mean_sales = statistics.mode(sales)
print(f"La moda es: {mean_sales}")

#--------------------------------------------------------------
#Desviacion de ventas

stdev_sales = statistics.stdev(sales)
print(f"Desviacion estandar: {stdev_sales}")

#--------------------------------------------------------------
#Hallar varianza

mode_sales = statistics.variance(sales)
print(f"La varianza es: {mode_sales}")

