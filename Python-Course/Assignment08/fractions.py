name = 'Hani'   #string
age = 36 #int
average = 15 #float
boy = True #boolean
girl  = False #boolean
today = {'year':1400, 'month':12, 'day':1}
time = {'hour':19, 'minute':32, 'second':6}
fraction = {'numinator':4, 'denominator': 6}


def multiply(x,y):
    result = {}
    result['num'] = x['num'] * y['num']
    result['den'] = y['den'] * y['den']
    return result

def sum(x,y):
    result = {}
    result['num'] = (x['num'] * y['den']) + (y['num'] * x['den'])
    result['den'] = x['den'] * y['den']
    return result
def abstract(x,y):
    result = {}
    result['num'] = (x['num'] * y['den']) - (y['num'] * x['den'])
    result['den'] = x['den'] * y['den'] 
    return result
def division(x,y):
    result = {}
    result['num'] = x['num'] * y['den']
    result['den'] = x['den'] * y['num']
    return result

def show(x):
    print(x['num'], '/', x['den'])

a = {'num':2, 'den':3}
b = {'num':5, 'den':4}
c = multiply(a,b)
d = sum(a,b)
e = abstract(a,b)
f = division(a,b)
show(f)