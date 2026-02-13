from enum import Enum, auto

class ProgressReport():
    class Stage(Enum):
            FIN_EXTRACT = auto()
            FIN_PREPROCESS = auto()
            FIN_TRANSCRIBE = auto()
            FIN_RENAME = auto()

    def __init__(self):
        self.total = 0
        self.completed = 0
        self.percent = 0
        self.stage=0
        self.curr_vid = 1
        self.total_vids = 1

        # callbacks
        self.on_progress = None
        self.on_done = None
    
    def set_total(self, num_vids):
        self.total = num_vids * 100
        self.total_vids = num_vids

    def update_progress(self, stage: "ProgressReport.Stage"):
        match stage:
            case self.Stage.FIN_EXTRACT:
                self.stage = stage
                self.completed += 15

            case self.Stage.FIN_PREPROCESS:
                self.stage = stage
                self.completed += 3

            case self.Stage.FIN_TRANSCRIBE:
                self.stage = stage
                self.completed += 80

            case self.Stage.FIN_RENAME:
                self.stage = stage
                self.completed += 2
                self.curr_vid += 1

        self.update_percent()


    def update_percent(self):
        self.percent = (self.completed / self.total) * 100
        self.on_progress(self.percent, self.stage)

    def done(self):
        self.on_done