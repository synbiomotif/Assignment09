#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Songli Zhu, 2022-Mar-24, Add Codes to 'Choose CD/Album' choice
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    print()
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. Otherwise reload will be canceled\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        flag = 1
        while flag:
            cd_idx = input('Select the CD / Album index: ')
            try:
                cd_idx = int(cd_idx)
                flag = 0
            except:
                print('\nCD index cannot be a string!\nPlease try again!')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        # TODONE add code to handle tracks on an individual CD
        while True:
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()
            if strChoice == 'x':
                break
            elif strChoice == 'a':
                track_info = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(track_info,cd)
                print('Track information successfully added.')
            elif strChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
            elif strChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                flag = 1
                while flag:
                    track_index = input('Please choose the track index you want to remove: ')
                    try:
                        track_index = int(track_index)
                        flag = 0
                    except:
                        print('Track index must be Integer!')
                cd.rmv_track(track_index)
            else:
                print('Invalid Choice, please select again!')            
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')
