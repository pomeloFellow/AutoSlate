import src.gui.logic.ProgressReport as pr

def update_pr_gui(progress_report: pr.ProgressReport, curr_stage):
    progress_report.update_progress(curr_stage)
    progress_report.on_progress(progress_report.percent, curr_stage)