import time
import requests
import wget
import os
import shutil
from zipfile import ZipFile


location = os.getcwd()

thecode = '''<!doctype html>

<html class="no-js" lang="zxx">

    <head>

    	<!-- metas -->
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
       	<meta name="description" content="Daniels is a responsive creative template">
		<meta name="keywords" content="portfolio, personal, corporate, business, parallax, creative, agency">

		<!-- title -->
		<title><|TITLE|></title>

		<!-- favicon -->
        <link href="<|YOUR_IMAGE_LINK|>" rel="icon" type="image/png">

        <!-- bootstrap css -->
		<link rel="stylesheet" href="css/bootstrap.min.css">

		<!-- google fonts -->
		<link href="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700,800,900" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css?family=Poppins:200,300,400,500,600,700,800" rel="stylesheet">

		<!-- owl carousel CSS -->
		<link rel="stylesheet" href="css/owl.carousel.min.css">
		<link rel="stylesheet" href="css/owl.theme.default.min.css">

		<!-- magnific-popup CSS -->
		<link rel="stylesheet" href="css/magnific-popup.css">

		<!-- animate.min CSS -->
		<link rel="stylesheet" href="css/animate.min.css">

		<!-- Font Icon Core CSS -->
		<link rel="stylesheet" href="css/font-awesome.min.css">
		<link rel="stylesheet" href="css/et-line.css">

		<!-- Core Style Css -->
        <link rel="stylesheet" href="css/style.css">

        <!--[if lt IE 9]-->
		<script src="js/html5shiv.min.js"></script>
		<!--[endif]-->

    </head>
    
    <body>

    	<!-- ====== Preloader ======  -->
	    <div class="loading">
			<div class="load-circle">
			</div>
		</div>
		<!-- ======End Preloader ======  -->

		<!-- ====== Navgition ======  -->
		<nav class="navbar navbar-default">
		  <div class="container">
		    <!-- Brand and toggle get grouped for better mobile display -->
		    <div class="navbar-header">
		      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#nav-icon-collapse" aria-expanded="false">
		        <span class="sr-only">Toggle navigation</span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		      </button>

		       <!-- logo -->
		      <a class="logo" href="#"><|NAME|></a>

		    </div>

		    <!-- Collect the nav links, and other content for toggling -->
		    <div class="collapse navbar-collapse" id="nav-icon-collapse">
		      
			  <!-- links -->
		      <ul class="nav navbar-nav navbar-right">
		        <li><a href="#home" data-scroll-nav="0" class="active">Home</a></li>
		        <li><a href="#hero" data-scroll-nav="1">About</a></li>
		        <li><a href="#service" data-scroll-nav="2">Services</a></li>
		        <li><a href="#clin" data-scroll-nav="4">Clients</a></li>
		        <li><a href="#contact" data-scroll-nav="6">Contact</a></li>
		      </ul>
		    </div><!-- /.navbar-collapse -->
		  </div><!-- /.container -->
		</nav>
		<!-- ====== End Navgition ======  -->

		<!-- ====== Header ======  -->
		<section id="home" class="header" data-scroll-index="0" style="background-image: url(images/bg.jpg);" data-stellar-background-ratio="0.8">

			<div class="v-middle">
				<div class="container">
					<div class="row">

						<!-- caption -->
						<div class="caption">
							<h5>Hello</h5>
							<h1 class="cd-headline clip">
					            <span class="blc">I Am </span>
					            <span class="cd-words-wrapper">
					              <b class="is-visible"><|FULLNAME|></b>
					              <b><|YOUR_JOB_1|></b>
					              <b><|YOUR_JOB_2|></b>
					            </span>
			          		</h1>

			          		<!-- social icons -->
			          		<div class="social-icon">
			          			<a href="<|FACEBOOK_LINK|>">
			          				<span><i class="fa fa-facebook" aria-hidden="true"></i></span>
			          			</a>
			          			<a href="<|TWITTER_LINK|>">
			          				<span><i class="fa fa-twitter" aria-hidden="true"></i></span>
			          			</a>
			          			<a href="<|INSTAGRAM_LINK|>">
			          				<span><i class="fa fa-instagram" aria-hidden="true"></i></span>
			          			</a>
			          			<a href="<|YOUTUBE_LINK|>">
			          				<span><i class="fa fa-youtube" aria-hidden="true"></i></span>
			          			</a>
			          		</div>
						</div>
						<!-- end caption -->
					</div>
				</div><!-- /row -->
			</div><!-- /container -->
		</section>
		<!-- ====== End Header ======  -->

		<!-- ====== Hero ======  -->
		<section class="hero section-padding pb-70" data-scroll-index="1" id="hero">
			<div class="container">
				<div class="row">

					<!-- hero image -->
					<div class="col-md-5">
						<div class="hero-img mb-30">
							<img src="<|YOUR_IMAGE_LINK|>" alt>
						</div>
					</div>

					<!-- content -->
					<div class="col-md-7">
						<div class="content mb-30">
							<h3>About Me.</h3>
							<span class="sub-title"><|YOUR_JOB_1|> & <|YOUR_JOB_2|></span>
							<p>I am <b><|FULLNAME|></b> <|SHORT_NOTE_ABOUT_YOU|></p>

							<!-- skills progress -->
							<div class="skills">
								<div class="item">
									<div class="skills-progress">
										<h6><|YOUR_SKILL_1|></h6>
										<span data-value="<|SKILL_PERENT_1|>%"></span>
									</div>
								</div>
								<div class="item">
									<div class="skills-progress">
										<h6><|YOUR_SKILL_2|></h6>
										<span data-value="<|SKILL_PERENT_2|>%"></span>
									</div>
								</div>
								<div class="item">
									<div class="skills-progress">
										<h6><|YOUR_SKILL_3|></h6>
										<span data-value="<|SKILL_PERENT_3|>%"></span>
									</div>
								</div>
							</div>
							<div class="clearfix"></div>

							<a href="" download>
								<span class="buton buton-bg">Download C.V</span>
							</a>
							<a href="" data-scroll-nav="6">
								<span class="buton">Contact Me</span>
							</a>

						</div>
					</div>
				</div><!-- /row -->
			</div><!-- /container -->
		</section>
		<!-- ====== End Hero ======  -->

		<!-- ====== Services ======  -->
		<section id="service" class="services section-padding bg-gray text-center pb-70" data-scroll-index="2">
			<div class="container">

				<!-- section heading -->
				<div class="section-head">
					<h3>Services.</h3>
				</div>

				<div class="row">

					<!-- items -->
					<div class="col-md-4">
						<div class="item">
							<span class="icon"><i class="fa fa-laptop" aria-hidden="true"></i></span>
							<h6><|SERVICE_HEAD_1|></h6>
							<p><|SERVICE_CONTENT_1|></p>
						</div>
					</div>
					<div class="col-md-4">
						<div class="item">
							<span class="icon"><i class="fa fa-bullhorn" aria-hidden="true"></i></span>
							<h6><|SERVICE_HEAD_2|></h6>
							<p><|SERVICE_CONTENT_2|></p>
						</div>
					</div>
					<div class="col-md-4">
						<div class="item">
							<span class="icon"><i class="fa fa-television" aria-hidden="true"></i></span>
							<h6><|SERVICE_HEAD_3|></h6>
							<p><|SERVICE_CONTENT_3|></p>
						</div>
					</div>
					
				</div><!-- /row -->
			</div><!-- /container -->
		</section>
		<!-- ====== End Services ======  -->

		<!--====== Numbers ======-->
		<div class="numbers section-padding text-center pb-70" id="numbers">
			<div class="container">
				<div class="row">

					<!-- items -->
					<div class="col-md-3">
						<div class="item">
							<span class="icon"><i class="fa fa-users" aria-hidden="true"></i></span>
							<h3 class="counter"><|NUMBER_OF_HAPPY_CUSTOMER|></h3>
							<p>Happy Customers</p>
						</div>
					</div>

					<div class="col-md-3">
						<div class="item">
							<span class="icon"><i class="fa fa-thumbs-up" aria-hidden="true"></i></span>
							<h3 class="counter"><|NUMBER_OF_COMPLETED_PROJECTS|></h3>
							<p>Complete Projects</p>
						</div>
					</div>

					<div class="col-md-3">
						<div class="item">
							<span class="icon"><i class="fa fa-bullhorn" aria-hidden="true"></i></span>
							<h3 class="counter"><|NUMBER_OF_LINE_CODE|></h3>
							<p>Lines Of Code</p>
						</div>
					</div>

					<div class="col-md-3">
						<div class="item">
							<span class="icon"><i class="fa fa-cloud-download" aria-hidden="true"></i></span>
							<h3 class="counter"><|NUMBER_OF_DOWNLOADED_FILE|></h3>
							<p>Files Downloaded</p>
						</div>
					</div>

				</div><!-- /row -->
			</div><!-- /container -->
		</div>
		<!--====== End Numbers ======-->

		<!--====== Clients ======-->
		<section class="clients section-padding bg-gray" data-scroll-index="4" id="clin">
			<div class="container">
				<div class="row">

					<!-- section heading -->
					<div class="section-head">
						<h3>Testimonials.</h3>
					</div>

					<!-- owl carousel -->
					<div class="col-md-offset-1 col-md-10">
						<div class="owl-carousel owl-theme text-center">

							<!-- citems -->
							<div class="citem">
								<div class="author-img">
									<img src="<|TESTMONIAL_USER_IMG1|>" alt>
								</div>
								<p><|TESTMONIAL_USER_NAME_SHORT1|></p>
								<h6><|TESTMONIAL_USER_NAME1|></h6>
								<span><|TESTMONIAL_USER_NAME_JOB_1|></span>
							</div>
							<div class="citem">
								<div class="author-img">
									<img src="<|TESTMONIAL_USER_IMG2|>" alt>
								</div>
								<p><|TESTMONIAL_USER_NAME_SHORT2|></p>
								<h6><|TESTMONIAL_USER_NAME2|></h6>
								<span><|TESTMONIAL_USER_NAME_JOB_2|></span>
							</div>
							<div class="citem">
								<div class="author-img">
									<img src="<|TESTMONIAL_USER_IMG3|>" alt>
								</div>
								<p><|TESTMONIAL_USER_NAME_SHORT3|></p>
								<h6><|TESTMONIAL_USER_NAME3|></h6>
								<span><|TESTMONIAL_USER_NAME_JOB_3|></span>
							</div>

							
						</div>
					</div>
				</div><!-- /row -->
			</div><!-- /container -->
		</section>
		<!--====== End clients ======-->

		

		

		<!--====== Contact ======-->
		<section class="contact section-padding" data-scroll-index="6" id="contact">
			<div class="container">
				<div class="row">
					
					<!-- section heading -->
					<div class="section-head">
						<h3>Contact Us.</h3>
					</div>

					<div class="col-md-offset-1 col-md-10">

						<!-- contact info -->
						<div class="info text-center mb-50">

							<div class="col-md-4">
								<div class="item">
									<span class="icon"><i class="fa fa-location-arrow" aria-hidden="true"></i></span>
									<h6>Address</h6>
									<p><|YOUR_ADDRESS|></p>
								</div>
							</div>

							<div class="col-md-4">
								<div class="item">
									<span class="icon"><i class="fa fa-envelope" aria-hidden="true"></i></span>
									<h6>Email</h6>
									<p><|YOUR_EMAIL|></p>
								</div>
							</div>

							<div class="col-md-4">
								<div class="item">
									<span class="icon"><i class="fa fa-phone" aria-hidden="true"></i></span>
									<h6>Phone</h6>
									<p><|YOUR_PHONE_NUMBER|></p>
								</div>
							</div>
							<div class="clearfix"></div>
						</div>

						<!-- contact form -->
						<form class="form" id="contact-form" method="post" action="contact.php">
		                    <div class="messages"></div>

		                    <div class="controls">

		                        <div class="row">
		                            <div class="col-md-6">
		                                <div class="form-group">
		                                    <input id="form_name" type="text" name="name" placeholder="Name" required="required">
		                                </div>
		                            </div>

		                             <div class="col-md-6">
		                                <div class="form-group">
		                                    <input id="form_email" type="email" name="email" placeholder="Email" required="required">
		                                </div>
		                            </div>
		                        </div>
		                        <div class="row">
		                            <div class="col-md-12">
		                                <div class="form-group">
		                                    <textarea id="form_message" name="message" placeholder="Message" rows="4" required="required"></textarea>
		                                </div>

		                                <input type="submit" value="Submit" class="buton buton-bg">
		                            </div>
		                        </div>
		                    </div>
		                </form>

					</div>
				</div><!-- /row -->
			</div><!-- /container -->
		</section>
		<!--====== End Contact ======-->

		<!--====== Footer ======-->
		<footer>
			<div class="container text-center">
				<div class="row">
					<p>Copy Right 2018 &copy; By Daniels All Rights Reserved</p>
				</div>
			</div>
		</footer>
		<!--====== End Footer ======-->



       
        <!-- jQuery -->
		<script src="js/jquery-3.0.0.min.js"></script>
		<script src="js/jquery-migrate-3.0.0.min.js"></script>

	  	<!-- bootstrap -->
		<script src="js/bootstrap.min.js"></script>

		<!-- scrollIt -->
		<script src="js/scrollIt.min.js"></script>

		<!-- magnific-popup -->
		<script src="js/jquery.magnific-popup.min.js"></script>

		<!-- owl carousel -->
		<script src="js/owl.carousel.min.js"></script>

		<!-- stellar js -->
		<script src="js/jquery.stellar.min.js"></script>

		<!-- animated.headline -->
		<script src="js/animated.headline.js"></script>

      	<!-- jquery.waypoints.min js -->
	  	<script src="js/jquery.waypoints.min.js"></script>

	  	<!-- jquery.counterup.min js -->
	  	<script src="js/jquery.counterup.min.js"></script>

      	<!-- isotope.pkgd.min js -->
      	<script src="js/isotope.pkgd.min.js"></script>

      	<!-- validator js -->
      	<script src="js/validator.js"></script>

      	<!-- custom script -->
        <script src="js/custom.js"></script>

    </body>
</html>
'''



