"""
Created on Sat Apr 18 11:59:24 2020

@author: chenjinghui
"""


Face Bullets Screen System  

Overview  
This system uses face recognize algorithm to find the faces in the frame of video, and then allow people 
to add his/her bullet screen on the frame around the face, the bullet screen will follow the face to move.

Installation Dependencies:  
Python-3.6  
dlib(base on python version 3.6)  
OpenCV-Python  

How to Run?  
1.install the dependencies  
2.git clone https://github.com/oldChen3/Face-Bullets-Screen-System.git  
3.cd face_bullet_screen  
4.python App_Main.py  
5.you can input key 's' to stop the video, then to input you words, the key 'Enter' will finish you input and continue the video  

Experiments:  

API Describe:  
class face_recog_pos::get_face_pos_in_image(image)->ret  
    @brief: get & return the faces on the input image  
    @param: image the image you what to find face  
    @return: ret is a list like [0,1,2,3, ... ], length is 4 times, and every 4 point present the 4 corner of a recentage  

FAQ:  
1.How to append your code for face recognize:  
 you can realize you own function, and replace the function class face_recog_pos::get_face_pos_in_image(image) in source code   

2.How to change the image size:  
  you can change the define Frame_WIDTH_DEF to your value, however if you changed it, you need to re-update the face position  

Claim:  
  all code is follow the license: MIT  
