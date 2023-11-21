from n_grams import n_grams

def main():
    n_grams(folder_path='fsg_h_files', file_name='FSG_H.txt', delimeters=' -\n,=', alphabet="1234567890qwertyuiopasdfghjklzxcvbnm -áéíóúàèëïöü")
    
if __name__ == '__main__':
    main()