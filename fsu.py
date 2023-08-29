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
     //enter the url which you want to post your files to
     url = "<your_url>"
     files = {"file": open(fs, "rb")}

     r = post(url, files=files)
     print("source:"+ r.text)
    
     uploadf()

uploadf()
