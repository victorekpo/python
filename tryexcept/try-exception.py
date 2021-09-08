try:
   raise Exception('Error')
except Exception as error:
    print("well, it WASN'T defined after all!")
    print(eval(repr(error)))
else:
    print("sure, it was defined.")
