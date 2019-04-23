# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:05:30 2019

@author: Brahim OULHAJ
         ⴱⵔⴰⵀⵉⵎ ⵓⵍⵃⴰI
"""

from num2words import num2words

def n2w(n,l='en'):
    nums = {
        0:"ⴰⵎⵢⴰ",1:"ⵢⴰⵏ",2:"ⵙⵉⵏ",3:"ⴽⵕⴰⴹ",4:"ⴽⴽⵓⵥ",5:"ⵙⵎⵎⵓⵙ",
        6:"ⵚⴹⵉⵚ",7:"ⵙⴰ",8:"ⵜⵜⴰⵎ",9:"ⵜⵜⵥⴰ",10:"ⵎⵔⴰⵡ",
        20:"(ⵙⵉⵎⵔⴰⵡ / ⴰⴳⵏⴰⵔ)",30:"ⴽⵕⴰⵎⵔⴰⵡ",40:"ⴽⴽⵓⵥⵎⵔⴰⵡ",50:"ⵙⵎⵎⵓⵙⵎⵔⴰⵡ",60:"ⵚⴹⵉⵚⵎⵔⴰⵡ",
        70:"ⵙⴰⵎⵔⴰⵡ",80:"ⵜⵜⴰⵎⵎⵔⴰⵡ",90:"ⵜⵜⵣⴰⵎⵔⴰⵡ",100:"ⵜⵉⵎⵉⴹⵉ",200:"ⵙⵏⴰⵜ ⵏ ⵜⵉⵎⵎⴰⴹ",
        300:"ⴽⵕⴰⵜ ⵏ ⵜⵉⵎⵎⴰⴹ",400:"ⴽⴽⵓⵥ ⵏ ⵜⵉⵎⵎⴰⴹ",500:"ⵙⵎⵎⵓⵙ ⵏ ⵜⵉⵎⵎⴰⴹ",600:"ⵚⴹⵉⵚ ⵏ  ⵜⵉⵎⵎⴰⴹ",
        700:"ⵙⴰ ⵏ ⵜⵉⵎⵎⴰⴹ",800:"ⵜⵜⴰⵎ ⵏ ⵜⵉⵎⵎⴰⴹ",900:"ⵜⵜⵣⴰⵜ ⵏ ⵜⵉⵎⵎⴰⴹ",1000:"ⵉⴼⴹ",
        1000000:"ⴰⴳⵏⴷⵉⴷ",1000000000:"ⵎⵍⵢⴰⵕ",'.':"ⵜⵉⵙⴽⵔⵜ",'-':"ⵓⵣⴷⵉⵔ"
    }
    
    if(l == 'tz'):
        if n<0:
                return nums.get("-")+", "+n2w(-1*n,'tz')
        if isinstance(n,int):
            if n in nums:
                return nums.get(n)
            else:
                if n%1000 == 0 and n<1000000:
                    return n2w(int(n/1000),'tz')+" ⵏ "+nums.get(1000)+"ⵏ"
                if n%1000000 == 0 and n<1000000000:
                    return n2w(int(n/1000000),'tz')+" ⵏ ⵉⴳⵏⴷⵉⴷⵏ"
                if n%1000000000 == 0 and n<1000000000000:
                    return n2w(int(n/1000000000),'tz')+" "+nums.get(1000000000)
                
                if n>10 and n<20:
                    return nums.get(n%10)+" ⴷ "+n2w((int)(n/10)*10,'tz')
                else:
                    if n>20 and n<100:
                        return nums.get((int)(n/10)*10)+" ⴷ "+n2w(n%10,'tz')
                    else:
                        if n>100 and n<1000:
                            return nums.get((int)(n/100)*100)+" ⴷ "+n2w(n%100, 'tz')
                        else:
                            if n>1000 and n<1000000:
                                return n2w((int)(n/1000)*1000,'tz')+" ⴷ "+n2w(n%1000,'tz')
                            else:
                                if n>1000000 and n<1000000000:
                                    return n2w((int)(n/1000000)*1000000,'tz')+" ⴷ "+n2w(n%1000000,'tz')
                                else:
                                    if n>1000000000 and n<1000000000000:
                                        return n2w((int)(n/1000000000)*1000000000,'tz')+" ⴷ "+n2w(n%1000000000,'tz')
                                    else:
                                        return 'too large'
        else:
            st = str(n).split(".")
            a = int(st[0])
            b = int(st[1])
            if a==0 and b==5:
                return 'ⴰⵣⴳⵏ'
            if b==5:
                return n2w(int(st[0]),'tz')+" ⴷ ⵓⵣⴳⵏ"
            else:
                return n2w(int(st[0]),'tz')+" "+nums.get(".")+" "+n2w(int(st[1]),'tz')
    else:
        return num2words(n,lang=l)
