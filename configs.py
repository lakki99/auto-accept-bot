# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22432833"))
    API_HASH = getenv("API_HASH", "897f1c440892cfc46c7e222dfb37d015")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002326767461")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "7592041488").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://lavanya143111443:wJ4EhAF0jCUOm35Z@cluster0.llqwyeo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
