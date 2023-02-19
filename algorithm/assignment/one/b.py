class Coor:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def new_envelope(old_envelope, new_rectangle):
    rx0 = new_rectangle[0]
    rx1 = new_rectangle[1]
    rh = new_rectangle[2]
    for item in old_envelope:
        # 处理前面超过原有信封的第一个坐标
        if item.x < rx0:
            old_envelope.insert(0, Coor(rx0, rh))
        if item.x > rx0 & item.x < rx1:
            if item.y < rh:
                item.y = rh
    #     处理后面超过原有信封的最后一个坐标

    for item in old_envelope:
        print(f"item is {item.x}, y is {item.y}")


# 顶出
# 前置超出
# envelope = {1: 4, 3: 0, 4: 3, 7: 0}
coor1 = Coor(1, 4)
coor2 = Coor(3, 0)
coor3 = Coor(4, 3)
coor4 = Coor(7, 0)
envelope = [coor1, coor2, coor3, coor4]
rectangle = (2, 8, 2)
new_envelope(envelope, rectangle)
