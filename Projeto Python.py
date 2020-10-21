import os
import shutil
import datetime

## dentro do diretorioc > publicacoes > {criar pasta (data atual ## 2020-10-21)}dentro dessa pasta > {criar pasta (old)}dentro dessa pasta > {criar pasta (new)}

## Criacao das pastas

# TENTATIVA ( 1 )

# dir = 'C:/publicacoes/2020-10-21/old'       
#os.makedirs(dir)
#dir = 'C:/publicacoes/2020-10-21/new'       
#os.makedirs(dir)

# TENTATIVA ( 2 )  - Atual!

datestring = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
print (datestring);
os.mkdir(datestring);

## copiar war area de trabalho > dentro da pasta {deploy}copiar arqui > {## online.war || dentro dessa pasta > {criar pasta (new)}

##Transferencia de arquivos

src = 'C:/Users/lucas/OneDrive/Área de Trabalho/deploy'
dst = 'C:/publicacoes/2020-10-21/new'

shutil.copyfile(src=src + '/online.war', dst=dst + '/online.war')






## fazer backup do war antigo dentro do diretorio > c > servidores > webapps >copiar o arquivo {online.war} || dentro dessa pasta > {criar pasta (old)}








## fazer backup da pasta videos para dentro do disco Co video está dentro da pasta c > servidores > webapps > online > $videos