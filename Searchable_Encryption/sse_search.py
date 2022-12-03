import pandas as pd
from Crypto.Cipher import AES
from Crypto.Hash import MD5
# import time

def build_codeword(ID, trapdoor):
    ID_index = MD5.new()
    ID_index.update(str(ID).encode('utf-8'))
    # print(trapdoor);
    ECB_cipher = AES.new(b']o\x1f\xbe\xbe-2\x12]\xf5 \nC!\x86\xa3', AES.MODE_ECB)
    # print(ECB_cipher.encrypt(ID_index.digest()))
    return ECB_cipher.encrypt(ID_index.digest())

# def build_codeword(ID, trapdoor):
#     ID_index = MD5.new()
#     ID_index.update(str(ID))
#     ECB_cipher = AES.new(trapdoor, AES.MODE_ECB)
#     return ECB_cipher.encrypt(ID_index.digest()).encode("hex")

def search_index(document, trapdoor):
    search_result = []
    data_index = pd.read_csv(document)
    data_index = data_index.values
    # print(data_index)
    # start_time = time.time()
    # print(trapdoor);
    
    for row in range(data_index.shape[0]):
        # print(data_index[row]);
        if str(build_codeword(row, trapdoor)) in data_index[row]:
            search_result.append(row)

    # print time.time() - start_time
    # print(search_result)
    return search_result

if __name__ == "__main__":

    # index_file_name = input("Please input the index file you want to search:  ")
    # keyword_trapdoor = input("Please input the file stored the trapdoor you want to search:  ")
    keyword_trapdoor = open("India_trapdoor").read().strip()
    search_result = search_index("yes_index.csv", keyword_trapdoor)
   
    print ("The identifiers of files that contain the keyword are: \n", search_result)


