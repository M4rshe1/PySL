from file_unorganizer import file_unorganized
from file_organizer import sort_files
from file_counter import count_files
from organizer_modules import select_folder

if __name__ == "__main__":
    while True:
        print("\n" * 20)
        print("#" * 50)
        print("#    Note that if you want to unsort or count    #")
        print("#    files, the folder you select, has to be     #")
        print("#    a folder that has been sorted before.       #")
        print("#" * 50)
        print("\n")
        print("Select what you want to do:")
        print("--- file management ---")
        print("  Sort files       [1]")
        print("  Unsort files     [2]")
        print("  Count files      [3]")
        print("  Exit             [exit]")
        choice = input("Please enter your choice below: \n>> ")
        folder = select_folder()
        if choice == "1":
            print("Sorting files...")
            countMoved = sort_files(folder)
            print("\n")
            print("#" * 31)
            print(f"   Sorted {countMoved} files/folders   ")
            print("#" * 31)
            print("\n")
        elif choice == "2":
            print("Unsorting files...")

            countMoved = file_unorganized(folder)
            print("\n")
            print("#" * 33)
            print(f"   Unsorted {countMoved} files/folders   ")
            print("#" * 33)
            print("\n")
        elif choice == "3":
            print("Counting files...")
            count = count_files(folder)
            print("\n" * 20)
            print("CATEGORY  : COUNT")
            print("-" * 20)
            for k, v in count.items():
                print(f"{k:<10}: {v['count']}")
            print("-" * 20)
            print("**TOTAL** : " + str(sum([v["count"] for k, v in count.items()])))
            print("\n")
        elif choice == "exit":
            exit()
        else:
            print("Invalid choice")
        input("Press Enter to continue...")
