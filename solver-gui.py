import tkinter as tk
from tkinter.ttk import Button, Entry


def set_grid(element, row, column, sticky, padx, pady):
    element.grid(row = row, column = column, sticky = sticky, padx = padx, pady = pady)

class Entry_Element():
    def __init__(self, master, width, content):
        self.element = tk.Entry(master, width = width, textvariable = content, )

class Button_Element():
    def init_button(self, master, text, command, padx, pady):
        self.button_elem = tk.Button(master, text = text, command = command, padx=padx, pady=pady)

class Label_Element():
    def __init__(self, master, text):
        self.element = tk.Label(master = master, text = text)

class Text_Element():
    def __init__(self, master, width = 15, height = 15):
        self.element = tk.Text(master = master, width = width, height = height)

class Scroll_Element():
    def __init__(self, master, orient, command):
        self.element = tk.Scrollbar(master, orient = orient, command = command)

class Text_Scrollbar_Element():
    def __init__(self, master, width, height, orient):
        self.text_elem = Text_Element(master = master, width = width, height = height)
        self.scroll_elem = Scroll_Element(master = master, orient = orient, command = self.text_elem.element.yview)
        self.text_elem.element['yscrollcommand'] = self.scroll_elem.element.set

class Label_Entry_Element(Label_Element, Entry_Element):
    def __init__(self, master, text, width, content):
        self.input_elem = Entry_Element(master, width, content)
        self.label_elem = Label_Element(master, text)

class Frame():
    def __init__(self, window):
        def solve(*args):
            # a bit hacky, but this works.
            import re
            word_list = []
            fixed_letter_input = fixed_letters.get()
            floating_letters_input = floating_letters.get()

            #Clear the answers field
            text_area.text_elem.element.delete(1.0, 'end')

            with open("words.txt", 'r') as final_word_list:
                word_list = final_word_list.readlines()

            word_len = len(word_list[0]) #get length of first word in word list. This assumes all words have same length.

            #Validate Answers
            if (len(fixed_letter_input) == 0):
                text_area.text_elem.element.insert('end', "[NOTE] Fixed letters empty. Assuming no fixed letters. \n")
            if (((len(fixed_letter_input) != word_len and len(fixed_letter_input) != 0) or len(floating_letters_input) > word_len)):
                text_area.text_elem.element.insert('end', "[ERROR] Recheck the lengths of your letters. \n")


            #First do the fixed letters. If fixed is empty, we do nothing and proceed to floating.
            if fixed_letters:
                fixed = fixed_letter_input.replace("*",".")
                pattern = re.compile(fixed)
                word_list = list(filter(pattern.match,word_list))
            
            #From word_list, we now have to make sure that ALL our floating characters exist for each word. Current implementation means keeping only words with a specific letter
            #in a loop.
            if floating_letters:
                for character in floating_letters_input:
                    pattern = re.compile(character)
                    word_list = list(filter(pattern.search,word_list))

            if banned_letters:
                for word in word_list:
                    for letter in word:
                        if letter in banned_letters.get():
                            break
                    else:
                        text_area.text_elem.element.insert('end', word)
            else:
                for word in word_list:
                    text_area.text_elem.element.insert('end', word)

            #return word_list

        self.frame = tk.Frame(window)
        self.frame.grid(column=0,row=0,padx=10)

        floating_letters = tk.StringVar()
        floating =  Label_Entry_Element(self.frame, "Floating Letters\nFormat: abcde", 15, floating_letters)
        set_grid(floating.input_elem.element, 0, 1, 'w', 10, 3)
        set_grid(floating.label_elem.element, 0, 0, 'e', 10, 3)

        fixed_letters = tk.StringVar()
        fixed = Label_Entry_Element(self.frame, "Fixed Letters\nFormat: **a*c", 15, fixed_letters)
        set_grid(fixed.input_elem.element, 1, 1, 'w', 10, 3)
        set_grid(fixed.label_elem.element, 1, 0, 'e', 10, 3)

        banned_letters = tk.StringVar()
        banned = Label_Entry_Element(self.frame, "Wrong Letters\nFormat: abcdef\n(Optional, Slower)", 15, banned_letters)
        set_grid(banned.input_elem.element, 2, 1, 'w', 10, 3)
        set_grid(banned.label_elem.element, 2, 0, 'e', 10, 3)

        solve_button = Button_Element()
        solve_button.init_button(self.frame, "Solve", solve, 25, 0)
        set_grid(solve_button.button_elem, 3, 1, 'n', 10, 3)

        text_area = Text_Scrollbar_Element(self.frame, 40, 5, 'vertical')
        set_grid(text_area.text_elem.element, 0, 2, tk.N + tk.S, 0, 3)
        text_area.text_elem.element.grid(rowspan = 3)
        set_grid(text_area.scroll_elem.element, 0, 3, 'ns', 0, 3)
        text_area.scroll_elem.element.grid(rowspan = 3)

class MainWindow():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Wordle-like Solver GUI")


if __name__ == "__main__":
    main_window = MainWindow()
    """ window = tk.Tk()
    window.title("Wordle-like Solver GUI") """

    main_frame = Frame(main_window.window)


    main_window.window.mainloop()