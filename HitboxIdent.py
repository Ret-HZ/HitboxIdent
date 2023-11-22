from enum import Enum
import cutie
import os


__version__ = "1.0"


class BonesOE(Enum):
    face = 0
    mune_n = 1
    ude1_l_n = 2
    ude1_r_n = 3
    ude2_l_n = 4
    ude2_r_n = 5
    ude3_l_n = 6
    ude3_r_n = 7
    ketu_n = 8
    asi1_l_n = 9
    asi1_r_n = 10
    asi2_l_n = 11
    asi2_r_n = 12
    asi3_l_n = 13
    asi3_r_n = 14


class BonesDE(Enum):
    null = 0
    face = 1
    ude3_r = 2
    ude3_l = 3
    asi3_r = 4
    asi3_l = 5
    kosi = 6
    mune = 7
    sync = 8
    ude1_r = 9
    ude1_l = 10
    ude2_r = 11
    ude2_l = 12
    asi1_r = 13
    asi1_l = 14
    asi2_r = 15
    asi2_l = 16
    ketu = 17
    buki_r = 18
    buki_l = 19


Bones = BonesDE



def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def get_set_bits_as_enum(value) -> list:
    set_bits = []

    for bit_position in range(value.bit_length()):
        if value & (1 << bit_position) != 0:
            try:
                set_bits.append(Bones(bit_position).name)
            except ValueError:
                print(f"Warning: bit {bit_position} goes beyond the enum range.")

    return set_bits



def map_enum_names_to_bits(string_list) -> int:
    result = 0

    for string_value in string_list:
        try:
            bit_enum = Bones[string_value.lower()]
            result |= (1 << bit_enum.value)
        except KeyError:
            print(f"Warning: '{string_value}' is not a valid bone.")

    return result



def cls_header():
    cls()
    print(r''' _    _ _ _   _               _____    _            _   
| |  | (_) | | |             |_   _|  | |          | |  
| |__| |_| |_| |__   _____  __ | |  __| | ___ _ __ | |_ 
|  __  | | __| '_ \ / _ \ \/ / | | / _` |/ _ \ '_ \| __|
| |  | | | |_| |_) | (_) >  < _| || (_| |  __/ | | | |_ 
|_|  |_|_|\__|_.__/ \___/_/\_\_____\__,_|\___|_| |_|\__|''')
    print(f"v{__version__}\n")



def identify_bones():
    cls_header()
    mask = cutie.get_number("Enter hitbox value (decimal):", allow_float=False)
    print("\nUsed bones: ", end="")
    print(*get_set_bits_as_enum(mask), sep=", ")
    input("\nPress ENTER to go back to mode selection...")
    choose_mode()



def make_hitbox():
    cls_header()
    print("Select bones: ")
    bone_names = [e.name for e in Bones]
    bone_indices = cutie.select_multiple(bone_names, hide_confirm=False)
    selected_bone_names = [bone_names[index] for index in bone_indices if 0 <= index < len(bone_names)]
    hitbox_bitmask = map_enum_names_to_bits(selected_bone_names)
    cls_header()
    print("Selected bones: ", end="")
    print (*selected_bone_names, sep=", ")
    print(f"\nHitbox value (decimal): {hitbox_bitmask}")
    input("\nPress ENTER to go back to mode selection...")
    choose_mode()



def choose_mode():
    cls_header()
    print("Select mode:")
    options = ["Identify bones", "Make hitbox"]
    choice = options[cutie.select(options)]
    if choice == options[0]:
        identify_bones()
    elif choice == options[1]:
        make_hitbox()



if __name__ == '__main__':
    cls_header()
    print("Select PXD version:")
    pxd_versions = ["Old Engine", "Dragon Engine"]
    pxd_version = pxd_versions[cutie.select(options=pxd_versions, selected_index=1)]
    if (pxd_version == pxd_versions[0]):
        Bones = BonesOE
    choose_mode()