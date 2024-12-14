# Proyecto Final Python Django - Pagina Web similar a un Blog

El siguiente proyecto incluye las fucionalidades para registrarse como usuario normal o administrador, iniciar sesion y visualizar un listado de las diferentes entradas realizadas por los administradores en el blog. Si el usuario es normal solo tendra acceso a visualizar la lista y acceder a ver el contenido completo de la entrada, y si es usuario administrador no solo podra tener accesos a lo mencionado recientemente sino que ademas podra ingresar nuevas entradas, editar las ingresadas y eliminar las que desee. Ambos tipos de usuarios tienen acceso a ver un sitio de "Acerca de" para conocer mas info sobre el creador del blog asi como tambien a sus datos, cambio de email y contraseña. Los usuarios ademas, podran cerrar sesion para salir del blog.

# Pasos para ejecutar:
1. Clona el repositorio en la terminal de tu maquina local: 
git clone https://github.com/VirginiaVega/Proyecto-final-VegaVirginia.git

2. Instala las dependencias del proyecto: 
pip install –r requirements.txt 

3. Activa el entorno virtual: 
source venv1/Scripts/activate

4. Inicia el servidor:
python manage.py runserver

5. Accede desde el navegador al proyecto: El inicio de sesion
http://localhost:8000

# Funcionalidades:

1. Creacion de usuarios: El usuario tendra inicialmente dos opciones principales: iniciar sesion o crear una cuenta, suponiendo no contar con una podra seleccionar crear una cuenta: Debera introducir su nombre de usuario, correo electronico en formato correcto, una contraseña y confirmar introduciendola nuevamente, seleccionar la opcion de si es usuario administrador o no y presionar el boton registrarse. Es importante tener en cuenta que el nombre de usuario no puede repetirse, el formato del correo elecrtonico incluye "@" y ".", la contraseña debe ser de 8 caracteres como minimo y la misma debe coincidir con la confirmacion.

2. Inicio sesion: Al terminar el registro, automaticamente aparecera la pantalla de inicio de sesion, en la misma debe intriducir su nombre de usuario, contraseña y presionar el boton "Iniciar sesion", los datos deben ingresarse si o si y la contraseña debe coincidir con la registrada.

3. Listado de Entradas en el inicio: Al iniciar sesion, la primer pantalla es la del listado de entradas registradas por usuarios. Podra visualizar una barra de navegacion con distintas opciones que dependiendo si es:
 - Usuario normal: podra ver las opciones "Inicio" "Acerca de" y opciones extra de su cuenta al presionar un desplegable con su nombre de usuario, con las opciones "Editar cuenta" y "Salir".
 - Usuario administrador: podra ver las opciones "Inicio", "Nueva entrada", "Acerca de" y opciones extra de su cuenta al presionar un desplegable con su nombre de usuario, con las opciones "Editar cuenta" y "Salir". Ademas, al ser usuario administrador, podra ver junto a su nombre de usuario la leyenda "ADMIN".
El inicio cuenta tambien con una leyenda de bienvenida al blog, y las distintas entradas registradas con informacion basica de las mismas como la imagen, la fecha, el titulo, subtitulo y un boton para "Leer mas" que podran tener el acceso tanto los usuarios administradores como los normales, para ver el detalle de la entrada.
Otra cosa a destacar es que junto al boton "Leer mas" habra dos opciones a las que solo tendran acceso los usuarios administradores, las cuales son: "Editar" y "Eliminar".
En el pie de pagina se ubica la nota de Copyright del sitio.

4. Detalle de la entrada: Como mencionamos anteriormente el usuario, tanto normal como administrador, podra seleccionar la opcion "Leer mas" en la entrada que desee para ver el detalle de la misma. En pantalla se muestra la imagen, fecha, titulo, subtitulo, el cuerpo de la entrada, el autor y el boton de retorno al listado de entradas.

5. Creacion de nueva entrada: La generacion de nuevas entradas solo esta disponible para usuarios administradores, en la barra de navegacion el admin selecciona la opcion "Nueva entrada" y aparecera la pantalla para comenzar a introducir un titulo, subtitulo, el cuerpo de la entrada, el autor y una imagen. Al introducir la informacion y presionar el boton "Guardar entrada" se guardara la misma y automaticamente retorna al listado de entradas. Todos los campos son requeridos a excepcion de la imagen, ya que el blog coloca una imagen por defecto en caso de no introducir una.

6. Edicion de entradas: La edicion de entradas solo esta disponible para usuarios administradores, en la que desee modificar debera seleccionar el boton "Editar" y llevara a la pantalla para modificar titulo, subtitulo, cuerpo, autor e imagen. Todos los campos deben contener informacion a excepcion de la imagen, en caso de no introducir una, quedara con la que tenia previamente, asi sea la que se le asigno por defecto.

7. Eliminacion de entradas: La eliminacion de entradas solo esta disponible para usuarios administradores, en la que desee eliminar debera seleccionar el boton "Eliminar" y llevara a la pantalla para indicar confirmacion de la accion. En caso de estar seguro seleccionar la opcion "Eliminar" y llevara al listado de entradas pudiendo observar que la entrada eliminada ya no se encuentra en la lista, o seleccionar la opcion "Volver" para retroceder sin borrar la entrada.

8. Acceso a "Acerca de": Este espacio comparte informacion sobre el creador del blog, y la invitacion a ponerse en contacto por redes sociales.

9. Acceso a Edicion de la cuenta: Tanto el usuario comun como el administrador tendran acceso al seleccionar en la barra de navegacion, en el desplegable donde aparece su nombre de usuario, a la opcion "Editar cuenta", en pantalla podra modificar tanto su email como su contraseña, teniendo que realizar el cambio de contraseña de manera obligatoria en caso de solo querer modificar el email, o solo realizando la modificacion de contraseña sin tocar el campo email. Al realizar cambios deseados y presionar el boton "Actualizar" automaticamente redirige al inicio de sesion para volver a introducir nombre de usuario y contraseña. La edicion del nombre de usuario no esta disponible.

10. Cierre de sesion: En el desplegable donde aparece su nombre de usuario tendra la opcion "Salir" para realizar el cierre de sesion. Al presionar, sera redirigido a un cartel de agradecimiento por acceder al sitio, con las opciones de "iniciar sesion" o "crear una cuenta".

# Acceso al link para video demostrativo:
Ingrese al siguiente link de Google Drive para ver un video de como funciona el sitio web:
https://drive.google.com/drive/folders/1hTtQIcqYOh-2hAMdEtfLUPrjUxZZbwXK?usp=sharing

# Despedida:
Quiero agradecer al profe Alejando y los tutores Enzo y Marcos por el tiempo y la dedicacion durante la cursada. Espero el sitio sea de su agrado. 

Virginia Vega - 13 de diciembre del 2024 -
