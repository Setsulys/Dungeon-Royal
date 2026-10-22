import pickle
import os

SAVE_FOLDER = "saves"
POSSIBLE_SLOTS=[1,2,3]

os.makedirs(SAVE_FOLDER,exist_ok=True)

def get_slot_path(slot_number):
    if slot_number not in POSSIBLE_SLOTS :
        raise ValueError("Slot number sho")
    return os.path.join(SAVE_FOLDER,f"save_{slot_number}.dat")

def save_game(data,slot_number):
    try:
        path = get_slot_path(slot_number)
        with open(path,"wb") as file:
            pickle.dump(data,file)
        print(f"Data saved sucessfully on [slot {slot_number}]")
    except Exception as e:
        print(f" Error during save:{e}")

def load_game(slot_number):
    path= get_slot_path(slot_number)
    try:
        with open(path,"rb") as file:
            data = pickle.load(file)
        print(f"[Slot {slot_number} loaded")
        return data
    except Exception:
        print(f" File [Slot {slot_number} is corrupted")
    return None