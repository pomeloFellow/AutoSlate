from enum import Enum, auto

class ProgressReport():
    class Stage(Enum):
            EXTRACTING = auto()
            PREPROCESSING = auto()
            TRANSCRIBING = auto()
            RENAMING = auto()
            DONE = auto()

    def __init__(self):
        self.total = 0
        self.completed = 0
        self.percent = 0
        self.stage = 0
        self.done_vids = 0
        self.total_vids = 1

        # curr vid
        self.curr_vid_prog = 0

        # callbacks
        self.on_progress = None
        self.on_done = None
    
    def set_total(self, num_vids):
        self.total = num_vids * 100
        self.total_vids = num_vids

    def update_progress(self, stage: "ProgressReport.Stage"):
        match stage:
            case self.Stage.PREPROCESSING:
                self.stage = stage
                self.curr_vid_prog = 15

            case self.Stage.TRANSCRIBING:
                self.stage = stage
                self.curr_vid_prog = 18

            case self.Stage.RENAMING:
                self.stage = stage
                self.curr_vid_prog = 98

            case self.Stage.EXTRACTING:
                self.stage = stage
                self.curr_vid_prog = 0
                self.done_vids += 1

            case self.Stage.DONE:
                self.stage = stage

        self.update_percent()


    def update_percent(self):
        past_vid_total = self.done_vids * 100
        self.completed = past_vid_total + self.curr_vid_prog

        self.percent = (self.completed / self.total) * 100
        self.on_progress(self.percent, self.stage)
        

    def done(self):
        self.on_done