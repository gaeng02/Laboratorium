from notion_client import Client 

def Create (date, completed, topic, host, title = "", self = "None", url = None) :
    new_data = {
        "Topic": {
            "title": [{"text": {"content": topic}}]
        },
        "Date": {
            "date": {"start": date}
        },
        "Completed": {
            "status": {"name" : completed}
        },
        "Host": {
            "select": {"name": host}
        },
        "Title" : {
            "rich_text" : [{"text" : {"content" : title}}]
        },
        "Self" : {
            "status": {"name" : self}
        },
        "URL" : {
            "url" : url
        }  
    }
    
    notion.pages.create(parent = {"database_id" : database_id}, properties = new_data)


    '''
    Date :: date
    Completed :: tag [완료, 미완료]
    Topic :: title 
    Host :: option
    _Title :: title
    _Self :: tag [None, ★☆☆☆☆, ★★☆☆☆, ★★★☆☆, ★★★★☆, ★★★★★]
    _URL ::
    '''

