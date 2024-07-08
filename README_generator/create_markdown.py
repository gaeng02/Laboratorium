def Readme (prompt : list) :

    '''
    prompt
    
    <Essential>
    :: project_name : str 
    :: project_purpose : str

    <Optional>
    :: start_date - str (format : "yyyy - mm - dd")
    :: last_update - str (format : "yyyy - mm - dd")
    :: contests - bool
    :: environment - list
    :: member - list
    :: library - list
    :: instruction - list
    '''

    Write(project_name)
    Write(project_purpose)

    if prompt[2] : Write(prompt[2])
        
    
    
def Write (cmd) :
    with open("Test.md", "w") as f :
        f.write(str(cmd), end = "\n")
    
'''
if (__name__ == "__main__") :
    Readme([])
'''
