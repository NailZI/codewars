# Name of file
# import
def order(sentence):
  # code here
  words = sentence.split(' ')
  res = ''
  for i in range(1, 10):
      for word in words:
          if str(i) in word:
              res += word + ' '
  return res.rstrip()


if __name__ == "__main__":
    # "is2 Thi1s T4est 3a" -->  "Thi1s is2 3a T4est"
    # "4of Fo1r pe6ople g3ood th5e the2" -->  "Fo1r the2 g3ood 4of th5e pe6ople"
    # "" -->  ""
    print(order("is2 Thi1s T4est 3a"))
