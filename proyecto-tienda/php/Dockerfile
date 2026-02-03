FROM php:7.4-apache
#Imagen
WORKDIR /app
# WORKDIR lo que hace es crear este directorio dentro del docker
RUN docker-php-ext-install mysqli
# RUN ejecuta un comando dentro del docker

# "docker-php-ext-install" es un script que viene preinstalado 
# exclusivamente en las imagenes oficiales de PHP en Docker 

# "mysqli" es el paquete que descargamos en este caso, el tema es 
# que se usa mysqli porque mysql esta obsoleto desde php 5.0

RUN docker-php-ext-install pdo pdo_mysql

# "pdo" (PHP Data Objects) es el estándar moderno en la industria del
# desarrollo con PHP.
# No se conecta a nada por sí sola, sino que define cómo PHP debe manejar bases de datos de forma general.

# "pdo_mysql" Es el "driver" específico. Es lo que permite que esa interfaz
# general de PDO sepa hablar concretamente con una BBDD de MySQL.
