#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This is a calulator to run various likelihood scenarios based on Richard Swineburnes book on the Resurrection.

# K = the evidence of natural theology for God's existence
# E = the detailed historical evidence of
    # e1 - life of Jesus as a prophet/revealter
    # e2 - supermiracle validation (resurrection)
    # e3 - being God incarnate satisfied in no other...than possible Jesus /good life
    #Please note, Swinburne dinstinguishes between e and f. E being the possible evidence of such a thing and f being the actual evidence of such a thing. I just stick with E. 
# H1 = the evidence that God became incarnate in Jesus
# H2 = the Hypothesis that Jesus Christ rose from the dead
# H = the conjunction of H1 and H2

# Our interest will be with the Probality of H given E and K or P(H | E & K) 
# Admittedly (as Swinburne points out), our values will be rough. That is why I am building this calculator so we can run hundreds of simulations. 

#Swinburne sets the likelihood of Theism given background knowledge at .5
#swinburne sets the likelihood of the claim that God became incarnate in a world of sin and suffering at .5


# In[2]:


#step 1 - Swinburne sets the likelihood of Theism given background knowledge at .5
#Please input your Probability of theism


p_tbk = float(input("Input a number from .1  1.0, what is the likelihood of God's Existence to you?")) 
#p_tbk is theism given background knowledge

print(f"Your probability of theism given background knowledge is {p_tbk:.2%}")
#this statement formats the input and outputs it as a percent to two decimal places. 

if p_tbk > .5:
    print("Why do you think the likelihood of God's existence is rather high?")
elif(p_tbk == .5):
    print("Philosopher of Religion, Richard Swineburne also estimates the same as you did. \n He figures this is a pretty safe bet")
else:    
    print("Why do you think the likelihood of God's existence is rather low? \nWhat tips the scales under 50% for you?")


# In[3]:


#step 2 #swinburne sets the likelihood of the claim that God became incarnate in a world of sin and suffering at .5,
#this is when we are assuming theism. So, given theism. 
p_iss = float(input("What is the likelihood that God became incarnate in \n in a world of sin and suffering?")) 
       #p_iss is the probability of incarnation given a world of sin and suffering
print(f"The probability of the incarnation when we assume theism is {p_iss:.2%}")


if p_iss > .5:
    print("Do you think it's rational to estimate that initial probability so high? \nHave you considered contrary evidence to your initial estimate? \nWhy do you hold this to be so certain?")
elif(p_iss == .5):
    print("Swineburne also estimates this number at .5. He seems to think that it's likelihood is just as probable as it's denial")
else:
    print("Thanks for your estimate. By answering lower than .5, are you implying \nThat God not revealing himself in/as a human is more likely than him doing so?")


# In[4]:


#step 3 is to define a probability of the incarnation given theism. .5 * .5
print("This step of the calculator takes your last two estimates and multiplies them together") 

p_ik = p_tbk * p_iss #probability of incarnation given theism 
print(f"The probability incarnation and theism is {p_ik:.2%}")


subtracted_value = 1.0 - p_ik #this is to be used two steps down. In Swinburnes original, the leftover is .75, but everyone elses will be different. 
print(f"This numer is the difference when subtracted from 100% {subtracted_value:.2%}")


# In[5]:


#step 4 is to take the probability of evidence given the incarnation and evidence for God's existence. 
#he places this rather low at 1/10
#the probability of the evidence 1-3, given the claim of the incarnation and the evidence for God's existence

p_eik = float(input("What's the probability of the evidence, given the incarnation and the background knowledge of God's existence? \n Swineburne's guess is to make this pretty low, at 1/10th or .1, You say, "))#the probability of evidence given incarnation and the background knowledge theism. 
print(f"The probability of the Evidence, given the incarnation and background knowledge of God's existence is {p_eik:.2%} ")


# In[6]:


#step 5 
#now, according to Swineburne's formula's we need to bring some of these together. 
#we are looking now for the p(e&c|k)= p(e|c&k)* p(c|k)
#take the last two cells and multiply them

combined_p_ik_eik = p_ik * p_eik
print(f"The combined probability of all together so far is {combined_p_ik_eik:.2%}")

print("swineburnes original numbers would have us at 1/40 or .025%")


# In[7]:


#step 6
#Question what is the p(~c/k) = 3/4, this is what it left from the 1/4 we assigned earlier. 
#Question: What is the chance that E will still occurr if there is no incarnation?
# This could be whether there is no God or he doesn't become incnarate. 
#Namely, what is the probability of those three pieces of evidence occuring in the same individual?
#At the outset, this seems immensley improbable. In the book he says that all three occurring in human history
#in various individuals is somewhat likely, especially with those that are non-miraculous. 
#but all three together in the same individual, fairuly unlikely. 
#swineburne assigns 1/1000 as the likelihood for the original example. 

evidence_occuring_no_god = float(input("Now, what is the likelihood, that Swineburne's three pieces of evidence \n 1. A man being considered a revealer or prophet \n 2. A Supermiracle for validation of who he is. \n 3. This person living the kind of life that is worth emulating by all. \n That all three of these happen in one person. \n Swineburne sees that there is a fairly high likelihood of each of of these \n occuring in three different persons. But, that all \n occuring in one person seems somewhat low. \n his initial estimate he places at .001 or 1/1000th. \n He ultimately thinks the likelihood is much lower than this, but \n for the sake of argument he places it there so that no \n thinks he is doctoring his numbers. He thinks many could \n agree to his estimates being reasonable enough."))
print(f"You said {evidence_occuring_no_god:}")



# e1 - life of Jesus as a prophet/revealter
    # e2 - supermiracle validation (resurrection)
    # e3 - being God incarnate satisfied in no other...than possible Jesus /good life

#This is a very key number. If you lower the likelihood of these three occuring in the same perons (e1-e3) 
#Then, all things staying the same, it only increases the likelihood in the final analysis. 
#but, if you raise the likelihood of this evidence occuring when there is no god, 
#then you are basically having to affirm a miracle, assuming you think the evidence for Jesus' res is compelling. 
#again, one can just say that the three e's, never all happened in Jesus. 
#thus, even if the likelihood for them occuring is minute, in the end they did not happen. 
#that of course would not be compelling. It goes back to e and if they occurred. 
#I suppose someone could argue that the likelihood of three such events occurring in the same person is high...
#Maybe they think that given all the possiblities of human life / interaction, the dice are bound to role three 6's.
#if you have enough roles, then you will get there. Thus, it is all random. 
#my thought would be, that something being random in a series of events, does not necessarily exclude meaningful...?
#still, they would have to deny resurrection...so that one should still keep the likelihood rather low of all three
#occurring in the same person. 


# In[8]:


#step 7
#taking all of these together

p_e_k = combined_p_ik_eik + (subtracted_value * evidence_occuring_no_god)  #and the 1/1000 from above
print(f"the next step, with your numbers, get's us to {p_e_k:.2%}")

print("swineburne's original numbers bring us to 103/4000 or .02575%")


# In[9]:


#let's finish the equation
#p(c|e&k)= p(e|c&K) * p(c|k) / p(e|k)

total_p = p_eik * p_ik / p_e_k
print(f"this is the likelihood everyone {total_p:.2%}")


# In[ ]:




