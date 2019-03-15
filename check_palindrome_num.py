def check_palindrome(num):
  tmp = num
  reversed_num = 0

  while tmp != 0:
    reversed_num = (reversed_num * 10) + (tmp % 10)
    tmp = int(tmp / 10)

  return num == reversed_num

check_palindrome(121)
check_palindrome(78991)