rects = [(1, 4, 4), (5, 6, 6), (6, 7, 2), (7, 8, 1), (8, 9, 1)]
rects2 = [(1, 5, 2), (3, 4, 4), (7, 10, 2), (8, 12, 1), (9, 13, 3), (11, 14, 4)]
env1 = [(1, 2), (15, 0)]
env2 = [(1, 2), (3, 4), (4, 2), (5, 0), (7, 2), (9, 3), (11, 4), (14, 0)]
env3 = [(1, 4, 4), (5, 6, 6), (6, 7, 2), (7, 8, 1), (8, 9, 1)]
env4 = [(10, 7), (15, 0)]


# env5 = [(4,1)]
def convertRectangleToEnvelope(rect):
    """
    change the representation of rectangle coordinates, for example, the new rectangel is (x1, x2, h)
    after transformation, it becomes [(x1, h), (x2, 0)], that means it becomes an envelope for easier integration
    :param rect: the new rectangle to be added to the existing envelope
    :return: the envelope format of this rectangle
    """
    x1, x2, h = rect
    return [(x1, h), (x2, 0)]


def mergeRectToEnvelope(envelope, rect):
    """
    add a new rectangle to a existing envelope
    :param rect: rectangle to be added
    :variable rect_envelope: the new rectangle need needs to be converted to envelope
    :param envelope: the existing envelope
    :return result_env: the new envelope containing the new rectangle
    """
    rect_envelope = convertRectangleToEnvelope(rect)
    result_env = mergeTwoEnvelopes(envelope, rect_envelope)
    return result_env


def generateEnvelope(rectangles):
    """
    Divide and conquer algorithm in order to split rectangles into two different arrays
    :param rectangles: rectangle array to be manipulated
    """
    if len(rectangles) == 0:
        return []
    if len(rectangles) == 1:
        return convertRectangleToEnvelope(rectangles[0])
    # mid point of rectangles
    mid = len(rectangles) // 2
    # two recursive calls with first half and second half using mid point
    left_envelope = generateEnvelope(rectangles[:mid])
    right_envelope = generateEnvelope(rectangles[mid:])

    return mergeTwoEnvelopes(left_envelope, right_envelope)


def minimumEnvelopeXValue(left_env_x, right_env_x):
    """
    find the minimum value between two x-axis coordinate
    :return: minimum value between two input
    """
    if (left_env_x < right_env_x):
        return left_env_x
    return right_env_x


def maximumEnvelopeYValue(left_env_y, right_env_y):
    """
    find the minimum value between two y-axis coordinate
    :return: minimum value between two input
    """
    if (left_env_y > right_env_y):
        return left_env_y
    return right_env_y


def mergeRectToEnvelope(envelope, rect):
    """
    add a new rectangle to a existing envelope
    :param rect: the new rectangle need to be added to the existing envelope
    :variable rect_envelope: the rectangle converted to envelope format
    :param envelope: the existing envelope
    :return result_env: the new envelope contains the new rectangle
    """
    rect_envelope = convertRectangleToEnvelope(rect)
    result_env = mergeTwoEnvelopes(envelope, rect_envelope)
    print(result_env)


def convertRectangleToEnvelope(rect):
    """
    change the representation of rectangle coordinates, for example, the new rectangle is (x1, x2, h)
    after transformation, it becomes [(x1, h), (x2, 0)], i.e., it become a envelope but only contains one rectangle
    :param rect: the new rectangle needs to be added to the existing envelope
    :return: the envelope format of this rectangle
    """
    x1, x2, h = rect
    return [(x1, h), (x2, 0)]


def mergeTwoEnvelopes(first_env, second_env):
    """
    merge two envelopes
    :param first_env: the first envelope
    :param second_env: the second envelope
    :return: the new envelope coordinates pair which includes two envelopes
    """
    # calculate two envelope's coordinates pair length
    len_1, len_2 = len(first_env), len(second_env)
    # if one of the envelopes empty, return the opposite one with no need to iterate
    if len_1 == 0:
        return second_env
    if len_2 == 0:
        return first_env
    # loop index for two envelopes
    i, j = 0, 0
    # result envelopes array
    result_env = []
    # loop two envelopes until one of them reaches the end
    while i < len_1 and j < len_2:
        # find the minimum x-axis coordinates
        min_x = minimumEnvelopeXValue(first_env[i][0], second_env[j][0])
        # if the minimum x coordinates belongs to the first envelope
        if min_x == first_env[i][0] and min_x != second_env[j][0]:
            # find the maximum height between of between first and second envelope
            if j - 1 >= 0:
                result_height = maximumEnvelopeYValue(first_env[i][1], second_env[j - 1][1])
            else:
                result_height = first_env[i][1]
            # move to next coordinate pair
            i += 1
        # if the minimum x coordinates belong to second envelope
        elif min_x != first_env[i][0] and min_x == second_env[j][0]:
            # this part is the same as in the previous if statement but with different iterator value
            if i - 1 >= 0:
                result_height = maximumEnvelopeYValue(first_env[i - 1][1], second_env[j][1])
            else:
                result_height = second_env[j][1]
            # move to next coordinate pair
            j += 1
        # if both first envelope and second envelope have the same x coordinate
        elif min_x == first_env[i][0] and min_x == second_env[j][0]:
            # find the maximum height between first envelope and second envelope
            result_height = maximumEnvelopeYValue(first_env[i][1], second_env[j][1])
            # move to next coordinate pair
            i += 1
            j += 1
        # if the height is different from the previous height, then append this coordinate pair to the result
        if len(result_env) == 0 or result_height != result_env[-1][1]:
            result_env.append((min_x, result_height))
    # append all the rest coordinate pairs to result array
    result_env += first_env[i:]
    result_env += second_env[j:]
    return result_env


print(mergeTwoEnvelopes(env1, env2))  # smaller envelope on the right
print(mergeTwoEnvelopes(env2, env1))  # smaller envelope on the left
print(mergeTwoEnvelopes(env3, env2))  # two big envelope merge
print(mergeTwoEnvelopes(env2, env3))  # two big envelope merge
print(mergeTwoEnvelopes(env2, env4))
print(mergeTwoEnvelopes(env4, env2))
print("Generate merged and computed envs ------------------")
print(generateEnvelope(rects))
print(generateEnvelope(rects2))
