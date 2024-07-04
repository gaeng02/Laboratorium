def Readme (prompt : list) : 
    with open("Test.md", "w") as f :
        f.write("Test")

if (__name__ == "__main__") :
    Readme([])
