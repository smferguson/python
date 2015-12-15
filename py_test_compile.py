import os
import py_compile

if __name__ == "__main__":
  try:
    for file in os.listdir("."):
      if file.endswith(".py"):
        print("compiling: %s " % file)
        py_compile.compile(file)
  except Exception, e:
    print e
    exit(1)
