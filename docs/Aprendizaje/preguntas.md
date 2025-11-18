cuando ejecuto una imagen no se sobreescribe? o se crea nuevamente y borra la anterior?

Docker construye una imagen nueva.

Si ya existe una imagen llamada fifa-ml-kedro:latest, Docker crea una nueva pero simplemente cambia el puntero del tag.

La imagen anterior sigue existiendo, solo que queda sin tag (llamada dangling image).

Estas ya no sirven → puedes borrarlas

¿Porque una imagen y un compose?

