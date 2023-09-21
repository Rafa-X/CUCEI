## Service - Application Blocker

This Windows service 
[**proc_blocker.py**](https://github.com/Rafa-X/CUCEI-Tolerante-a-fallas/blob/main/Windows%20Services/custom_services/proc_blocker.py) checks apps status and block specified apps, using the psutil library in Python and the NSSM for the installation.

When the service is installed there is needed to specify the names of the objective apps, those are saved in a list of **targets**.
<p align="center" style="margin-bottom: 0px !important;">
    <img width=70% src="../Images/WinService part 1.png" align="center">
</p>

When an app is opened, an executable is called and the service catch the name of it, here is where the comparison happens. Using a psutil method called .process_iter which returns an iterator yielding a process class instances for all the running processes, this is compared to the **targets** list checking if there is an app to block.
<p align="center" style="margin-bottom: 0px !important;">
    <img width=70% src="../Images/WinService part 2.png" align="center">
</p>

And in the main function first asks for the arguments, specified when the service is installed, then saves it in the list **targets**, when an executable is called the service gets its name and evaluates if its one to block or just one to let it run.
<p align="center" style="margin-bottom: 0px !important;">
    <img width=70% src="../Images/WinService part 3.png" align="center">
</p>


## Steps
1. The first step is to create the application we want to deploy as a service, in this case the app blocker [**proc_blocker.py**](https://github.com/Rafa-X/CUCEI-Tolerante-a-fallas/blob/main/Windows%20Services/custom_services/proc_blocker.py).

2. For the app to be installed I used this free tool called [**NSSM - Non-Sucking Service Manager**](https://nssm.cc/), this allows us to install, start, stop and unistall Windows services through an interface with several tools for setting up the service.
   
3. Move the app file and the NSSM executable in the same folder of the root directory. In my case will be: *C:\custom_services\*.

4. Now in a console as administrator run the NSSM and begin the installation of the service:
    <p align="center" style="margin-bottom: 0px !important;">
        <img width="400"  src="../Images/NSSM cmd.png" align="center">
    </p>
    and this, the NSSM installation form will open:
    <p align="center" style="margin-bottom: 0px !important;">
        <img width="400" src="../Images/NSSM form.png" align="center">
    </p>

5. Now for the setting up of the service in the form, it's needed to specify 3 things:
   - **Path**: Indicates the directory of the Python interpreter.
   - **Startup directory**: Indicates the directory in which is located the service code. In my case: C:\custom_services\ 
   - **Arguments**: Name of the executables to block, for example: proclocker.py chrome.exe firefox.exe.

   <p align="center" style="margin-bottom: 0px !important;">
       <img width="400" src="../Images/NSSM form filled.png" align="center">
   </p>

6. Then just push **install service** and restart the computer, the service will run automatically.
7. To stop/remove the service just run this commands in a console in the folder of the service:
   <p align="center" style="margin-bottom: 0px !important;">
       <img src="../Images/remove proc.png" align="center">
   </p>
