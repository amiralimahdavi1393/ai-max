from shape import draw,select,title,clear
from __for__ import main,tk,comb,lbl,message_show,Button,wait
from random import choice
def ok():
    global comb

    Computer=choice(select)
    if comb.get()=='stone':
        
        title('You🫵')
        draw.stone()
        wait(1)
        clear()
        if Computer=='scissor':
            
            title('Computer💻')
            draw.scissor()
            message_show.info('winer','✅your winer✅')
        if Computer=='paper':
            
            title('Computer💻')
            draw.paper()
            message_show.info('gameover','❌your gameover❌')
        if Computer=='stone':
          
            title('Computer💻')
            draw.stone()
            message_show.info('equal','🟰you and computer are equal🟰')
        wait(1)
        exit()
    if comb.get()=='paper':
        
        title('You🫵')
        draw.paper()
        wait(1)
        clear()
        if Computer=='stone':
            
            title('Computer💻')
            draw.stone()
            message_show.info('winer','✅your winer✅')
        if Computer=='scissor':
            
            title('Computer💻')
            draw.scissor()
            message_show.info('gameover','❌your gameover❌')
        if Computer=='paper':
          
            title('Computer💻')
            draw.paper()
            message_show.info('equal','🟰you and computer are equal🟰')
        wait(1)
        exit()
    if comb.get()=='scissor':
        
        title('You🫵')
        draw.scissor()
        wait(1)
        clear()
        if Computer=='paper':
            
            title('Computer💻')
            draw.paper()
            message_show.info('winer','✅your winer✅')
        if Computer=='stone':
            
            title('Computer💻')
            draw.stone()
            message_show.info('gameover','❌your gameover❌')
        if Computer=='scissor':
          
            title('Computer💻')
            draw.scissor()
            message_show.info('equal','🟰you and computer are equal🟰')
        wait(1)
        exit()



main.screen('select')
main.color_background(color='cyan')
lbl=lbl('I choose the ','cyan','black')
comb=comb(tk,values=select)
but=Button(tk,text='ok',bg='green',command=ok)
lbl.grid(row=0,column=0,columnspan=False)
comb.grid(row=0,column=1)
but.grid(row=1,column=1)

main.show()
