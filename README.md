
# Basquiat_Style_GAN
   The project is about using Deep Learning techniques to generate art work in the style of painter Jean-Michel Basquiat. The Generative Adversarial Network (GAN) technique allows us to obtain a first set of output with the Basquiat’s typical content (choice of colours, distribution of colours). This first output is far from satisfactory because it is limited by the constraints often faced by GANs. The resolution is inadequate, and the Basquiat’s style is absent. In order to overcome these constraints, we applied a super resolution algorithm and then created an artistic style transfer algorithm. The result is a new, original piece with satisfactory resolution and that displays the content and style typical of Basquiat’s art work. This is a novel approach in Deep Learning applied to paintings. Other approaches mix the work of multiple painters in the dataset and thus don’t need to capture the particular style of an artist. 

----------------------------------------------------------
The colab file is located here : <br /> https://drive.google.com/open?id=11aK1sfjuXd3WXtReqb7ICdFdpxjGT89a
----------------------------------------------------------
--------------
# |File system |
--------------
![Process of the file](https://drive.google.com/open?id=1SjOn_FdTU6NbAYvWyJ9wxsW6ij1yOc17)
- Data_Augmentation.py 
This file takes 76 image-inputs from net scraping function. Then doing augmentation process inorder to get 523 images<br />
	- input : Data1<br />
	- output : Data 2<br />
- Resize.py and 
The file reshapes multiple-size images from the Data2 into 500x420 Data3A<br />
	- input : Data2<br />
	- output : Data3A<br />
- (1)Basquiat_GAN.ipynb<br />
The GAN method learns input from Data3A and generate around 500 images for Data4<br />
	- input : Data3A/1<br />
	- output : Data4<br />
- (2)resize_and_superres.ipynb<br />
This process samples 5 images from the range of image number 450 to 500<br />
	<<resize part >> Resize the image to 512x512 pixels<br />
	- input : Data4<br />
	- output : Data4_resize<br />
	<<super resolution part >> Highen th picture resolution by 10 iterations<br />
	The file work in the enhancenet_pretrained folder.<br />
	- input : Data4_resize<br />
	- output : Data5 // 5 images with 500x420 pixels<br />
- (3)Artistic_Style.ipynb<br />
	Generate the new image as a combination of each image from Data5 with 4 style image from Data1/Data1_Style<br />
	- input : Data5<br />
	- output : Data6 // 20 images with 500x420 pixels <br />
(4)Data_Selection_with_GANDis.ipynb<br />
	This file use the discriminator model, which trained from (1)Basquiat_GAN.ipynb of 450 to 500 iterations, to choose the most Basquiat-liked picture.<br />
	- input : Data6<br />
	- output : Data7 // 1 image with 500x420 pixels<br />
----------------------------------------------------------
# Credit 

- Data super resolution : 
	<p>EnhanceNet
	Single Image Super-Resolution
	Through Automated Texture Synthesis
		Max-Planck Instite for Intelligent Systems
		Spemanstr. 34, 72076 Tübingen, Germany   </p>
	[link](https://webdav.tuebingen.mpg.de/pixel/enhancenet/?fbclid=IwAR1nttfTyG2pgpwHuo31qgDxIQEbB-MBFCV1k6ms23Arwz2Nbv8ZikY2x-E)
- Artistic style transfer :
	<p>Thanks to Mr. Harish Narayanan
	Follow the original git here :  </p> [Github](https://github.com/hnarayanan/artistic-style-transfer/blob/master/notebooks/6_Artistic_style_transfer_with_a_repurposed_VGG_Net_16.ipynb)  

---------------------------------------------------------
**** Additional ****<br />
-- The discriminator for the data _selection part could be choosen in the folder 'model'. The graph images are considered for the number of model.The number of model between 450-500 is reccommend<br />
-- The online colab source code  will be available until 2021. <br />

Writer : 
- Kunch Ringrod 58070501105
- Augustin Morieux 62540460024 <br />
King Mongkut's University of Technology Thonburi (Thailand) <br />
Updated on 11/25/2019 11.00 pm.
 
