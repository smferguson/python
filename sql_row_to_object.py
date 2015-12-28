
import datetime
import decimal

# given an object and a row of data from a sql query populate the object
# the row must be a dictionary
def SQLRowToObject(obj, row):
  for column in obj:
    if type(obj[column]) is dict:
      obj[ column ] = BuildObjectFromRow(obj[column], row)
    elif type(obj[column]) is list:
      # NoOp
      continue
    elif type(row[column]) in [datetime.datetime, datetime.date]:
      obj[column] = int(time.mktime((row[column]).timetuple()))
    elif type(row[column]) in [float, decimal.Decimal]:
      obj[column] = float(row[column])
    elif type(row[column]) is str:
      obj[column] = row[column].decode('utf-8')
    else:
      obj[column] = row[column]
  return obj
