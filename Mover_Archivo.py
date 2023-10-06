import os
import shutil

from_dir = 'C:/Users/blanc/Documents/Proyectos de clase/Practicas'
to_dir = 'C:/Users/blanc/Documents/Proyectos de clase/separados'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file in list_of_files:
    name, extension = os.path.splitext(file)

    if extension == '' :
        continue
    elif extension in [ '.txt', '.doc', '.docx', '.pdf', '.zip']:
        
        ruta1 = from_dir + '/' + file
        ruta2 = to_dir + '/' + extension
        ruta3 = to_dir + '/' + extension + '/' + file

        if os.path.exists(ruta2):

            print('Moviendo archivo: ', name)
            shutil.move( ruta1, ruta3)

        else:

            print('creando carperta...')
            os.makedirs(ruta2)

            print('Moviendo archivo: ', name)
            shutil.move( ruta1, ruta3)

