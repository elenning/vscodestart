import test


import crystalcontrol
#import CrystalModel
#import CrystalViewer

def useControl():
    control = crystalcontrol
    control.hejhej()

def multiply_by_4(x):
    return x*4

def main():
    
    print(multiply_by_4(test.xcord))
    test.runAndJump

if __name__ == '__main__':
    main()
    ''' 
    controller = CrystalControl()
    viewer = CrystalViewer()
    model = CrystalModel()
    
    controller.start()
    
    while controller.notDone() == True:
    
     controller.update()
    '''
