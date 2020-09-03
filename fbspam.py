#!/usr/bin/python
# coding=utf-8
#///.coded by YOUSEF WAMEEDH
import time
import os,sys
from YOUSEF import c
from YOUSEF import s
from YOUSEF import f

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

green = '\033[32;1m'

gta = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
  #//Colors 
white = '\033[1;37m' # White 
prred = '\033[31m' # red
orange = '\033[33m' # orange
blue = '\033[34m' # blue
p  = '\033[35m' # purple
C  = '\033[36m' # cyan
green = ("\033[92m")
pryellow = ("\033[93m")
prlight=("\033[94m")
prCyan=("\033[96m")
prgray = ("\033[97m")
prBlack=("\033[98m")



class fbspam:
  def __init__(self):
      self.cade=(green+'[💡]YOUSEF)=>:  ')
      print prCyan+"""
██╗   ██╗ ██████╗ ██╗   ██╗███████╗███████╗███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██╔════╝██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║███████╗█████╗  █████╗  
  ╚██╔╝  ██║   ██║██║   ██║╚════██║██╔══╝  ██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝███████║███████╗██║     
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝ 
        THE TOOL MADE BY YOUSEF\n 
         facebook : iaem hacker
          developer: YOUSEF
       """
      print '-'*43
      time.sleep(1)
      return self.choose()
      
      
      
  def choose(self):
      print (p+'         ({1})'+prlight+' Custom Messager')
      print (p+'         ({2}) '+prCyan+'Spammer Message')
      print (p+'         ({3}) '+green+'Custom List Messager')
      print (p+'         ({4}) '+p+'GROUP CHAT SPAMMER')
      print (p+'         ({0}) '+c+'Exit')
      time.sleep(1)
      print
      return self.mee()
      
      
      
  def mee(self):
      inn =raw_input(self.cade+'')
      if (inn=='1' ):
          print
          c.shit2()
      elif (inn=='2'):
          print
          s.shit()
      elif (inn=='3'):
          print
          f.shit3()
      elif (inn=='4'):
          self.buy()
      elif (inn=='0'):
          time.sleep(1)
          exit()
      else:
          return self.mee()
      
     
      
  def buy(self):
      print
      print ('[🔗]Paid .this option is locked')
      
 





       
       
       

       
if __name__ == "__main__":
	YOUSEF()