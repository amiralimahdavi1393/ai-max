import speech_recognition as sr
import pyautogui as p
import turtle as t
import time as ti

name='مکس'
exit_command=['خروج','خارج','تموم','بیرون','خاموش','پایان']
prev_command=['قبلی','قبل','عقب','قبلیه']
next_command=['بعدی','جدید','خوب نیست']
play_command=['پلی','شروع','استارت','حرکت','پخش']
stop_command=['استوپ','استاپ','توقّف','وایستا','واستا']
sound_command=['آهنگ','آهنگ','صدا','موسیقی','موزیک']
mute_command=['میوت','ببند','ساکت','سکوت']
sound_vol_down=['کم','پایین']
sound_vol_up=['بالا','زیاد']
shot=p.screenshot()


light_up=['بالا','زیاد']
light_down=['کم','پایین']

game_command=['بازی','گیم','سرگرمی']













def voice():
    while True:
        r=sr.Recognizer()

        mic=sr.Microphone(device_index=1)
        
        try:
            with mic as s:
                a=r.listen(s)
                command=r.recognize_google(a,language='fa-IR').lower()
                if name in command:
                    if 'بکش' in command:
                        if 'دایره' in command:
                            t.circle(50)
                            ti.sleep(0.2)
                            exit()
                    elif 'سلام' in command:
                        print('hello amirali')
                    elif any(item in command for item in  exit_command):
                        print('ok')
                        ti.sleep(0.2)
                        exit()
                    elif any(nexter in command for nexter in next_command):
                        print('next...')
                        ti.sleep(0.2)
                        p.press('nexttrack')
                    elif any(prev in command for prev in prev_command):
                        print('prev...')
                        ti.sleep(0.2)
                        p.press('prevtrack')
                    elif any(stop in command for stop in stop_command):
                        print('stop...')
                        ti.sleep(0.2)
                        p.press('playpause')
                    elif any(play in command for play in play_command):
                        print('play...')
                        ti.sleep(0.2)
                        p.press('playpause')
                    elif any(music in command for music in sound_command):
                        if any(mute in command for mute in mute_command):
                            print('muting...')
                            ti.sleep(0.2)
                            p.prees('f1')
                        elif any(up in command for up in sound_vol_up):
                            print('maxing sound...')
                            ti.sleep(0.2)
                            p.prees('f3',presses=10)


                        elif any(down in command for down in sound_vol_down):
                            print('lowing sound...')
                            ti.sleep(0.2)
                            p.prees('f2',presses=10)
                    elif 'نور' in command:
                        if any(item in command for item in light_up):
                            print('ok')
                            ti.sleep(0.2)
                            p.press('f6',presses=5)
                        elif any(item in command for item in light_down):
                            print('ok')
                            ti.sleep(0.2)
                            p.press('f5',presses=5)
                    elif 'اسکرین شات' in command or 'عکس از صفحه' in command:
                        print('screenshot...')
                        shot.save('screenshot_AI.png')
                        print('ok')
                    elif any(item in command for item in game_command):
                        import game
            
        except Exception as e:
            print('بنال دیگه')
            r=sr.Recognizer()
            continue
voice()







