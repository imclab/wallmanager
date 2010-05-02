from pymt import *
from gesture.gesture_scan import GestureScan
from mtmenu.proxy import *
from pymt.ui.window.win_glut import MTWindowGlut
from mtmenu.models import ApplicationProxy, CategoryProxy
from mtmenu.utils import *
from mtmenu.ui import *


if __name__ == '__main__':
    # Start TUIO proxy
    proxy.start()
    

    apps_grid.add( getAllApplications() )
    category_grid.add( getAllCategories() )
    
    # Top left logo
<<<<<<< HEAD:mtmenu/main.py
    icon = MTScatterImage(filename= 'images/logo.png', pos=(40,480), scale= 0.5)
    main_label =  MTLabel(label='SenseWall', pos= (110, 490), font_size= 40)
    secondary_label = MTLabel(label='http://sensewall.dei.uc.pt', pos= (110, 478), font_size= 16)
=======
    icon = MTScatterImage(filename= 'images/logo.png', pos=(30,580), scale= 0.5)
    main_label =  MTLabel(label='SenseWall', pos= (100, 590), font_size= 40)
    secondary_label = MTLabel(label='http://sensewall.dei.uc.pt', pos= (100, 580), font_size= 16)

>>>>>>> d6119fe... Top left logo.:mtmenu/main.py

    # Add widgets to Scatter
    scatter.add_widget(apps_grid)
    scatter.add_widget(category_grid)
    scatter.add_widget( icon )
    scatter.add_widget( main_label )
    scatter.add_widget( secondary_label )
    
    # Add Scatter to MainWindow
    main_window.add_widget(scatter)
    
    #Add gesture recognition
    main_window.add_widget(GestureScan())
    
    
    # Execute main loop
    runTouchApp()
