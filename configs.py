# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "26515166"))
    API_HASH = getenv("API_HASH", "71b53a38b57308cc7b8d48b83f387970")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002873429188")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "8134543713").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://lavanya143111443:wJ4EhAF0jCUOm35Z@cluster0.llqwyeo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
