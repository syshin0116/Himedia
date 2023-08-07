class MyFile:
  def my_read(self, file):
    with open(file, "r") as f:
      print(f.read())

  def my_writer(self, file):
    with open(file, "w") as f:
      for x in range(2, 10):
        f.write("\n")
        for y in range(1, 10):
          data = str(x)+"*"+ str(y)+"="+ str(x*y)+"|"
          f.write(data)

if __name__ == '__main__' :
  file = "2단에서5단까지.txt"
  m=MyFile()
  m.my_writer(file)
  m.my_read(file)