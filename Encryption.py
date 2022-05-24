from tkinter import *
from tkinter import ttk, font
from tkinter import messagebox


def create_window(evt):
    global morse
    global ar
    global cf
    print(evt)

    if code.get() == codes[0]:
        morse = Toplevel(window)
        morse.title("Coding and Decoding Morse")
        morse.minsize(300, 250)

        window.withdraw()

        code_morse_dico = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                           'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                           'S': '...',
                           'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                           'e': '.',
                           'f': '..-.', 'g': '--.', 'h': '....',
                           'i': '..', 'j': '.---', 'k': '-.-',
                           'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
                           's': '...',
                           't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
                           'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-',
                           '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
                           '?': '..--..',
                           '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-'}

        def morse_latin(phrase):
            phrase += ' '
            decode = ''
            citext = ''
            for letter in phrase:
                if letter != ' ':
                    i = 0
                    citext += letter
                else:
                    i += 1
                    if i == 2:
                        decode += ' '
                    else:
                        decode += list(code_morse_dico.keys())[list(code_morse_dico.values()).index(citext)]
                        citext = ''
            return decode

        def latin_morse(phrase):
            code = ''
            for letter in phrase:
                if letter != ' ':
                    code += code_morse_dico[letter] + ' '
                else:
                    code += ' '

            return code

        def back(old, new):
            old.deiconify()
            new.destroy()

        phrase = StringVar()
        choice = IntVar()
        result = StringVar()

        frame1m = ttk.Frame(morse, padding=20)
        frame1m.grid()
        frame2m = ttk.Labelframe(morse, text='Choose an option', padding=20)
        frame2m.grid()

        Label(frame1m, text="Morse Code", font='helvetica 14', foreground='blue').grid()
        Entry(frame1m, textvariable=phrase, width=50).grid(padx=20, pady=10)

        codm = ttk.Radiobutton(frame2m, text="Code", variable=choice, value=0).grid()
        decodm = ttk.Radiobutton(frame2m, text="Decode", variable=choice, value=1).grid()
        Label(morse, textvariable=result, font='helvetica 16').grid()
        Button(morse, text='Code/Decode', width=12, font=("Verdana", 12),
               command=lambda: result.set(latin_morse(phrase.get())) if choice.get() == 0
               else result.set(morse_latin(phrase.get()))).grid()
        Button(morse, text='Back', width=12, font=("Verdana", 12),
               command=lambda: back(window, morse)).grid(padx=5, pady=10)



    elif code.get() == codes[1]:
        ar = Toplevel(window)
        ar.title("coding and decoding reverse alphabet")
        ar.minsize(500, 300)

        window.withdraw()

        alph = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
                'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
                'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a', 'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W',
                'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M',
                'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C',
                'Y': 'B', 'Z': 'A'}

        def alphabetInv():
            x = chainar.get()
            i = 0
            ch = ""
            alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for l in x:
                if (l in alphabet) == False:
                    ch = ch + l
                    chainfar.set(ch)
                else:
                    ch = ch + alph[l]
                    chainfar.set(ch)

        def errorboxar():
            messagebox.showerror('Error',
                                 "coding and decoding \nreverse alphabet have\n the same result")

        def returnar():
            ar.destroy()
            window.deiconify()

        chainar = StringVar()
        chainfar = StringVar()

        frame1ar = ttk.Frame(ar, padding=20)
        frame1ar.grid()
        frame3ar = ttk.Labelframe(ar, text='Choisir une option', padding=20)
        frame3ar.grid()
        frame2ar = ttk.Frame(ar, padding=20)
        frame2ar.grid()

        chainar_entry = ttk.Entry(frame1ar, textvariable=chainar)
        chainar_label = ttk.Label(frame1ar)
        transar_button = ttk.Button(frame2ar, text="code/Decode", command=alphabetInv)
        resultatar_label = ttk.Label(frame2ar, textvariable=chainfar, font='helvetica 16')
        returnar_button = ttk.Button(frame2ar, text="return", command=returnar)
        phrasear_label = ttk.Label(frame2ar, text='Result:')
        coding_rdbutton = ttk.Radiobutton(frame3ar, text='coding', command=errorboxar)
        decoding_rdbutton = ttk.Radiobutton(frame3ar, text='Decoding', command=errorboxar)

        chainar_label.grid(row=0, column=0, padx=10, pady=20)
        chainar_entry.grid(row=0, column=1, padx=10)
        transar_button.grid(row=1, column=1, padx=10)
        resultatar_label.grid(row=1, column=2, padx=10)
        returnar_button.grid(row=2, column=2, padx=10, pady=10)
        phrasear_label.grid(row=0, column=2, padx=10, pady=10)
        coding_rdbutton.grid(row=1, column=0)
        decoding_rdbutton.grid(row=2, column=0)

    elif code.get() == codes[2]:
        cf = Toplevel(window)
        cf.title("coding and decoding Caeser")
        cf.minsize(500, 300)

        window.withdraw()

        def afficherResultat():
            if choice.get() == 1:
                chainCod = chain.get()
                ch = ''
                cle = cleVar.get()
                alphabet = "abcdefghijklmnopqrstuvwxyz"
                j = 0
                for x in chainCod:

                    if x in alphabet.upper():
                        i = 0
                        alphabetmaj = alphabet.upper()
                        while i < 26:
                            if x == alphabetmaj[i] and i < 26 - cle:
                                ch = ch + alphabetmaj[i + cle]
                            if x == alphabetmaj[i] and i >= 26 - cle:
                                ch = ch + alphabetmaj[j]
                                j += 1
                            i += 1

                    elif (x in alphabet) == False:
                        ch = ch + x

                    else:
                        i = 0
                        while i < 26:
                            if x == alphabet[i] and i < 26 - cle:
                                ch = ch + alphabet[i + cle]
                            if x == alphabet[i] and i >= 26 - cle:
                                ch = ch + alphabet[j]
                                j += 1
                            i += 1
                chainf.set(ch)
            if choice.get() == 0:
                chainDecod = chain.get()
                ch = ''
                cle = cleVar.get()
                alphabet = "abcdefghijklmnopqrstuvwxyz"
                for x in chainDecod:
                    if x in alphabet.upper():
                        alphabetmaj = alphabet.upper()
                        i = 0
                        while i < 26:
                            if x == alphabetmaj[i]:
                                ch = ch + alphabetmaj[i - cle]
                            i += 1
                    elif (x in alphabet) == False:
                        ch = ch + x

                    else:
                        i = 0
                        while i < 26:
                            if x == alphabet[i]:
                                ch = ch + alphabet[i - cle]
                            i += 1
                chainf.set(ch)

        def returncf():
            cf.destroy()
            window.deiconify()

        chain = StringVar()
        chainf = StringVar()
        choice = IntVar()
        cleVar = IntVar()

        frame1cf = ttk.Frame(cf, padding=20)
        frame1cf.grid()
        frame2cf = ttk.Labelframe(cf, text='Choose an option', padding=20)
        frame2cf.grid()
        frame3cf = ttk.Frame(cf, padding=20)
        frame3cf.grid()

        cle_entry = ttk.Entry(frame1cf, textvariable=cleVar)
        cle_label = ttk.Label(frame1cf, text="Key: ")
        chain_entry = ttk.Entry(frame1cf, textvariable=chain)
        chain_label = ttk.Label(frame1cf, text="Chain: ")
        trans_button = ttk.Button(frame3cf, text="Code/Decode", command=afficherResultat)
        resultat_label = ttk.Label(frame3cf, textvariable=chainf, font='helvetica 14')
        return_button = ttk.Button(frame3cf, text="Back", command=returncf)

        codingRdb = ttk.Radiobutton(frame2cf, text='Coding ', variable=choice, value=1)
        decodingRdb = ttk.Radiobutton(frame2cf, text='Decoding', variable=choice, value=0)
        choice.set(1)

        chain_label.grid(row=0, column=0, padx=10, pady=10)
        chain_entry.grid(row=0, column=1, padx=10, pady=10)
        cle_label.grid(row=1, column=0, padx=10)
        cle_entry.grid(row=1, column=1, padx=10)
        trans_button.grid(row=1, column=1, padx=10)
        resultat_label.grid(row=1, column=2, padx=10)
        return_button.grid(row=2, column=2, padx=10)
        codingRdb.grid(row=1, column=0, padx=10)
        decodingRdb.grid(row=2, column=0, padx=10)


window = Tk()
window.minsize(300, 200)
window.title("Encryption")

morse = None
ar = None
cf = None

code = StringVar()

label1 = ttk.Label(window, text="Welcome", font='Helvetica 18', foreground='red')
label1.grid(pady=10)

label2 = ttk.Label(window, text="   Choose which function you want to use", font='Helvetica 12',
                   foreground='blue')
label2.grid(pady=10)

codes = ["Morse", "Alphabet Reverse", "Caesar's Cipher"]
combobox = ttk.Combobox(window, value=codes, textvariable=code, state='readonly')
combobox.bind('<<ComboboxSelected>>', create_window)
combobox.grid(pady=10)

close = ttk.Button(text='Quit', command=window.destroy)
close.grid(pady=10)

window.mainloop()