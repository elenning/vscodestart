import CrystalControl
import CrystalModel
import CrystalViewer

if __name__ == "__main__":
    print("inside main function")

    controller = CrystalControl()
    viewer = CrystalViewer()
    model = CrystalModel()

    controller.start()

    while controller.notDone() == True:
        controller.update()
