# class Coor:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# def new_envelope(old_envelope, new_rectangle):
#     rx0 = new_rectangle[0]
#     rx1 = new_rectangle[1]
#     rh = new_rectangle[2]
#     for item in old_envelope:
#         # 处理前面超过原有信封的第一个坐标
#         if item.x < rx0:
#             old_envelope.insert(0, Coor(rx0, rh))
#         if item.x > rx0 & item.x < rx1:
#             if item.y < rh:
#                 item.y = rh
#     #     处理后面超过原有信封的最后一个坐标
#
#     for item in old_envelope:
#         print(f"item is {item.x}, y is {item.y}")
#
#
# # 顶出
# # 前置超出
# # envelope = {1: 4, 3: 0, 4: 3, 7: 0}
# coor1 = Coor(1, 4)
# coor2 = Coor(3, 0)
# coor3 = Coor(4, 3)
# coor4 = Coor(7, 0)
# envelope = [coor1, coor2, coor3, coor4]
# rectangle = (2, 8, 2)
# new_envelope(envelope, rectangle)

rects = [(1, 4, 4), (5, 6, 6), (6, 7, 2), (7, 8, 1), (8, 9, 1)]


def find_envelope(rectangles):
    if len(rectangles) == 0:
        return []
    if len(rectangles) == 1:
        x1, x2, h = rectangles[0]
        return [(x1, h), (x2, 0)]

    mid = len(rectangles) // 2
    left_envelope = find_envelope(rectangles[:mid])
    right_envelope = find_envelope(rectangles[mid:])

    return merge_envelopes(left_envelope, right_envelope)


def merge_envelopes(left_envelope, right_envelope):
    i, j = 0, 0
    left_height, right_height = 0, 0
    output = []

    while i < len(left_envelope) and j < len(right_envelope):
        x1 = min(left_envelope[i][0], right_envelope[j][0])
        if left_envelope[i][0] == x1:
            left_height = left_envelope[i][1]
            i += 1
        if right_envelope[j][0] == x1:
            right_height = right_envelope[j][1]
            j += 1
        h = max(left_height, right_height)
        if len(output) == 0 or h != output[-1][1]:
            output.append((x1, h))

    output += left_envelope[i:]
    output += right_envelope[j:]

    return output


print(find_envelope(rects))