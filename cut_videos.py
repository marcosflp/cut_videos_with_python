import sys
import re
from history_times import all_history_list
from moviepy import editor as mpy


def get_history(scenes_list):
    clip = mpy.VideoFileClip(sys.argv[1])
    scenes_data_list = []

    for x in scenes_list:
        scene_in = re.search(r'(\d+):(\d+):(\d+)', x[0])
        scene_out = re.search(r'(\d+):(\d+):(\d+)', x[1])
        
        start_time_of_scene = int(scene_in.group(1))*3600 + int(scene_in.group(2))*60 + int(scene_in.group(3))
        end_time_of_scene = int(scene_out.group(1))*3600 + int(scene_out.group(2))*60 + int(scene_out.group(3))

        scene = clip.subclip(start_time_of_scene, end_time_of_scene)
        
        scenes_data_list.append(scene)

    return mpy.concatenate_videoclips(scenes_data_list)


if __name__ == "__main__":
    movie_splited = []

    for x in all_history_list:
        movie_splited.append(get_history(x))

    movie = mpy.concatenate_videoclips(movie_splited)

    movie.write_videofile('video.mp4')
