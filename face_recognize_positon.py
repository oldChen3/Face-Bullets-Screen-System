# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:28:18 2020

@author: 老陈三
"""

import cv2
from dlib import get_frontal_face_detector
from os import rename, remove
from PIL import ImageFont, ImageDraw, Image
from face_recognition import face_locations
import numpy as np


class face_recog_pos():
    def update_face_pos(self, video_path, pos_file_path):
        pos_fd = open(pos_file_path, 'w')
        vs = cv2.VideoCapture(video_path)
        frame_no = 0
        #detector = get_frontal_face_detector()
        while True:
            frame = vs.read()
            frame = frame[1]
            if frame is None:
                break
            #ret = self.get_face_pos_in_image(detector,frame)
            ret = self.get_face_pos_v2(frame)
            pos_fd.write(str(frame_no)+'-'+str(len(ret)))
            for val in ret:
                pos_fd.write('-'+str(val))
            pos_fd.write('- \n')
            frame_no += 1
        vs.release()
        cv2.destroyAllWindows()
        pos_fd.close()
        
    def update_all_bullets_screen(self,video_path,bullet_file_path,text):
        bullet_fd = open(bullet_file_path, 'w')
        vs = cv2.VideoCapture(video_path)
        #frame_no = 0
        while True:
            frame = vs.read()
            frame = frame[1]
            if frame is None:
                break
            bullet_fd.write(text+'\n')
        bullet_fd.close()
        
    def show_video_with_bullets(self, video_path, pos_file_path, bullets_path, bullets_path_backup):
        pos_fd = open(pos_file_path, 'r')
        bullets_fd = open(bullets_path, 'r+')
        bullets_backup_fd = open(bullets_path_backup, 'w')
        vs = cv2.VideoCapture(video_path)
        frame_no = 0
        text_file = ' '
        text_user = ' '
        text = ''
        while True:
            frame = vs.read()
            frame = frame[1]
            if frame is None:
                break
            (h, w) = frame.shape[:2]
            width=1000
            r = width / float(w)
            dim = (width, int(h * r))
            img = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
            ret = self.read_face_pos(frame_no, pos_fd)
            text_file = self.read_bullet_screen(bullets_fd)
            text_file = text_file.strip('\n')
            if text_user == ' ':
                text = text_file
            else:
                text = text_user
            if cv2.waitKey(30) == ord('s'):
                text_user = self.input_bullet_text_eng()
                text = text_user
                #self.write_bullet_screen(bullets_fd,text)
                print(text)
            self.write_bullet_screen(bullets_backup_fd,text)
            for p in ret['Position']:
                cv2.rectangle(img,(p[0],p[1]),(p[2],p[3]),(100,0,0),1)
                self.show_bullet_on_img(img,(p[2],p[3]),text)
            cv2.imshow("face detect", img)
            frame_no += 1
        pos_fd.close()
        bullets_fd.close()
        bullets_backup_fd.close()
        remove(bullets_path)
        rename(bullets_path_backup,bullets_path)
            
        cv2.destroyAllWindows()
        print('frame_no = ' + str(frame_no))
            
    def read_face_pos(self,frame_no,pos_fd):
        ret = {'Frame_no':0,'lens':0, 'Position':[]}
        contexts = contexts = pos_fd.readline()
        if contexts != " ":
            contexts = contexts.strip('\n')
            contexts = contexts.strip(' ')
            contexts = contexts.replace('--','-')
            res_str = contexts.split('-')
            ret['Frame_no'] = int(res_str[0])
            ret['lens'] = int(res_str[1])
            i = 0
            while i < ret['lens']:
                #print("ret['Frame_no'] = " + res_str[0])
                ret['Position'].append([int(res_str[i+2]),int(res_str[i+3]), 
                                       int(res_str[i+4]),int(res_str[i+5])])
                i = i + 4
        return ret
    
    def get_face_pos_v2(self,frame):
        ret = []
        (h, w) = frame.shape[:2]
        width=1000
        r = width / float(w)
        dim = (width, int(h * r))
        img = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        rgb_frame = img[:, :, ::-1]
        find_face_locations = face_locations(rgb_frame)
        draw_img = img.copy()
        
        for face_location in find_face_locations:
            top, right, bottom, left = face_location
            ret += [left,top, right, bottom]
            cv2.rectangle(draw_img,(left,top),(right,bottom),(255,0,0),2)
        cv2.imshow("face detect", draw_img)
        cv2.waitKey(1)
        return ret
        

    def get_face_pos_in_image(self,detector,img):
        (h, w) = img.shape[:2]
        width=1000
        r = width / float(w)
        dim = (width, int(h * r))
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        draw_img = img.copy()
        cv2.imshow("Image", img)
        
        # 人脸检测
        ret = []
        rects = detector(gray, 1)
        for (i, rect) in enumerate(rects):
            ret += [rect.left(),rect.top(),rect.right(),rect.bottom()]
            cv2.rectangle(draw_img,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(255,0,0),2)
        cv2.imshow("face detect", draw_img)
        cv2.waitKey(1)
        return ret
    
    def show_bullet_on_img(self,img, pos, text):
        """
        draw_img = ImageDraw.Draw(img)
        draw_img.text(pos,text,(255,255,0))
        """
        cv2.putText(img, text,pos,cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,255,0), 1, cv2.LINE_AA)
        
    def show_utf8_bullet_on_img(self, img, pos, text):
        img_pillow = Image.fromarray(img)
        draw_img = ImageDraw.Draw(img_pillow)
        draw_img.text(pos,text,fill=(0,120,0,0))
        img = np.array(img_pillow)
        return img
    
    def input_bullet_text_eng(self):
        text = input('input bullet : \n')
        return text
    
    def write_bullet_screen(self,fd,text):
        fd.write(text+'\n')
    
    def read_bullet_screen(self, fd):
        text = fd.readline()
        return text
    