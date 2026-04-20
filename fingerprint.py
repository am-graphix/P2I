from pyfingerprint import Pyfingerprint
import time
import serial
import os

class Biometrics():
    def __init__(self,usb = '/tty/USB0'):
        self.fingerprint = None
        self.__initialized = False
        self.__communicating = False
        self.__add1 = '/tty/USB0'
        self.__add2 = '/tty/USB1'
        self.base_path = os.path.join(os.getcwd(),'static/fingerprints')
        

    def initialize(self,attempts = 2):
        try:
            self.fingerprint = Pyfingerprint(self.add1)

            if not self.fingerprint:
                self.initialized = False
                return False
            self.__initialized = True
            print('Initializing..............')

            for attempt in attempts:
                try:
                    if self.fingerprint.verifyPassword():
                        self.__communicating = True
                        print('Fingeprint connection successfully established...')
                        return True
                    else:
                        print(f'Attempt {attempt+1}/{attempts} failed.. \n retrying...')
                        time.sleep(0.3)
                except Exception as e:
                    print(f'Communication error.. : {e} \n retrying...')
                    time.sleep(0.3)

        except serial.Serialutil.SerialException as e:
            self.__communicating = False
            print(f'Port error : {e}')
            return False

        except Exception as e:
            self.__communicating = False
            print(f'Unexpected error : {e}')
            return False


    def enroll_fingerprint(self,buffer_no,timeout):
        if not self.__initialized and self.__communicating:
            print('Fingerprint scanner not ready...')
            return False
        
        if buffer_no not in[0x01,0x02]:
            print(f'invaid buffer number: {buffer_no}\n Must be 0x01 or 0x02')
            return False
        
        print(f'Enrolling fingerprint in buffer {buffer_no}... \n please place your finger on the scanner........')
        
        try:
            start_time = time.time()
            while not self.fingerprint.readImage():
                if time.time() - start_time > timeout:
                    print('Timeout.....')
                    return False
                time.sleep(0.1)
            
            print('Finger detected... converting Image....')

            self.fingerprint.convertImage(buffer_no)
            print(f'Template recorded in buffer {buffer_no}')

            return True

        except Exception as e:
            print(f'Enrollment error : {e}')
            return False

    def process_fingerprint(self):
        if not self.__initialized and self.__communicating:
            print('Process_fingerprint error : Scanner not ready')
            return 0

        try:
            print('Comparing fingerprints...')
            comparison_score = self.fingerprint.compareCharacteristics()

            if comparison_score > 0:
                print(f'Match found... comparison score : {comparison_score}')
                return comparison_score
            else:
                print('Fingers do not match')
                return comparison_score

        except Exception as e:
            print(f'Comparison error : {e}')
            return 0

    def store_fingerprint(self):
        if not self.__initialized and self.__communicating:
            print('Store fingerprint error : Scanner not ready')
            return False
        
        try:
            self.fingerprint.createTemplate()
            print('Template created successfully...')

            pos = self.fingerprint.storeTemplate()
            print(f'Fingerprint stored at position {pos}')
            return pos

        except Exception as e:
            print(f'Store fingerprint error : {e}')
            return None

    def download_fingerprint(self,img_name):
        if not self.__initialized and self.__communicating:
            print('Scanner not ready.....')
            return False

        try:


    
            



    