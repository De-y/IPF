import os, socket, geocoder, time
from requests import get

print(
  "Hello there! I am currently grabbing some information about your computer, please wait on stand-by while I do so."
)
host_name = socket.gethostname()
IP = socket.gethostbyname(host_name)
print('Your local IP Address is: ' + IP)
ip = get('https://api.ipify.org').content.decode('utf8')
print('Your public IP address is: {}'.format(ip))

g = geocoder.ip('me')
time.sleep(0.5)
print('SENDING IP ADDRESS TO COMMAND AND CONTROL SERVER...')
time.sleep(0.9)
print(
  f'SUCCESSFULLY SENT! I am currently setting up a site containing your ip address, which your local address will point; I am also sending your location back to the command and control server, which is: {g.latlng}'
)
time.sleep(2.4)
print(
  'Finished! The domain that I set up is at https://t-mobils.cf\n\nVisit it or I will send all this information to the FIB >:)'
)
input('Press Enter to continue.\n')

time.sleep(3)
print("Alright. Have a good day!")
time.sleep(2)