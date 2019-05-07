import random

q = open("Usuario1.txt","w+")
g = open("Usuario2.txt","w+")
q1 = open("Score1.txt","w+")
g1 = open("Score2.txt","w+")
q.close()
g.close()
q1.close()
g1.close()
#################################################################
def convBin(num):
    binario=""
    res=""
    return Aux_convBin(num,binario,res)
def Aux_convBin(num,binario,res):
    if(num==0): #caso base
        res=res+"0"
        return int(res)
    else:
        if(num>2):#Caso recursivo
            #print("caso recursivo")
            temp=num%2
            binario=binario + str(temp)
            #print(num," antes")
            num=num//2
            #print(num," despues")
            return Aux_convBin(num, binario, res)
        
        if(num==2): #caso salida
            binario=binario+"0"
            binario=binario+"1"
            x=len(binario)-1
            return Aux_Bin(binario, res,x)
        elif(num//2==0): #caso Salida
            binario=binario+"1"
            x=len(binario)-1
            return Aux_Bin(binario, res,x)
def Aux_Bin(binario, res,x):
    if(x==0):#caso salida
        res=res+binario[0]
        return int(res)
    else:
        res=res+binario[x]
        return Aux_Bin(binario, res, x-1)
#################################################################
def convOct(num):
    octal=""
    res=""
    return Aux_convOct(num,octal,res)
def Aux_convOct(num,octal,res):
    if(num==0): #caso base
        res=res+"0"
        return int(res)
    else:
        if((num//8)>8):#caso recursivo
            #print("Caso Resursivo")
            temp=num%8
            octal=octal+str(temp)
            #print(num," antes")
            num=num//8
            #print(num," despues")
            return Aux_convOct(num,octal,res)
        if((num//8)<8): #caso salida
            #print("caso salida")
            temp=num%8
            octal=octal+str(temp)
            octal=octal+str(num//8)
            x=len(octal)-1
            return Aux_Oct(octal,res,x)
def Aux_Oct(octal, res,x):
    if(x==0):#caso salida
        res=res+octal[0]
        return int(res)
    else:
        res=res+octal[x]
        return Aux_Bin(octal, res, x-1)
##################################################################
def convHex(num):
    hexadecimal=""
    res=""
    return Aux_convHex(num,hexadecimal,res)
def Aux_convHex(num,hexadecimal,res):
    if(num==0): #caso base
        res=res+"0"
        return res
    else:
        if((num//16)>16):#caso recursivo
            #print("Caso Resursivo")
            temp=num%16
            if(temp==15):
                temp="F"
            if(temp==14):
                temp="E"
            if(temp==13):
                temp="D"
            if(temp==12):
                temp="C"
            if(temp==11):
                temp="B"
            if(temp==10):
                temp="A"
            hexadecimal=hexadecimal+str(temp)
            #print(num," antes")
            num=num//16
            #print(num," despues")
            return Aux_convHex(num,hexadecimal,res)
        if((num//16)<16): #caso salida
            #print("caso salida")
            temp=num%16
            if(temp==15):
                temp="F"
            if(temp==14):
                temp="E"
            if(temp==13):
                temp="D"
            if(temp==12):
                temp="C"
            if(temp==11):
                temp="B"
            if(temp==10):
                temp="A"            
            hexadecimal=hexadecimal+str(temp)
            if(temp!="F" and temp!="E" and temp!="D" and temp!="C" and temp!="B" and temp!="A"):
                hexadecimal=hexadecimal+str(num//16)
                #print("here")            
            x=len(hexadecimal)-1
            return Aux_Hex(hexadecimal,res,x)
def Aux_Hex(hexadecimal, res,x):
    if(x==0):#caso salida
        res=res+hexadecimal[0]
        return res
    else:
        res=res+hexadecimal[x]
        return Aux_Hex(hexadecimal, res, x-1)
####################################################################################

def Tabla_conv(num,Dificultad):
    if(int(Dificultad)==1):
        return num
    if(int(Dificultad)==2):
        return convBin(num)
    if(int(Dificultad)==3):
        return convOct(num)
    if(int(Dificultad)==4):
        return convHex(num)
####################################################################################   
def ResMatriz(Matriz,Dificultad):
    z=0
    w=0
    Filas=4
    Columnas=4
    tabla=""
   
    f = open("Usuario_Actual.txt","r")
    Usuario_Actual = f.read()
    
    f1 = open("Score_Actual.txt","r")
    Score_Actual = f1.read()
    
    
    q = open("Usuario1.txt","r")
    Usuario1 = q.read()
    
    
    q1 = open("Score1.txt","r")
    Score1 = q1.read()

    
    g = open("Usuario2.txt","r")
    Usuario2 = g.read()

    
    g1 = open("Score2.txt","r")
    Score2 = g1.read()

    if(Score1 == ""):
        q = open("Usuario1.txt","w")
        q1 = open("Score1.txt","w")
        Usuario1 = Usuario_Actual
        Usuario1 = str(Usuario1)
        Score1 = Score_Actual
        Score1 = str(Score1)
        q.write(Usuario1)
        q1.write(Score1)
        f.close()
        f1.close()
        q.close()
        q1.close()
        g.close()
        g1.close()
    else:
        if(int(Score_Actual)>=int(Score1)):
            g = open("Usuario2.txt","w")
            g1 = open("Score2.txt","w")
            Usuario2 = Usuario1
            Usuario2 = str(Usuario2)
            Score2 = Score1
            Score2 = str(Score2)
            g.write(Usuario2)
            g1.write(Score2)
            
            q = open("Usuario1.txt","w")
            q1 = open("Score1.txt","w")
            Usuario1 = Usuario_Actual
            Usuario1 = str(Usuario1)
            Score1 = Score_Actual
            Score1 = str(Score1)
            q.write(Usuario1)
            q1.write(Score1)
            f.close()
            f1.close()
            q.close()
            q1.close()
            g.close()
            g1.close()
        else:
            if(Score2 == ""):
                g = open("Usuario2.txt","w")
                g1 = open("Score2.txt","w")
                Usuario2 = Usuario_Actual
                Usuario2 = str(Usuario2)
                Score2 = Score_Actual
                Score2 = str(Score2)
                g.write(Usuario1)
                g1.write(Score1)
                f.close()
                f1.close()
                q.close()
                q1.close()
                g.close()
                g1.close()
            else:              
                if(int(Score_Actual)>=int(Score2)):
                    g = open("Usuario2.txt","w")
                    g1 = open("Score2.txt","w")
                    Usuario2 = Usuario_Actual
                    Usuario2 = str(Usuario2)
                    Score2 = Score_Actual
                    Score2 = str(Score2)
                    g.write(Usuario2)
                    g1.write(Score2)
                    f.close()
                    f1.close()
                    q.close()
                    q1.close()
                    g.close()
                    g1.close()
    
    print("Leaderboard:")
    print("1.Usuario: ",Usuario1," Score: ",Score1)
    print("2.Usuario: ",Usuario2," Score: ",Score2)
    print("\n")

    
    
    f = open("Usuario_Actual.txt","r")
    Usuario = f.read()
    f1 = open("Score_Actual.txt","r")
    score_Actual = f1.read() 
    q1 = open("Score1.txt","r")
    score_Best = q1.read()
    
    
    print("Usuario: ",Usuario,"\t"+"Score: ",score_Actual,"\t"+"Best: ",score_Best)
    print("\n")

    f.close()
    f1.close()
    q1.close()
    
    return Aux_ResMatriz(Matriz,Filas,Columnas,z,w,tabla,Dificultad)
    

def Aux_ResMatriz(Matriz,Filas,Columnas,z,w,tabla,Dificultad):
    
    
    if(w<Columnas and z<Filas):
        num = Matriz[z][w]
        temp = Tabla_conv(num,Dificultad)
        tabla= tabla + "\t" + "\t" +str(temp)
        return Aux_ResMatriz(Matriz,Filas,Columnas,z,w+1,tabla,Dificultad)
    
    else:
        
        if(z==Filas):
            print(tabla,"\t")
        else:
            print(tabla,"\t")
            return Aux_ResMatriz(Matriz,Filas,Columnas,z+1,0,"",Dificultad)
####################################################################################
def Arriba(Matriz,GameExit):
    z = 0
    w = 0
    ceros = 0
    suma = 1
    return Aux_Arriba(Matriz,z,w,ceros,suma,GameExit)

def Aux_Suma_Arriba(Matriz,z,w,ceros,suma,GameExit):
    if(w==4):
        suma=0
        return Aux_Arriba(Matriz,0,0,0,suma,GameExit)
    else:
        if(Matriz[z][w]==0):
            if(z<3):                
                return Aux_Suma_Arriba(Matriz,z+1,w,ceros,suma,GameExit)
            else:#z==3              
                return Aux_Suma_Arriba(Matriz,0,w+1,ceros,suma,GameExit)
                
        if(Matriz[z][w]!=0):
            if(z==0):
                if(Matriz[z][w]==Matriz[z+1][w]):
                    Matriz[z][w] = Matriz[z][w]*2
                    Matriz[z+1][w] = 0
                    f = open("Score_Actual.txt","r")
                    score_Actual = f.read()
                    score_Actual = int(score_Actual) + int(Matriz[z][w])
                    score_Actual = str(score_Actual)
                    f = open("Score_Actual.txt","w")
                    f.write(score_Actual)
                    f.close()
                    return Aux_Suma_Arriba(Matriz,z+1,w,ceros,suma,GameExit)
                else:
                    
                    return Aux_Suma_Arriba(Matriz,z+1,w,ceros,suma,GameExit)

            if(z<3):
                if(Matriz[z][w]==Matriz[z+1][w]):
                    Matriz[z][w] = Matriz[z][w]*2
                    Matriz[z+1][w] = 0
                    f = open("Score_Actual.txt","r")
                    Score_Actual = f.read()
                    Score_Actual = int(Score_Actual) + int(Matriz[z][w])
                    Score_Actual = str(Score_Actual)
                    f = open("Score_Actual.txt","w")
                    f.write(Score_Actual)
                    f.close()
                    return Aux_Suma_Arriba(Matriz,z+1,w,ceros,suma,GameExit)
                else:
                    return Aux_Suma_Arriba(Matriz,z+1,w,ceros,suma,GameExit)

            else:#z==3           
                return Aux_Suma_Arriba(Matriz,0,w+1,ceros,suma,GameExit)
                
        

def Aux_Arriba(Matriz,z,w,ceros,suma,GameExit):
    #print("z:",z," w:",w)
    #print("Ceros:",ceros)
    #print("z-ceros:",z-ceros)
    if(w==4):
        if(suma==1):
            Aux_Suma_Arriba(Matriz,0,0,0,suma,GameExit)
    else:   
        if(Matriz[z][w]==0):
            ceros = ceros+1
            if(z<3):
                return Aux_Arriba(Matriz,z+1,w,ceros,suma,GameExit)
            else:#z==3
                return Aux_Arriba(Matriz,0,w+1,0,suma,GameExit)
        if(Matriz[z][w]!=0):
            if(z<3):
                if(ceros>0): 
                    Matriz[z-ceros][w]= Matriz[z][w]
                    #print("Move Matriz[",z,"][",w,"] to Matriz[",z-ceros,"][",w,"]")
                    Matriz[z][w] = 0
                    return Aux_Arriba(Matriz,z+1,w,ceros,suma,GameExit)
                else:
                    return Aux_Arriba(Matriz,z+1,w,0,suma,GameExit)
            else:#z==3
                if(ceros>0):
                    Matriz[z-ceros][w] = Matriz[z][w]
                    #print("Move Matriz[",z,"][",w,"] to Matriz[",z-ceros,"][",w,"]")
                    Matriz[z][w] = 0
                    return Aux_Arriba(Matriz,0,w+1,0,suma,GameExit)
                else:
                    return Aux_Arriba(Matriz,0,w+1,0,suma,GameExit)


###########################################################################################

def Abajo(Matriz,GameExit):
    z = 3
    w = 0
    ceros = 0
    suma = 1
    return Aux_Abajo(Matriz,z,w,ceros,suma,GameExit)


def Aux_Suma_Abajo(Matriz,z,w,ceros,suma,GameExit):
    if(w==4):
        suma=0
        return Aux_Abajo(Matriz,0,0,0,suma,GameExit)
    
    else:
        if(Matriz[z][w]==0):
            if(z>0):
                return Aux_Suma_Abajo(Matriz,z-1,w,ceros,suma,GameExit)
            else:#z==0
                return Aux_Suma_Abajo(Matriz,3,w+1,ceros,suma,GameExit)
                
        if(Matriz[z][w]!=0):
            if(z==3):
                if(Matriz[z][w]==Matriz[z-1][w]):
                    Matriz[z][w] = Matriz[z][w]*2
                    Matriz[z-1][w] = 0
                    f = open("Score_Actual.txt","r")
                    Score_Actual = f.read()
                    Score_Actual = int(Score_Actual) + int(Matriz[z][w])
                    Score_Actual = str(Score_Actual)
                    f = open("Score_Actual.txt","w")
                    f.write(Score_Actual)
                    f.close()
                    return Aux_Suma_Abajo(Matriz,z-1,w,ceros,suma,GameExit)
                else:
                    return Aux_Suma_Abajo(Matriz,z-1,w,ceros,suma,GameExit)

            if(z>0):
                if(Matriz[z][w]==Matriz[z-1][w]):
                    Matriz[z][w] = Matriz[z][w]*2
                    Matriz[z-1][w] = 0
                    f = open("Score_Actual.txt","r")
                    Score_Actual = f.read()
                    Score_Actual = int(Score_Actual) + int(Matriz[z][w])
                    Score_Actual = str(Score_Actual)
                    f = open("Score_Actual.txt","w")
                    f.write(Score_Actual)
                    f.close()
                    return Aux_Suma_Abajo(Matriz,z-1,w,ceros,suma,GameExit)
                else:
                    return Aux_Suma_Abajo(Matriz,z-1,w,ceros,suma,GameExit)

            else:#z==0
                return Aux_Suma_Abajo(Matriz,3,w+1,ceros,suma,GameExit)



def Aux_Abajo(Matriz,z,w,ceros,suma,GameExit):
    #print("z:",z," w:",w)
    #print("Ceros:",ceros)
    #print("z-ceros:",z-ceros)
    if(w==4):
        if(suma==1):
            Aux_Suma_Abajo(Matriz,3,0,0,suma,GameExit)
    else:   
        if(Matriz[z][w]==0):
            ceros = ceros+1
            if(z>0):
                return Aux_Abajo(Matriz,z-1,w,ceros,suma,GameExit)
            else:#z==0
                return Aux_Abajo(Matriz,3,w+1,0,suma,GameExit)
        if(Matriz[z][w]!=0):
            if(z>0):
                if(ceros>0): 
                    Matriz[z+ceros][w]= Matriz[z][w]
                    #print("Move Matriz[",z,"][",w,"] to Matriz[",z-ceros,"][",w,"]")
                    Matriz[z][w] = 0
                    return Aux_Abajo(Matriz,z-1,w,ceros,suma,GameExit)
                else:
                    return Aux_Abajo(Matriz,z-1,w,0,suma,GameExit)
            else:#z==0
                if(ceros>0):
                    Matriz[z+ceros][w] = Matriz[z][w]
                    #print("Move Matriz[",z,"][",w,"] to Matriz[",z-ceros,"][",w,"]")
                    Matriz[z][w] = 0
                    return Aux_Abajo(Matriz,3,w+1,0,suma,GameExit)
                else:
                    return Aux_Abajo(Matriz,3,w+1,0,suma,GameExit) 


###########################################################################################

def Derecha(Matriz,GameExit):
    z = 0
    w = 3
    ceros = 0
    suma = 1
    return Aux_Derecha(Matriz,z,w,ceros,suma,GameExit)

def Aux_Suma_Derecha(Matriz,z,w,ceros,suma,GameExit):
    #print("z:",z," w:",w)
    if(z==4):
        suma=0
        return Aux_Derecha(Matriz,0,3,0,suma,GameExit)
    else:
        #print(Matriz[z][w])
        if(Matriz[z][w]==0):
            #print("Caso 0")
            if(w>0):
                return Aux_Suma_Derecha(Matriz,z,w-1,ceros,suma,GameExit)
            else:#w==0
                return Aux_Suma_Derecha(Matriz,z+1,3,ceros,suma,GameExit)
                
        if(Matriz[z][w]!=0):
            if(w==3):
                #print("suma caso inicio")
                if(Matriz[z][w]==Matriz[z][w-1]):
                    Matriz[z][w] = Matriz[z][w]*2
                    Matriz[z][w-1] = 0
                    f = open("Score_Actual.txt","r")
                    Score_Actual = f.read()
                    Score_Actual = int(Score_Actual) + int(Matriz[z][w])
                    Score_Actual = str(Score_Actual)
                    f = open("Score_Actual.txt","w")
                    f.write(Score_Actual)
                    f.close()
                    return Aux_Suma_Derecha(Matriz,z,w-1,ceros,suma,GameExit)
                else:
                    return Aux_Suma_Derecha(Matriz,z,w-1,ceros,suma,GameExit)

            if(w>0):
                #print("suma")
                if(Matriz[z][w]==Matriz[z][w-1]):
                    Matriz[z][w] = Matriz[z][w]*2
                    Matriz[z][w-1] = 0
                    f = open("Score_Actual.txt","r")
                    Score_Actual = f.read()
                    Score_Actual = int(Score_Actual) + int(Matriz[z][w])
                    Score_Actual = str(Score_Actual)
                    f = open("Score_Actual.txt","w")
                    f.write(Score_Actual)
                    f.close()
                    return Aux_Suma_Derecha(Matriz,z,w-1,ceros,suma,GameExit)
                else:
                    return Aux_Suma_Derecha(Matriz,z,w-1,ceros,suma,GameExit)

            else:#w==0
                return Aux_Suma_Derecha(Matriz,z+1,3,ceros,suma,GameExit)
                
        

def Aux_Derecha(Matriz,z,w,ceros,suma,GameExit):
    #print("z:",z," w:",w)
    #print("Ceros:",ceros)
    #print("w-ceros:",w-ceros)
    if(z==4):
        if(suma==1):
            Aux_Suma_Derecha(Matriz,0,3,0,suma,GameExit)
    else:   
        if(Matriz[z][w]==0):
            #print(Matriz[z][w])
            ceros = ceros+1
            if(w>0):
                return Aux_Derecha(Matriz,z,w-1,ceros,suma,GameExit)
            else:#w==0
                return Aux_Derecha(Matriz,z+1,3,0,suma,GameExit)
        if(Matriz[z][w]!=0):
            if(w>0):
                if(ceros>0): 
                    Matriz[z][w+ceros]= Matriz[z][w]
                    #print("Move Matriz[",z,"][",w,"] to Matriz[",z-ceros,"][",w,"]")
                    Matriz[z][w] = 0
                    return Aux_Derecha(Matriz,z,w-1,ceros,suma,GameExit)
                else:
                    return Aux_Derecha(Matriz,z,w-1,0,suma,GameExit)
            else:#w==0
                if(ceros>0):
                    Matriz[z][w+ceros] = Matriz[z][w]
                    #print("Move Matriz[",z,"][",w,"] to Matriz[",z-ceros,"][",w,"]")
                    Matriz[z][w] = 0
                    return Aux_Derecha(Matriz,z+1,3,0,suma,GameExit)
                else:
                    return Aux_Derecha(Matriz,z+1,3,0,suma,GameExit)

    
###########################################################################################
def Izquierda(Matriz,GameExit):
    z = 0
    w = 0
    ceros = 0
    suma = 1
    return Aux_Izquierda(Matriz,z,w,ceros,suma,GameExit)

def Aux_Suma_Izquierda(Matriz,z,w,ceros,suma,GameExit):
    #print("z:",z," w:",w)
    if(z==4):
        suma=0
        return Aux_Izquierda(Matriz,0,0,0,suma,GameExit)
    else:
        #print(Matriz[z][w])
        if(Matriz[z][w]==0):
            #print("Caso 0")
            if(w<3):
                return Aux_Suma_Izquierda(Matriz,z,w+1,ceros,suma,GameExit)
            else:#w==3
                return Aux_Suma_Izquierda(Matriz,z+1,0,ceros,suma,GameExit)
                
        if(Matriz[z][w]!=0):
            if(w==0):
                #print("suma caso inicio")
                if(Matriz[z][w]==Matriz[z][w+1]):
                    Matriz[z][w] = Matriz[z][w]*2
                    Matriz[z][w+1] = 0
                    f = open("Score_Actual.txt","r")
                    Score_Actual = f.read()
                    Score_Actual = int(Score_Actual) + int(Matriz[z][w])
                    Score_Actual = str(Score_Actual)
                    f = open("Score_Actual.txt","w")
                    f.write(Score_Actual)
                    f.close()
                    return Aux_Suma_Izquierda(Matriz,z,w+1,ceros,suma,GameExit)
                else:
                    return Aux_Suma_Izquierda(Matriz,z,w+1,ceros,suma,GameExit)

            if(w<3):
                #print("suma")
                if(Matriz[z][w]==Matriz[z][w+1]):
                    Matriz[z][w] = Matriz[z][w]*2
                    Matriz[z][w+1] = 0
                    f = open("Score_Actual.txt","r")
                    Score_Actual = f.read()
                    Score_Actual = int(Score_Actual) + int(Matriz[z][w])
                    Score_Actual = str(Score_Actual)
                    f = open("Score_Actual.txt","w")
                    f.write(Score_Actual)
                    f.close()
                    return Aux_Suma_Izquierda(Matriz,z,w+1,ceros,suma,GameExit)
                else:
                    return Aux_Suma_Izquierda(Matriz,z,w+1,ceros,suma,GameExit)

            else:#w==3
                return Aux_Suma_Izquierda(Matriz,z+1,0,ceros,suma,GameExit)
                
        

def Aux_Izquierda(Matriz,z,w,ceros,suma,GameExit):
    #print("z:",z," w:",w)
    #print("Ceros:",ceros)
    #print("w-ceros:",w-ceros)
    if(z==4):
        if(suma==1):
            Aux_Suma_Izquierda(Matriz,0,0,0,suma,GameExit)
    else:   
        if(Matriz[z][w]==0):
            #print(Matriz[z][w])
            ceros = ceros+1
            if(w<3):
                return Aux_Izquierda(Matriz,z,w+1,ceros,suma,GameExit)
            else:#w==3
                return Aux_Izquierda(Matriz,z+1,0,0,suma,GameExit)
        if(Matriz[z][w]!=0):
            if(w<3):
                if(ceros>0): 
                    Matriz[z][w-ceros]= Matriz[z][w]
                    #print("Move Matriz[",z,"][",w,"] to Matriz[",z-ceros,"][",w,"]")
                    Matriz[z][w] = 0
                    return Aux_Izquierda(Matriz,z,w+1,ceros,suma,GameExit)
                else:
                    return Aux_Izquierda(Matriz,z,w+1,0,suma,GameExit)
            else:#w==3
                if(ceros>0):
                    Matriz[z][w-ceros] = Matriz[z][w]
                    #print("Move Matriz[",z,"][",w,"] to Matriz[",z-ceros,"][",w,"]")
                    Matriz[z][w] = 0
                    return Aux_Izquierda(Matriz,z+1,0,0,suma,GameExit)
                else:
                    return Aux_Izquierda(Matriz,z+1,0,0,suma,GameExit)
###########################################################################################

def Random(Matriz,z,w,ceros):
    if(ceros==0):
        if(z==4):
            ceros=0
            #print("No se genera random")
        else:
            if(Matriz[z][w]==0):
                ceros = 1
                return Random(Matriz,z,w,ceros)
            if(Matriz[z][w]!=0):
                if(w==3):
                    return Random(Matriz,z,w-1,ceros)
                if(w>0):
                    return Random(Matriz,z,w-1,ceros)
                else:#w==0
                    return Random(Matriz,z+1,3,ceros)
    else:
        z = random.randint(0,3)
        w = random.randint(0,3)
        num = random.randint(1,10)
        if(Matriz[z][w]!=0):#Exista un numero
            return Random(Matriz,z,w,ceros)
        else:
            if(num==10):
                Matriz[z][w] = 4
            else:
                Matriz[z][w] = 2
    
###########################################################################################

def juego_GameExit(Matriz,z,w,Busqueda,GameExit):
    
    if(Busqueda==1):
        if(z==4):
            Busqueda = 2
            return juego_GameExit(Matriz,0,0,Busqueda,GameExit)
        else:
            #print("Matriz[",z,"][",w,"]=",Matriz[z][w])
            if(Matriz[z][w]==2048):
                return 3
            if(Matriz[z][w]==0):
                return False

            if(Matriz[z][w]!=0):
                if(w==3):
                    if(Matriz[z][w]==Matriz[z][w-1]):
                        return False
                        
                    else:
                        return juego_GameExit(Matriz,z,w-1,Busqueda,GameExit)

                if(w>0):
                    if(Matriz[z][w]==Matriz[z][w-1]):
                        return False
                    else:
                        return juego_GameExit(Matriz,z,w-1,Busqueda,GameExit)

                else:#w==0
                    return juego_GameExit(Matriz,z+1,3,Busqueda,GameExit)
    if(Busqueda==2):
        if(w==4):
            return True
        else:
            #print("Matriz[",z,"][",w,"]=",Matriz[z][w])
            if(Matriz[z][w]==2048):
                return 3
            if(Matriz[z][w]==0):
                return False
            if(Matriz[z][w]!=0):
                if(z==0):
                    if(Matriz[z][w]==Matriz[z+1][w]):
                        return False
                        
                    else:
                        return juego_GameExit(Matriz,z+1,w,Busqueda,GameExit)

                if(z<3):
                    if(Matriz[z][w]==Matriz[z+1][w]):
                        return False
                    else:
                        return juego_GameExit(Matriz,z+1,w,Busqueda,GameExit)

                else:#z==3
                    return juego_GameExit(Matriz,0,w+1,Busqueda,GameExit)


###########################################################################################

def main(partida):
    if(partida==1):
        ########################
        Usuario = input("Ingrese su Nickname: ")
        print("Ingrese el Modo Numerico: (1)Decimal  (2)Binario  (3)Octal  (4)Hexadecimal")  
        Dificultad = input("Modo: ")
        print("\n")
        print("INSTRUCCIONES:")
        print("Las teclas de direcciones son: w a s d")
        print("La tecla w es para mover hacia arriba")
        print("La tecla s es para mover hacia abajo")
        print("La tecla a es para mover hacia la izquierda")
        print("La tecla d es para mover hacia la derecha")
        print("Para seleecionar el next move preciona una tecla de direccion y luego la tecla ENTER")
        Matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        #Matriz = [[1024,16,8,4],[1024,8,4,2],[32,512,2,4],[128,4,16,2]]
        GameExit = False
        ########################
        f = open("Usuario_Actual.txt","w+")
        Usuario_Actual = Usuario
        Usuario_Actual = str(Usuario_Actual)
        f.write(Usuario_Actual)
        f1 = open("Score_Actual.txt","w+")
        Score_Actual = 0
        Score_Actual = str(Score_Actual)
        f1.write(Score_Actual)
        f.close()
        f1.close()

        
        ########################
        Random(Matriz,0,3,0)
        Random(Matriz,0,3,0)
        print("\n"*3)
        ResMatriz(Matriz,Dificultad)
        return juego(GameExit,Matriz,Dificultad)
    else:
        ########################
        print("Ingrese el Modo Numerico: (1)Decimal  (2)Binario  (3)Octal  (4)Hexadecimal")  
        Dificultad = input("Modo: ")
        print("\n")
        print("INSTRUCCIONES:")
        print("Las teclas de direcciones son: w a s d")
        print("La tecla w es para mover hacia arriba")
        print("La tecla s es para mover hacia abajo")
        print("La tecla a es para mover hacia la izquierda")
        print("La tecla d es para mover hacia la derecha")
        print("Para seleecionar el next move preciona una tecla de direccion y luego la tecla ENTER")
        Matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        #Matriz = [[32,16,8,4],[64,8,4,2],[32,512,2,4],[128,4,16,2]]
        GameExit = False
        ########################
        f1 = open("Score_Actual.txt","w")
        Score_Actual = 0
        Score_Actual = str(Score_Actual)
        f1.write(Score_Actual)
        f1.close()
        ########################
        Random(Matriz,0,3,0)
        Random(Matriz,0,3,0)
        print("\n"*3)
        ResMatriz(Matriz,Dificultad)
        return juego(GameExit,Matriz,Dificultad)

def juego(GameExit,Matriz,Dificultad):
    key = input("Next Move: ")
    GameExit = juego_GameExit(Matriz,0,3,1,GameExit)
    if(GameExit==True):
        print("You Lose")
        return juego_Aux(0)
    if(GameExit!=True and GameExit!=False):
        print("You Win!!!!")
        return juego_Aux(0)
    else:
        if(key=="w"):
            print("Arriba")
            Arriba(Matriz,GameExit)
            Random(Matriz,0,3,0)
            print("\n"*5)
            ResMatriz(Matriz,Dificultad)
            return juego(GameExit,Matriz,Dificultad)
        if(key=="s"):
            print("Abajo")
            Abajo(Matriz,GameExit)
            Random(Matriz,0,3,0)
            print("\n"*3)
            ResMatriz(Matriz,Dificultad)
            return juego(GameExit,Matriz,Dificultad)
        if(key=="a"):
            print("Izquierda")
            Izquierda(Matriz,GameExit)
            Random(Matriz,0,3,0)
            print("\n"*3)
            ResMatriz(Matriz,Dificultad)
            return juego(GameExit,Matriz,Dificultad)
        if(key=="d"):
            print("Derecha")
            Derecha(Matriz,GameExit)
            Random(Matriz,0,3,0)
            print("\n"*3)
            ResMatriz(Matriz,Dificultad)
            return juego(GameExit,Matriz,Dificultad)
        else:
            print("Input incorrecto")
            return juego(GameExit,Matriz,Dificultad)

def juego_Aux(restart):
    if(restart==0):
        print("Quieres jugar de nuevo? (1)Si (2)No")
        restart = int(input())
    if(restart==1):
        print("Quieres jugar con el mismo Nickname? (1)Si (2)No")
        partida = int(input())
        if(partida==1):
            return main(2)
        if(partida==2):
            return main(1)
        else:
            print("Input incorrecto")
            return juego_Aux(1)
    if(restart==2):
        print("Gracias por jugar!!!")
        print("Hecho por Adrian Gomez")
    else:
        print("Input incorrecto")
        return juego_Aux(restart)




main(1)













    









        
