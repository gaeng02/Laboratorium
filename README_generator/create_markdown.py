def Readme (prompt : list) :

    '''
    prompt
    :: project_name : str
    :: project_purpose : str
    :: start_date - str (format : "yyyy - mm - dd")
    :: last_update - str (format : "yyyy - mm - dd")
    :: contests - bool
    :: environment - list
    :: member - list
    :: library - list
    :: instruction - list
    '''
        
    with open("Test.md", "w") as f :
        for item in prompt :
            f.write(str(item), end = "\n")
    

'''
if (__name__ == "__main__") :
    Readme([])
'''
