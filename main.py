from detect import detect
from calculate_target_pos import calculate_target_pos
from sent_drone import sent_drone
from collect_data import collect_data
from update_conf_score import update_conf_score


if __name__ == "__main__":
    print('Starting....\n')
    #connect to the drone


    conf_thres = 0.25

    quit=False
    while not quit:
        xyxy,conf,label = detect()
        #check if object's confidence is above threshold
        if label == 'object' and conf>conf_thres:
            #put label on the frame
            pass
        elif label == 'object' and conf<=conf_thres:
            #put label with question mark
            #sent the drone to check
            pos = calculate_target_pos(cur_drone_pos)#this funciton should return a tuple of (x1,y1,angle)
            success = sent_drone(pos)#should use PID control to send the drone to the target position, return boolean
            if success:
                collect_data()
                new_conf_score = update_conf_score()#input: image data, output:new score
                #put the new label on the web_frame
        #ask to continue
        if input('press q to quit')=='q':
            quit = True
    print('Program Ended')
