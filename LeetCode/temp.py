# V = 4
# def colorGraph(G, color, pos, c):
#     color[pos] = c
#     for i in range(0, V):
#         if G[pos][i]:
#             if color[i] == -1:
#                 if not colorGraph(G, color, i, 1 - c):
#                     return False
#             elif color[i] == c:
#                 return False
#     return True
#
#
# def isBipartite(G):
#     color = [-1] * V
#     pos = 0
#     for i in range(V):
#         if color[i] == -1:
#             if not colorGraph(G, color, pos, 1):
#                 return False
#         pos+=1
#
#     return True , color
#
#
# if __name__ == "__main__":
#     node_flag = []
#     G = [[0, 1, 0, 1],
#          [1, 0, 1, 0],
#          [0, 1, 0, 1],
#          [1, 0, 1, 0]]
#     # G = [[0,0,0,1,1,0],
#     #      [0,0,0,0,1,1],
#     #      [0,0,0,0,0,1],
#     #      [1,0,0,0,0,0],
#     #      [1,1,0,0,0,0],
#     #      [0,1,1,0,0,0]]
#     # G = [[0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0],
#     #      [0,0,0,0,0,0,1,1],[1,1,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],
#     #      [1,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0]]
#     if isBipartite(G):
#         print("Yes")
#     else:
#         print("No")
#     print(isBipartite(G)[1])
#
"""
KM算法
复杂度O(E*V*V)?
"""
# a = -float('inf')
# # a = 5
# graph = [
#     [4, 2, 6, a, a],
#     [2, 6, a, 6, 3],
#     [a, 3, 6, a, a],
#     [a, 8, 2, a, a],
#     [a, a, a, 3, 1]
# ]
# label_left, label_right = [max(g) for g in graph], [0 for _ in graph]
# S, T = {}, {}
#
# visited_left = [False for _ in graph]
# visited_right = [False for _ in graph]
# slack_right = [float('inf') for _ in graph]
#
#
# def find_path(i, visited_left, visited_right, slack_right):
#     visited_left[i] = True
#     for j, match_weight in enumerate(graph[i]):
#         if visited_right[j]:
#             continue
#         gap = label_left[i] + label_right[j] - match_weight
#         if gap == 0:
#             visited_right[j] = True
#             if j not in T or find_path(T[j], visited_left, visited_right, slack_right):
#                 T[j] = i
#                 S[i] = j
#                 return True
#
#         else:
#             slack_right[j] = min(slack_right[j], gap)
#     return False
#
# def KM():
#     m = len(graph)
#     for i in range(m):
#         # 重置辅助变量
#         slack_right = [float('inf') for _ in range(m)]
#         while True:
#             visited_left = [False for _ in graph]
#             visited_right = [False for _ in graph]
#             if find_path(i,visited_left,visited_right, slack_right):
#                 break
#             d = float('inf')
#             for j, slack in enumerate(slack_right):
#                 if not visited_right[j] and slack < d:
#                     d = slack
#             for k in range(m):
#                 if visited_left[k]:
#                     label_left[k] -= d
#                 if visited_right[k]:
#                     label_right[k] += d
#     return S, T
#
# KM()
# print(S)

a = [(1,3), (3,2), (5,6)]
print(a[1][1])