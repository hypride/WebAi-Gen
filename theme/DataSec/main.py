import time
import requests
import wget
import os
from zipfile import ZipFile


location = os.getcwd()

thecode = '''<!doctype html>
<html lang="en">
<head>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="icon" href="images/favicon.png" type="image/png">
<title>Satner Portfolio</title>

<link rel="stylesheet" href="css/bootstrap.css">
<link rel="stylesheet" href="css/style_1.css">
<link rel="stylesheet" href="css/font-awesome.min.css">
<link rel="stylesheet" href="css/owl.carousel.min.css">
<link rel="stylesheet" href="css/magnific-popup.css">
<link rel="stylesheet" href="css/nice-select.css">

<link rel="stylesheet" href="css/style.css">
</head>
<body>

<header class="header_area">
<div class="main_menu">
<nav class="navbar navbar-expand-lg navbar-light">
<div class="container">

<a class="navbar-brand logo_h" href="index.html"><h1 style="color: #7c50eb;"><|YOUR_NAME|></h1></a>
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>

<div class="collapse navbar-collapse offset" id="navbarSupportedContent">
<ul class="nav navbar-nav menu_nav justify-content-end">
<li class="nav-item active"><a class="nav-link" href="#home">Home</a></li>
<li class="nav-item"><a class="nav-link" href="#about">About</a></li>
<li class="nav-item"><a class="nav-link" href="#service">Services</a></li>
<li class="nav-item"><a class="nav-link" href="#test">testimonial</a></li>

</li>
<li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
</ul>
</div>
</div>
</nav>
</div>
</header>


<section class="home_banner_area" id="home">
<div class="banner_inner">
<div class="container">
<div class="row">
<div class="col-lg-7">
<div class="banner_content">
<h3 class="text-uppercase">Hell0</h3>
<h1 class="text-uppercase">I am <|FULL_NAME|></h1>
<h5 class="text-uppercase"><|YOUR_JOB|></h5>
<div class="d-flex align-items-center">
<a class="primary_btn" href="<|LINKDIN_LINK|>"><span>Hire Me</span></a>
<a class="primary_btn tr-bg" href="<|CV_DOWNLOAD_LINK|>"><span>Get CV</span></a>
</div>
</div>
</div>
<div class="col-lg-5">
<div class="home_right_img">
<img class src="images/home-right.png" alt>
</div>
</div>
</div>
</div>
</div>
</section>


<section class="about_area section_gap" id="about">
<div class="container">
<div class="row justify-content-start align-items-center">
<div class="col-lg-5">
<div class="about_img">
<img class src="images/about-us.png" alt>
</div>
</div>
<div class="offset-lg-1 col-lg-5">
<div class="main_title text-left">
<h2>let’s <br>
Introduce about <br>
myself</h2>
<p>
<|SHORT_NOTE_ABOUT_YOU|>
</p>
<a class="primary_btn" href="<|CV_DOWNLOAD_LINK|>"><span>Download CV</span></a>
</div>
</div>
</div>
</div>
</section>





<section class="features_area" id="service">
<div class="container">
<div class="row justify-content-center">
<div class="col-lg-8 text-center">
<div class="main_title">
<h2>service offers </h2>
<p>
Is give may shall likeness made yielding spirit a itself togeth created
after sea <br> is in beast beginning signs open god you're gathering ithe
</p>
</div>
</div>
</div>
<div class="row feature_inner">
<div class="col-lg-3 col-md-6">
<div class="feature_item">
<img src="images/s1.png" alt>
<h4><|YOUR_SERVICE1|></h4>
<p><|YOUR_SERVICE_SHORT1|></p>
</div>
</div>
<div class="col-lg-3 col-md-6">
<div class="feature_item">
<img src="images/s2.png" alt>
<h4><|YOUR_SERVICE2|></h4>
<p><|YOUR_SERVICE_SHORT2|></p>
</div>
</div>
<div class="col-lg-3 col-md-6">
<div class="feature_item">
<img src="images/s3.png" alt>
<h4><|YOUR_SERVICE3|></h4>
<p><|YOUR_SERVICE_SHORT3|></p>
</div>
</div>
<div class="col-lg-3 col-md-6">
<div class="feature_item">
<img src="images/s4.png" alt>
<h4><|YOUR_SERVICE4|></h4>
<p><|YOUR_SERVICE_SHORT4|></p>
</div>
</div>
</div>
</div>
</section>




<div class="testimonial_area section_gap_bottom" id="test">
<div class="container">
<div class="row justify-content-center">
<div class="col-lg-8 text-center">
<div class="main_title">
<h2>client say about me</h2>
<p>Is give may shall likeness made yielding spirit a itself togeth created after sea is in beast <br>
beginning signs open god you're gathering ithe</p>
</div>
</div>
</div>
<div class="row">
<div class="testi_slider owl-carousel">
<div class="testi_item">
<div class="row">
<div class="col-lg-4">
<img src="<|TESTMONIAL_USER_IMG1|>" alt>
</div>
<div class="col-lg-8">
<div class="testi_text">
<h4><|TESTMONIAL_USER_NAME1|></h4>
<p><|TESTMONIAL_USER_NAME_SHORT1|></p>
</div>
</div>
</div>
</div>
<div class="testi_item">
<div class="row">
<div class="col-lg-4">
<img src="<|TESTMONIAL_USER_IMG2|>" alt>
</div>
<div class="col-lg-8">
<div class="testi_text">
<h4><|TESTMONIAL_USER_NAME2|></h4>
<p><|TESTMONIAL_USER_NAME_SHORT2|></p>
</div>
</div>
</div>
</div>
<div class="testi_item">
<div class="row">
<div class="col-lg-4">
<img src="<|TESTMONIAL_USER_IMG3|>" alt>
</div>
<div class="col-lg-8">
<div class="testi_text">
<h4><|TESTMONIAL_USER_NAME3|></h4>
<p><|TESTMONIAL_USER_NAME_SHORT3|></p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>


<section class="newsletter_area" id="contact">
<div class="container">
<div class="row justify-content-center align-items-center">
<div class="col-lg-12">
<div class="subscription_box text-center">
<h2 class="text-uppercase text-white">Get Into Touch</h2>
<p class="text-white">
Click the button to contact me through Telegram.
</p>

<button class="primary-btn hover d-inline" style="margin-top: 20px;" herf="<|CONTACT_LINK_TELEGRAM|>">Contact Me...</button>
<div class="info"></div>
</form>
</div>
</div>
</div>
</div>
</div>
</section>


<footer class="footer_area">
<div class="container">
<div class="row justify-content-center">
<div class="col-lg-12">
<div class="footer_top flex-column">
<div class="footer_logo">
<a href="#">
<h1></h1>
</a>
<h4>Follow Me</h4>
</div>
<div class="footer_social">
<a href="<|FACEBOOK_LINK|>"><i class="fa fa-facebook"></i></a>
<a href="<|INSTAGRAM_LINK|>"><i class="fa fa-instagram"></i></a>
<a href="<|YOUTUBE_LINK|>"><i class="fa fa-youtube"></i></a>
</div>
</div>
</div>
</div>
<div class="row footer_bottom justify-content-center">
<p class="col-lg-8 col-sm-12 footer-text">

Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
</p>
</div>
</div>
</footer>



<script src="js/jquery-3.2.1.min.js"></script>
<script src="js/popper.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/stellar.js"></script>
<script src="js/jquery.magnific-popup.min.js"></script>
<script src="js/jquery.nice-select.min.js"></script>
<script src="js/imagesloaded.pkgd.min.js"></script>
<script src="js/isotope-min.js"></script>
<script src="js/owl.carousel.min.js"></script>
<script src="js/jquery.ajaxchimp.min.js"></script>
<script src="js/mail-script.js"></script>
<script src="https://kit.fontawesome.com/83fe534cf6.js" crossorigin="anonymous"></script>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCjCGmQ0Uq4exrzdcL6rvxywDDOvfAu6eE"></script>
<script src="js/gmaps.min.js"></script>
<script src="js/theme.js"></script>

</body>
</html>'''



