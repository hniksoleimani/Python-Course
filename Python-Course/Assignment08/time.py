



def sum(x,y):
    result = {}
    result['h'] = x['h'] + y['h']
    result['m'] = x['m'] + y['m']
    result['s'] = x['s'] + y['s']

    if result['s'] >= 60:
        result['s'] -= 60
        result['m'] += 1
    if result['m'] >=60:
        result['m'] -= 60
        result['h'] += 1



    return result

def abs(x,y):
    result = {}
    result['h'] = x['h'] + y['h']
    result['m'] = x['m'] + y['m']
    result['s'] = x['s'] + x['s']

    
    if result['s'] <= -1:
        result['s'] += 60
        result['m'] -= 1
    if result['m'] <= -1:
        result['m'] += 60
        result['h'] -= 1


def show(x):
    print(x['h'], ':', x['m'], ':', x['s'])


t1 = {'h':2, 'm':30, 's':45}
t2 = {'h':3, 'm':17, 's': 40}

time = sum(t1,t2)
show(time)