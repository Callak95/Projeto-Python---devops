import os
import shutil
import datetime
import time
import subprocess

## dentro do diretorioc > publicacoes > {criar pasta (data atual ## 2020-10-21)}dentro dessa pasta > {criar pasta (old)}dentro dessa pasta > {criar pasta (new)}

## Criacao das pastas

# TENTATIVA ( 1 )

dir = 'C:/publicacoes/2020-10-21/old'       
os.makedirs(dir)
dir = 'C:/publicacoes/2020-10-21/new'       
os.makedirs(dir)

# TENTATIVA ( 2 )- 

#datestring = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#print (datestring)
#os.mkdir(datestring)

#from datetime import datetime

#today = datetime.now()
 
#if today.hour < 12:
   # h = "00"
#else:
   # h = "12"

#os.makedirs(today.strftime('%Y-%m-%d'))
#os.chdir('C:/publicacoes/',today,'/new')

          
## copiar war area de trabalho > dentro da pasta {deploy}copiar arqui > {## online.war || dentro dessa pasta > {criar pasta (new)}

## Transferencia de arquivos

src = 'C:/Users/lucas/OneDrive/Área de Trabalho/deploy'
dst = 'C:/publicacoes/2020-10-21/new'

shutil.copyfile(src=src + '/online.war', dst=dst + '/online.war')


## fazer backup do war antigo dentro do diretorio > c > servidores > webapps >copiar o arquivo {online.war} || dentro dessa pasta > {criar pasta (old)}

## Backup do Servidor -> Pasta Old.

src = 'C:/servidores/webapps/'
dst = 'C:/publicacoes/2020-10-21/old'

shutil.copyfile(src=src + '/online.war', dst=dst + '/online.war')




## Criar um "stop" no servidor Tomcat

scriptName = 'tomact_init.py'
tomcatBinDir = '/apps/apache-tomcat-7.0.63/bin'
tomcatShutdownPeriod = 5
commandToCheckTomcatProcess = "ps -ef | grep -v grep | grep " + tomcatBinDir + " | wc -l" 
commandToFindTomcatProcessId = 'ps -ef | grep -v grep | grep ' + tomcatBinDir + ' | awk \'{print $2}\''

def isProcessRunning():
    pStatus = True
    tProcess = subprocess.Popen(commandToCheckTomcatProcess, stdout=subprocess.PIPE, shell=True)
    out, err = tProcess.communicate()
    if int(out) < 1:
        pStatus = False
    return pStatus

def usage():
    print ("Uso: python " + scriptName + " start|stop|status|restart")
    print ("ou")
    print ("Uso: <path>/" + scriptName + " start|stop|status|restart")

def start():
    if isProcessRunning():
        print ("O processo Tomcat já está em execução")
    else:
        print ("Iniciando o tomcat")
        subprocess.Popen([tomcatBinDir + "/startup.sh"], stdout=subprocess.PIPE)

def stop():
    if isProcessRunning():
        print ("Parando o tomcat")
        subprocess.Popen([tomcatBinDir + "/shutdown.sh"], stdout=subprocess.PIPE)
        time.sleep(tomcatShutdownPeriod)
        if isProcessRunning():
            tPid = subprocess.Popen([commandToFindTomcatProcessId], stdout=subprocess.PIPE, shell=True)
            out, err = tPid.communicate()
            subprocess.Popen(["kill -9 " + out], stdout=subprocess.PIPE, shell=True)
            print ("Tomcat falhou em desligar " + out)
    else:
       print ("O processo Tomcat não está em execução") 

def status():
    if isProcessRunning():
        tPid = subprocess.Popen([commandToFindTomcatProcessId], stdout=subprocess.PIPE, shell=True)
        out, err = tPid.communicate()
        print ("O processo Tomcat está sendo executado " + out)
    else:
       print ("O processo Tomcat não está em execução") 

if len(sys.argv) != 2:
    print ("Missing argument")
    usage()
    sys.exit(0)
else:
    action = sys.argv[1]

if action == 'start':
    start()
elif action == 'stop':
    stop()
elif action == 'status':
    status() 
elif action == 'restart':
    stop()
    start()
else:
    print ("Invalid argument")
    usage()







## fazer backup da pasta videos para dentro do disco Co video está dentro da pasta c > servidores > webapps > online > $videos




## Em Construcao !


















