import config as configController
import activation
import inputController
import macroInputEvent
import console
import time


config = configController.loadConfig()




inputController = inputController.inputController();
inputController.addInputEvent(macroInputEvent.macroInputEvent(config['start'], config['macros']), 'macroInput')
activationThread = activation.activationThread(1, 'activationThread', inputController.get('macroInput').macroActivatedEvent, config['threshhold']);
activationThread.start()
inputController.get('macroInput').setActivation(activationThread)



consoleThread = console.consoleThread(2, 'consoleThread')
descStop = "stops the programm"
def stop():
    activationThread.stopThread()
    consoleThread.stopThread()
    print('---------script stopped----------')

descReload = "reload the configs"
def reload():
    global config
    config = configController.loadConfig()
    inputController.get('macroInput').setConfigs(config['start'], config['macros'])
    activationThread.setThreshhold(config['threshhold'])
    print('---------config reloaded---------')


descHelp = "show all commands"
def help():
    print('--------------help---------------')
    commands = consoleThread.getCommands()
    for key in commands:
        print(key + ': ' + commands[key])
    print('---------------------------------')

descConfig = "show all configs"
def showConfig():
    print('-------------config--------------')
    print('activation_string: ' + config['start'])
    print('threshhold: ' + str(config['threshhold']) + 's')
    print('macros:')
    for macro in config['macros']:
        print('\t' + macro['key'] + ': ' + macro['macro'])
    print('---------------------------------')



consoleThread.addCommand('stop', stop, descStop);
consoleThread.addCommand('reload', reload, descReload);
consoleThread.addCommand('config', showConfig, descConfig);
consoleThread.addCommand('help', help, descHelp);
consoleThread.start()
print('---------script started----------')
print('---------console started---------')

consoleThread.join()
