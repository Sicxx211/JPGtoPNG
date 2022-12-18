# JPG to PNG convertor 



# Why I wrote the code


I wrote this code for convenience, I could use the web to convert all of my files from JPG to PNG but sometimes it would just take too long to do it,just imagine if I had a folder with thousands of JPG images, it would take ages to do this conversion using the web, so I fixed this problem with this script, it's easy to use, not to complex, and fast.



# How I wrote the code


image_folder = sys.argv[1] <br>
output_folder = sys.argv[2] <br>
if not os.path.exists(output_folder): <br>
os.makedirs(output_folder)  <br>
for filename in os.listdir(image_folder): <br>
img = Image.open(f'{image_folder}{filename}') <br>
clean_name = os.path.splitext(filename)[0] <br>
img.save(f'{output_folder}{clean_name}.png' , 'png') <br>
print('all done!') <br>
<br>
*Instance of running the code ->$ python3 pngconverter.py pokedex converted
