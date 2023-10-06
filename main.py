import sys
import clipboard
import json

DATA_FILE = "data.json"

# get data from clipboad - clipboard.paste()
# insert data to clipboard - clipboard.copy("value")

def save_data(filepath,data):
    with open(filepath,'w') as f :
        json.dump(data,f)
    
#save("test.json",{"key": "value"}) 

def load_data(filepath):
    try:
        with open (filepath,'r') as f :
            data = json.load(f)
            return data
    except:
        return {}
            

if len(sys.argv) == 2 :
    command = sys.argv[1]
    data = load_data(DATA_FILE)

    if command.lower() == "save":
        key = input("Enter Key : ")
        data[key] = clipboard.paste()
        save_data(DATA_FILE,data)
        print("Data Saved !")
        
    elif command.lower() == "load":
        key = input("Enter Key : ")
        if key in data:
            clipboard.copy(data[key])
            print("Copied to Clipboard!")
        else:
            print("Key Does Not Exist!")
        
    elif command.lower() == "list":
        if len(data) >=1 :
            for key in data:
                print(key)
        else:
            print("Nothing Exists!")
                    
    elif command.lower() == "delete":
        key = input("Enter Key to Delete : ")
        if key in data:
            del data[key]
            save_data(DATA_FILE,data)
            print("Deleted Sucessfully!")
        else:
            print("Key Does Not Exist!")

    elif command.lower() == "help":
        print("Expected arguments:")
        print("1. save")
        print("2. load")
        print("3. list")
        print("4. delete")

    else:
        print("Unknown Command")
        
else:
    print("Pass an agrument")
    print("help - 'python pythonfilename.py help'")
