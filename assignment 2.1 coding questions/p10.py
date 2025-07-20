def largest_rectangle(heights):
    heights = [-1] + heights + [-1]
    from_left = [0] * len(heights)
    stack = [0]

    for i in range(1, len(heights) - 1):
        while heights[stack[-1]] >= heights[i]:
            stack.pop()
        from_left[i] = stack[-1]
        stack.append(i)

    from_right = [0] * len(heights)
    stack = [len(heights) - 1]

    for i in range(1, len(heights) - 1)[::-1]:
        while heights[stack[-1]] >= heights[i]:
            stack.pop()
        from_right[i] = stack[-1]
        stack.append(i)

    max_area = 0
    for i in range(1, len(heights) - 1):
        max_area = max(max_area, heights[i] * (from_right[i] - from_left[i] - 1))

    return max_area
