# split your data into train and test

import os
import random
import shutil

input_directory = 'images'
split = 0.3 # test percentage


def create_train(dir_name, file_list):
    train_directory = 'train' + '_' + input_directory

    if not os.path.exists(train_directory):
        os.makedirs(train_directory)
        
    train_folder = train_directory +  '/' + dir_name

    if not os.path.exists(train_folder):
        os.makedirs(train_folder)
    
    for i in range(len(file_list)):
        src = input_directory + '/' + dir_name + '/' + file_list[i]
        dest = train_folder + '/' + file_list[i]
        shutil.move(src, dest)


def create_test(dir_name, file_list):
    test_directory = 'test' + '_' + input_directory

    if not os.path.exists(test_directory):
        os.makedirs(test_directory)
    
    test_folder = test_directory + '/' + dir_name

    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    
    for i in range(len(file_list)):
        src = input_directory + '/' + dir_name + '/' + file_list[i]
        dest = test_folder + '/' + file_list[i]
        shutil.move(src, dest)
        

if __name__ == "__main__":
    for root, dirs, files in os.walk(input_directory):  
        for dir in dirs:
            print(dir)
            for root1, dirs1, files1 in os.walk(input_directory + '/'+ dir):
                train_list = []
                test_list = []
                total_files = list(range(len(files1)))
                test_list_index = random.sample(range(1, len(files1)), int(0.3 * len(files1)))
                train_list_index = list(set(total_files) - set(test_list_index))

                for i in test_list_index:
                    test_list.append(files1[i])

                for i in train_list_index:
                    train_list.append(files1[i])
                
                create_train(dir, train_list)
                create_test(dir, test_list)

    shutil.rmtree(input_directory)
