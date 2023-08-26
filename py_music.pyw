# Importing all the necessary modules
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import pygame.mixer as mixer        # pip install pygame
import os
import tkinter
import tkinter.messagebox
import pygame

#note i like to comment out unused commands and leave them there.
def music_player():
    mixer.init()

    # Play, Stop, Load and Pause & Resume functions
    def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
        try:
            song_name.set(songs_list.get(ACTIVE))

            mixer.music.load(songs_list.get(ACTIVE))
            mixer.music.play()

            status.set("Song PLAYING")
        except pygame.error as exc:
            tkinter.messagebox.showerror(title="Error: No file found.", message="No such file exists or your file is not in mp3, ogg, or wav format.")

    def keep_playing(song_name: StringVar, songs_list: Listbox, status: StringVar):
        for song in songs_list:
            mixer.music.load(song)
            mixer.music.play()

    def stop_song(status: StringVar):
        mixer.music.stop()
        status.set("Song STOPPED")


    def load(listbox):
        tkinter.messagebox.showinfo(title="Usage", message="Open a folder with all your music inside; open a playlist. (no zip)")
        os.chdir(filedialog.askdirectory(title='Open a song folder'))
        
        tracks = os.listdir()

        for track in tracks:
            listbox.insert(END, track)
            

    def onefile_load(listbox):
        # os.(filedialog.askopenfile(title="Open a individual file."))
        file = askopenfilename(filetypes =[('Waveform Audio File Format', '*.wav'), ('Ogg Vorbis Audio File', '*.ogg'), ('MPEG-1 Audio Layer 3', '*.mp3')])
        if file is not None:
            listbox.insert(END, file)
        else:
            tkinter.messagebox.showerror(title="No file", message="You did not provide a valid file.")
    def clear_playlist(listbox):
        tracks = os.listdir()
        for track in tracks:
            listbox.remove(END, track)
    def pause_song(status: StringVar):
        mixer.music.pause()
        status.set("Song PAUSED")


    def resume_song(status: StringVar):

        mixer.music.unpause()
        status.set("Song RESUMED")


    # Creating the master GUI
    root = Tk()
    root.geometry('1200x700')     #this is a comment
    root.title('PyMusic: By TheSpikyHedgehog')
    root.resizable(0, 0)

    # All the frames
    song_frame = LabelFrame(root, text='Current Song', bg='LightBlue', width=900, height=580)
    song_frame.place(x=0, y=0)

    button_frame = LabelFrame(root, text='Control Buttons', bg='LightBlue', width=900, height=620)
    button_frame.place(y=80)

    listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue')
    listbox_frame.place(x=550, y=0, height=700, width=650)

    # All StringVar variables
    current_song = StringVar(root, value='<Not selected>')

    song_status = StringVar(root, value='<Not Available>')

    # Playlist ListBox
    playlist = Listbox(listbox_frame, font=('Lucida-Grande', 11), selectbackground='Gold')

    scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
    scroll_bar.pack(side=RIGHT, fill=BOTH)

    playlist.config(yscrollcommand=scroll_bar.set)

    scroll_bar.config(command=playlist.yview)

    playlist.pack(fill=BOTH, padx=5, pady=10)

    # SongFrame Labels
    Label(song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)

    song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25)
    song_lbl.place(x=150, y=20)

    # Buttons in the main screen
    pause_btn = Button(button_frame, text='Pause', bg='Aqua', font=("monospace", 14), width=7,
                        command=lambda: pause_song(song_status))
    pause_btn.place(x=15, y=10)

    stop_btn = Button(button_frame, text='Stop', bg='Aqua', font=("monospace", 14), width=7,
                    command=lambda: stop_song(song_status))
    stop_btn.place(x=105, y=10)

    play_btn = Button(button_frame, text='Play', bg='Aqua', font=("monospace", 14), width=7,
                    command=lambda: play_song(current_song, playlist, song_status))
    play_btn.place(x=195, y=10)

    resume_btn = Button(button_frame, text='Resume', bg='Aqua', font=("monospace", 14), width=7,
                        command=lambda: resume_song(song_status))
    resume_btn.place(x=285, y=10)

    load_btn = Button(button_frame, text='Load Song From Playlist', bg='Gold', font=("monospace", 14), width=35,
                    command=lambda: load(playlist))
    load_btn.place(x=10, y=55)

    onefile_load_btn = Button(button_frame, text='Load Song Onefile', bg='Gold', font=("monospace", 14), width=35, command=lambda: onefile_load(playlist))
    onefile_load_btn.place(x=10, y = 90)

    # Label at the bottom that displays the state of the music
    Label(root, textvariable=song_status, bg='SteelBlue', font=('Times', 9), justify=LEFT).pack(side=BOTTOM, fill=X)

    root.update()
    root.mainloop()
music_player()
