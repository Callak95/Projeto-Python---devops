import os
import shutil
#import datetime
import subprocess

##dentro do diretorioc > publicacoes > {criar pasta (data atual ## 2020-10-21)}dentro dessa pasta > {criar pasta (old)}dentro dessa pasta > {criar pasta (new)}

##  Criacao das pastas

#  TENTATIVA ( 1 )

dir = 'C:/publicacoes/2020-10-21/old'       
os.makedirs(dir)
dir = 'C:/publicacoes/2020-10-21/new'       
os.makedirs(dir)

#TENTATIVA ( 2 )- 

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

          
##copiar war area de trabalho > dentro da pasta {deploy}copiar arqui > {## online.war || dentro dessa pasta > {criar pasta (new)}

##  Transferencia de arquivos

src = 'C:/Users/lucas/OneDrive/Área de Trabalho/deploy'
dst = 'C:/publicacoes/2020-10-21/new'

shutil.copyfile(src=src + '/online.war', dst=dst + '/online.war')


##fazer backup do war antigo dentro do diretorio > c > servidores > webapps >copiar o arquivo {online.war} || dentro dessa pasta > {criar pasta (old)}

##  Backup do Servidor -> Pasta Old.

src = 'C:/servidores/webapps/'
dst = 'C:/publicacoes/2020-10-21/old'

shutil.copyfile(src=src + '/online.war', dst=dst + '/online.war')



##  Criar um "stop" no servidor Tomcat

proc=input("Entrar com o modo :")
os.environ["JAVA_HOME"] = '/usr/lib/jvm/java-7-openjdk-amd64'
os.environ["CATALINA_HOME"] = '/export/apps/tomcat7'

if proc == "start":
    os.getcwd()
    os.chdir("/export/apps/tomcat7/bin/")
    os.getcwd()
    subprocess.call('sh catalina.sh start',shell=True)
    print ("Tomcat iniciado com sucesso!")
elif proc == "stop":
    os.getcwd()
    os.chdir("/export/apps/tomcat7/bin/")
    os.getcwd()
    subprocess.call('sh catalina.sh stop',shell=True)
    print ("Tomcat parou com sucesso!")
elif proc == "restart":
    os.getcwd()
    os.chdir("/export/apps/tomcat7/bin/")
    os.getcwd()
    subprocess.call('sh catalina.sh stop',shell=True)
    subprocess.call('sh catalina.sh start',shell=True)
    print ("Tomcat reiniciado com sucesso!")
else:
    print ("error: Digitar Qualquer modo! Referencia -> start || restart || stop")




## fazer backup da pasta videos para dentro do disco Co video está dentro da pasta c > servidores > webapps > online > $videos


##  Em Construcao !


















