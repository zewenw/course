def merge_rect_2_envelope(rect, second_envelope):
    """
    add a new rectangle to a existing envelope
    :param rect: the new rectangle need to be added to the existing envelope
    :param second_envelope: the existing envelope
    :return: the new envelope contains the new rectangle
    """
    first_envelope = convert_rectangle_2_envelope(rect)
    result_env = merge_two_envelope(first_envelope, second_envelope)
    print(result_env)


def convert_rectangle_2_envelope(rect):
    """
    change the representation of rectangle coordinates, for example, the new rectangel is (x1, x2, h)
    after transformation, it becomes [(x1, h), (x2, 0)], i.e., it become a envelope but only contains one rectangle
    :param rect: the new rectangle need to be added to the existing envelope
    :return: the envelope format of this rectangle
    """
    x1, x2, h = rect
    return [(x1, h), (x2, 0)]


def merge_two_envelope(first_env, second_env):
    """
    merge two envelopes
    :param first_env: the first envelope
    :param second_env: the second envelope
    :return: the new envelope coordinates pair which includes two envelopes
    """
    # calculate two envelope's coordinates pair length
    len_1, len_2 = len(first_env), len(second_env)
    # two base case, if one of the two envelopes is empty, just return the other one
    if len_1 == 0:
        return second_env
    if len_2 == 0:
        return first_env
    # sort two array based on the x-axis coordiantes
    first_env = sorted(first_env, key=lambda x: x[0])
    second_env = sorted(second_env, key=lambda x: x[0])
    # loop index for two envelope
    i, j = 0, 0
    # result coordinates array
    result_env = []
    # loop two envelope until one of them reaches the end
    while i < len_1 and j < len_2:
        # find the minimum x-axis coordinates
        min_x = min(first_env[i][0], second_env[j][0])
        # whether the minimum x coordinates belong to first envelope
        if min_x == first_env[i][0] and min_x != second_env[j][0]:
            # find the maximum height between first envelope corresponding height or second envelope previous
            # corresponding height
            if j - 1 >= 0:
                result_height = max(first_env[i][1], second_env[j - 1][1])
            else:
                result_height = first_env[i][1]
            # move to next coordinate pair
            i += 1
            # if the height is different with previous height, then append this coordinate pair to the result
            if len(result_env) == 0 or result_height != result_env[-1][1]:
                result_env.append((min_x, result_height))
        # whether the minimum x coordinates belong to second envelope
        elif min_x != first_env[i][0] and min_x == second_env[j][0]:
            # this part is quite similar to the one above
            if i - 1 >= 0:
                result_height = max(first_env[i - 1][1], second_env[j][1])
            else:
                result_height = second_env[j][1]
            j += 1
            if len(result_env) == 0 or result_height != result_env[-1][1]:
                result_env.append((min_x, result_height))
        # both first envelope and second envelope have same x coordinate
        elif min_x == first_env[i][0] and min_x == second_env[j][0]:
            # find the maximum height between first envelope and second envelope
            result_height = max(first_env[i][1], second_env[j][1])
            i += 1
            j += 1
            # if the height is different with previous height, then append this coordinate pair to the result
            if len(result_env) == 0 or result_height != result_env[-1][1]:
                result_env.append((min_x, result_height))
    # append all the rest coordinates pair to result array
    result_env += first_env[i:]
    result_env += second_env[j:]
    return result_env


if __name__ == '__main__':
    # case 1
    # rect = (1, 15, 8)
    # left_env = [(1,8), (15, 0)]
    # case 2
    # rect = (1, 5, 3)

    # case 3
    rect = (1, 15, 1)

    # case 4
    # rect = (1, 2, 2)

    # case 5
    # rect = (10, 15, 2)

    envelope = [(1, 2), (3, 4), (4, 2), (5, 0), (7, 2), (9, 3), (11, 4), (14, 0)]
    merge_rect_2_envelope(rect, envelope)
