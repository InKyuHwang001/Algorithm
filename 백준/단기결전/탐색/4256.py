import sys
input = sys.stdin.readline()

def make_postorder(preorder, inorder):
  if preorder == []:
    return
  if len(preorder) == 1:
    print(preorder[0], end=' ')
    return
  if len(preorder) == 2:
    print(preorder[1], preorder[0], end=' ')
    return

  root_idx = inorder.index(preorder[0])

  left_in = inorder[0:root_idx]
  left_pre = preorder[1:1+len(left_in)]
  make_postorder(left_pre, left_in)

  right_in = inorder[root_idx+1:]
  right_pre = preorder[len(left_pre)+1:]
  make_postorder(right_pre, right_in)
  print(preorder[0], end=' ')

for _ in range(int(input())):
  N = int(input())
  preorder = list(map(int, input().split()))
  inorder = list(map(int, input().split()))
  make_postorder(preorder, inorder)