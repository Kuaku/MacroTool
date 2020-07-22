import json

def loadConfig():
    configFile = open("./config.json", "r");
    configRaw = configFile.read();
    configFile.close();

    return json.loads(configRaw);
