def balancedBrackets(string):
  bracketStack = []
  for bracket in string:
    if isLeft(bracket):
      bracketStack.append(bracket)
    else:
      match = bracketStack.pop()
      if not isMatch(match, bracket):
        return False
  return not bracketStack

def isLeft(bracket):
  return bracket in ['(', '[', '{']

def isMatch(left, right):
  return (left, right) in [('(', ')'), ('[', ']'), ('{', '}')]

print(balancedBrackets('([])(){}(())()()'))
print(balancedBrackets('([])(){}(()()()'))