import pymongo

def Schedule_db_init():
    client = pymongo.MongoClient()
    mydb = client['EZSchooldb']

    mycol = mydb['ScheduleClasses']

    data = [
        {
             "monday1": ["הסטוריה", "הסטוריה", "תנך", "חשבון", "חשבון"],
            "sunday1": ["", "הסטוריה", "חשבון", "חשבון", "חשבון"],
            "tuesday1": ["", "תנך", "תנך", "עברית", "עברית"],
            "wednesday1": ["עברית", "עברית", "חשבון", "חשבון", "חשבון"],
            "thursday1": ["חשבון", "חשבון", "", "חשבון", "הסטוריה"],
            "name": "class1"},
        {
            "monday2": ["חשבון", "חשבון", "חשבון", "הסטוריה", "הסטוריה"],
            "sunday2": ["", "עברית", "תנך", "תנך", "תנך"],
            "thursday2": ["הסטוריה", "הסטוריה", "היסטוריה", "חשבון", "חשבון"],
            "tuesday2": ["עברית", "עברית", "תנך", "תנך", "תנך"],
            "wednesday2": ["חשבון", "חשבון", "עברית", "עברית", "הסטוריה"],
            "name": "class2"
        },
        {
            "monday3": ["הסטוריה", "הסטוריה", "הסטוריה", "חשבון", "חשבון"],
            "sunday3": ["תנך", "עברית", "עברית", "תנך", "תנך"],
            "thursday3": ["חשבון", "חשבון", "חשבון", "תנך", "תנך"],
            "tuesday3": ["עברית", "עברית", "הסטוריה", "הסטוריה", "חשבון"],
            "wednesday3": ["חשבון", "חשבון", "הסטוריה", "עברית", "עברית"],
            "name": "class3"},
    {
            "monday4": ["עברית", "עברית", "עברית", "חשבון", "חשבון"],
            "sunday4": ["חשבון", "חשבון", "תנך", "תנך", "תנך"],
            "thursday4": ["הסטוריה", "הסטוריה", "הסטוריה", "חשבון", "חשבון"],
            "tuesday4": ["עברית", "עברית", "עברית", "חשבון", "הסטוריה"],
            "wednesday4": ["הסטוריה", "תנך", "תנך", "עברית", "עברית"],
            "name": "class4"
            },
        {
            "monday5": ["חשבון", "חשבון", "חשבון", "הסטוריה", "הסטוריה"],
            "sunday5": ["תנך", "חשבון", "תנך", "תנך", "תנך"],
            "thursday5": ["הסטוריה", "הסטוריה", "הסטוריה", "חשבון", "חשבון"],
            "tuesday5": ["עברית", "עברית", "עברית", "חשבון", "הסטוריה"],
            "wednesday5": ["הסטוריה", "הסטוריה", "תנך", "עברית", "עברית"],
            "name": "class5"},
        {
                "monday6": ["חשבון", "חשבון", "חשבון", "הסטוריה", "הסטוריה"],
                "sunday6": ["עברית", "עברית", "תנך", "תנך", "תנך"],
                "thursday6": ["הסטוריה", "הסטוריה", "היסטוריה", "חשבון", "חשבון"],
                "tuesday6": ["עברית", "עברית", "תנך", "תנך", "תנך"],
                "wednesday6": ["חשבון", "חשבון", "עברית", "עברית", "הסטוריה"],
                "name": "class6"}
    ]
    for item in data:
        exisiting_item = mycol.find_one({'name': item['name']})
        if exisiting_item == None:
            mycol.insert_one(item)



