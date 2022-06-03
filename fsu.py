def uploadf():

    fs = input("enter a file name:")
    
    if fs == "quit":

      exit()

    else:
    
     print("\n")

     try:
       from requests import post
     except:
       print("requests module not found")

     url = "http://0x0.st/"
     files = {"file": open(fs, "rb")}

     r = post(url, files=files)
     print("source:"+ r.text)
    
     uploadf()

uploadf()