print("====================================================")
print("====================================================")
print("====================================================")
print("Loading the files from database.....")
url='https://github.com/hackerstore/WebAi-Gen/raw/main/theme-src/datasec.zip'
wget.download(url)
with ZipFile("datasec.zip", 'r') as zObject:
		zObject.extractall(path = location )
os.remove("datasec.zip")
time.sleep(5)
time.sleep(2)
print(" ")
print("====================================================")
print("====================================================")
print("Selected Theme : DataSec")
time.sleep(1)
print('Sections of Website:')
print("1] Home Section")
print("2] About Section")
print("3] Service Section")
print("3] Testominal Section")
print("4] Contact Section")
y_or_n = input("Are Sure to countine?[Y/N] Would you want to see the model page?[model]")
if y_or_n == "y":
	time.sleep(5)
	print("We need to take the information of the website..")
	print("So Please Give the informations That We ask to you.")
	print("=====================================================")
	print("!!!!!Make It Accurate You Can't Edit the information That You Give!!!!!!")
	print("=====================================================")
	colorlib1_name = input("Your Name : ")
	colorlib1_fullname = input("Your Full Name: ")
	colorlib1_job = input("Your Job: ")
	colorlib1_aboutnote = input("A Small About Note: ")
	print("========================================")
	time.sleep(2)
	print("Setting The Datas")
	time.sleep(2)
	print("Let's Jump to Service Section....")
	time.sleep(1)
	colorlib1_servicesubhead1 = input("Your First Service : ")
	colorlib1_servicesubcontent1 = input("A Small Note for It : ")
	colorlib1_servicesubhead2 = input("Your Second Service : ")
	colorlib1_servicesubcontent2 = input("A Small Note for It : ")
	colorlib1_servicesubhead3 = input("Your Thrid Service : ")
	colorlib1_servicesubcontent3 = input("A Small Note for It : ")
	colorlib1_servicesubhead4 = input("Your Fourth Service : ")
	colorlib1_servicesubcontent4 = input("A Small Note for It: ")
	print("========================================")
	print("This Section Finished.....")
	time.sleep(2)
	print("Setting The Datas")
	time.sleep(2)
	print("Let's Jump to Testominal Section....")
	time.sleep(1)
	colorlib1_testominaluserimg1 = input("Image of the First Person(Link ends With .jpg, .png) : ")
	colorlib1_testominalusername1 = input("Name of the first User : ")
	colorlib1_testominalusershort1 = input("Words Of the first person : ")
	colorlib1_testominaluserimg2 = input("Image of the First Person(Link ends With .jpg, .png) : ")
	colorlib1_testominalusername2 = input("Name of the first User : ")
	colorlib1_testominalusershort2 = input("Words Of the first person : ")
	colorlib1_testominaluserimg3 = input("Image of the First Person(Link ends With .jpg, .png) : ")
	colorlib1_testominalusername3 = input("Name of the first User : ")
	colorlib1_testominalusershort3 = input("Words Of the first person : ")
	print("========================================")
	print("This Section Finished.....")
	time.sleep(2)
	print("Setting The Datas")
	time.sleep(2)
	print("Let's Jump to Contact Section....")
	time.sleep(1)
	colorlib1_contacttglink = input("Your Telegram Link To Contact : ")
	colorlib1_fblink = input("Your Facebook Link : ")
	colorlib1_ytlink = input("Your Youtube Link : ")
	colorlib1_iglink = input("Your Instagram Link : ")
	colorlib1_linkdinlink = input("Your Linked In Link : ")
	colorlib1_cvlink = input("Your CV Downloading Link : ")
	print("========================================")
	print("It Finished.....")
	time.sleep(1)
	print("Setting The Datas")
	time.sleep(2)
	print("We are editing the code.")
	print("This will take so time!!!!")


	


	xxx = thecode.replace("<|YOUR_NAME|>", colorlib1_name).replace("<|FULL_NAME|>", colorlib1_fullname).replace("<|YOUR_JOB|>", colorlib1_job).replace("<|LINKDIN_LINK|>", colorlib1_linkdinlink).replace("<|CV_DOWNLOAD_LINK|>", colorlib1_cvlink).replace("<|SHORT_NOTE_ABOUT_YOU|>", colorlib1_aboutnote).replace("<|YOUR_SERVICE1|>", colorlib1_servicesubhead1).replace("<|YOUR_SERVICE_SHORT1|>", colorlib1_servicesubcontent1).replace("<|YOUR_SERVICE2|>", colorlib1_servicesubhead2).replace("<|YOUR_SERVICE_SHORT2|>", colorlib1_servicesubcontent2).replace("<|YOUR_SERVICE3|>", colorlib1_servicesubhead3).replace("<|YOUR_SERVICE_SHORT3|>", colorlib1_servicesubcontent3).replace("<|YOUR_SERVICE4|>", colorlib1_servicesubhead4).replace("<|YOUR_SERVICE_SHORT4|>", colorlib1_servicesubcontent4).replace("<|TESTMONIAL_USER_IMG1|>", colorlib1_testominaluserimg1).replace("<|TESTMONIAL_USER_NAME1|>", colorlib1_testominalusername1).replace("<|TESTMONIAL_USER_NAME_SHORT1|>", colorlib1_testominalusershort1).replace("<|TESTMONIAL_USER_IMG2|>", colorlib1_testominaluserimg2).replace("<|TESTMONIAL_USER_NAME2|>", colorlib1_testominalusername2).replace("<|TESTMONIAL_USER_NAME_SHORT2|>", colorlib1_testominalusershort2).replace("<|TESTMONIAL_USER_IMG3|>", colorlib1_testominaluserimg3).replace("<|TESTMONIAL_USER_NAME3|>", colorlib1_testominalusername3).replace("<|TESTMONIAL_USER_NAME_SHORT3|>", colorlib1_testominalusershort3).replace("<|CONTACT_LINK_TELEGRAM|>", colorlib1_contacttglink).replace("<|FACEBOOK_LINK|>", colorlib1_fblink).replace("<|INSTAGRAM_LINK|>", colorlib1_iglink).replace("<|YOUTUBE_LINK|>", colorlib1_ytlink)
	text_file = open("index.html", "w")
	text_file.write(xxx)
	text_file.close()
	time.sleep(2)


	





elif y_or_n == "n":
	main()
elif y_or_n == "model":
	print("MOnjikko")