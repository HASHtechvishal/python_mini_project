from plyer import notification
import time


if __name__=="__main__": #separate  your code	
    while True:    
	    notification.notify(
			title = "****** Take rest ******",
			message=" rest HERE" ,
			#app_icon="image path",
            app_icon = None,
			# displaying time
			timeout=5)
		# waiting time
time.sleep(60*60)

#pythonw filename.py it run in background