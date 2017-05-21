import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

from gooey import Gooey, GooeyParser
import datetime
import argparse
import requests
import time
import json

@Gooey
def main():
    """Usage: posts-by-user.py filename.json

Assumes filename.json is a JSON GroupMe transcript.
    """
    
    
    #if len(sys.argv) < 2:
     #   print(main.__doc__)
     # sys.exit(1)
    parser = GooeyParser(description="My Cool GUI Program!") 
	
    parser.add_argument('--TranscriptFile',
                            help='Enter the transcript file!')
    parser.add_argument('--minNumLikes',
                            help='Enter the minimum number of likes whose messages you want to display!',
                            type=int)
    parser.add_argument('--wordToCheck',
                            help='Enter a word you want to check for in the transcript!')
    
	
	
    args = parser.parse_args()
    fileForTranscript = args.TranscriptFile
    minLikes = args.minNumLikes
    word = args.wordToCheck
	
    print fileForTranscript
    print minLikes
    print word
	
    transcriptFile = open(fileForTranscript)
    transcript = json.load(transcriptFile)
    transcriptFile.close()

    print ' '
    print ' '
    print '*****************************************************'
    print '*****************************************************'
    print '*****************************************************'
    print 'Checking transcript... ' + transcriptFile.name
    print '*****************************************************'
    print '*****************************************************'
    print '*****************************************************'
    print ' '
    print ' '
    #use this for terminal input
	#minLikes = input("Enter the minimum number of likes the grext posts that u wanna check for should have: ")
    print ' '
    print 'Here is a list of those who wrote posts with atleast ' + str(minLikes) + ' likes: '
    print ' '
    
    names = {}
    counts = {}
    likes = {}
    
    totalLikesGiven = 0
 
    for message in transcript:
        name = message[u'name']
        id = message[u'user_id']
        text = message [u'text']
        faves = message[u'favorited_by']
        nlikes = faves if faves == 0 else len(faves)
        
        names[id] = name
        
        if nlikes >= minLikes:
            print (str(nlikes) + ' like comment by '+ name + '\n' + '"'+str(text)+'"' + '\n').encode(sys.getdefaultencoding(), 'replace')
            #likes[id] = likes[id] + nlikes
        
        if id not in likes:
            likes[id] = 0
        else:
            likes[id] = likes[id] + nlikes
            totalLikesGiven = totalLikesGiven + nlikes

        if id not in counts:
            counts[id] = 0
        else:
            counts[id] = counts[id] + 1
            

    totalMessages = len(transcript)
    print '________________________________________________________'
    print ' '
    print('Total Message Count: ' + str(totalMessages))
    print ' '
    
    
    nameArray = []
    countArray = []
    likeArray = []
    nameIndex = 0
    countIndex = 0
    likeIndex = 0
    for id, count in counts.items():
        name = names[id]
        countpercentage = round(count/float(totalMessages) * 100)
        #like = likes[id]
        print(name + ': ' + str(count) + ' (' + str(countpercentage) + '%)')
        countArray.append(count)
        countIndex = countIndex + 1



    
    print '________________________________________________________'  
    print ' '
    print 'Total Likes Given: ' + str(totalLikesGiven)
    print ' '
    
    for id, like in likes.items():
        name = names[id]
        likespercentage = round(like/float(totalLikesGiven) * 100)
        #like = likes[id]
        print(str(like) + ' likes were given to the posts of ' + name + ' which is ' + str(likespercentage) +'%')
        likeArray.append(like)
        likeIndex = likeIndex + 1
        nameArray.append(name)
        nameIndex = nameIndex + 1
    
    print '________________________________________________________'
    print ' '
    print 'But what about that ratio though?'
    print ' '
    for countIndex in range(countIndex):
        print nameArray[countIndex]
        print 'Total Recieved Likes: ' + str(likeArray[countIndex])
        print 'Total Posts: ' + str(countArray[countIndex])
        if countArray[countIndex]>0: #AKA if you're not Mansa and have received atleast 1 like
            likeRatio = round(likeArray[countIndex]/float(countArray[countIndex]) * 100)
        else:
            likeRatio = 0
        print 'Like/Post Ratio: ' + str(likeRatio) + '%'
        print ' '
        
        
    print '________________________________________________________'  
    print ' '
    print 'Message count by the month: '
    monthCount = [0,0,0,0,0,0,0,0,0,0,0,0] #Jan -> Dec
    for message in transcript:
        time = datetime.datetime.fromtimestamp(message[u'created_at']).strftime('%m')
        monthCount[int(time)-1]=monthCount[int(time)-1]+1 #increment the month in which the comment was posted in
              
    total = sum(monthCount)
    print '\nJanuary: ' + str(monthCount[0]) + ' (' + str("%.1f" %((monthCount[0]/float(total))*100)) +'%)'
    print 'February: ' + str(monthCount[1]) + ' (' + str("%.1f" %((monthCount[1]/float(total))*100)) +'%)'
    print 'March: ' + str(monthCount[2]) + ' (' + str("%.1f" %((monthCount[2]/float(total))*100)) +'%)'
    print 'April: ' + str(monthCount[3]) + ' (' + str("%.1f" %((monthCount[3]/float(total))*100)) +'%)'
    print 'May: ' + str(monthCount[4]) + ' (' + str("%.1f" %((monthCount[4]/float(total))*100)) +'%)'
    print 'June: ' + str(monthCount[5]) + ' (' + str("%.1f" %((monthCount[5]/float(total))*100)) +'%)'
    print 'July: ' + str(monthCount[6]) + ' (' + str("%.1f" %((monthCount[6]/float(total))*100)) +'%)'
    print 'August: ' + str(monthCount[7]) + ' (' + str("%.1f" %((monthCount[7]/float(total))*100)) +'%)'
    print 'September: ' + str(monthCount[8]) + ' (' + str("%.1f" %((monthCount[8]/float(total))*100)) +'%)'
    print 'October: ' + str(monthCount[9]) + ' (' + str("%.1f" %((monthCount[9]/float(total))*100)) +'%)'
    print 'November: ' + str(monthCount[10]) + ' (' + str("%.1f" %((monthCount[10]/float(total))*100)) +'%)'
    print 'December: ' + str(monthCount[11]) + ' (' + str("%.1f" %((monthCount[11]/float(total))*100)) +'%)'
    
    print '________________________________________________________'  
    print ' '
    print 'Message count by the hour: '
    timeOfDay = [0,0,0,0] #Morning(5am-Noon), Afternoon(Noon-5pm), Evening (5pm-9pm), Night(9pm-4am)
    for message in transcript:
        time = datetime.datetime.fromtimestamp(message[u'created_at']).strftime('%H')
        #increment the time-of-day in which the comment was posted in
        #before 5am
        if int(time) < 5:
            timeOfDay[3]=timeOfDay[3]+1 
        #5am - Noon
        elif int(time) < 12:
            timeOfDay[0]=timeOfDay[0]+1 
        #Noon - 5pm
        elif int(time) < 17:
            timeOfDay[1]=timeOfDay[1]+1 
        #5pm - 9pm 
        elif int(time) < 21:
             timeOfDay[2]=timeOfDay[2]+1  
        #after 9pm
        else:
             timeOfDay[3]=timeOfDay[3]+1       

    print '\nMorning (5am-Noon): ' + str(timeOfDay[0]) + ' (' + str("%.1f" %((timeOfDay[0]/float(total))*100)) +'%)'
    print 'Afternoon (Noon-5pm): ' + str(timeOfDay[1]) + ' (' + str("%.1f" %((timeOfDay[1]/float(total))*100)) +'%)'
    print 'Evening (5pm-9pm): ' + str(timeOfDay[2]) + ' (' + str("%.1f" %((timeOfDay[2]/float(total))*100)) +'%)'
    print 'Night (9pm-4am): ' + str(timeOfDay[3]) + ' (' + str("%.1f" %((timeOfDay[3]/float(total))*100)) +'%)\n'

    print '________________________________________________________'  
    print ' '
    print "Who's said what words the most???\n"
    #word = raw_input("Enter word to check: ")
    print ' '
    
    
    wordByPersonCount = {}
    
    for message in transcript:
        text = message [u'text']
        name = message[u'name']
        id = message[u'user_id']
        
        if str(word) in str(text): #if the word is in the post
            print str(name) + ': ' + str(text)  #print out the post
            #counts[id] = counts[id] + 1     #increment the person's 
           
        
    #print str(counts[id])
        if id not in wordByPersonCount:
            wordByPersonCount[id] = 0
        else:
            wordByPersonCount[id] = wordByPersonCount[id] + 1
            #print str(wordByPersonCount[id])


if __name__ == '__main__':
    main()
    print '\n**************************************************'
    sys.exit(0)
