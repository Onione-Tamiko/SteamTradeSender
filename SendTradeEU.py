from steampy.client import SteamClient, Asset
from steampy.models import GameOptions
from steampy.utils import GameOptions
from openpyxl import load_workbook
import json,os,ast,time

print('''

░██████╗████████╗███████╗░█████╗░███╗░░░███╗  ██████╗░░█████╗░████████╗
██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║  ██╔══██╗██╔══██╗╚══██╔══╝
╚█████╗░░░░██║░░░█████╗░░███████║██╔████╔██║  ██████╦╝██║░░██║░░░██║░░░
░╚═══██╗░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  ██╔══██╗██║░░██║░░░██║░░░
██████╔╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  ██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░
                            BY_ONIONE_TAMIKO
''')


def SerchFile(username):
    #Path to the folder with .mafile files
    #C:\\Folder\\maFiles - example
    directory = 'your_path'
    files = os.listdir(directory)
    files = [x.split('.')[0] for x in files]
    files.remove('manifest')
    for file in files:
        #The path to the file .maFile, we only change 
        #C:\\Folder\\{file}.maFile - example
        sec_open = open(f"your_path\{file}.maFile",'r') 
        data = sec_open.read()
        sec_open.close()
        data = json.loads(data)
        name_acc = data["account_name"]
        if username == name_acc:
            identity_secret = data["identity_secret"]
            break
        else:
            pass
    return file,identity_secret

def Read(acc):
    #The path to the Excel file with login:password:api key:recipient id
    #C:\\Folder\\name.xlsx - example
    adressbook = "your_pathe"
    wb = load_workbook(filename = adressbook)
    #The name of the page in the Excel workbook
    sheet = wb['your_name']
    #The letter of the column with logins, We change it if necessary*
    #                   ↓
    username  = sheet[f'A{acc}'].value
    if username == None:
        pass
    else:
        username = username.lower()
    #The letter of the password column, We change it if necessary*
    #                  ↓
    password = sheet[f'B{acc}'].value
    #The letter of the column with api keys, We change it if necessary*
    #                    ↓
    steam_key  = sheet[f'C{acc}'].value
    #The letter of the column with the recipient id,We change it if necessary*
    #                          ↓
    partner_steam_id = sheet[f'D{acc}'].value
    wb.close()
    return username,password,steam_key,partner_steam_id
tryies = 1  
acc = 1
while True:
    try:
        username,password,steam_key,partner_steam_id = Read(acc)
        if username == None:
            break
        else:
            pass
        steam_id,identity_secret = SerchFile(username)
        #Path to the files .mafile
        #C:\\Folder\\maFiles\\{steam_id}.maFile - example
        steam_guard = f"your_path\{steam_id}.maFile"* 
        steam_client = SteamClient(steam_key)
        steam_client.login(username, password, steam_guard)
        print(f"{username}:Authorization has been completed...")
        game = GameOptions.STEAM
        my_items = steam_client.get_my_inventory(game,steam_id = steam_id)
        des = list(my_items.keys())
        id_card = []
        for i in des:
            item = my_items[i]['tags']
            for result, dic_ in enumerate(item):
                #The tag by which we determine that the card is from sale.*Steam 3000*
                if dic_.get('localized_tag_name', '') == 'Steam 3000':
                    id_card.append(i)
                    break
                else:
                    result = None
        card_to_trade = []
        for i in id_card:
            itemiv = my_items[i]
            my_asset = Asset(itemiv['id'], game)
            card_to_trade.append(my_asset)
        print(f"{username}:Found {len(card_to_trade)} sale cards...")
        steam_client.make_offer(card_to_trade, [], partner_steam_id, '',identity_secret,steam_id)
        print(f"{username}:Items sent | exchange confirmed in mobile.out...")
        steam_client.logout()
        time.sleep(5)
        acc+=1
        tryies = 1 
    except Exception as ex:
        if tryies == 4:
            acc += 1
            print(f"{username}:Error | skip...")
        else:
            tryies += 1
print("The bot has finished its work...")

        
        
    
        
    
    
    



