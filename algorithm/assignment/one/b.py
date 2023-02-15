def new_envelope(old_envelope, new_rectangle):
    rx0 = new_rectangle[0]
    rx1 = new_rectangle[1]
    rx2 = new_rectangle[2]
    for x, y in old_envelope.items():
        # 处理前面超过原有信封的第一个坐标
        if x > rx0 & x < rx2:
            if y < rx2:
                old_envelope[x] = rx2
    #     处理后面超过原有信封的最后一个坐标

    for x, y in old_envelope.items():
        print(f"x is {x}, y is {y}")

顶出
前置超出
# envelope = {1: 4, 3: 0, 4: 3, 7: 0}
envelope = {1: 4, 3: 0, 4: 1, 7: 0}
rectangle = (2, 8, 2)
new_envelope(envelope, rectangle)
