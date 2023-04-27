# Complemento Beep Keyboard para NVDA #

Este complemento permite al usuario configurar NVDA para que emita pitidos con algunos eventos del teclado.

Copyright (C) 2019 - 2023 David CM <dhf360@gmail.com>

Este paquete se distribuye bajo los términos de la Licencia Pública General GNU, versión 2 o posterior.

## Características

  Este complemento proporciona las siguientes funciones que puedes usar para adaptar el comportamiento del teclado de NVDA:

* Beep para mayúsculas cuando el bloqueo de mayúsculas está activado: si esta característica está habilitada, NVDA emitirá un pitido cuando escribas caracteres y  el bloqueo de mayúsculas se encuentre activado. Es útil por ejemplo, si se activó el bloqueo mayúsculas sin querer. ¡No cometas más errores con mayúsculas!
* Pitido para caracteres escritos cuando se presiona shift: con esta función, NVDA emitirá un pitido si escribe un carácter con la tecla shift presionada.
* Pitido para cambios de teclas de alternancia: con esta función, NVDA emitirá un pitido más alto si se activa una tecla de alternancia, y un tono más bajo si se apaga. Tenga en cuenta que Windows tiene una función de cambio de pitido keis incorporada en el Centro de facilidad de acceso. Esta característica nativa funciona bien si no utiliza la configuración de distribución del teclado de la computadora portátil.
* Anunciar cambios de teclas de alternancia: justo cuando está activado el "Bip para cambios de teclas de alternancia". Puedes habilitar o deshabilitar NVDA para anunciar el estado de la tecla de alternancia.
* Pitido para caracteres específicos: NVDA emitirá un pitido para todos los caracteres que configures en la configuración avanzada.
* Deshabilitar el pitido en los campos de contraseña: esta función está habilitada de forma predeterminada para evitar riesgos de seguridad. Desactívelo si desea escuchar pitidos en los campos de contraseña.

## Requisitos
  Necesitas NVDA 2018.2 o posterior.

## Instalación
  Solo instálalo como un complemento de NVDA.

## Uso
  Para habilitar o deshabilitar funciones, ve a la configuración de NVDA y selecciona la categoría de teclado de pitidos. En esa categoría puede configurar todas las funciones compatibles con este complemento.

"Beep para mayúsculas cuando el bloqueo de mayúsculas está activado" está habilitado de forma predeterminada.
Si necesita más configuraciones, abra el cuadro de diálogo de configuración avanzada que contiene las siguientes opciones:

* Caracteres ignorados con shift presionado: todos los caracteres aquí serán ignorados y emitirán un pitido cuando se presione shift. Las secuencias de escape están permitidas, p. "\t" para tabulador, "\r" para retorno de carro.
* Pitar siempre para los siguientes caracteres: configura aquí todos los caracteres para los que quieras pitidos de NVDA. Las secuencias de escape están permitidas, p. "\t" para tabulador, "\r" para retorno de carro.
* Seleccionar tono a configurar: puede configurar parámetros para todos los tonos. Seleccione uno aquí y establezca los parámetros en los siguientes cuadros de texto. Cuando cambie la selección, NVDA emitirá un pitido para el tono seleccionado actual con los parámetros actuales establecidos en el diálogo.
* Tono de tono: tono de tono para el tono seleccionado actual.
* Duración del tono: duración del tono para el tono seleccionado actualmente.
* Volumen de tono: volumen de tono para el tono seleccionado actualmente.
* Tono de prueba: este botón le permite reproducir una prueba con los parámetros establecidos actualmente.
* Presione el botón OK para guardar la configuración o cancelar para descartar.

## contribuciones, informes y donaciones

Si te gusta mi proyecto o este software te es útil en tu vida diaria y te gustaría contribuir de alguna manera, puedes donar a través de los siguientes métodos:

* [PayPal.](https://paypal.yo/davicm)
* [Ko-fi.](https://ko-fi.com/davidacm)
* [criptomonedas y otros métodos.](https://davidacm.github.io/donations/)

Si desea corregir errores, informar problemas o nuevas funciones, puede contactarme en: <dhf360@gmail.com>.

  O en el repositorio github de este proyecto:
  [Beep teclado en GitHub](https://github.com/davidacm/beepKeyboard)

    Puede obtener la última versión de este complemento en ese repositorio.
