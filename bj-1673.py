try:
    while 1:
        coupon, needstamp = map(int, input().split())
        chi = coupon
        stamp = coupon
        temp = 0
        while 1:
            if stamp < needstamp: break
            chi += stamp // needstamp
            temp = stamp // needstamp
            stamp %= needstamp
            stamp += temp
        print(chi)
except Exception:
    exit()