import os
import time
import webbrowser
from PIL import Image
import pyautogui
import pyperclip as pc 

def main():
    listaCod = [4309209, 4309258, 4309407]  # lista com o código do seu município
    print(len(listaCod))
    url = "https://www.car.gov.br/publico/imoveis/index"
    webbrowser.open(url, 2)
    time.sleep(7)
    
    for muni in listaCod:
        situacao = False
        vezes = 1
        muni = str(muni)
        while not situacao:                             
            dicio = {'11':"RO", '12':"AC",'13':"AM",'14':"RR",'15':"PA",'16':"AP",'17':"TO",
                     '21':"MA",'22':"PI",'23':"CE",'24':"RN",'25':"PB", '26':"PE",'27':"AL",'28':"SE",'29':"BA",
                     '31':"MG",'32':"ES",'33':"RJ",'35':"SP",
                     '41':"PR",'42':"SC",'43':"RS",
                     '50':"MS",'51':"MT",'52':"GO",'53':"DF"}  # dicionario de código de estado e sigla do estado
            sigla = dicio[muni[:2]]
            url = "https://www.car.gov.br/publico/municipios/downloads?sigla=" + sigla
            webbrowser.open(url, 2)
            time.sleep(7)
            situacao = busca(muni, vezes)
            pyautogui.moveTo(500, 500)
            time.sleep(0.5)
            pyautogui.hotkey("ctrl", "w")
            time.sleep(3)
            pyautogui.hotkey("ctrl", "r")
            time.sleep(7)
#repetição
def busca(ibgeid , vezesb):
    i = 0
    while i < 8:
        pyautogui.press('tab')
        time.sleep(0.2)
        i = i+1
    time.sleep(1)
    pyautogui.hotkey("shift", "f10")
    time.sleep(2)
    pyautogui.press('up')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('up')
    time.sleep(1)
    pyautogui.press('up')
    time.sleep(1)
    pyautogui.hotkey("shift", "f10")
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pc.copy('<button type="button" class="btn btn-shp btn-sm btn-download" title="Baixar Shapefile" data-tipodownload="shapefile" data-municipio="'+ibgeid+'"><h4><i class="fa fa-globe"></i></h4></button>')
    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "enter")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "shift" , "i")
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(0.1)
    pyautogui.press('tab')
    time.sleep(0.1)
    pc.copy(f"umemail{ibgeid}@gmail.com")
    time.sleep(0.6)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    while True:
        texto = ""
        while True:
            vezesb += 1
            if vezesb > 15: # 15 é o número de tentativas maxímo#
                return True
            time.sleep(2)
            pyautogui.press('tab')
            time.sleep(2)
            pyautogui.press("apps")
            time.sleep(1)
            pyautogui.press('n')
            time.sleep(3)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press("apps")
            time.sleep(1)
            pyautogui.press('s')
            time.sleep(1)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.hotkey("ctrl", "shift" , "i")
            os.chdir('C:/Users/joao/Downloads')
            for arq in os.listdir():
                if arq.startswith("www.car.gov.br"): # inicio de nome da imagem baixada
                    os.rename(arq,"captcha.png")
                    break

            if "captcha.png" not in os.listdir():
                pyautogui.hotkey("tab", presses = 3, interval = 0.1)
                time.sleep(0.1)
                pyautogui.hotkey("enter")
                time.sleep(3)
            else:
                img = Image.open("C:/Users/joao/Downloads/captcha.png").convert("RGBA")

                width, height = img.size
                img_com_fundo_branco = Image.new("RGBA", (width, height), (255, 255, 255))  # Criar uma imagem com fundo branco
                img_com_fundo_branco.paste(img, (0, 0), img)  # Colar a imagem RGB na imagem com fundo branco

                pixels = img_com_fundo_branco.load()
                for x in range(width):
                    nomedospixels = ""
                    vermelhovirabranco = True
                    for y in range(height):
                        r, g, b, a = pixels[x, y]
                        media = int((r + g + b)/3)
                        if media > 210:
                            nomedospixels = nomedospixels + "b"
                        elif media < 49:
                            nomedospixels = nomedospixels + "p"
                        else:
                            nomedospixels = nomedospixels + "v"

                    if "vp" in nomedospixels or "pv" in nomedospixels:
                        vermelhovirabranco = False
                        
                    for y in range(height):
                        r, g, b, a = pixels[x, y]
                        media = int((r + g + b)/3)
                        if x == 0 or y == 0 or x == width or y == height:
                            pixels[x, y] = (255, 255, 255, a)
                        elif media > 210:
                            pixels[x, y] = (255, 255, 255, a)
                        else: 
                            # ra, ga, ba, aa = pixels[x,(y-1)] # acima
                            # mediaacima = int((ra + ga + ba)/3)
                            # rl, gl, bl, al = pixels[(x-1),y] # esquerda
                            # mediaesquerda = int((rl + gl + bl)/3)
                            if media > 40 and vermelhovirabranco:
                                pixels[x, y] = (255, 255, 255, a)
                            else:
                                pixels[x, y] = (media, media, media, a)

                img_com_fundo_branco.save("C:/Users/joao/Downloads/captcha.png")
                pyautogui.hotkey("ctrl", "t")
                time.sleep(1.5)
                pc.copy("file:///C:/Users/joao/Downloads/captcha.png")
                time.sleep(1)
                pyautogui.hotkey("ctrl", "v")
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(3)

                pyautogui.moveTo(971, 565)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(1)
                pyautogui.hotkey('p')
                time.sleep(1)

                # botao texto do google lens
                pyautogui.moveTo(1694, 451)
                time.sleep(1)
                pyautogui.click(button='left')

                # botao selecionar texto
                pyautogui.moveTo(1694, 280)
                time.sleep(1)
                pyautogui.click(button='left')

                # botao copiar texto
                pyautogui.hotkey("shift", "tab")
                time.sleep(1)
                pyautogui.hotkey('enter')
                texto_anterior = texto
                texto = pc.paste()

                #fechar len
                time.sleep(2)
                pyautogui.moveTo(1872, 136)
                time.sleep(0.2)
                pyautogui.click(button='left')

                pyautogui.hotkey("ctrl", "w")
                time.sleep(1)
                os.remove("C:/Users/joao/Downloads/captcha.png")

                if len(texto) == 5 and texto != texto_anterior:
                    break
                else:
                    for i in range(3):
                        pyautogui.hotkey("tab")
                        time.sleep(0.1)
                    pyautogui.hotkey("enter")
                    time.sleep(2)

        time.sleep(3)
        for i in range(4):
            pyautogui.hotkey("tab")
            time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)


        os.chdir('C:/Users/joao/Downloads')
        qtde = len(os.listdir())

        pyautogui.hotkey("tab")
        time.sleep(0.5)
        pyautogui.hotkey("enter")
        time.sleep(6)

        novaqtde = len(os.listdir())
        print(qtde)
        print(novaqtde)
        if qtde < novaqtde:
            pyautogui.hotkey("esc")
            time.sleep(2)
            break
        else:
            for i in range(2):
                pyautogui.hotkey("shift", "tab")
                time.sleep(1)
            pyautogui.hotkey("enter")
            time.sleep(2)

    return True

main()
