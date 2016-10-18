import lcd_16x2 as lcd
from time import sleep

lcd.lcd_init()
lcd.lcd_CursorOFF()
lcd.lcd_Clear()

global yazi,k
yazi = ""
k = ""

def main():
 while(1):
  sleep(1)
  print "c : clear ,h : cursorHome , o : cursor on , p : cursorOff , l: CursorBlink, w: write"
  print "sL : Shitleft, sR : ShiftRight ,sAL : shiftAnimLeft , sAR : shiftAnimRight"
  k = str(raw_input("secim gir:"))
  print "",k
  if(k == "c"):
   lcd.lcd_Clear()
  elif(k == "o"):
   lcd.lcd_CursorON()
  elif(k == "p"):
   lcd.lcd_CursorOFF()
  elif(k == "l"):
   lcd.lcd_CursorBlink()
  elif(k == "w"):
   yazi = str(raw_input("1.satır Ekrana Yaz: "))
   lcd.lcd_string(yazi,lcd.LCD_LINE_1)
   yazi = str(raw_input("2.Satır Ekrana Yaz: "))
   lcd.lcd_string(yazi,lcd.LCD_LINE_2)
  elif(k == "sL"):
   lcd.lcd_ShiftLefts(int(raw_input("ne kadar kaydırılıcak : ")))
  elif(k == "sR"):
   lcd.lcd_ShiftRight()
  elif(k == "h"):
   lcd.lcd_CursorHome()
  elif(k == "sAL"):
   lcd.lcd_ShiftAnimLeft(2,1)
  elif(k == "sAR"):
   lcd.lcd_ShiftAnimRight(2,2)

main()
