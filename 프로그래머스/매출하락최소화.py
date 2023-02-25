from collections import defaultdict
def solution(sales, links):
    d = defaultdict(list)
    for a, b in links:
        d[a].append(b)

    def dfs(node):
        if not d[node]:
            return sales[node-1], 0     # select, ignore

        child_in = []
        child_out = []
        for child in d[node]:
            ci, co = dfs(child)
            child_in.append(ci)
            child_out.append(co)

        out_sum = sum(child_out)
        # select the node, not any of children
        select_node = sales[node-1] + out_sum

        # ignore the node, select an optimal children
        ignore_node = float('inf')
        for ci, co in zip(child_in, child_out):
            ignore_node = min(ignore_node, ci + out_sum - co)

        # return select_node, ignore_node (but should min to optimize)
        return select_node, min(ignore_node, select_node)

    ceo_in, ceo_out = dfs(1)
    return min(ceo_in, ceo_out)


args = [
    [[14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]],
    [[5, 6, 5, 3, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]],
    [[5, 6, 5, 1, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]],
    [[10, 10, 1, 1], [[3, 2], [4, 3], [1, 4]]],
]

sols = [
    44,
    6,
    5,
    2,
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')