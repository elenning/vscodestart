import test

import CrystalControl
import CrystalModel
import CrystalViewer

print("Hej, utanförish main")

if __name__ == "__main__":
    main()

def main():
    print("inside main function")

    controller = CrystalControl()
    viewer = CrystalViewer()
    model = CrystalModel()
    
    controller.start()
    
    while controller.notDone() == True:
    
        controller.update()

