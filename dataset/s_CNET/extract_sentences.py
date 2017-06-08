#from BeautifulSoup import BeautifulSoup
import re, string, codecs, os
#import nltk
#from nltk import tokenize
#from nltk.tokenize import RegexpTokenizer

#tokenizer = RegexpTokenizer(r'\w+')

def main():
    
    
    lines = [line.rstrip('\n') for line in open('exp.list')]
    for file in lines:
        #print file

        posts = [line.rstrip('\n') for line in open("raw_threads/" + file)]
        
        
        
        #reader = open("Plain_threads/"+l, "r")
        ##writer = open("Cleaned_threads/"+l, "w")
        #info_writer = open("Cleaned_threads/"+l[:-4]+"_infos", "w")
        depth_writer = open("raw_threads/"+ file + ".text.all.parsed.ner.depth", "w")
        thread_dict = {}
        idx = 1

        for line in posts:   
            # new post
            post_level = 0
            line = line.split("\t")
            #print idx

            if len(line) == 10:
                thread_id = line[0]
                time_order = line[1]
                CNET_thread_id = line[2]
                CNET_post_id = line[3]
                CNET_parent = line[4]
                user_id = line[5]
                post_time = line[6]
                post_time_number = line[7]
                subject = line[8]
                post_text = line[9]
                
                # extract sentences
                #print "post_id: " + CNET_post_id + "\t" + "parent_id " + CNET_parent
                
                # compute depth
                
                if CNET_parent == "nr": # first post in a thread so level = 0
                    thread_dict.update({CNET_post_id:0})
                else: # it's parent is in the dic ==> find the parent and update the level
                    parent_level = thread_dict[CNET_parent]
                    thread_dict.update({CNET_post_id:parent_level})
                    
                deep = thread_dict[CNET_post_id]
                print deep

                #reading the number of sentences after using open nlp to sentence detection
                real_post = "exp.fragments/"+ file + ".text.frag_" + str(idx) + ".sent"
                print real_post
                sent_list = [line.rstrip('\n') for line in open(real_post)]

                for sentence in sent_list:
                    # tokenize the sentence to remove punctuation
                    
                    depth_writer.write(str(deep) + "\n")
               	    deep +=1 
                
                #update the thread depth
                thread_dict.update({CNET_post_id:deep})
                # write information abt the post into a separated file
                #info_writer.write("Post ID: "+ CNET_post_id + " Number of sentences: " + str(len(post_sentences)) + " Parent: " + CNET_parent + "\n")
                idx +=1;
            
if __name__=='__main__':
    main()
