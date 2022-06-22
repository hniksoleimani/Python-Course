
def sum(x,y):

    result = {}
    result['rel'] = x['rel'] + y['rel']
    result['img'] = x['img'] + y['img']
    return result


def abstract(x,y):

    result = {}
    result['rel'] = x['rel'] - y['rel']
    result['img'] = x['img'] - y['img']
    return result

def multiplication(x,y):

    result = {}
    result['rel'] = (x['rel'] * y['rel']) -  (x['img'] * y['img'])
    result['img'] = (x['img'] * y['rel']) + (x['rel'] * y['img'])
    return result


def show(x):
    print(str(x['rel']) + '+' + str(x['img']) + 'i' )

a = {'rel':5, 'img':7}
b = {'rel':6, 'img':4}


c = sum(a,b)
d = abstract(a,b)
e = multiplication(a,b)
show(e)