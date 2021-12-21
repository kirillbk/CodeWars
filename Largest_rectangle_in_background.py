# Largest Rectangle in Background
# Imagine a photo taken to be used in an advertisement. The background on the left of the motive is whitish and you want to write some text on that background.
# So you scan the photo with a high resolution scanner and, for each line, count the number of pixels from the left that are sufficiently white and suitable for being written on. Your job is to find the area of the largest text box you can place on those pixels.

# Example: In the figure below, the whitish background pixels of the scanned photo are represented by asterisks.

# *********************************
# *********
# *******
# ******
# ******
# ******
# **************
# **************
# **************
# ***************
# *********************

# If you count the pixels on each line from the left you get the list (or array, depending on which language you are using) [33, 9, 7, 6, 6, 6, 14, 14, 14, 15, 21]. The largest reactangle that you can place on these pixels has an area of 70, and is represented by the dots in the figure below.

# *********************************
# *********
# *******
# ******
# ******
# ******
# ..............
# ..............
# ..............
# ..............*
# ..............*******

# Write a function that, given a list of the number whitish pixels on each line in the background, returns the area of the largest rectangle that fits on that background.


def largest_rect(histogram):
    max_area = 0
    stack = []
    for i in range(len(histogram)):
        while stack and histogram[i] <= histogram[stack[-1]]:
            height = histogram[stack.pop()]
            width = i - stack[-1] - 1 if stack else i
            max_area = max(max_area, height * width)
        stack.append(i)
    while stack:
        height = histogram[stack.pop()]
        width = len(histogram) - stack[-1] - 1 if stack else len(histogram)
        max_area = max(max_area, height * width)
    return max_area

assert largest_rect([3, 5, 12, 4, 10]) == 16
assert largest_rect([6, 2, 5, 4, 5, 1, 6]) ==  12
assert largest_rect([9, 7, 5, 4, 2, 5, 6, 7, 7, 5, 7, 6, 4, 4, 3, 2]) == 36
assert largest_rect([]) == 0
assert largest_rect([0]) ==  0
assert largest_rect([0, 0, 0]) == 0
assert largest_rect([1, 1, 1]) == 3
assert largest_rect([1, 2, 3]) == 4
assert largest_rect([3, 2, 1]) == 4