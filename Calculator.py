import math, speech_recognition as sr

def a():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print('Speak now 🎙️')
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            conv_in=[('x','*'),('into','*'),('by','/'),('sin','math.sin('),('cos','math.cos('),('tan','math.tan('),('raise to the power','**')]
            for i in conv_in:
                j,k=i
                text=text.replace(j,k)
            inp_eqn=text+' '
            l=len(inp_eqn)
            for i in range(l):
                if inp_eqn[i:i+6]=='square':
                    if inp_eqn[i:i+14]=='square root of':
                        inp_eqn=inp_eqn[:i]+'math.sqrt('+inp_eqn[i+14:]
                    else:
                        inp_eqn=inp_eqn[:i]+'** 2'+inp_eqn[i+6:]
                if inp_eqn[i:i+4]=='cube':
                    if inp_eqn[i:i+12]=='cube root of':
                        for j in range(i+13,l):
                            if j==l-1 or inp_eqn[j]==' ':
                                inp_eqn=inp_eqn[:i]+inp_eqn[i+13:j+1]+' ** (1/3)'+inp_eqn[j+1:]
                    else:
                        inp_eqn=inp_eqn[:i]+'** 3'+inp_eqn[i+4:]
            for i in range(l):
                if inp_eqn[i:i+9] in ('math.sin(','math.cos(','math.tan(',):
                    for j in range(i+10,l):
                        if inp_eqn[j]==' ' or j==l-1:
                            inp_eqn=inp_eqn[:j+1]+' ) '+inp_eqn[j+1:]
                            break
                if inp_eqn[i:i+10]=='math.sqrt(':                              
                    for j in range(i+11,l):
                        if j==l-1 or inp_eqn[j]==' ':
                            inp_eqn=inp_eqn[:j]+' ) '+inp_eqn[j+1:]
                            break
            try:
                ans=eval(inp_eqn)
                conv_out=[('math.sqrt','√'),('math.sin','sin'),('math.cos','cos'),('math.tan','tan'),(' + ','+'),(' - ','-'),(' * ','✕'),(' / ','/'),(' ** ','^')]
                for i in conv_out:
                    j,k=i
                    inp_eqn=inp_eqn.replace(j,k)
                out_eqn=inp_eqn.replace(' ','')
                print(out_eqn+' = '+str(ans))
            except:
                print('Could not interpret. Please try again.')
        except:
            print('Could not detect voice. Please try again.')

while True:
    inp=int(input('1 -> Manually type mathematical expression\n2 -> Use speech recognition to input mathematical expression\n3 -> Exit\nEnter your command: '))
    if inp==1:
        try:
            print('Answer: '+str(eval(input('Type mathematical expression: '))))
        except:
            print('Could not interpret. Please try again.')
        print()
        continue
    elif inp==2:
        a()
        print()
        continue
    elif inp==3:
        print('Thank you for using this program.')
        break
    else:
        print('Please enter a valid input.\n')
        print()
        continue


