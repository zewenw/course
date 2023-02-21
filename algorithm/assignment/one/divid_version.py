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


left_envelope = [(1, 3), (5, 0)]
right_envelope = [(1, 2), (3, 4), (4, 2), (5, 0), (7, 2), (9, 3), (11, 4), (14, 0)]
print(merge_envelopes(left_envelope, right_envelope))
