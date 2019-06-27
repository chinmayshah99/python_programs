# Split your data into train and test set
# MIT License
# Copyright (c) 2019 Chinmay Shah

'''
    Given structure of your data:
    data
    |-class 1
    |-class 2
    |-class 3
    .
    .
    Splits the data randomly into train and test. Takes %test data as i/p

    train_data              test_data
    |-class 1               |-class 1
    |-class 2               |-class 2
    |-class 3               |-class 3

    At the end, removes the input directory, i.e., `data` in this case
'''
'''
    Usage:
    Zip file - python3 split_dataset.py -z image.zip    
    Direcotry - python3 split_dataset.py image
    Add split %(directory) - python3 split_dataset.py -t 0.4 image
    Add split %(zip) - python3 split_dataset.py -z -t 0.4 image.zip
    
'''

import os
import random
import shutil
import argparse
import zipfile



def create_train(input_directory ,dir_name, file_list):
    train_directory = 'train' + '_' + input_directory

    if not os.path.exists(train_directory):
        os.makedirs(train_directory)

    train_folder = train_directory + '/' + dir_name

    if not os.path.exists(train_folder):
        os.makedirs(train_folder)

    for i in range(len(file_list)):
        src = input_directory + '/' + dir_name + '/' + file_list[i]
        dest = train_folder + '/' + file_list[i]
        shutil.move(src, dest)


def create_test(input_directory ,dir_name, file_list):
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

def extract_zip(input_zip):
    print('extracting ' + input_zip)
    zip_ref = zipfile.ZipFile(input_zip, 'r')
    zip_ref.extractall('/')
    zip_ref.close()
    print('extracted!')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",
                        help="Name of zip file/ directory name")
    parser.add_argument("-z", "--zip", action="store_true",
                        help="True if a zip file")
    parser.add_argument("-t", "--test", default = 0.3,
                        help="Test split percentage")

    args = parser.parse_args()

    if args.zip:
        extract_zip(args.filename)
        input_directory = (args.filename).rsplit('.', 1)[0]

    else:
        if os.path.isdir(args.filename):
            input_directory = args.filename
        else:
            raise NotADirectoryError

    for root, dirs, files in os.walk(input_directory):
        for dir in dirs:
            print(dir)
            for root1, dirs1, files1 in os.walk(input_directory + '/' + dir):
                train_list = []
                test_list = []
                total_files = list(range(len(files1)))
                test_list_index = random.sample(range(1, len(files1)), int(float(args.test) * len(files1)))
                train_list_index = list(set(total_files) - set(test_list_index))

                for i in test_list_index:
                    test_list.append(files1[i])

                for i in train_list_index:
                    train_list.append(files1[i])

                create_train(input_directory ,dir, train_list)
                create_test(input_directory ,dir, test_list)

    shutil.rmtree(input_directory)  # removes the i/p folder
