def arithmetic_arranger(problems, flag=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  result = []
  for problem in problems:
    ret = splitor(problem, flag)
    if ret[0] is None:
      return ret[1]
    result.append(ret)

  rz = list(zip(*result))
  r = ["    ".join(z) for z in rz]
  arranged_problems = "\n".join(r)

  return arranged_problems


def splitor(problem, flag):
  li = problem.split()
  l = max(len(li[0]), len(li[2]))
  if l > 4:
    return (None, "Error: Numbers cannot be more than four digits.")
  lm = l + 2
  first = f"{li[0]:>{lm}}"
  second = li[1] + " " + f"{li[2]:>{l}}"
  third = "-" * lm
  ans = solver(li[0], li[1], li[2])
  if not isinstance(ans, int) and ans[0] == None:
    return (ans)
  fourth = f"{ans:>{lm}}"
  if flag:
    return (first, second, third, fourth)
  return (first, second, third)


def solver(a, s, b):
  try:
    if s == '+':
      return (int(a) + int(b))
    elif s == '-':
      return (int(a) - int(b))
    else:
      return (None, "Error: Operator must be '+' or '-'.")
  except ValueError:
    return (None, "Error: Numbers must only contain digits.")
