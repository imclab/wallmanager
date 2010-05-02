from pymt.ui.widgets.modalwindow import MTModalWindow
from mtmenu.ui.votepopup import VotePopup
from threading import Timer


class CoverWindow( MTModalWindow ):

    def __init__(self, **kwargs):
        self.vote = VotePopup()
        self.timer = Timer(10.0, self.display)
        super(CoverWindow, self).__init__(**kwargs)
        
        
    def show(self, app):
        self.vote.app = app
        self.add_widget( self.vote )
        self.timer.start()
    
        
    def hide(self):
        self.timer.cancel()
        self.remove_widget( self.vote )
        self.parent.remove_widget( self )

