---
layout: post
title: Análisis del ransomware Satana
comments: True
author: Sadfud
tags: [Análisis de malware]
---

Si hay un tipo de malware preferido por los cibercriminales, esa es la familia de los ransomware. Desde la aparicion a finales de 2013 del conocido como "virus de la policia" esta familia de malware no ha parado de crecer, dado que es facil de programar y  rentable para los cibercriminales. 

A continuacion procederé a analizar detalladamente un nuevo ransomware descubierto a finales de Junio y conocido como "Satana".
Las muestras en las que se basa el análisis de esta entrada son;
46bfd4f1d581d7c0121d2b19a005d3df Como muestra principal

https://virustotal.com/en/file/683a09da219918258c58a7f61f7dc4161a3a7a377cf82a31b840baabfb9a4a96/analysis/

d236fcc8789f94f085137058311e848b Como muestra de malware unpacked

## H2 1.	Información de versiones

A día de hoy 12 de Julio de 2016, únicamente se ha distribuido una versión del código malicioso Satana.

## H2 2.	Extensiones a cifrar

Satana cifra los archivos con extensión
.bak .doc .jpg .jpe .txt .tex .dbf .db .xls 
.cry .xml .vsd .pdf . csv .bmp .tif .1cd .tax 
.gif .gbr .png .mdb .mdf .sdf .dwg .dxf .dgn 
.stl .gho .v2i .3ds .ma .ppt .acc .vpd .odt 
.ods .rar .zip .7z .cpp .pas .asm 

## H2 3.	Extension añadida a los archivos cifrados

Tras cifrar los archivos el malware cambia el nombre de los mismos con el formato <dirección de email>__<nombre_original >
![FIG1](https://i.gyazo.com/04f52d0425115f9cf1403f257ab9d7ee.png)

## H2 4.	Análisis dinámico del código malicioso

Tras la ejecución del binario malicioso este crea una copia de si mismo en %TEMP% con un nombre aleatorio y posteriormente borra el archivo original. Además crea un archivo de texto bajo el nombre de ¡satana!.txt también en %TEMP%.
Una vez terminado este proceso ejecuta el archivo de nombre aleatorio creado en la carpeta temporal, el cual requiere al usuario permisos de ejecución como administrador.
Cuando el usuario concede los permisos de ejecución, el malware crea 2 entradas en el registro de Windows.
![FIG4](https://i.gyazo.com/7d9df3a79c12df7a533866b2aacbf0a4.png)
La primera bajo el nombre de “BTC” contiene la dirección de bitcoin asociada a la cartera que debe recibir el pago
La segunda bajo el nombre de “E-mail” contiene una dirección de E-mail, la misma que se muestra en el nuevo nombre de los archivos cifrados.
![FIG5](https://i.gyazo.com/8e1c07ad603c992e6917d4f43d09bf7c.png)

## H2 5.	Ataque de bajo nivel

Este ransomware no actua en modo kernel, como si lo hacen otros como por ejemplo Petya.

## H2 6.	Ataque de alto  nivel.

Una vez el malware ha sido ejecutado simplemente se instala de forma silenciosa en el equipo y espera al reinicio del equipo (sin forzarlo) para mostrar el siguiente mensaje 
![FIG2](https://i.gyazo.com/ab67ea9348b5a6844e43e904de69979f.png)
*Es el mismo contenido que el del fichero ¡satana!.txt

## H2 7.	Metodo de cifrado de archivos.

Satana divide los archivos en partes de 32 bytes que cifra de forma independiente para posteriormente juntarlas usando el método RTDSC (Read Time-Stamp Counter).
El algoritmo de cifrado es una modificación de AES 256.

## H2 8.	Llave de cifrado

Aparentemente la llave de cifrado es siempre la misma. Un mismo archivo siempre devuelve archivos cifrados idénticos.

## H2 9.	Medidas de protección anti reversing en el payload.

El payload esta empaquetado, pero puede ser fácilmente desempaquetado usando un debugger como OllyDbg, basta con colocar un BP en RtlDecompressBuffer.
Tambien impide la restauración del equipo a un punto anterior a la infección.
![FIG3](https://i.gyazo.com/581fbf16dc6f24af6f0a170603977f81.png)

## H2 10.	Conexión con el C&C 

El malware conecta con el C&C y envía la siguiente información en un paquete sin cifrar.
id=7
&code=100
&sdata=5.1.2600 0 1 HOME User 0&name=payload.exe
&md5=59E18B50B822020294A8EA0A4154C7597847B3A6359A08194F4865D804BD7E6
&dlen=66ABDE777F35E50F671B6034FA6453AD
Este proceso muestra un grave fallo en el payload, ya que si en el momento de la infeccion el C&C esta offline la llave se pierde y los archivos no pueden ser recuperados.

## H2 12.	Detecion con regla YARA

rule: Satana_Ransomware
{
	 meta:
    Description = "Deteccion de ransomware Satana"
    Author = "SadFud"
    Date = "12/07/2016"
	
	strings:
	$satana = { !satana! } nocase
	
	condition:
	$satana
}

## H2 11.	Conclusion

Observando el funcionamiento del programa y los fallos que tiene, es posible que esta solo sea una versión de prueba y que la verdadera campaña de infección masiva aun no haya comenzado.

## H2 12.	Descarga de muestras

http://www27.zippyshare.com/v/WjzkYiPy/file.html
Contraseña:indeseables

