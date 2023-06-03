from socket import*
import urllib.error, urllib.request

def main ():

    print ("\n" + gethostbyname(gethostname()))
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverPort = 12000

    serverSocket.bind((gethostname(), serverPort))
    serverSocket.listen(1)

    while True:
        print ('Ready to connect')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024)

            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            connectionSocket.send(bytes("HTTP/1.1 200 OK\n\n", 'UTF-8'))

            for i in range (0, len(outputdata)):
                connectionSocket.send(bytes(outputdata[i], 'UTF-8'))
            connectionSocket.close()
            print("HTTP/1.1 200 OK\n")

        except FileNotFoundError:
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found\n\n", 'UTF-8'))
            connectionSocket.close()
            print("HTTP/1.1 404 Not Found\n")
        
        except urllib.error.HTTPError as err:
            print("HTTP/1.1 400 Bad Request")
        
        

        pass

if __name__ == '__main__':
    main()
