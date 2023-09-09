def trap(height: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        print(stack)

        while stack and height[i] > height[stack[-1]]:

            top = stack.pop()
            print(top)
            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * waters

        stack.append(i)

    return volume


H, W = map(int, input().split())

heights = list(map(int, input().split()))
result = trap(heights)
print(result)