print("====================================================")
print("====================================================")
print("====================================================")
print("Loading the files from database.....")
url='https://github.com/hackerstore/WebAi-Gen/raw/main/theme-src/colorlib.zip'
wget.download(url)
with ZipFile("colorlib.zip", 'r') as zObject:
		zObject.extractall(path = location )
os.remove("colorlib.zip")
time.sleep(5)
time.sleep(2)
print(" ")
print("====================================================")
print("====================================================")
print("Selected Theme : ColorLib")
time.sleep(1)
print('Sections of Website:')
print("1] Main Section")
print("2] About Section")
print("3] Skill Section")
print("3] Portfolio Section")
print("4] Contact Section")
print("5] Footer Section")
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
	colorlib1_job2 = input("Your other Job: ")
	colorlib1_yourimg = input("Your Image Link: ")
	colorlib1_aboutnote = input("A Small About Note: ")
	colorlib1_skilname1 = input("Your Skill : ")
	colorlib1_skilpercent1 = input("Your Skill Percent (Out of 100): ")
	colorlib1_skilname2 = input("Your Second Skill: ")
	colorlib1_skilpercent2 = input("Your Second Skill Percent (Out of 100): ")
	colorlib1_skilname3 = input("Your Third Skill: ")
	colorlib1_skilpercent3 = input("Your Third Skill Percent (Out of 100): ")
	

	print("========================================")
	time.sleep(4)
	print("Setting The Datas")
	time.sleep(3)
	print("Let's Jump to Service Section....")
	time.sleep(2)
	colorlib1_servicesubhead1 = input("Your First Service : ")
	colorlib1_servicesubcontent1 = input("A Small Note for It : ")
	colorlib1_servicesubhead2 = input("Your Second Service : ")
	colorlib1_servicesubcontent2 = input("A Small Note for It : ")
	colorlib1_servicesubhead3 = input("Your Thrid Service : ")
	colorlib1_servicesubcontent3 = input("A Small Note for It : ")
	print("========================================")
	time.sleep(4)
	print("Setting The Datas")
	time.sleep(3)
	print("Let's Jump to Numbers Section....")
	time.sleep(2)
	colorlib1_numberofhappyones = input("Number of happy coustmer in your service : ")
	colorlib1_numberofprojects = input("Number of your completed projects : ")
	colorlib1_lineofcode = input("Number of your line of code : ")
	colorlib1_downloadedfile = input("Number of Downloaded files : ")
	print("========================================")
	print("This Section Finished.....")
	time.sleep(3)
	print("Setting The Datas")
	time.sleep(2)
	print("Let's Jump to Testominal Section....")
	time.sleep(1)
	colorlib1_testominaluserimg1 = input("Image of the First Person(Link ends With .jpg, .png) : ")
	colorlib1_testominalusername1 = input("Name of the first User : ")
	colorlib1_testominalusershort1 = input("Words Of the first person : ")
	colorlib1_testominaluserjob1 = input("Job Of the first person : ")
	colorlib1_testominaluserimg2 = input("Image of the Second Person(Link ends With .jpg, .png) : ")
	colorlib1_testominalusername2 = input("Name of the Second User : ")
	colorlib1_testominalusershort2 = input("Words Of the second person : ")
	colorlib1_testominaluserjob2 = input("Job Of the Second person : ")
	colorlib1_testominaluserimg3 = input("Image of the Thrid Person(Link ends With .jpg, .png) : ")
	colorlib1_testominalusername3 = input("Name of the Thrid User : ")
	colorlib1_testominalusershort3 = input("Words Of the Thrid person : ")
	colorlib1_testominaluserjob3 = input("Job Of the Thrid person : ")
	print("========================================")
	print("This Section Finished.....")
	time.sleep(3)
	print("Setting The Datas")
	time.sleep(2)
	print("Let's Jump to Contact Section....")
	time.sleep(1)
	colorlib1_address = input("Your Address: ")
	colorlib1_email = input("Your Email: ")
	colorlib1_number = input("Your Phone Number: ")
	colorlib1_contacttglink = input("Your Telegram Link To Contact : ")
	colorlib1_fblink = input("Your Facebook Link : ")
	colorlib1_ytlink = input("Your Youtube Link : ")
	colorlib1_twtlink = input("Your Twitter Link : ")
	colorlib1_iglink = input("Your Instagram Link : ")
	colorlib1_linkdinlink = input("Your Linked In Link : ")
	colorlib1_cvlink = input("Your CV Downloading Link : ")
	print("========================================")
	print("It Finished.....")
	time.sleep(3)
	print("Setting The Datas")
	time.sleep(2)
	print("We are editing the code.")
	print("This will take so time!!!!")


	


	xxx = thecode.replace("<|TITLE|>", colorlib1_name+" - Personal Website").replace("<|NAME|>", colorlib1_name).replace("<|FULLNAME|>", colorlib1_fullname).replace("<|YOUR_JOB_1|>", colorlib1_job).replace("<|YOUR_JOB_2|>", colorlib1_job2).replace("<|SHORT_NOTE_ABOUT_YOU|>", colorlib1_aboutnote).replace("<|YOUR_SKILL_1|>", colorlib1_skilname1).replace("<|SKILL_PERENT_1|>", colorlib1_skilpercent1).replace("<|YOUR_SKILL_2|>", colorlib1_skilname2).replace("<|SKILL_PERENT_2|>", colorlib1_skilpercent2).replace("<|YOUR_SKILL_3|>", colorlib1_skilname3).replace("<|SKILL_PERENT_3|>", colorlib1_skilpercent3).replace("<|YOUR_IMAGE_LINK|>", colorlib1_yourimg).replace("<|CONTACT_LINK|>", colorlib1_contacttglink).replace("<|SERVICE_HEAD_1|>", colorlib1_servicesubhead1).replace("<|SERVICE_HEAD_2|>", colorlib1_servicesubhead2).replace("<|SERVICE_HEAD_3|>", colorlib1_servicesubhead3).replace("<|SERVICE_CONTENT_1|>", colorlib1_servicesubcontent1).replace("<|SERVICE_CONTENT_2|>", colorlib1_servicesubcontent2).replace("<|SERVICE_CONTENT_3|>", colorlib1_servicesubcontent3).replace("<|NUMBER_OF_HAPPY_CUSTOMER|>", colorlib1_numberofhappyones).replace("<|NUMBER_OF_COMPLETED_PROJECTS|>", colorlib1_numberofprojects).replace("<|NUMBER_OF_LINE_CODE|>", colorlib1_lineofcode).replace("<|NUMBER_OF_DOWNLOADED_FILE|>", colorlib1_downloadedfile).replace("<|TESTMONIAL_USER_IMG1|>", colorlib1_testominaluserimg1).replace("<|TESTMONIAL_USER_NAME_SHORT1|>", colorlib1_testominalusershort1).replace("<|TESTMONIAL_USER_NAME1|>", colorlib1_testominalusername1).replace("<|TESTMONIAL_USER_NAME_JOB_1|>", colorlib1_testominaluserjob1).replace("<|TESTMONIAL_USER_IMG2|>", colorlib1_testominaluserimg2).replace("<|TESTMONIAL_USER_NAME_SHORT2|>", colorlib1_testominalusershort2).replace("<|TESTMONIAL_USER_NAME2|>", colorlib1_testominalusername2).replace("<|TESTMONIAL_USER_NAME_JOB_2|>", colorlib1_testominaluserjob2).replace("<|TESTMONIAL_USER_IMG3|>", colorlib1_testominaluserimg3).replace("<|TESTMONIAL_USER_NAME_SHORT3|>", colorlib1_testominalusershort3).replace("<|TESTMONIAL_USER_NAME3|>", colorlib1_testominalusername3).replace("<|TESTMONIAL_USER_NAME_JOB_3|>", colorlib1_testominaluserjob3).replace("<|YOUR_ADDRESS|>", colorlib1_address).replace("<|YOUR_EMAIL|>", colorlib1_email).replace("<|YOUR_PHONE_NUMBER|>", colorlib1_number).replace("<|FACEBOOK_LINK|>", colorlib1_fblink).replace("<|TWITTER_LINK|>", colorlib1_twtlink).replace("<|INSTAGRAM_LINK|>", colorlib1_iglink).replace("<|YOUTUBE_LINK|>", colorlib1_ytlink).replace("<|CV_DOWNLOAD_LINK|>", colorlib1_cvlink)
	text_file = open("index.html", "w")
	text_file.write(xxx)
	text_file.close()


	time.sleep(2)


	





elif y_or_n == "n":
	main()
elif y_or_n == "model":
	print("MOnjikko")