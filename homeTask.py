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



