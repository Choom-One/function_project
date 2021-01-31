def in_sm(w):
    w *= 2.54
    return w
print(in_sm(float(input('input inch: '))))

def sm_in(e):
    e *= 0.393701
    return e
print(sm_in(float(input('input sm: '))))

def ml_km(q):
    q *= 1.60934
    return q
print(ml_km(float(input('input ml: '))))

def km_ml(x):
    x *= 0.621371
    return x
print (km_ml(float(input('input km: '))))
#
def lb_kg(f):
    f *= 0.453592
    return f
print(lb_kg(float(input('input lb: '))))

def kg_lb(t):
    t *= 2.20462
    return t
print(kg_lb(float(input('input kg: '))))

def oz_gr(y):
    y *= 0.035274
    return y
print(oz_gr(float(input('input oz: '))))

def gr_oz(u):
    u *= 28.3495
    return u
print(gr_oz(float(input('input gr: '))))





