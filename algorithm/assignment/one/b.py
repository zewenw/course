def new_envelope(old_envelope, new_rectangle):
    rx0 = new_rectangle[0]
    rx1 = new_rectangle[1]
    rx2 = new_rectangle[2]
    for x, y in old_envelope.items():
        # ����ǰ�泬��ԭ���ŷ�ĵ�һ������
        if x > rx0 & x < rx2:
            if y < rx2:
                old_envelope[x] = rx2
    #     ������泬��ԭ���ŷ�����һ������

    for x, y in old_envelope.items():
        print(f"x is {x}, y is {y}")

����
ǰ�ó���
# envelope = {1: 4, 3: 0, 4: 3, 7: 0}
envelope = {1: 4, 3: 0, 4: 1, 7: 0}
rectangle = (2, 8, 2)
new_envelope(envelope, rectangle)
