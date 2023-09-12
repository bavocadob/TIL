def backtrack(val, device_idx, multi_plug):
    if device_idx == K:
        return val

    if device[device_idx] in multi_plug:
        return backtrack(val, device_idx + 1, multi_plug)
    else:
        if len(multi_plug) < N:
            multi_plug.add(device[device_idx])
            return backtrack(val, device_idx + 1, multi_plug)
        else:
            target_idx = 0
            target_num = 0
            temp = device[device_idx:]
            for plug in multi_plug:
                idx = temp.index(plug) if plug in temp else 100
                if idx > target_idx:
                    target_idx = idx
                    target_num = plug

            multi_plug.remove(target_num)
            multi_plug.add(device[device_idx])
            return backtrack(val + 1, device_idx + 1, multi_plug)


N, K = map(int, input().split())

device = list(map(int, input().split()))

m = set()

print(backtrack(0, 0, m))
