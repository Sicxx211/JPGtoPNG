#JPG to PNG Script 

import os
import sys

image_folder = sys.argv[1] #This will allow us to input the name of the folder we want to work on

output_folder = sys.argv[2]#This will allow us to input the name of the new folder we want to create for the new images

if not os.path.exists(output_folder): #This will check if the new folder doesn't exists

os.makedirs(output_folder) #This command, in case the new folder doesn't exists, will create it

for filename in os.listdir(image_folder): #This for loop will take all the images in the specified folder we give it and convert the images from jpg to png

img = Image.open(f'{image_folder}{filename}') #This will open the images inside the specified folder

clean_name = os.path.splitext(filename)[0] #This will clear out the .jpg in the name of the file so when we save it it will have only .png not .jpg.png

img.save(f'{output_folder}{clean_name}.png' , 'png') #This will save the images in the new folder that we specified, converting them to PNG

print('all done!') #This will print out everytime a file is converted
