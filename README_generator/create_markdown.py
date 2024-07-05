def Readme (prompt : list) : 
    with open("Test.md", "w") as f :
        for item in prompt :
            f.write(str(item), end = "\n")
    

'''
if (__name__ == "__main__") :
    Readme([])
'''
