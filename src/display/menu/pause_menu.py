import pickle
import os

SAVE_FOLDER = "saves"

os.makedirs(SAVE_FOLDER,exist_ok=True)

def get_slot_path(slot_number):
    if slot_number not in 3:
        raise ValueError("Slot number sho")