/*
*@file ejemplo_pcap
*@brief Programa que permite capturar paquetes, ya sea uno o
*      indefinidos y lo muestra en pantalla
*@author Vilchis Domínguez Miguel Alonso
*@version 1.0
*/

/*++++++++++++++++Compilacion y uso +++++++++++++++++++++++++
  *Para instalar libpcap: apt-get install libpcap-dev
 *Para compilar el programa la linea de comandos corrrespondiente
 *es: gcc ejercicio1.c -o ej1 -lpcap
 *Y como super usuario se ejecuta ./ej1
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */

 #include <stdio.h>
 #include <stdlib.h>
 #include <pcap.h>
 #include <arpa/inet.h>
 #include "ejercicio1.h"

 /**************************************************************
 *
 *@brief Funcion que será llamada si queremos capturar solo un
 *       paquete
 *
 ***************************************************************/
char *dev;
pcap_t *handle;
 int opcionUnPaquete () {
     //Obtenemos interfaz disponible
     char errbuf[PCAP_ERRBUF_SIZE];
     //char *dev;
     const struct ip_header *ip;
     pcap_t *captura;
     const u_char *paquete;
     struct pcap_pkthdr h;

     //Abrimos la interfaz de red
     captura = pcap_open_live(dev,BUFSIZ,1,1000, errbuf);
     //Si la captura no fue exitosa salimos del programa
     if(captura== NULL) {
         printf("En captura ERROR: %s\n", errbuf);
         return EXIT_FAILURE;
     }
     //Capturamos un paquete
     paquete = pcap_next(captura, &h);
     //Si ocurrió un error al recibir un paquete salimos
     if(paquete == NULL) {
         printf("Al recibir un paquete ERROR: %s \n",errbuf);
         return EXIT_FAILURE;
     }

     ip = (struct ip_header*)(paquete + TAM_ETHERNET);
     printf("\n----------------------------------------------------------\n" );
     printf("El paquete lo envia: (%x )%s\n", ip -> ip_src, inet_ntoa(ip->ip_src), inet_ntoa(ip->ip_src));
     printf("El paquete lo recibe: (%x)%s\n",((*ip).ip_dst),inet_ntoa(ip->ip_dst) );
     printf("El paquete es:\n");
     int i;
     for(i = 0;i < h.len; i++) {
         printf("%x ", paquete[i]);
     }
     printf("\n");
     //printf("De: (%x )%s -> (%x)%s \n",ip -> ip_src, inet_ntoa(ip->ip_src),((*ip).ip_dst),inet_ntoa(ip->ip_dst));
     //printf("Protocolo :%x", ip->ip_p);

     return EXIT_SUCCESS;
 }

 int main () {
    //Dado que al tratar de usar una interfaz de red disponible
    //Libpcap busca usa la primera, entonces la siguiente secuencia
    //Nos indica cual es la primera.

    char ebuf[PCAP_ERRBUF_SIZE];
    pcap_if_t* deviceList;
    pcap_if_t* d;
    //char** devL =
    int c = 1;
    char* dl[9];
    printf("Lista de dispositivos:\n" );
    printf("|Numero | Nombre Dispositivo\n" );
    pcap_findalldevs(&deviceList,ebuf);
    while(deviceList->next != NULL ) {
        dl[c] = deviceList->name;
        printf("|   %d   |    %s \n",c,(deviceList->name));
        deviceList = deviceList->next;
        c++;
    }
    printf("Ingresa el numero del dispositivo:\n");
    int x;
    scanf("%d", &x);
    dev = dl[x];
    printf("Se abre el dispositvo: %s\n",dev );

    handle = pcap_open_live(dev, BUFSIZ, 1, 1000, ebuf);
    //pcap_loop(handle,-1,opcionUnPaquete, NULL);
    printf("\n/////////////////////////////////////////////////////////////\n");
    while(x>0){
      opcionUnPaquete();
    }


    //Para varios paquetes :
    return 0;
}