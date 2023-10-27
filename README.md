#Automação em Python para download de shapefiles do SICAR

**Contexto:** Os shapefiles armazenados neste site (https://www.car.gov.br/publico/municipios/downloads). 
São dados públicos de cadastro das propriedades rurais contendo a delimitação de terrenos e diferentes tipos de uso dentro deles (área de preservação permanente, área de reserva legal, hidrografia etc...) tais dados são produzidos pelos próprios proprietários creio que por meio da contratação de topógrafo. 
Esses dados estão divididos arquivos .zip por município mediante preenchimento de captcha.
No Brasil há 5568 municípios cada um deles possui um código de identificação que pode ser consultado em: https://www.ibge.gov.br/explica/codigos-dos-municipios.php. 
Dessa forma afim de facilitar o download desses shapesfiles desenvolvi essa automação que faz uso do Google Lens para resolução do captcha.


##Bibliotecas Usadas
 - os (Para gerenciar os arquivos baixados)
 - time (Para inserir pausas que permitem o carregamento)
 - webbrowser (Para acessar o site que armazena os shapefiles)
 - Pillow (Para editar a imagem de captcha)
 - pyautogui (Para realizar digitação e movimentação no site)
 - pyperclip (Para facilitar a inserção de texto em certos campos)


##Informações Gerais
 - Versão Python: Python 3.12.0
 - Navegador: Google Chrome, versão 118.0.5993.90 (Compilação oficial) (64 bits)
              O download está configurado para que não seja solicitado confirmação antes de baixar.
 - Dimensões da tela: 1440x900


 ##Observações 
 - Certos parâmetros como posição do inseridas no pyautogui precisam ser conferidos de acordo com seu monitor.
 - As pausas definidas também podem ser alteradas a depender da sua velocidade download.
 - O Google Lens não é a solução ideal para esse tipo de automação em minha experiência ele acerta em torno de 1 captcha entre 7 captcha o que é muito lento ainda.
 - Alguns municípios não possuem shapefiles, de modo que ao final da execução é impresso no terminal a lista dos minicipios que não obtiveram sucesso em 10 tentativas.


 ##Pontos a melhorar
 - Uma exelente futura atualização seria a criação de um OCR treinado especificamente com os captchas do próprio site https://www.car.gov.br/publico/municipios/
 - Refazer sem o uso do Chrome e sem o PyAutoGui, ou seja, só pelo terminal.


 ##Ideias Relacionadas ao Tema
 - Seria interessante a simplificação e união do shapefiles de todo o Brasil de modo a desenvolver um shape com área cultivavel nacional podendo assim cruzar isso com o mapa de solos, uso de solo, temperatura, queimadas etc...

