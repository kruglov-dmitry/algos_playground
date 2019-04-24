#
#   https://leetcode.com/problems/rectangle-overlap/
#
#   Given two rectangles defined by pairs of top left corner and bottom right corner
#   check whether they overlap or not.
#   NOTE: in case they just touch border of each other it doesnt count as overlap
#


def rectangles_overlap(rec1, rec2):
    x1 = rec1[0]
    y1 = rec1[1]
    x2 = rec1[2]
    y2 = rec1[3]

    x10 = rec2[0]
    y10 = rec2[1]
    x20 = rec2[2]
    y20 = rec2[3]

    if x1 < x10 < x2:
        return y1 < y10 < y2 or y1 < y20 < y2 or y10 < y1 < y20 or y10 < y2 < y20
    elif x1 < x20 < x2:
        return y1 < y10 < y2 or y1 < y20 < y2 or y10 < y1 < y20 or y10 < y2 < y20
    elif x10 < x1 < x20:
        return y1 < y10 < y2 or y1 < y20 < y2 or y10 < y1 < y20 or y10 < y2 < y20
    elif x10 < x2 < x20:
        return y1 < y10 < y2 or y1 < y20 < y2 or y10 < y1 < y20 or y10 < y2 < y20


rec1 = [7, 8, 13, 15]
rec2 = [10, 8, 12, 20]

print rectangles_overlap(rec1, rec2)
