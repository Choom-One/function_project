def in_sm(w):
    w *= 2.54
    return w


# print(in_sm(float(input('input in: '))))
#
#
def sm_in(e):
    e *= 0.393701
    return e
#
#
# print(sm_in(float(input('input sm: '))))
#
#
def ml_km(q):
    q *= 1.60934
    return q
#
#
# print(ml_km(float(input('input ml: '))))
#
#
def km_ml(x):
    x *= 0.621371
    return x
#
#
# print(km_ml(float(input('input km: '))))
#
#
# #
def lb_kg(f):
    f *= 0.453592
    return f
#
#
# print(lb_kg(float(input('input lb: '))))
#
#
def kg_lb(t):
    t *= 2.20462
    return t
#
#
# print(kg_lb(float(input('input kg: '))))
#
#
def oz_gr(y):
    y *= 0.035274
    return y
#
#
# print(oz_gr(float(input('input oz: '))))
#
#
def gr_oz(u):
    u *= 28.3495
    return u
#
#
# print(gr_oz(float(input('input gr: '))))
#
#
def gal_l(i):
    i *= 3.78541
    return i
#
#
# print(gal_l(float(input('input gal: '))))
#
#
def l_gal(o):
    o *= 0.264172  # я использовал американский галлон
    return o
#
#
# print(l_gal(float(input('input l: '))))
#
#
def pt_l(p):
    p *= 0.56826125  # пинту я брал британскую
    return p
#
#
# print(pt_l(float(input('input pt: '))))
#
#
def l_pt(g):
    g *= 1.7597504
    return g
#
#
# print(l_pt(float(input('input l: '))))




def converter(x):
    while True:
        if x == 0:
            break
        if x == 1:
            print(in_sm(float(input('input in: '))))
            continue

        if x == 2:
            print(sm_in(float(input('input sm: '))))
            continue

        if x == 3:
            print(ml_km(float(input('input ml: '))))
            continue

        if x == 4:
            print(km_ml(float(input('input km: '))))
            continue

        if x == 5:
            print(lb_kg(float(input('input lb: '))))
            continue

        if x == 6:
            print(kg_lb(float(input('input kg: '))))
            continue

        if x == 7:
            print(oz_gr(float(input('input oz: '))))
            continue

        if x == 8:
            print(gr_oz(float(input('input gr: '))))
            continue

        if x == 9:
            print(gal_l(float(input('input gal: '))))
            continue

        if x == 10:
            print(l_gal(float(input('input l: '))))
            continue

        if x == 11:
            print(pt_l(float(input('input pt: '))))
            continue

        if x == 12:
            print(l_pt(float(input('input l: '))))
            continue


print('If you wanna close this, input 0')
print(converter(int(input('choose your conversion: '))))



