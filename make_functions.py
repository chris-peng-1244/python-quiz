def make_functions():
  flist = []

  for i in [1, 2, 3]:
    def print_i(var):
      def print_var():
        print(var)
      return print_var
    flist.append(print_i(i))

  return flist

functions = make_functions()
for f in functions:
  f()