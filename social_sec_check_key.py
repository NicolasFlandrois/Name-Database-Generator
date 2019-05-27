#!usr/bin/python3.7
# Date: Mon 27 May 2019 09:24:24 CEST 
# Author: Nicolas Flandrois
# Description: Script checking french social security identification number, 
# checking the control key (last 2 digits)

ss =int(
	input(
		"""Please type the social security number, without the control key: """)
	)

a = int(97-(ss-((round((ss/97), 0))*97)))
print("The control key is: ", a)