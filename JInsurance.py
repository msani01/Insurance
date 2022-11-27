#1 Write an application that allows the user to choose insurance options.
# The user can select only one of two
# insurance types—HMO (health maintenance organization) or PPO (preferred
# provider organization).
# As the user selects each option, display(print) its name and price;
# the HMO costs $200 per month, the PPO costs $600 per month. Save the file as JInsurance.py.
# Push the code to your github account
# 2. Network detector. Save the file as NetworkDetector.py
# Push your code to your github account
##Solution 

def app (name):
    print('Hello', name)
app('Sani')

insurance = ['Health Maintenance Organization (HMO)', 'Preferred Provider Organization (PPO)']
for index,option in enumerate (insurance,start=1):
    print(index,option)

b = int(input('Which of our services can we help you with! '))
if b == 1:
    print(f'Health Maintenance Organization (HMO)\nPrice = $200 per month.')
elif b == 2:
    print(f'Preferred Provider Organization (PPO)\nPrice = $600 per month.')
else:
    print('Incorrect input \nPlease try again')