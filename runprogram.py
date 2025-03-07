from controlTV import ControlTV
import time

menu = """Press 0️⃣ turn off\nPress 1️⃣ mute\nPress 2️⃣ up volume\nPress 3️⃣ low volumen\nPress 4️⃣ up channel\nPress 5️⃣ low channel\nPress 6️⃣ write de channel\nPress 7️⃣ get information\n Press 'q' to leave
"""

def main():
    controls_list = []
    mycontrol = ControlTV()

    try:
        while True:
            # Aseguramos que la entrada sea explícita
            user_input = input("Write '1' to turn on or '0' to turn off or 'q' to leave: ")
            if user_input == '1':
                mycontrol.turn_on()
                while True: # BUCLE TURN ON
                    print("\n################################\n")
                    print("Information control TV")
                    print(mycontrol.info())
                    print("\n################################\n")

                    print(menu)
                    print()
                    option = input("What do you want to do? ")

                    # Manejo del 'q' fuera del match
                    if option == 'q':
                        print("Exiting...")
                        break

                    match int(option):
                        case 0:
                            print("TV is turn OFF")
                            mycontrol.turn_off()
                            break
                        case 1:
                            print("TV is mute")
                            mycontrol.mute()
                        case 2:
                            print("UP the volume")
                            mycontrol.up_volume()
                        case 3:
                            print("LOW the volume")
                            mycontrol.low_volume()
                        case 4:
                            print("UP channel")
                            mycontrol.up_channel()
                        case 5:
                            print("LOW channel")
                            mycontrol.low_channel()
                        case 6:
                            channel = int(input("What is the channel? "))
                            mycontrol.find_channel(channel)
                            print(f"Channel is {mycontrol.channel}\n")
                        case 7:
                            print(mycontrol.info())

                        case _:
                            print("Choose an option betweet 0 and 7\n")
            elif user_input == 'q':
                break
            else:
                if not mycontrol.is_on:
                    print("Already turn off the control TV")
                print("You need turn on the Control for use it!\n")
                if mycontrol.is_on:
                    mycontrol.turn_off()
                time.sleep(2)

    except KeyboardInterrupt:
        print("Interruption with the keyboard Ctrl + c")

if __name__ == "__main__":
    main()