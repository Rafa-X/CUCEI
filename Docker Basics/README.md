## Docker Basic App
The goal with this app is to underteand the elemental way to work with docker and apps. Creates the containers and the images using a **docker-compose** file, then displays a series of random data created with the module "Faker". <br>

This random data is from the Faker method .profile(), gets **n** characteristics that a persons profile can contain.

> [!NOTE]
> There is no need to install manually the required modules, the **Dockerfile** already does when the image is created. You can see them in the file **requirements.txt**.
<p align="center" style="margin-bottom: 0px !important;">
  <img width="550"  src="images/dockerfile.png" align="center">
</p>


1. To create the container and the image of the project there are no need to execute a bunch of commands, just run the **docker-compose** file:
<p align="center" style="margin-bottom: 0px !important;">
  <img width="150"  src="images/command1.png" align="center">
</p>
<br>
<p align="center" style="margin-bottom: 0px !important;">
  <img width="600"  src="images/docker_compose.png" align="center">
</p>

2. The service only runs locally, as specified in the **docker-compose** file, the faker service runs in the port **3000**:
<p align="center" style="margin-bottom: 0px !important;">
  <img width="400"  src="images/port_faker.png" align="center">
</p>

3. And the port to access the functions on the web browser is the **5000**:  (while the port of the container is also the 3000)
<p align="center" style="margin-bottom: 0px !important;">
  <img width="400"  src="images/port_web.png" align="center">
</p>
