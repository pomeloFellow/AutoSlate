# core util.logic
import src.utils.utils as util
import src.filesys.files as fs
import src.audio.preprocessor as preprocessor
import src.audio.transcriber as transcriber

def relabel_videos(input_folder):
    # check if input_folder is directory
    util.log(input_folder)
    fs.is_dir(input_folder)

    # make array of video posixpaths
    video_paths = fs.video_paths_in_folder(input_folder)
    util.log(video_paths)

    # for every video path
    # assumes video_paths_in_folder() "checks" files are videos
    for video_path in video_paths:
        # get audio info (label, confidence)
        audio, clip_time = preprocessor.test_preprocessor(video_path)
        util.log(clip_time)
        whisper_result = transcriber.transcribe(audio, clip_time)
        util.log(whisper_result)
        util.log(transcriber.total_audio_confidence(whisper_result))
        audio_text = transcriber.get_text(whisper_result)
        util.log(audio_text)

        # get video info (label, confidence)

        # relabel video
        new_label = fs.text_to_file_name(audio_text)
        fs.rename_video(video_path, new_label + ".mp4")