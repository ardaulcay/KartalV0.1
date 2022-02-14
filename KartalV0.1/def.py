import time

ymid = 0
xmid = 0
h = 0
w = 0
lxp = 0
lyp = 0

def takeoff():
    print("full throttle")
    print("elevator up")
    print("ascend to 20m")

def land():
    print("2/3 throttle")
    print("land")

def wtflt():
    print("stabilise control surface")
    print("3/4 throttle")
    print("u turn")

def wait():
    if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:
        print("4")
        if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:
            time.sleep(1)
            if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:
                print("3")
                if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:
                    time.sleep(1)
                    if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:
                        print("2")
                        if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:
                            time.sleep(1)
                            if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:
                                print("1")
                                if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:
                                    time.sleep(1)
                                    if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:
                                        print("0")
                                        if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:
                                            time.sleep(1)
                                            if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:            
                                                print("succesful")


def times():
    time.sleep(10)
    tm = True

def lr():
        if xmid <= 64:
            print("turn left")
        elif xmid <= 128:
            print("turn left")
        elif xmid <= 192:
            print("turn left")
        elif xmid <= 256:
            print("turn left")
        elif xmid == 320:
            print("x ok")
        elif xmid <= 384:
            print("turn right")
        elif xmid <= 448:
            print("turn right")
        elif xmid <= 512:
            print("turn right")
        elif xmid <= 576:
            print("turn right")
        elif xmid <= 640:
            print("turn right")
        else:
            print("x err")
        
        time.sleep(2)

def ud():
        if ymid <= 48:
            print("pull up")
        elif ymid <= 96:
            print("pull up")
        elif ymid <= 144:
            print("pull up")
        elif ymid <= 192:
            print("pull up")
        elif ymid == 240:
            print("y ok")
        elif ymid <= 288:
            print("push down")
        elif ymid <= 336:
            print("push down")
        elif ymid <= 384:
            print("push down")
        elif ymid <= 432:
            print("push down")
        elif ymid <= 480:
            print("push down")
        else:
            print("y err")
        
        time.sleep(2)

def sd():
        if h <= 50 and w <= 50:
            print("throttle up")
        elif h <= 100 and w <= 100:
            print("throttle up")
        elif h <= 150 and w <= 150:
            print("throttle ok")
        elif h <= 200 and w <= 200:
            print("throttle down")
        elif h <= 250 and w <= 250:
            print("throttle down")
        else:
            print("throttle err")
        
        time.sleep(2)

def xlp():
    if xmid >= 0 and xmid < 160:
        lxp = 1
    if xmid >= 160 and xmid < 320:
        lxp = 2
    if xmid >= 320 and xmid < 480:
        lxp = 3
    if xmid >= 480 and xmid <= 640:
        lxp = 4

def ylp():
    if ymid >= 0 and ymid < 120:
        lyp = 1
    if ymid >= 120 and ymid < 240:
        lyp = 2
    if ymid >= 240 and ymid < 360:
        lyp = 3
    if ymid >= 360 and ymid <= 480:
        lyp = 4

def lp():
        if lxp == 1 and lyp == 1:
            print("lu")
        if lxp == 2 and lyp == 1:
            print("mul")
        if lxp == 3 and lyp == 1:
            print("mur")
        if lxp == 4 and lyp == 1:
            print("ru")
        if lxp == 1 and lyp == 2:
            print("lum")
        if lxp == 2 and lyp == 2:
            print("mmul")
        if lxp == 3 and lyp == 2:
            print("mmur")
        if lxp == 4 and lyp == 2:
            print("rum")
        if lxp == 1 and lyp == 3:
            print("ldm")
        if lxp == 2 and lyp == 3:
            print("mmdl")
        if lxp == 3 and lyp == 3:
            print("mmdr")
        if lxp == 4 and lyp == 3:
            print("rdm")
        if lxp == 1 and lyp == 4:
            print("ld")
        if lxp == 2 and lyp == 4:
            print("mdl")
        if lxp == 3 and lyp == 4:
            print("mdr")
        if lxp == 4 and lyp == 4:
            print("rd")