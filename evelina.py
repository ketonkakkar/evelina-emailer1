import smtplib
import os
import sys
import commands

def send_email(message, from_ad, to_ad):
    server = smtplib.SMTP('smtp.sccs.swarthmore.edu:25')
    username = '' #NOTE: Fill in if you have access to a mail server
    password = '' #NOTE: Fill in if you have access to a mail server

    server.starttls()
    server.login(username,password)
    server.sendmail(from_ad, to_ad, message)
    server.quit()

def generate_email(num, person_mappings, email_mappings, cc_name, cc_ad):
    filepath = "letters/LETTER_%d.txt" % num
    correspondence = person_mappings[num]
    from_name = correspondence[0]
    to_name = correspondence[1]
    from_ad = email_mappings[from_name]
    to_ad = email_mappings[to_name]

    with open(filepath) as fp:
        output = fp.readlines()
    setting = output[2].split(to_name.upper(), 1)
    subject = output[0].rstrip() + " -- " + setting[1]
    subject.rstrip()
    message = """From: %s <%s>
To: "%s" <%s>
Cc: "%s" <%s>
MIME-Version: 1.0
Content-type: text/html
Subject: %s
""" %(from_name, from_ad, to_name, to_ad, cc_name, cc_ad, subject)

    message += '\r\n'
    message += "<!DOCTYPE html><head>"
    message += output[0]
    message += "</head><body>"
    #message += "<p>"
    full_text = "".join(output[1:len(output) - 1])
    full_text = full_text.replace('\r\n', "<br>")
    message += full_text
    message += "</body>"
    to_ad = [to_ad] + [cc_ad]
    with open("message.txt", 'w') as fp:
        fp.write(message)
    with open("message.html", 'w') as fp:
        fp.write(message)        
    return message, from_ad, to_ad

#this function returns a dictionary mapping a letter to a sender and recipient
def letter_writers():
    list_of_lists = []
    person_mappings= {}
    h_v = [1, 3, 6, 7, 27] #Howard to Villars
    v_h =[2, 4, 5, 28, 38] #Villars to Howard
    e_v = [8, 10, 16, 25, 26, 30, 32, 36, 40, 42, 46, 47, 50, 62, 68, 75, 84] #Evelina to Villars
    v_e = [9, 15, 24, 29, 37, 39, 49, 56, 67, 73, 83] #Villars to Evelina
    h_jb = [31] #Howard to John Belmont
    jb_h = [35] #John Belmont to Howard
    e_m = [41, 57, 58] #Evelina to Mirvan
    lb_jb = [74] #Lady Belmont to John Belmont
    eic_v = [11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 23, 33, 34, 43, 44, 45, 48,
    51, 52, 53, 54, 55, 63, 64, 65, 66, 69, 70, 71, 72, 76, 77, 78, 79, 80, 81, 82] #Evelina in continuation, Villars
    eic_m = [59, 60, 61] #Evelina in continuation, Mirvin
    e_v.extend(eic_v)
    e_v.sort()
    e_m.extend(eic_m)
    e_m.sort()
    person_mappings.update(dict.fromkeys(h_v, ["Lady Howard", "Rev. Mr. Villars"]))
    person_mappings.update(dict.fromkeys(v_h, ["Mr. Villars", "Lady Howard"]))
    person_mappings.update(dict.fromkeys(e_v, ["Evelina Anville", "Rev. Mr. Villars"]))
    person_mappings.update(dict.fromkeys(v_e, ["Mr. Villars", "Evelina Anville"]))
    person_mappings.update(dict.fromkeys(h_jb, ["Lady Howard", "Sir John Belmont"]))
    person_mappings.update(dict.fromkeys(jb_h, ["Sir John Belmont", "Lady Howard"]))
    person_mappings.update(dict.fromkeys(lb_jb, ["Lady Belmont", "Sir John Belmont"]))
    email_mappings = {"Lady Howard":"lhoward1@swarthmore.edu",
    "Mr. Villars": "avillar1@swarthmore.edu",
    "Evelina Anville": "eanvill1@swarthmore.edu",
    "Rev. Mr. Villars": "avillar1@swarthmore.edu",
    "Sir John Belmont": "jbelmon1@swarthmore.edu",
    "Lady Belmont": "cbelmon1@swarthmore.edu"}
    return person_mappings, email_mappings

def parameters_from_file():
    with open("parameters.txt") as fp:
        parameters = fp.readlines()
        parameters = [item.rstrip() for item in parameters]
    return parameters

def main():
    if (len(sys.argv) >= 2):
        directory = sys.argv[1]
        os.chdir(directory)
    parameters = parameters_from_file()
    first_name = parameters[0]
    last_name = parameters[1]
    cc_name = first_name + " " + last_name
    cc_ad = parameters[2]
    with open("letter_number.txt") as fp:
       num = int(fp.readline())

    if not (1 <= num <= 84):
        print "ERROR: num out of range"
        sys.exit()
        
    person_mappings, email_mappings = letter_writers()
    message, from_ad, to_ad = generate_email(num, person_mappings, email_mappings, cc_name, cc_ad)
    #send_email(message, from_ad, to_ad) NOTE: UNCOMMENT TO SEND EMAIL
    os.remove("letter_number.txt")
    with open("letter_number.txt", 'w') as l:
        l.write(str(num +1))
         
if __name__ == "__main__": main()
