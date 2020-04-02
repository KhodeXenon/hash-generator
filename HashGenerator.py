__coder__ = "KhodeXenon[Amin]"
__email_ = "Khodexenon@gmail.com"
import hashlib

class HashTool():
    def __init__(self ,hash):
        self.hash = hash.encode()

    def md5_encrypt(self):
        my_hash = hashlib.md5()
        my_hash.update(self.hash)
        print("+------------------------------------------------------------------------------------------------+")
        print("|                                                                                                |")
        print("|                                                                                                |")
        print(" Your (MD5) hash is : " + my_hash.hexdigest())
        print("|                                                                                                |")
        print("|                                                                                                |")
        print("+------------------------------------------------------------------------------------------------+")
        input("press enter to continue ...")

    def sha256_encrypt(self):
        my_hash = hashlib.sha256()
        my_hash.update(self.hash)
        print("+------------------------------------------------------------------------------------------------+")
        print("|                                                                                                |")
        print("|                                                                                                |")
        print(" Your (SHA256) hash is : " + my_hash.hexdigest())
        print("|                                                                                                |")
        print("|                                                                                                |")
        print("+------------------------------------------------------------------------------------------------+")
        input("press enter to continue ...")


    def sha512_encrypt(self):
        my_hash = hashlib.sha512()
        my_hash.update(self.hash)
        print("+------------------------------------------------------------------------------------------------+")
        print("|                                                                                                |")
        print("|                                                                                                |")
        print(" Your (SHA512) hash is : " + my_hash.hexdigest())
        print("|                                                                                                |")
        print("|                                                                                                |")
        print("+------------------------------------------------------------------------------------------------+")
        input("press enter to continue ...")


    def sha3_256_encrypt(self):
        my_hash = hashlib.sha3_256()
        my_hash.update(self.hash)
        print("+------------------------------------------------------------------------------------------------+")
        print("|                                                                                                |")
        print("|                                                                                                |")
        print(" Your (SHA3_256) hash is : " + my_hash.hexdigest())
        print("|                                                                                                |")
        print("|                                                                                                |")
        print("+------------------------------------------------------------------------------------------------+")
        input("press enter to continue ...")

    def sha3_384_encrypt(self):
        my_hash = hashlib.sha3_384()
        my_hash.update(self.hash)
        print("+------------------------------------------------------------------------------------------------+")
        print("|                                                                                                |")
        print("|                                                                                                |")
        print(" Your (SHA3_384) hash is : " + my_hash.hexdigest())
        print("|                                                                                                |")
        print("|                                                                                                |")
        print("+------------------------------------------------------------------------------------------------+")
        input("press enter to continue ...")

    def sha3_224_encrypt(self):
        my_hash = hashlib.sha3_224()
        my_hash.update(self.hash)
        print("+------------------------------------------------------------------------------------------------+")
        print("|                                                                                                |")
        print("|                                                                                                |")
        print(" Your (SHA3_224) hash is : " + my_hash.hexdigest())
        print("|                                                                                                |")
        print("|                                                                                                |")
        print("+------------------------------------------------------------------------------------------------+")
        input("press enter to continue ...")

    def sha3_512_encrypt(self):
        my_hash = hashlib.sha3_512()
        my_hash.update(self.hash)
        print("+------------------------------------------------------------------------------------------------+")
        print("|                                                                                                |")
        print("|                                                                                                |")
        print(" Your (SHA3_512) hash is : " + my_hash.hexdigest())
        print("|                                                                                                |")
        print("|                                                                                                |")
        print("+------------------------------------------------------------------------------------------------+")
        input("press enter to continue ...")

    def sha1_encrypt(self):
        my_hash = hashlib.sha1()
        my_hash.update(self.hash)
        print("+------------------------------------------------------------------------------------------------+")
        print("|                                                                                                |")
        print("|                                                                                                |")
        print(" Your (SHA1) hash is : " + my_hash.hexdigest())
        print("|                                                                                                |")
        print("|                                                                                                |")
        print("+------------------------------------------------------------------------------------------------+")
        input("press enter to continue ...")

    def sha384_encrypt(self):
        my_hash = hashlib.sha3_384()
        my_hash.update(self.hash)
        print("+------------------------------------------------------------------------------------------------+")
        print("|                                                                                                |")
        print("|                                                                                                |")
        print(" Your (SHA384) hash is : " + my_hash.hexdigest())
        print("|                                                                                                |")
        print("|                                                                                                |")
        print("+------------------------------------------------------------------------------------------------+")
        input("press enter to continue ...")

    def sha224_encrypt(self):
        my_hash = hashlib.sha224()
        my_hash.update(self.hash)
        print("+------------------------------------------------------------------------------------------------+")
        print("|                                                                                                |")
        print("|                                                                                                |")
        print(" Your (SHA224) hash is : " + my_hash.hexdigest())
        print("|                                                                                                |")
        print("|                                                                                                |")
        print("+------------------------------------------------------------------------------------------------+")
        input("press enter to continue ...")



while True:
    print("\n Options :")
    print("\t1)MD5")
    print("\t2)sha256")
    print("\t3)sha512")
    print("\t4)sha3_256")
    print("\t5)sha3_384")
    print("\t6)sha3_224")
    print("\t7)sha3_512")
    print("\t8)sha1")
    print("\t9)sha384")
    print("\t10)sha224")
    print("")

    hash_type = input("Hash number :").lower()
    hash_text = input("String :")
    hash_connection = HashTool(hash_text)
    if hash_type == "md5" or hash_type == "1":
        hash_connection.md5_encrypt()

    elif hash_type == "sha256" or hash_type == "2":
        hash_connection.sha256_encrypt()

    elif hash_type == "sha512" or hash_type == "3":
        hash_connection.sha512_encrypt()

    elif hash_type == "sha3_256" or hash_type == "4":
        hash_connection.sha3_256_encrypt()

    elif hash_type == "sha3_384" or hash_type == "5":
        hash_connection.sha3_384_encrypt()

    elif hash_type == "sha3_224" or hash_type == "6":
        hash_connection.sha3_224_encrypt()

    elif hash_type == "sha3_512" or hash_type == "7":
        hash_connection.sha3_512_encrypt()

    elif hash_type == "sha1" or hash_type == "8":
        hash_connection.sha1_encrypt()

    elif hash_type == "sha384" or hash_type == "9":
        hash_connection.sha384_encrypt()

    elif hash_type == "sha224" or hash_type == "10":
        hash_connection.sha224_encrypt()

    else:
        print("Invalid option")
        again = input("again ? (y) :").lower()
        if again == "y" :
            continue
        else:
            break
