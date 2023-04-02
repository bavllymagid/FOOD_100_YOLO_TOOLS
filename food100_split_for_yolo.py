import glob, os
import shutil
# Percentage of images to be used for the test set
percentage_test = 10;

# create train and test directories if not exist 
if not os.path.exists('food100/train'):
    os.makedirs('food100/train/images')
    os.makedirs('food100/train/labels')
    
if not os.path.exists('food100/test'):
    os.makedirs('food100/test/images')
    os.makedirs('food100/test/labels')

# Populate train and test directories
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob("../UECFOOD100/*/*.jpg"):

    if counter == index_test:
        counter = 1
        shutil.move(pathAndFilename, 'food100/test/images/' + pathAndFilename.split('/')[-1])
        labels_path = 'labels' + '/' + pathAndFilename.split('/')[-2]
        shutil.move(labels_path + '/' + pathAndFilename.split('/')[-1].split('.')[0] + '.txt', 'food100/test/labels/' + pathAndFilename.split('/')[-1].split('.')[0] + '.txt')
    else:
        shutil.move(pathAndFilename, 'food100/train/images/' + pathAndFilename.split('/')[-1])
        labels_path = 'labels' + '/' + pathAndFilename.split('/')[-2]
        shutil.move(labels_path + '/' + pathAndFilename.split('/')[-1].split('.')[0] + '.txt', 'food100/train/labels/' + pathAndFilename.split('/')[-1].split('.')[0] + '.txt')
        counter = counter + 1
