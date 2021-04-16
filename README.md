A program that renders the 18th century epistolary novel _Evelina_ as a series of email exchanges between characters that you are cc'd on.

Powered by the Swarthmore College Computer Society (SCCS)'s mail server, which can only be used locally. To use this program, you need access to a mail server. For the time being, I will run the progam locally on SCCS's server, and to use the program without having access to a mail server, email me at kkakkar1 [at] swarthmore [dot] edu, and I will run it with your address. The code on this repository is the same as I will run, except with the server login information omitted.

This is an inelegant solution, and I am working to find a better one.

If you run it currently, the program will save two files in your working directory, 'message.txt' and 'message.html'. These are two different file formats of the message that would get emailed to you if the send_email function were uncommented. If you have access to a mail server, follow the instructions in the "NOTE" comments. 

This program is adaptable; feel free to play around with some of the functions.

Run with Python version 2.7.11

## About 
The epistolary novel is a novel represented in a series of letters. When thinking about Habermas's _Structural Transformation of the Public Sphere_ (1962) and what a modern day form of epistolarity is, I think of email, and how much of our routine correspondence occurs over it. Also, in light of Benedict Anderson's _Imagined Communities_ (1983), this email sender both aims to capture a serialized form of reading a novel. Much of the way we consume news in the present is in our email inboxes, (think daily updates from _The Times_).


## One usage (one letter a day)
 The primary way to use this program is to automate the sending of emails in the form of a cronjob. 

First:

In the command line, 'cd' into the directory you've saved the downloaded files in. Then, in the command line type:

```python create_letters.py```

This will generate a series of letters from the novel Evelina and store them in a subfolder called 'letters'.

Next:

Enter 'crontab -e' in the command line. This will open a file in the text editor Vim.

Paste the following line into the open file:

```30 14 * * * python [directory]/evelina.py [directory]```

where [directory] is the file path in which you have saved 'evelina.py'

Add a new line below the one you just inserted and save the file and exit ('esc' then ':wq' in vim).

The above line of code will call the file 'evelina.py' once a day at 14:30 (2:30 pm). You can edit the '30' and the '14' to change the time of day at which the letter sends. Look up: 'crontab usage' for more info. 

Next: edit the 'paramters.txt' file to contain the following information in the same format as is currently present in the file. Each should have it's own line. 

Firstname

Lastname

Email

Last: edit the file 'letter_number.txt' to contain (on the first line) the number of the letter you'd like to send first (it is 1 by default, because you'd start the novel at the first letter). 

## Alternate Usage (single letter)

If you want to just send a single letter to your email.

Run:

```create_letters.py```

Then:

Keep the 'parameters.txt' file the same way as you would in the above usage. 

Change 'letter_number.txt' to contain the number of the letter you would like to send. 

Don't make a cron job.

In your working directory, run:

```python evelina.py```

**note, the program is structured such that evelina.py is in the same folder as other files it calls on.**
>This will be the case by default, so be careful about alterations. 

Also, due to the spam filtering of most email clients, check your spam folder for the emails.

I have checked for some errors, but the error checking is not robust. Please contact me at ketonkakkar@gmail.com if you run into issues. 

Cheers,

Keton
