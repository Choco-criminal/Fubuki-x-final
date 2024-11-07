class Config(object):
    LOGGER = True
    API_ID =25475489 
    API_HASH = "3fc2b371f4fbb0166758736414d8be92"
    TOKEN = "7617090520:AAH6OqlzkAGlJUhtd6O3yd9sRfDo6lxwn00"  
    OWNER_ID=1266240012
    
    SUPPORT_CHAT = "mylove2958" 
    START_IMG = "https://envs.sh/pC0.mp4"
    EVENT_LOGS = (-1002122538649)
    MONGO_DB_URI= "mongodb+srv://Choco:Choco@cluster0.yddf3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
   
    DATABASE_URL = "postgres://avnadmin:AVNS_TbzxTp8QTaLOy_GjvCr@choco-chocoxgithub-f883.j.aivencloud.com:16510/defaultdb?sslmode=require"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""
    )
    TIME_API_KEY = ""

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
