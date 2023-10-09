import os
import cv2

sample=cv2.imread("SOCOFing/Altered/Altered-hard/150__M_Right_index_finger_Obl.BMP")

#sample=cv2.resize(sample, None, fx=2.5,fy=2.5)
#cv2.imshow("sample",sample)
#cv2.waitKey(0)


best_score=0
image=filename=None
kp1,kp2,mp=None,None,None

l=[file for file in os.listdir("SOCOFing/Real")]

counter=0
for file in l[:1000]:
    if counter%50==0:
        print(counter)
    counter+=1
    fingerprint_image=cv2.imread("SOCOFing/Real/"+file)
    sift=cv2.SIFT_create()

    keypoints1, descriptors1=sift.detectAndCompute(sample,None)
    keypoints2, descriptors2=sift.detectAndCompute(fingerprint_image,None)

    matches=cv2.FlannBasedMatcher({'algorithm':1,'trees':10},{}).knnMatch(descriptors1,descriptors2,k=2)


    match_points=[]

    for p,q in matches:
        if p.distance<0.1*q.distance:
            match_points.append(p)


    keypoints=0

    if len(keypoints1)<len(keypoints2):
        keypoints=len(keypoints1)
    else:
        keypoints=len(keypoints2)


    if len(match_points)/keypoints * 100 >best_score:
        best_score=len(match_points)/keypoints * 100

        filename=file
        image=fingerprint_image
        kp1=keypoints1
        kp2=keypoints2
        mp=match_points


print("best match:"+filename)
print("score:"+str(round(best_score,3)))

result=cv2.drawMatches(sample, kp1, image,kp2,mp,None)
result=cv2.resize(result,None, fx=4,fy=4)
cv2.imshow("Result",result)
cv2.waitKey(0)


    
    
