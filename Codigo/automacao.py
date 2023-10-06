import os
import time
import webbrowser
from PIL import Image
import pyautogui
import pyperclip as pc

def main():
    listacod = [4309209, 4309258, 4309407]  # lista com o código do IBGE dos municípios desejados
    url = "https://www.car.gov.br/publico/imoveis/index"
    webbrowser.open(url, 2)
    time.sleep(7)
    for muni in listacod:
        situacao = False
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
            situacao = busca(muni)
            pyautogui.moveTo(500, 500)
            time.sleep(0.5)
            pyautogui.hotkey("ctrl", "w", interval= 3)
            pyautogui.hotkey("ctrl", "r", interval= 7)
#repetição
def busca(ibgeid):
    vezesb = 1
    pyautogui.press('tab', presses= 8, interval= 0.2)
    time.sleep(1)
    pyautogui.hotkey("shift", "f10", interval= 2)
    pyautogui.press('up', interval= 1)
    pyautogui.press('enter', interval= 2)
    pyautogui.press('up', presses= 2, interval= 1)
    pyautogui.hotkey("shift", "f10", interval= 1)
    pyautogui.press('down', presses= 2, interval= 1)
    pyautogui.press('enter', interval= 1)
    pc.copy('<button type="button" class="btn btn-shp btn-sm btn-download" title="Baixar Shapefile" data-tipodownload="shapefile" data-municipio="'+ibgeid+'"><h4><i class="fa fa-globe"></i></h4></button>')
    pyautogui.hotkey("ctrl", "a", interval= 1)
    pyautogui.hotkey("ctrl", "v", interval= 1)
    pyautogui.hotkey("ctrl", "enter", interval= 1)
    pyautogui.hotkey("ctrl", "shift" , "i", interval= 3)
    pyautogui.press('enter', interval= 1)
    pyautogui.press('tab', presses= 2, interval= 0.1)
    pc.copy(f"umemail{ibgeid}@gmail.com")
    time.sleep(0.6)
    pyautogui.hotkey("ctrl", "v", interval= 1)
    while True:
        texto = ""
        while True:
            vezesb += 1
            if vezesb > 15: # 15 é o número de tentativas maxímo#
                return True
            time.sleep(2)
            pyautogui.press('tab', interval= 2)
            pyautogui.press("apps", interval= 1)
            pyautogui.press('n', interval= 3)
            pyautogui.press('up', presses= 2, interval= 1)
            pyautogui.press("apps", interval= 1)
            pyautogui.press('s', interval= 1)
            pyautogui.press('up', interval= 1)
            pyautogui.press('enter', interval= 2)
            pyautogui.hotkey("ctrl", "shift" , "i", interval= 1)

            os.chdir('C:/Users/joao/Downloads')
            for arq in os.listdir():
                if arq.startswith("www.car.gov.br"): # inicio de nome da imagem baixada
                    os.rename(arq,"captcha.png")
                    break

            if "captcha.png" not in os.listdir():
                pyautogui.hotkey("tab", presses = 3, interval = 0.1)
                time.sleep(0.1)
                pyautogui.hotkey("enter", interval = 3)
            else:
                img = Image.open("C:/Users/joao/Downloads/captcha.png").convert("RGBA")
                width, height = img.size
                img_com_fundo_branco = Image.new("RGBA", (width, height), (255, 255, 255))  # Criar uma imagem com fundo branco
                img_com_fundo_branco.paste(img, (0, 0), img)  # Colar a imagem RGB na imagem com fundo branco
                pixels = img_com_fundo_branco.load() # Carrega pixels
                for x in range(width):
                    nomedospixels = ""
                    vermelhovirabranco = True
                    for y in range(height):
                        r, g, b, a = pixels[x, y]
                        media = int((r + g + b)/3)
                        if media > 210:
                            nomedospixels = nomedospixels + "b"
                        elif media < 40:
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
                        elif media > 40 and vermelhovirabranco:
                            pixels[x, y] = (255, 255, 255, a)
                        else:
                            pixels[x, y] = (media, media, media, a)

                img_com_fundo_branco.save("C:/Users/joao/Downloads/captcha.png")
                pyautogui.hotkey("ctrl", "t", interval = 2.5)
                pc.copy("file:///C:/Users/joao/Downloads/captcha.png")
                pyautogui.hotkey("ctrl", "v", interval = 1)
                pyautogui.press('enter', interval = 3)

                pyautogui.moveTo(734, 470)
                time.sleep(1)
                pyautogui.click(button='right', interval = 1)
                pyautogui.press('p', interval = 1)

                # botao texto do google lens
                pyautogui.moveTo(1264, 333)
                time.sleep(2)
                pyautogui.click(button='left')

                # botao selecionar texto
                pyautogui.moveTo(1264, 674)
                time.sleep(2)
                pyautogui.click(button='left')

                # botao copiar texto
                pyautogui.moveTo(1183, 443)
                time.sleep(2)
                pyautogui.click(button='left')
                texto_anterior = texto
                texto = pc.paste()

                #fechar len
                pyautogui.moveTo(1400, 109)
                time.sleep(2)
                pyautogui.click(button='left')
                time.sleep(1)
                pyautogui.hotkey("ctrl", "w", interval = 1)
                os.remove("C:/Users/joao/Downloads/captcha.png")

                if len(texto) == 5 and texto != texto_anterior:
                    break
                else:
                    pyautogui.press("enter", interval= 2)
                    pyautogui.hotkey("shift", "tab", interval= 0.1)

        time.sleep(3)
        pyautogui.press("tab", interval= 1)
        pyautogui.hotkey("ctrl", "a", interval= 0.5)
        pyautogui.hotkey("ctrl", "v", interval= 0.5)

        os.chdir('C:/Users/joao/Downloads')
        qtde = len(os.listdir())
        pyautogui.press("tab", interval = 0.5)
        pyautogui.press("enter", interval = 4)

        novaqtde = len(os.listdir())
        print(qtde)
        print(novaqtde)
        if qtde < novaqtde:
            pyautogui.press("esc", interval = 2)
            break
        else:
            pyautogui.hotkey("shift", "tab", presses= 2, interval= 1)
            pyautogui.press("enter", interval= 2)

    return True

main()
