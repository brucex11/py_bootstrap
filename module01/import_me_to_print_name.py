
def run_as_main():
  print(f'main __name__: {__name__}')

def run_as_import():
  print(f'import __name__: {__name__}')

if( __name__ == '__main__' ):
  run_as_main()
else:
  run_as_import()
