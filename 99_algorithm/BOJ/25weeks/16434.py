import sys

input = sys.stdin.readline


def check(max_hp):
    cur_hp = max_hp
    cur_atk = base_atk

    for types, attack_damage, hp in rooms:
        if types == 1:
            need = hp // cur_atk if hp % cur_atk == 0 else hp // cur_atk + 1
            cur_hp -= (need - 1) * attack_damage

            if cur_hp <= 0:
                return False
        else:
            cur_hp = min(max_hp, cur_hp + hp)
            cur_atk += attack_damage

    return True


rooms = []

N, base_atk = map(int, input().split())

for _ in range(N):
    t, a, h = map(int, input().split())
    rooms.append((t, a, h))

left = 1
right = 1_000_000 * 1_000_000 * N

ans = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
