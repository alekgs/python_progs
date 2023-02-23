from time import sleep
# from progress.bar import PixelBar
# from tqdm import tqdm
from alive_progress import alive_bar
# import PySimpleGUI as sg

# mylist = [i for i in range(100)]
mylist = ['123233.txt', '78253233.txt', '98833.txt', '546733.txt', '887651.txt', '112.txt', '00347347.txt']

# # Define the window's contents
# layout = [[sg.Text("What's your name?")],  # Part 2 - The Layout
#           [sg.Input()],
#           [sg.Button('Ok')]]
#
# # Create the window
# window = sg.Window('Window Title', layout)  # Part 3 - Window Defintion
#
# # Display and interact with the Window
# event, values = window.read()  # Part 4 - Event loop or Window.read call
#
# # Do something with the information gathered
# print('Hello', values[0], "! Thanks for trying PySimpleGUI")
#
# # Finish up by removing from the screen
# window.close()  # Part 5 - Close the Window

# bar
# ('smooth', 'classic', 'classic2', 'brackets', 'blocks', 'bubbles', 'solid', # 'checks',
# 'circles', 'squares', 'halloween', 'filling', 'notes', 'ruler', 'ruler2', 'fish', 'scuba')

# spinners
# ('classic', 'stars', 'twirl', 'twirls', 'horizontal', 'vertical', 'waves', 'waves2', 'waves3', 'dots',
# 'dots_waves', 'dots_waves2', 'it', 'ball_belt', 'balls_belt', 'triangles', 'brackets', 'bubbles', 'circles',
# 'squares', 'flowers', 'elements', 'loving', 'notes', 'notes2', 'arrow', 'arrows', 'arrows2', 'arrows_in',
# 'arrows_out', 'radioactive', 'boat', 'fish', 'fish2', 'fishes', 'crab', 'frank', 'wait', 'wait2', 'wait3', 'pulse')

# letters = [chr(ord('A') + x) for x in range(26)]
# with alive_bar(26, title='Alphabet', force_tty=True) as bar:
#     for c in letters:
#         bar.title = f'letter: {c}'
#         sleep(0.3)
#         bar()


with alive_bar(len(mylist), force_tty=True, dual_line=True, title='Processing', bar='smooth', stats=None, ) as bar:
    for i in mylist:
        bar.title(i)
        sleep(.25)
        bar()
    bar.title('Done')

#


# from tqdm import tqdm
# for i in tqdm(mylist):
#     time.sleep(0.1)

# from alive_progress import alive_bar
#
# for total in 5000, 7000, 4000, 0:
#     with alive_bar(total) as bar:
#         for i in range(5000):
#             time.sleep(0.001)
#             bar()

# from tqdm import tqdm
# from time import sleep
#
# # оборачиваем итератор range(100) классом tqdm()
# for i in tqdm(mylist, ncols=80, ascii=False, desc='Total'):
#     tqdm.write(str(i))
#     sleep(0.1)
