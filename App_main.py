# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:14:21 2020

@author: 老陈三
"""

from face_recognize_positon import face_recog_pos
import cv2
from dlib import get_frontal_face_detector

VIDEO_PATH = r'./videos/3.mp4'
POS_FILE_PATH = r'./files/pos.txt'
BULLETS_FILE_PATH = r'./files/bullets.txt'
BULLETS_BACKUP_FILE_PATH = r'./files/bullets_backup.txt'

face_pos = face_recog_pos()

#face_pos.update_all_bullets_screen(VIDEO_PATH, BULLETS_FILE_PATH, ' ')
#face_pos.update_face_pos(VIDEO_PATH, POS_FILE_PATH)
face_pos.show_video_with_bullets(VIDEO_PATH, POS_FILE_PATH, BULLETS_FILE_PATH, BULLETS_BACKUP_FILE_PATH)