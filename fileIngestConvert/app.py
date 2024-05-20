import csv
import can 
import os
import random


blf_directory_path = "inputs/"
csv_directory_path = "outputs/"
#log = can.BLFReader("inputs/file.blf")


def generate_random_can_message():
    arbitration_id = random.randint(0, 0x7FF)
    data_length = random.randint(0, 20)
    data = [random.randint(0, 0x77) for i in range(data_length)]
    return can.Message(arbitration_id= arbitration_id, data= data, is_extended_id= False)
    
number_files = 20
for i in range( number_files):
    blf_name_file = "inputs/input_file"+str(i)+".blf"
    msg = generate_random_can_message()
    with can.BLFWriter(blf_name_file) as writer:
        writer.on_message_received(msg)
        

blf_files = [f for f in os.listdir(blf_directory_path) if f.endswith('.blf')]
    
for blf_file in blf_files:
    blf_file_path = os.path.join(blf_directory_path, blf_file)
    csv_file_path = os.path.join(csv_directory_path, blf_file.replace('.blf', '.csv'))

    try:
        with can.BLFReader(blf_file_path) as log:
            with open(csv_file_path, "w", newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["Timestamp", "ID", "DLC", "Data"])
                
                for msg in log:
                    csv_writer.writerow([msg.timestamp, hex(msg.arbitration_id), msg.dlc, msg.data.hex()])
    except can.CanError as e:
        print(f"Failed to read BLF file {blf_file}: {e}")