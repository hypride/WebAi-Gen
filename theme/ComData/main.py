import time
import requests
import wget
import os
from zipfile import ZipFile


location = os.getcwd()

thecode = '''<!doctype html>
<html class="no-js" lang="zxx">

<head>
   <meta charset="utf-8">
   <meta http-equiv="x-ua-compatible" content="ie=edge">
   <title><|NAME|> - <|SLOGAN|></title>
   <meta name="description" content>
   <meta name="viewport" content="width=device-width, initial-scale=1">

   <!-- Place favicon.ico in the root directory -->
   <link rel="shortcut icon" type="image/x-icon" href="images/favicon.png">

   <!-- CSS here -->
   <link rel="stylesheet" href="css/bootstrap.css">
   <link rel="stylesheet" href="css/animate.css">
   <link rel="stylesheet" href="css/swiper-bundle.css">
   <link rel="stylesheet" href="css/slick.css">
   <link rel="stylesheet" href="css/nouislider.css">
   <link rel="stylesheet" href="css/magnific-popup.css">
   <link rel="stylesheet" href="css/font-awesome-pro.css">
   <link rel="stylesheet" href="css/spacing.css">
   <link rel="stylesheet" href="css/main.css">
</head>
<body>


   <div class="back-to-top-wrapper back_to_top-2">
      <button id="back_to_top" type="button" class="back-to-top-btn">
         <svg width="12" height="7" viewBox="0 0 12 7" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 6L6 1L1 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
         </svg>
      </button>
   </div>
   <!-- back to top end -->

   <!-- header-area-start -->
   <header>
      <div id="header-sticky" class="tptransparent__header header-green header-spaces">
         <div class="container">
            <div class="tp-mega-menu-wrapper">
               <div class="row align-items-center">
                  <div class="col-xl-1 col-lg-6 col-sm-4 col-6">
                     <div class="tplogo__area">
                        <a href="index.html">
                           <img src="fonts/logo-green.svg" alt="logo">
                        </a>
                     </div>
                  </div>
                  <div class="col-xl-7 col-lg-5  d-none d-xl-block">
                     <div class="tpmenu__area main-mega-menu pl-35">
                        <nav class="tp-main-menu-content">
                           <ul class="tp-onepage-menu">
                              <li class="has-mega-menu"><a href="#home">Home</a></li>
                              <li><a href="#about">About</a></li>
                              <li><a href="#services-one-page">Service</a></li>
                              <li><a href="#test">Testmonial</a></li>
                              <li><a href="#contact-one-page">Contact</a></li>
                           </ul>
                        </nav>
                     </div>
                  </div>
                  <div class="col-xl-4 col-lg-6 col-sm-8 col-6">
                     <div class="tpheader__right d-flex align-items-center justify-content-end">
                        <div class="d-none d-md-block">
                        </div>
                        <div class="tpheader-btn-two ml-25 d-none d-md-block">
                           <a href="<|CONTACT_LINK|>">Hire Us</a>
                        </div>
                        <div class="offcanvas-btn d-xl-none ml-20">
                           <button class="offcanvas-open-btn"><i class="fa-solid fa-bars"></i></button>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </header>
   <!-- header-area-end -->

   <!-- offcanvas area start -->
   <div class="offcanvas__area">
      <div class="offcanvas__wrapper">
         <div class="offcanvas__close">
            <button class="offcanvas__close-btn offcanvas-close-btn">
               <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M11 1L1 11" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M1 1L11 11" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
               </svg>
            </button>
         </div>
         <div class="offcanvas__content">
            <div class="offcanvas__top mb-50 d-flex justify-content-between align-items-center">
               <div class="offcanvas__logo logo">
                  <a href="home-main.html">
                     <img src="fonts/logo-green.svg" alt="logo">
                  </a>
               </div>
            </div>
            <div class="tp-main-menu-mobile mb-35"></div>
            <div class="offcanvas__btn">
               <a href="<|CONTACT_LINK|>" class="tp-btn w-100">Getting Started</a>
            </div>
            <div class="offcanvas__contact mb-40">
               <p class="offcanvas__contact-call"><a href="tel:<|PHONE_NUMBER|>"><|PHONE_NUMBER|></a></p>
               <p class="offcanvas__contact-mail"><a href="mailto:<|MAIL|>"><|MAIL|></a></p>
            </div>
            <div class="offcanvas__social">
               <a href="<|FB_LINK|>"><i class="fab fa-facebook-f"></i></a>
               <a href="<|TWT_LINK|>"><i class="fab fa-twitter"></i></a>
               <a href="<|YT_LINK|>"><i class="fab fa-youtube"></i></a>
               <a href="<|IG_LINK|>"><i class="fab fa-instagram"></i></a>
            </div>
         </div>
      </div>
   </div>
   <div class="body-overlay"></div>
   <!-- offcanvas area end -->

   <main>

      <!-- banner-area-start -->
      <div class="banner-area tpbanner-space-two" data-background="assets/img/banner/banner-2-bg-1.png">
         <div class="container">
            <div class="row justify-content-center">
               <div class="col-lg-7 col-md-7 order-2 order-md-1">
                  <div class="tpbanner-content-two">
                     <div class="tpbanner-title-two mb-20"><span><|MAIN_KEYWORD|>
                           <svg width="406" height="40" viewBox="0 0 406 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M3.14977 24.4029C3.14977 24.4029 256.329 -7.75032 398.26 15.5002" stroke="#FFCE5A" stroke-width="5" stroke-linecap="round"/>
                              <path d="M3.59029 19.0626C3.59029 19.0626 261.471 -1.12129 402.878 28.422" stroke="#FFCE5A" stroke-width="5" stroke-linecap="round"/>
                           </svg>
                        </span> <|MAIN_HEAD|></div>
                     <p><|SUB_HEAD|></p>
                     <div class="tpbanner-two-btn mb-35">
                        <a class="green-btn" href="<|CONTACT_LINK|>">Hire us</a>
                     </div>
                     
                  </div>
               </div>
               <div class="col-lg-5 col-md-5 order-1 order-md-2">
                  <div class="tpbanner-two-shape p-relative" data-parallax="{"x": 15, "smoothness": 10}">
                     <img src="images/banner-2-thumb-1.png" alt>
                     <div class="tpbanner-two-shape-round">
                        <div class="tpbanner-two-shape-one">
                           <img src="images/banner-2-shape-1.png" alt>
                        </div>
                        <div class="tpbanner-two-shape-two">
                           <img src="images/banner-2-shape-2.png" alt>
                        </div>
                     </div>
                     <div class="tpbanner-two-shape-three">
                        <img src="images/banner-2-shape-3.png" alt>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
      <!-- banner-area-end -->


      <!-- drive-area-start -->
      <section class="drive-area p-relative drive-section-bottom pb-120" id="about">
         <div class="container">
            <div class="row justify-content-center">
               <div class="col-lg-9">
                  <div class="tpsection-wrapper text-center mb-85">
                     <h2 class="tpsection-title-two">Use <|NAME|> to Drive Growth at <br>
                        <span class="big-shape">Your Business.
                           <svg width="335" height="33" viewBox="0 0 335 33" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M2.64842 20.1323C2.64842 20.1323 211.522 -6.39416 328.614 12.7876" stroke="#FFCE5A" stroke-width="5" stroke-linecap="round"/>
                              <path d="M3.01153 15.7265C3.01153 15.7265 215.763 -0.925266 332.424 23.448" stroke="#FFCE5A" stroke-width="5" stroke-linecap="round"/>
                           </svg>
                        </span>
                     </h2>
                  </div>
               </div>
            </div>
            <div class="tp-drive-shape p-relative">
               <div class="row drive-section-bottom mb-200">
                  <div class="col-lg-6">
                     <div class="tpdrive-thumb p-relative ml-100 ">
                        <img src="images/drive-thumb-b-1.png" alt>
                        <div class="tpdrive-thumb-shape">
                           <div class="tpdrive-thumb-shape-five">
                              <img src="images/settings-3.png" alt>
                           </div>
                           <div class="tpdrive-thumb-shape-six">
                              <img src="images/settings-4.png" alt>
                           </div>
                           <div class="tpdrive-thumb-shape-seven">
                              <img src="images/list-text.png" alt>
                           </div>
                        </div>
                     </div>
                  </div>
                  <div class="col-lg-6">
                     <div class="tpdrive-wrapper mt-10 ml-55 mr-95">
                        <div class="tpdrive-content">
                           <span>About Us</span>
                           <h5 class="tpdrive-title mb-20">How We Can <br>Help You at Your Business.</h5>
                        </div>
                        
                           <p><|ABOUT_YOUR_COMPANY|>
                           </p>
                           <div class="tpdrive-content-btn">
                              <a class="green-btn" href="<|CONTACT_LINK|>">Hire Us</a>
                           </div>
                     </div>
                  </div>
               </div>
               <div class="drive-big-shape d-none d-lg-block">
                  <svg width="1172" height="600" viewBox="0 0 1172 600" fill="none" xmlns="http://www.w3.org/2000/svg">
                     <path class="line-dash-path" d="M1 0V280.251C1 291.296 9.95431 300.251 21 300.251H1151C1162.05 300.251 1171 309.205 1171 320.251V600" stroke="#BDC1C6" stroke-dasharray="5 5"/>
                  </svg>
                  <div class="drive-shape">
                     <div class="drive-big-shape-one wow bounceIn" data-wow-delay=".5s" data-wow-duration=".3s">
                        <img src="images/side-line-1.png" alt>
                     </div>
                     <div class="drive-big-shape-two wow bounceIn" data-wow-duration=".5s" data-wow-delay=".3s">
                        <img src="images/side-line-2.png" alt>
                     </div>
                     <div class="drive-big-shape-three wow bounceIn" data-wow-duration=".5s" data-wow-delay=".3s">
                        <img src="images/side-line-3.png" alt>
                     </div>
                  </div>
               </div>
               <div class="row">
                  <div class="col-lg-6">
                     <div class="tpdrive-wrapper ml-100">
                        <div class="tpdrive-content">
                           <span>Client Satisfaction?</span>
                           <h5 class="tpdrive-title mb-15">Fostering Client Satisfaction <br> Elevating Experiences</h5>
                           <div class="tpdrive-progress">
                           <div class="tpdrive-bar-item mb-30">
                              <h4 class="tpdrive-bar-title mb-15">
                                 <span>
                                    <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                       <path d="M4.552 1H13.44C16.288 1 17 1.712 17 4.552V9.616C17 12.464 16.288 13.168 13.448 13.168H4.552C1.712 13.176 1 12.464 1 9.624V4.552C1 1.712 1.712 1 4.552 1Z" stroke="#ADB0B4" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                       <path d="M9 13.176V17" stroke="#ADB0B4" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                       <path d="M1 9.80005H17" stroke="#ADB0B4" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                       <path d="M5.3999 17H12.5999" stroke="#ADB0B4" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                    </svg>
                                 </span> Satisfied Projects
                              </h4>
                              <div class="tpdrive-bar-progress">
                                 <div class="progress">
                                    <div class="progress-bar wow slideInLeft" data-wow-delay=".1s" data-wow-duration="1.3s" role="progressbar" data-width="<|SATFIED_CLINT_PERCET|>%" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100" style="width: <|SATFIED_CLINT_PERCET|>%;">
                                       <span><|SATFIED_CLINT_PERCET|></span>
                                    </div>
                                 </div>
                              </div>
                           </div>
                           <div class="tpdrive-bar-item yellow-bar">
                              <h4 class="tpdrive-bar-title mb-15">
                                 <span>
                                    <svg width="15" height="18" viewBox="0 0 15 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                       <path d="M14 5V13C14 16.2 13.1875 17 9.9375 17H5.0625C1.8125 17 1 16.2 1 13V5C1 1.8 1.8125 1 5.0625 1H9.9375C13.1875 1 14 1.8 14 5Z" stroke="#ADB0B4" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                       <path d="M9.125 3.80005H5.875" stroke="#ADB0B4" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                       <path d="M7.49961 14.68C8.19514 14.68 8.75898 14.1248 8.75898 13.44C8.75898 12.7551 8.19514 12.2 7.49961 12.2C6.80408 12.2 6.24023 12.7551 6.24023 13.44C6.24023 14.1248 6.80408 14.68 7.49961 14.68Z" stroke="#ADB0B4" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                    </svg>
                                 </span> Unsatisfied Projects
                              </h4>
                              <div class="tpdrive-bar-progress">
                                 <div class="progress">
                                    <div class="progress-bar wow slideInLeft" data-wow-delay=".1s" data-wow-duration="1.5s" role="progressbar" data-width="<|UNSATFIED_CLINT_PERCET|>%" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100" style="width: <|UNSATFIED_CLINT_PERCET|>%;">
                                       <span><|UNSATFIED_CLINT_PERCET|></span>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                           
                        </div>
                     </div>
                  </div>
                  <div class="col-lg-6">
                     <div class="tpdrive-thumb p-relative">
                        <img src="images/drive-thumb-b-2.png" alt>
                        <div class="tpdrive-thumb-shape">
                           <div class="tpdrive-thumb-shape-one">
                              <img src="images/search-content.png" alt>
                           </div>
                           <div class="tpdrive-thumb-shape-two">
                              <img src="images/cheackmark-1.png" alt>
                           </div>
                           <div class="tpdrive-thumb-shape-three">
                              <img src="images/settings.png" alt>
                           </div>
                           <div class="tpdrive-thumb-shape-four">
                              <img src="images/settings-2.png" alt>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </section>
      <!-- drive-area-end -->


     

      

      <!-- services-area-start -->
      <section id="services-one-page"  class="services-area tp-large-box services-bg-two p-relative fix" data-background="assets/img/banner/services-bg.png">
         <div class="services-shape d-none d-xl-block">
            <div class="services-shape-one">
               <img src="images/services-2shape-1.png" alt>
            </div>
            <div class="services-shape-two">
               <img src="images/services-2shape-2.png" alt>
            </div>
         </div>
         <div class="container">
            <div class="row">
               <div class="row justify-content-center">
                  <div class="col-lg-8">
                     <div class="tpsection-wrapper text-center mb-60">
                        <h2 class="tpsection-title-two">Check why you Should <br>
                           <span class="big-shape2">
                              Choose Us
                              <svg width="246" height="24" viewBox="0 0 246 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                 <path d="M2.74431 14.6419C2.74431 14.6419 154.652 -4.65014 239.811 9.30024" stroke="#FFCE5A" stroke-width="5" stroke-linecap="round"/>
                                 <path d="M3.00783 11.4374C3.00783 11.4374 157.737 -0.672988 242.581 17.053" stroke="#FFCE5A" stroke-width="5" stroke-linecap="round"/>
                              </svg>
                           </span>
                        </h2>
                     </div>
                  </div>
               </div>
            </div>
            <div class="row">
               <div class="col-lg-6">
                  <div class="services-two mb-30">
                     <div class="services-two-bg"></div>
                     <div class="services-two-icon">
                        <img src="images/services-icon-1.png" alt>
                     </div>
                     <div class="services-two-content">
                        <span><|SERVICE_HEAD1|></span>
                        <h4 class="services-two-title"><|SERVICE_SUB1|></h4>
                     </div>
                  </div>
               </div>
               <div class="col-lg-6">
                  <div class="services-two mb-30">
                     <div class="services-two-bg"></div>
                     <div class="services-two-icon">
                        <img src="images/services-icon-2.png" alt>
                     </div>
                     <div class="services-two-content">
                        <span><|SERVICE_HEAD2|></span>
                        <h4 class="services-two-title"><|SERVICE_SUB2|></h4>
                     </div>
                  </div>
               </div>
               <div class="col-lg-6">
                  <div class="services-two mb-30">
                     <div class="services-two-bg"></div>
                     <div class="services-two-icon">
                        <img src="images/services-icon-3.png" alt>
                     </div>
                     <div class="services-two-content">
                        <span><|SERVICE_HEAD3|></span>
                        <h4 class="services-two-title"><|SERVICE_SUB3|></h4>
                     </div>
                  </div>
               </div>
               <div class="col-lg-6">
                  <div class="services-two mb-30">
                     <div class="services-two-bg"></div>
                     <div class="services-two-icon">
                        <img src="images/services-icon-4.png" alt>
                     </div>
                     <div class="services-two-content">
                        <span><|SERVICE_HEAD4|></span>
                        <h4 class="services-two-title"><|SERVICE_SUB4|></h4>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </section>
      <!-- services-area-end -->

      

      

      

      <!-- testimonial-area-start -->
      <section class="testimonial-area pt-85" id="test">
         <div class="container">
            <div class="tptestimonial-two-bg">
               <div class="row justify-content-center">
                  <div class="col-xxl-8 col-lg-10 col-md-9">
                     <div class="tptestimonial-area-two p-relative">
                        <div class="tptestimonial-active-two">
                           <div class="tptestimonial-two-item">
                              <div class="tptestimonial-two">
                                 <div class="tptestimonial-two-avatar">
                                    <img src="<|TESTMONIAL_USER_IMG1|>" alt>
                                 </div>
                                 <div class="tptestimonial-two-content">
                                    <i>
                                       <svg width="32" height="20" viewBox="0 0 32 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                          <path d="M10.3376 2.213C9.04053 2.94247 8.04356 3.73741 7.34664 4.59782C6.63037 5.45823 6.13672 6.47762 5.8657 7.656C6.13672 7.58119 6.4271 7.51572 6.73684 7.45961C7.04658 7.40349 7.42408 7.37544 7.86933 7.37544C8.87598 7.37544 9.79552 7.51572 10.628 7.79629C11.441 8.07686 12.1476 8.479 12.7477 9.00273C13.3285 9.54516 13.7834 10.2092 14.1125 10.9948C14.4223 11.7803 14.5771 12.6782 14.5771 13.6882C14.5771 14.5673 14.4223 15.3903 14.1125 16.1572C13.7834 16.9241 13.3188 17.5881 12.7187 18.1492C12.0992 18.7291 11.3442 19.178 10.4537 19.496C9.54386 19.8326 8.51785 20.001 7.37568 20.001C6.38839 20.001 5.44949 19.8139 4.55898 19.4398C3.64912 19.0845 2.8651 18.5701 2.2069 17.8967C1.52934 17.2234 0.996977 16.4097 0.6098 15.4558C0.203268 14.5206 0 13.4731 0 12.3134C0 10.7984 0.212948 9.42358 0.63884 8.18908C1.06473 6.97329 1.65517 5.86973 2.41016 4.87839C3.1458 3.90575 4.02662 3.0547 5.05263 2.32522C6.07865 1.59575 7.19177 0.969145 8.39202 0.445419L10.3376 2.213ZM27.7604 2.213C26.4634 2.94247 25.4664 3.73741 24.7695 4.59782C24.0532 5.45823 23.5596 6.47762 23.2886 7.656C23.5596 7.58119 23.85 7.51572 24.1597 7.45961C24.4694 7.40349 24.8469 7.37544 25.2922 7.37544C26.2989 7.37544 27.2184 7.51572 28.0508 7.79629C28.8639 8.07686 29.5705 8.479 30.1706 9.00273C30.7514 9.54516 31.2063 10.2092 31.5354 10.9948C31.8451 11.7803 32 12.6782 32 13.6882C32 14.5673 31.8451 15.3903 31.5354 16.1572C31.2063 16.9241 30.7417 17.5881 30.1416 18.1492C29.5221 18.7291 28.7671 19.178 27.8766 19.496C26.9667 19.8326 25.9407 20.001 24.7985 20.001C23.8113 20.001 22.8724 19.8139 21.9819 19.4398C21.072 19.0845 20.288 18.5701 19.6298 17.8967C18.9522 17.2234 18.4198 16.4097 18.0327 15.4558C17.6261 14.5206 17.4229 13.4731 17.4229 12.3134C17.4229 10.7984 17.6358 9.42358 18.0617 8.18908C18.4876 6.97329 19.078 5.86973 19.833 4.87839C20.5687 3.90575 21.4495 3.0547 22.4755 2.32522C23.5015 1.59575 24.6146 0.969145 25.8149 0.445419L27.7604 2.213Z" fill="#C0BBB5"/>
                                       </svg>
                                    </i>
                                    <p><|TESTMONIAL_USER_WORDS1|>
                                    </p>
                                    <div class="tptestimonial-two-avatar-info">
                                       <h5 class="title"><|TESTMONIAL_USER_NAME1|></h5>
                                      
                                    </div>
                                 </div>
                              </div>
                           </div>
                           <div class="tptestimonial-two-item">
                              <div class="tptestimonial-two">
                                 <div class="tptestimonial-two-avatar">
                                    <img src="<|TESTMONIAL_USER_IMG2|>" alt>
                                 </div>
                                 <div class="tptestimonial-two-content">
                                    <i>
                                       <svg width="32" height="20" viewBox="0 0 32 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                          <path d="M10.3376 2.213C9.04053 2.94247 8.04356 3.73741 7.34664 4.59782C6.63037 5.45823 6.13672 6.47762 5.8657 7.656C6.13672 7.58119 6.4271 7.51572 6.73684 7.45961C7.04658 7.40349 7.42408 7.37544 7.86933 7.37544C8.87598 7.37544 9.79552 7.51572 10.628 7.79629C11.441 8.07686 12.1476 8.479 12.7477 9.00273C13.3285 9.54516 13.7834 10.2092 14.1125 10.9948C14.4223 11.7803 14.5771 12.6782 14.5771 13.6882C14.5771 14.5673 14.4223 15.3903 14.1125 16.1572C13.7834 16.9241 13.3188 17.5881 12.7187 18.1492C12.0992 18.7291 11.3442 19.178 10.4537 19.496C9.54386 19.8326 8.51785 20.001 7.37568 20.001C6.38839 20.001 5.44949 19.8139 4.55898 19.4398C3.64912 19.0845 2.8651 18.5701 2.2069 17.8967C1.52934 17.2234 0.996977 16.4097 0.6098 15.4558C0.203268 14.5206 0 13.4731 0 12.3134C0 10.7984 0.212948 9.42358 0.63884 8.18908C1.06473 6.97329 1.65517 5.86973 2.41016 4.87839C3.1458 3.90575 4.02662 3.0547 5.05263 2.32522C6.07865 1.59575 7.19177 0.969145 8.39202 0.445419L10.3376 2.213ZM27.7604 2.213C26.4634 2.94247 25.4664 3.73741 24.7695 4.59782C24.0532 5.45823 23.5596 6.47762 23.2886 7.656C23.5596 7.58119 23.85 7.51572 24.1597 7.45961C24.4694 7.40349 24.8469 7.37544 25.2922 7.37544C26.2989 7.37544 27.2184 7.51572 28.0508 7.79629C28.8639 8.07686 29.5705 8.479 30.1706 9.00273C30.7514 9.54516 31.2063 10.2092 31.5354 10.9948C31.8451 11.7803 32 12.6782 32 13.6882C32 14.5673 31.8451 15.3903 31.5354 16.1572C31.2063 16.9241 30.7417 17.5881 30.1416 18.1492C29.5221 18.7291 28.7671 19.178 27.8766 19.496C26.9667 19.8326 25.9407 20.001 24.7985 20.001C23.8113 20.001 22.8724 19.8139 21.9819 19.4398C21.072 19.0845 20.288 18.5701 19.6298 17.8967C18.9522 17.2234 18.4198 16.4097 18.0327 15.4558C17.6261 14.5206 17.4229 13.4731 17.4229 12.3134C17.4229 10.7984 17.6358 9.42358 18.0617 8.18908C18.4876 6.97329 19.078 5.86973 19.833 4.87839C20.5687 3.90575 21.4495 3.0547 22.4755 2.32522C23.5015 1.59575 24.6146 0.969145 25.8149 0.445419L27.7604 2.213Z" fill="#C0BBB5"/>
                                       </svg>
                                    </i>
                                    <p><|TESTMONIAL_USER_WORDS2|>
                                    </p>
                                    <div class="tptestimonial-two-avatar-info">
                                       <h5 class="title"><|TESTMONIAL_USER_NAME2|></h5>
                                       
                                    </div>
                                 </div>
                              </div>
                           </div>
                           <div class="tptestimonial-two-item">
                              <div class="tptestimonial-two">
                                 <div class="tptestimonial-two-avatar">
                                    <img src="<|TESTMONIAL_USER_IMG3|>" alt>
                                 </div>
                                 <div class="tptestimonial-two-content">
                                    <i>
                                       <svg width="32" height="20" viewBox="0 0 32 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                          <path d="M10.3376 2.213C9.04053 2.94247 8.04356 3.73741 7.34664 4.59782C6.63037 5.45823 6.13672 6.47762 5.8657 7.656C6.13672 7.58119 6.4271 7.51572 6.73684 7.45961C7.04658 7.40349 7.42408 7.37544 7.86933 7.37544C8.87598 7.37544 9.79552 7.51572 10.628 7.79629C11.441 8.07686 12.1476 8.479 12.7477 9.00273C13.3285 9.54516 13.7834 10.2092 14.1125 10.9948C14.4223 11.7803 14.5771 12.6782 14.5771 13.6882C14.5771 14.5673 14.4223 15.3903 14.1125 16.1572C13.7834 16.9241 13.3188 17.5881 12.7187 18.1492C12.0992 18.7291 11.3442 19.178 10.4537 19.496C9.54386 19.8326 8.51785 20.001 7.37568 20.001C6.38839 20.001 5.44949 19.8139 4.55898 19.4398C3.64912 19.0845 2.8651 18.5701 2.2069 17.8967C1.52934 17.2234 0.996977 16.4097 0.6098 15.4558C0.203268 14.5206 0 13.4731 0 12.3134C0 10.7984 0.212948 9.42358 0.63884 8.18908C1.06473 6.97329 1.65517 5.86973 2.41016 4.87839C3.1458 3.90575 4.02662 3.0547 5.05263 2.32522C6.07865 1.59575 7.19177 0.969145 8.39202 0.445419L10.3376 2.213ZM27.7604 2.213C26.4634 2.94247 25.4664 3.73741 24.7695 4.59782C24.0532 5.45823 23.5596 6.47762 23.2886 7.656C23.5596 7.58119 23.85 7.51572 24.1597 7.45961C24.4694 7.40349 24.8469 7.37544 25.2922 7.37544C26.2989 7.37544 27.2184 7.51572 28.0508 7.79629C28.8639 8.07686 29.5705 8.479 30.1706 9.00273C30.7514 9.54516 31.2063 10.2092 31.5354 10.9948C31.8451 11.7803 32 12.6782 32 13.6882C32 14.5673 31.8451 15.3903 31.5354 16.1572C31.2063 16.9241 30.7417 17.5881 30.1416 18.1492C29.5221 18.7291 28.7671 19.178 27.8766 19.496C26.9667 19.8326 25.9407 20.001 24.7985 20.001C23.8113 20.001 22.8724 19.8139 21.9819 19.4398C21.072 19.0845 20.288 18.5701 19.6298 17.8967C18.9522 17.2234 18.4198 16.4097 18.0327 15.4558C17.6261 14.5206 17.4229 13.4731 17.4229 12.3134C17.4229 10.7984 17.6358 9.42358 18.0617 8.18908C18.4876 6.97329 19.078 5.86973 19.833 4.87839C20.5687 3.90575 21.4495 3.0547 22.4755 2.32522C23.5015 1.59575 24.6146 0.969145 25.8149 0.445419L27.7604 2.213Z" fill="#C0BBB5"/>
                                       </svg>
                                    </i>
                                    <p><|TESTMONIAL_USER_WORDS3|>
                                    </p>
                                    <div class="tptestimonial-two-avatar-info">
                                       <h5 class="title"><|TESTMONIAL_USER_NAME3|></h5>
                                      
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                        <div class="tptestimonial-two-nav"></div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </section>
      <!-- testimonial-area-end -->

      <!-- faq-area-start -->
      <section class="faq-area pt-115 pb-15" id="faqs">
         <div class="container">
            <div class="row">
               <div class="col-lg-6">
                  <div class="tp-faq-wrapper mb-80">
                     <div class="tpsection-wrapper mb-25">
                        <h2 class="tpsection-title-two mb-40">Frequently<br> Asked
                           <span>
                              Questions
                              <svg width="306" height="31" viewBox="0 0 306 31" fill="none" xmlns="http://www.w3.org/2000/svg">
                                 <path d="M2.89242 18.9903C2.89242 18.9903 192.778 -5.15589 299.226 12.3064" stroke="#FFCE5A" stroke-width="5" stroke-linecap="round"/>
                                 <path d="M3.2201 14.9796C3.2201 14.9796 196.633 -0.186388 302.688 21.9968" stroke="#FFCE5A" stroke-width="5" stroke-linecap="round"/>
                              </svg>
                           </span>
                        </h2>
                        <p>Can’t find what you are looking for?</p>
                        <b>We would like to chat with you.</b>
                     </div>
                     <div class="tp-faq-img p-relative">
                        <span>
                           <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path opacity="0.4" d="M29.6447 26.693L30.3466 32.3807C30.5266 33.8746 28.9247 34.9186 27.6467 34.1446L20.105 29.6628C19.2771 29.6628 18.4671 29.6088 17.6752 29.5008C19.0071 27.9349 19.7991 25.9549 19.7991 23.813C19.7991 18.7012 15.3712 14.5615 9.89945 14.5615C7.81153 14.5615 5.88562 15.1554 4.28368 16.1994C4.22968 15.7494 4.21167 15.2994 4.21167 14.8314C4.21167 6.64172 11.3214 0 20.105 0C28.8887 0 35.9984 6.64172 35.9984 14.8314C35.9984 19.6912 33.4965 23.9931 29.6447 26.693Z" fill="white"/>
                              <path d="M19.7992 23.8126C19.7992 25.9545 19.0073 27.9345 17.6753 29.5004C15.8934 31.6603 13.0675 33.0462 9.89961 33.0462L5.20179 35.8361C4.40982 36.3221 3.40186 35.6561 3.50985 34.7382L3.95984 31.1924C1.54793 29.5184 0 26.8365 0 23.8126C0 20.6447 1.69194 17.8549 4.28384 16.1989C5.88577 15.155 7.81169 14.561 9.89961 14.561C15.3714 14.561 19.7992 18.7008 19.7992 23.8126Z" fill="white"/>
                           </svg>
                        </span>
                        <!-- <img src="assets/img/shape/faq-shape-1.png" alt=""> -->
                        <div class="tp-faq-shape">
                           <img src="images/faq-shape-2.png" alt>
                        </div>
                     </div>
                  </div>
               </div>
               <div class="col-lg-6">
                  <div class="tp-accordion tp-green-accordion">
                     <div class="accordion mb-35" id="accordionExample">
                        <div class="accordion-item">
                           <h2 class="accordion-header" id="headingOne">
                              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
                                 <|FAQ1|>
                              </button>
                           </h2>
                           <div id="collapseOne" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
                              <div class="accordion-body">
                                 <|FAQ_ANS1|>
                              </div>
                           </div>
                        </div>
                        <div class="accordion-item">
                           <h2 class="accordion-header" id="headingTwo">
                              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                                 <|FAQ2|>
                              </button>
                           </h2>
                           <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
                              <div class="accordion-body">
                                 <|FAQ_ANS2|>
                              </div>
                           </div>
                        </div>
                        <div class="accordion-item">
                           <h2 class="accordion-header" id="headingThree">
                              <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="true" aria-controls="collapseThree">
                                <|FAQ3|>
                              </button>
                           </h2>
                           <div id="collapseThree" class="accordion-collapse collapse show" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
                              <div class="accordion-body">
                                 <|FAQ_ANS3|>
                              </div>
                           </div>
                        </div>
                        
                     </div>
                     <div class="tp-accordion-btn">
                        <a href="<|CONTACT_LINK|>">Conctact Us <i class="fa-light fa-arrow-right"></i></a>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </section>
      <!-- faq-area-end -->

      <!-- social-area-start -->
      <div class="social-area pt-120">
         <div class="container">
            <div class="row">
               <div class="col-lg-6">
                  <div class="tpsocial tpsocial-facebook mb-30">
                     <div class="tpsocial-bg"></div>
                     <div class="tpsocial-text">
                        <a href="<|FB_LINK|>"><i class="fa-brands fa-facebook"></i> Follow us on Facebook for Small Busoness
                           Updates</a>
                     </div>
                  </div>
               </div>
               <div class="col-lg-6">
                  <div class="tpsocial tpsocial-insta mb-30">
                     <div class="tpsocial-bg"></div>
                     <div class="tpsocial-text">
                        <a href="<|IG_LINK|>"><i class="fa-brands fa-instagram"></i> Follow us on Instagram for Small Business
                           Inspiration</a>
                     </div>
                  </div>
               </div>
               <div class="col-lg-6">
                  <div class="tpsocial tpsocial-pin mb-30">
                     <div class="tpsocial-bg"></div>
                     <div class="tpsocial-text">
                        <a href="<|YT_LINK|>"><i class="fa-brands fa-youtube"></i> Get our Newsletter for Small Business Tips &
                           News</a>
                     </div>
                  </div>
               </div>
               <div class="col-lg-6">
                  <div class="tpsocial tpsocial-twitt mb-30">
                     <div class="tpsocial-bg"></div>
                     <div class="tpsocial-text">
                        <a href="<|TWT_LINK|>"><i class="fa-brands fa-twitter"></i> Follow us on Twitter for Small Busoness
                           Updates</a>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
      <!-- social-area-end -->

      <!-- cta-area-start -->
      <section id="contact-one-page" class="cta-area pt-105">
         <div class="container">
            <div class="row justify-content-center">
               <div class="col-lg-8">
                  <div class="tpsection-wrapper text-center mb-50">
                     <p>No time to wait ? Call us ☕️ 🍞</p>
                     <h2 class="tpsection-title-two">Get into Touch.. <br>
                     </h2>
                  </div>
               </div>
            </div>
            <div class="row justify-content-center">
               <div class="col-lg-6">
                  <div class="tpcta-wrapper text-center">
                     <a class="tpcta-btn mr-5" href="tel:<|PHONE_NUMBER|>"><|PHONE_NUMBER|></a>
                     <a class="green-btn" href="<|CONTACT_LINK|>">Contact Us</a>
                  </div>
               </div>
            </div>
         </div>
      </section>
      <!-- cta-area-end -->

      <!-- brand-area-start -->
      <div class="brand-area pb-30 pt-85">
         <div class="container">
            <div class="row justify-content-center">
               <div class="col-xxl-10 col-xl-8 col-lg-10">
                  <div class="tpbrand tpbrand-active">
                     <div class="tpbrand-item">
                        <img src="images/brand-1.png" alt>
                     </div>
                     <div class="tpbrand-item">
                        <img src="images/brand-2.png" alt>
                     </div>
                     <div class="tpbrand-item">
                        <img src="images/brand-3.png" alt>
                     </div>
                     <div class="tpbrand-item">
                        <img src="images/brand-4.png" alt>
                     </div>
                     <div class="tpbrand-item">
                        <img src="images/brand-5.png" alt>
                     </div>
                     <div class="tpbrand-item">
                        <img src="images/brand-6.png" alt>
                     </div>
                     <div class="tpbrand-item">
                        <img src="images/brand-4.png" alt>
                     </div>
                     <div class="tpbrand-item">
                        <img src="images/brand-5.png" alt>
                     </div>
                     <div class="tpbrand-item">
                        <img src="images/brand-6.png" alt>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
      <!-- brand-area-end -->

   </main>

   <!-- footer-area-start -->
   <footer>
      <div class="footer-area pt-100 footer-bg2 p-relative">
         <div class="footer-main-shape">
            <img src="images/footer-2-bg-2.png" alt>
         </div>
         <div class="footer-shape-left d-none d-xl-block">
            <div class="footer-shape-left-one">
               <img src="images/footer-dew-shape.png" alt="footer-shape">
            </div>
            <div class="footer-shape-left-two">
               <img src="images/footer-dot-1.png" alt="footer-shape">
            </div>
            <div class="footer-shape-left-three">
               <img src="images/footer-leaf-shape.png" alt="footer-shape">
            </div>
            <div class="footer-shape-left-four">
               <img src="images/footer-man-shape.png" alt="footer-shape">
            </div>
         </div>
         <div class="footer-shape-right d-none d-xl-block">
            <div class="footer-shape-right-one">
               <img src="images/footer-man-shape-2.png" alt="footer-shape">
            </div>
            <div class="footer-shape-right-two">
               <img src="images/footer-dot-1.png" alt="footer-shape">
            </div>
            <div class="footer-shape-right-three">
               <img src="images/footer-plant.png" alt="footer-shape">
            </div>
            <div class="footer-shape-right-four">
               <img src="images/footer-rocket.png" alt="footer-shape">
            </div>
         </div>
         <div class="container">
            <div class="footer-top">
               <div class="row">
                  <div class="col-lg-3 col-md-6 col-sm-12">
                     <div class="footer-widget footer-2-col-1 mb-30">
                        <div class="footer-widget-logo mb-20">
                           <a href="index.html">
                              <span>
                                 <svg width="105" height="26" viewBox="0 0 105 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" clip-rule="evenodd" d="M50.953 12.563C50.953 14.8455 50.2037 16.7587 48.6946 18.3133C47.4476 19.5977 45.9813 20.3603 44.2955 20.5771V22.7445H45.2588V24.8771C47.8142 24.4891 50.0405 23.3332 51.9457 21.4146C54.3432 19.0064 55.5393 16.063 55.5393 12.5844C55.5393 11.5836 55.435 10.6257 55.2396 9.70788C55.1968 9.49382 55.1406 9.28243 55.0871 9.07371C55.5367 8.92654 55.8578 8.50376 55.8578 8.00606C55.8578 7.73313 55.7588 7.48695 55.6009 7.29429L58.6379 2.81228C58.7209 2.82834 58.5282 2.83904 58.8788 2.83904C59.2293 2.83904 59.9999 2.33599 59.9999 1.71787C59.9999 1.09976 59.4969 0.596703 58.8788 0.596703C58.2606 0.596703 57.7629 1.28707 57.7629 1.71787C57.7629 2.15136 57.8405 2.18882 57.9717 2.37345L54.9078 6.89827L54.7393 6.88221C54.5814 6.88221 54.4315 6.91432 54.2951 6.97587C54.1319 7.04811 53.982 7.16317 53.875 7.29964L48.6732 5.69682C48.6063 5.13758 48.1327 4.71212 47.5627 4.71212C47.1587 4.71212 46.8028 4.92619 46.6048 5.24728C46.5004 5.41586 46.4415 5.61387 46.4415 5.83329C46.4415 6.08482 46.5298 6.31494 46.6717 6.50492L43.3617 11.4445C43.2948 11.4338 43.2305 11.4284 43.1637 11.4284C42.5455 11.4284 42.0425 11.9261 42.0425 12.5443C42.0425 13.1624 42.5455 13.6654 43.1637 13.6654C43.7818 13.6654 44.2795 13.1624 44.2795 12.5443C44.2795 12.2874 44.1912 12.0519 44.044 11.8592L47.3353 6.9277C47.4075 6.94376 47.4771 6.94911 47.5547 6.94911C47.8999 6.94911 48.2103 6.79123 48.4136 6.54506C48.5019 6.63336 48.5875 6.71899 48.6758 6.80729C48.8498 6.9946 49.021 7.17923 49.1789 7.37724C50.3616 8.83021 50.953 10.5641 50.953 12.563Z" fill="#59B642"/>
                                    <path fill-rule="evenodd" clip-rule="evenodd" d="M43.1396 4.44722C44.1618 4.44722 45.1197 4.62115 46.0001 4.97168C46.2997 4.42581 46.8804 4.0512 47.5547 4.0512C48.2932 4.0512 48.9381 4.51144 49.2003 5.17237L53.6984 6.55577C53.7921 6.4969 53.8857 6.44071 53.982 6.39254C53.4281 5.41854 52.7351 4.50609 51.8922 3.65785C49.4706 1.22553 46.57 0 43.2065 0C40.9802 0 38.9011 0.559247 36.9692 1.67507C35.0426 2.79624 33.528 4.31343 32.4283 6.22129C31.6898 7.50569 31.1974 8.87571 30.9512 10.3233C28.452 10.3233 25.9073 10.2966 23.3733 10.2966V14.6742C25.9287 14.6742 28.4065 14.7063 30.9512 14.7063C31.3606 17.1895 32.4845 19.3944 34.3281 21.3156C36.1878 23.269 38.4302 24.4517 41.0525 24.8611V24.845C41.7535 24.9654 42.476 25.0323 43.2092 25.0323C43.6346 25.0323 44.0628 25.0109 44.4722 24.9735V23.5339H43.5089V20.5717C43.3885 20.5771 43.2627 20.5824 43.1423 20.5824C40.9428 20.5824 39.0938 19.8118 37.6006 18.2786C36.1396 16.7801 35.3904 14.891 35.3583 12.5951C35.3583 10.2324 36.1022 8.28435 37.6006 6.7511C39.0911 5.22053 40.9401 4.44722 43.1396 4.44722Z" fill="#010F1C"/>
                                    <path fill-rule="evenodd" clip-rule="evenodd" d="M17.0476 0.596703H30.0575V5.04392H21.5617C21.5617 10.0236 21.5617 15.0007 21.5617 19.9804H30.0575V24.4276H17.0476V0.596703Z" fill="#010F1C"/>
                                    <path fill-rule="evenodd" clip-rule="evenodd" d="M14.5752 3.83981L11.209 6.8073C10.0317 5.17237 8.83022 4.35089 7.61004 4.35089C7.00798 4.35089 6.52098 4.50876 6.14904 4.82719C5.7664 5.14561 5.57909 5.50685 5.57909 5.90554C5.57909 6.30424 5.71021 6.68688 5.97779 7.03742C6.34973 7.51371 7.4602 8.53053 9.31454 10.0959C11.0512 11.5435 12.1028 12.4586 12.4693 12.8359C13.3898 13.7671 14.0454 14.6528 14.428 15.4957C14.8107 16.3493 15.0087 17.2751 15.0087 18.2759C15.0087 20.2346 14.329 21.8428 12.9724 23.1245C11.6265 24.3928 9.86041 25.035 7.68229 25.035C5.98047 25.035 4.50341 24.6203 3.24577 23.7881C1.98011 22.9452 0.896401 21.6447 0 19.86L3.82375 17.5561C4.97168 19.662 6.29621 20.7136 7.78932 20.7136C8.57066 20.7136 9.22892 20.4834 9.75873 20.0285C10.2885 19.579 10.5588 19.0492 10.5588 18.4578C10.5588 17.9227 10.3554 17.3795 9.95139 16.839C9.55804 16.3038 8.67235 15.4716 7.30232 14.3611C4.7041 12.2499 3.02368 10.6123 2.2691 9.46439C1.50916 8.31646 1.13187 7.17121 1.13187 6.02328C1.13187 4.3723 1.76069 2.95411 3.01298 1.77675C4.27864 0.591357 5.8333 0 7.68229 0C8.87036 0 10.0022 0.278286 11.0806 0.82683C12.1563 1.37805 13.3176 2.37881 14.5752 3.83981Z" fill="#010F1C"/>
                                    <path d="M83.8083 24.503H79.2406V8.14876C79.2406 7.82934 79.1767 7.53122 79.0489 7.25439C78.9318 6.97756 78.7668 6.738 78.5538 6.5357C78.3515 6.32275 78.112 6.15772 77.8351 6.0406C77.5583 5.92348 77.2602 5.86492 76.9408 5.86492C76.6213 5.86492 76.3232 5.92348 76.0464 6.0406C75.7695 6.15772 75.5247 6.32275 75.3117 6.5357C75.1094 6.738 74.9497 6.97756 74.8326 7.25439C74.7155 7.53122 74.6569 7.82934 74.6569 8.14876V24.503H70.0732V8.14876C70.0732 7.82934 70.0147 7.53122 69.8976 7.25439C69.7804 6.97756 69.6154 6.738 69.4025 6.5357C69.2002 6.32275 68.9606 6.15772 68.6838 6.0406C68.4069 5.92348 68.1088 5.86492 67.7894 5.86492C67.47 5.86492 67.1718 5.92348 66.895 6.0406C66.6182 6.15772 66.3733 6.32275 66.1604 6.5357C65.9581 6.738 65.7983 6.97756 65.6812 7.25439C65.5641 7.53122 65.5055 7.82934 65.5055 8.14876V24.503H60.9219V8.14876C60.9219 7.20115 61.0976 6.3121 61.4489 5.48161C61.8109 4.64048 62.3007 3.91114 62.9182 3.29359C63.5464 2.6654 64.2758 2.17562 65.1063 1.82426C65.9474 1.46225 66.8418 1.28125 67.7894 1.28125C68.6412 1.28125 69.461 1.43564 70.2489 1.74441C71.0368 2.04253 71.7449 2.47907 72.3731 3.05403C73.0012 2.47907 73.704 2.04253 74.4812 1.74441C75.2691 1.43564 76.089 1.28125 76.9408 1.28125C77.8884 1.28125 78.7774 1.46225 79.6079 1.82426C80.449 2.17562 81.1784 2.6654 81.7959 3.29359C82.4241 3.91114 82.9139 4.64048 83.2653 5.48161C83.6273 6.3121 83.8083 7.20115 83.8083 8.14876V24.503Z" fill="#010F1C"/>
                                    <path d="M98.0544 24.503H93.4867V17.3321C92.4752 17.0765 91.5435 16.6666 90.6917 16.1023C89.8506 15.538 89.1266 14.8672 88.5197 14.09C87.9128 13.3021 87.439 12.4343 87.0983 11.4867C86.7682 10.5284 86.6032 9.52227 86.6032 8.46818V1.60067H91.1868V8.46818C91.1868 9.09637 91.304 9.69262 91.5382 10.2569C91.7831 10.8106 92.1132 11.295 92.5284 11.7103C92.9437 12.1255 93.4281 12.4556 93.9818 12.7005C94.5461 12.9347 95.1423 13.0518 95.7705 13.0518C96.3987 13.0518 96.9896 12.9347 97.5433 12.7005C98.1076 12.4556 98.5974 12.1255 99.0126 11.7103C99.4279 11.295 99.7526 10.8106 99.9868 10.2569C100.232 9.69262 100.354 9.09637 100.354 8.46818V1.60067H104.922V8.46818C104.922 9.52227 104.752 10.5284 104.411 11.4867C104.081 12.4343 103.612 13.3021 103.005 14.09C102.398 14.8672 101.674 15.538 100.833 16.1023C99.9922 16.6666 99.0659 17.0765 98.0544 17.3321V24.503Z" fill="#010F1C"/>
                                 </svg>
                              </span>
                           </a>
                        </div>
                        <div class="footer-widget-newsletter2 mb-40">
                           <h4 class="title">Subscribe our Newsletter!</h4>
                           <form action="#">
                              <div class="footer-widget-newsletter2-input2">
                                 <input type="email" placeholder="Email">
                                 <button>Subscribe</button>
                              </div>
                           </form>
                        </div>
                        <div class="footer-widget-content">
                           <div class="footer-widget-social2">
                              <a class="footer-facebook" href="<|FB_LINK|>"><i class="fa-brands fa-facebook-f"></i></a>
                              <a href="<|TWT_LINK|>"><i class="fa-brands fa-twitter"></i></a>
                              <a class="footer-linkedin" href="<|YT_LINK|>"><i class="fa-brands fa-youtube"></i></a>
                              <a class="footer-insta" href="<|IG_LINK|>"><i class="fa-brands fa-instagram"></i></a>
                           </div>
                        </div>
                     </div>
                  </div>
                  <div class="col-lg-3 col-md-6 col-sm-6">
                     <div class="footer-widget footer-widget-2 footer-2-col-2 mb-40">
                        <h4 class="footer-widget-title mb-15">Information</h4>
                        <div class="footer-widget-link">
                           <ul>
                              <li><a href="#home">Home</a></li>
                              <li><a href="#about">About Us</a></li>
                              <li><a href="#services-one-page">Service</a></li>
                              <li><a href="#test">Testmonial</a></li>
                              <li><a href="#contact-one-page">Contact Us</a></li>
                           </ul>
                        </div>
                     </div>
                  </div>
                  <div class="col-lg-3 col-md-6 col-sm-6">
                     
                  </div>
                  <div class="col-lg-3 col-md-6 col-sm-6">
                     <div class="footer-widget footer-widget-2 footer-2-col-4 mb-40">
                        <h4 class="footer-widget-title mb-20">Contact Us</h4>
                        <div class="tpcontact-info-links">
                           <a href="tel:<|PHONE_NUMBER|>">
                              <i><img src="images/phone-icon.png" alt></i> <|PHONE_NUMBER|>
                           </a>
                           <a href="mailto:information@gmail.com">
                              <i><img src="images/massage-icon.png" alt></i><|MAIL|>
                           </a>
                           <a href="#">
                              <i><img src="images/location-icon.png" alt></i> <|ADDRESS|>
                           </a>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
            <div class="footer-bottom">
               <div class="row">
                  <div class="col-lg-12">
                     <div class="footer-widget-copyright footer-widget-copyright2 text-center">
                        <span>© 2023 Copyrights by company. All Rights Reserved. Designed by <a target="_blank" href="https://themeforest.net/user/theme_pure/portfolio">Theme_Pure.</a></span>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </footer>
   <!-- footer-area-end -->


   <!-- JS here -->
   <script src="js/jquery.js"></script>
   <script src="js/waypoints.js"></script>
   <script src="js/bootstrap-bundle.js"></script>
   <script src="js/meanmenu.js"></script>
   <script src="js/swiper-bundle.js"></script>
   <script src="js/slick.js"></script>
   <script src="js/nouislider.js"></script>
   <script src="js/magnific-popup.js"></script>
   <script src="js/parallax.js"></script>
   <script src="js/nice-select.js"></script>
   <script src="js/wow.js"></script>
   <script src="js/isotope-pkgd.js"></script>
   <script src="js/imagesloaded-pkgd.js"></script>
   <script src="js/purecounter.js"></script>
   <script src="js/parallax-scroll.js"></script>
   <script src="js/ajax-form.js"></script>
   <script src="js/main.js"></script>
</body>

</html>'''



print("====================================================")
print("====================================================")
print("====================================================")
print("Loading the files from database.....")
url='https://github.com/hackerstore/WebAi-Gen/raw/main/theme-src/ComData.zip'
wget.download(url)
with ZipFile("ComData.zip", 'r') as zObject:
		zObject.extractall(path = location )
os.remove("ComData.zip")
time.sleep(5)
time.sleep(2)
print(" ")
print("====================================================")
print("====================================================")
print("Selected Theme : ComData")
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
	colorlib1_name = input("Your Company Name : ")
	colorlib1_solgon = input("Your Slogon: ")
	colorlib1_mainkeyword = input("Your Company Main Keyword: ")
	colorlib1_mainhead = input("Main Heading of the Website: ")
	colorlib1_subhead = input("Sub Heading of the Website: ")
	colorlib1_aboutcompany = input("A Small Short Note About Your Company: ")
	colorlib1_satfiedclint = input("The Percentage rate of Satisfied Clients (100): ")
	colorlib1_unsatfiedclint = input("The Percentage rate of Unsatisfied Clients (100): ")
	print("========================================")
	time.sleep(2)
	print("Setting The Datas")
	time.sleep(2)
	print("Let's Jump to Service Section....")
	time.sleep(1)
	colorlib1_servicehead1 = input("Your First Service : ")
	colorlib1_servicecontent1 = input("A Small Note for It : ")
	colorlib1_servicehead2 = input("Your Second Service : ")
	colorlib1_servicecontent2 = input("A Small Note for It : ")
	colorlib1_servicehead3 = input("Your Thrid Service : ")
	colorlib1_servicecontent3 = input("A Small Note for It : ")
	colorlib1_servicehead4 = input("Your Fourth Service : ")
	colorlib1_servicecontent4 = input("A Small Note for It : ")
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
	print("Let's Jump to FQS Section....")
	time.sleep(1)
	colorlib1_faq1 = input("FAQ First Question : ")
	colorlib1_faqans1 = input("FAQ First Answer : ")
	colorlib1_faq2 = input("FAQ First Question : ")
	colorlib1_faqans2 = input("FAQ Second Answer : ")
	colorlib1_faq3 = input("FAQ First Question : ")
	colorlib1_faqans3 = input("FAQ Thrid Answer : ")
	print("========================================")
	print("This Section Finished.....")
	time.sleep(2)
	print("Setting The Datas")
	time.sleep(2)
	print("Let's Jump to Contact Section....")
	time.sleep(1)
	colorlib1_contactlink = input("Your Contact Main Contact Link: ")
	colorlib1_fblink = input("Your Facebook Link : ")
	colorlib1_twtlink = input("Your Twitter Link: ")
	colorlib1_ytlink = input("Your Youtube Link : ")
	colorlib1_iglink = input("Your Instagram Link : ")
	colorlib1_mail = input("Your Email : ")
	colorlib1_address = input("Your Address : ")
	colorlib1_phonenumber = input("Your Phone Number : ")
	print("========================================")
	print("It Finished.....")
	time.sleep(1)
	print("Setting The Datas")
	time.sleep(2)
	print("We are editing the code.")
	print("This will take so time!!!!")


	


	xxx = thecode.replace("<|NAME|>", colorlib1_name).replace("<|SLOGAN|>", colorlib1_solgon).replace("<|CONTACT_LINK|>", colorlib1_contactlink).replace("<|FB_LINK|>", colorlib1_fblink).replace("<|TWT_LINK|>", colorlib1_twtlink).replace("<|YT_LINK|>", colorlib1_ytlink).replace("<|IG_LINK|>", colorlib1_iglink).replace("<|MAIN_KEYWORD|>", colorlib1_mainkeyword).replace("<|MAIN_HEAD|>", colorlib1_mainhead).replace("<|SUB_HEAD|>", colorlib1_subhead).replace("<|ABOUT_YOUR_COMPANY|>", colorlib1_aboutcompany).replace("<|SATFIED_CLINT_PERCET|>", colorlib1_satfiedclint).replace("<|UNSATFIED_CLINT_PERCET|>", colorlib1_unsatfiedclint).replace("<|SERVICE_HEAD1|>", colorlib1_servicehead1).replace("<|SERVICE_SUB1|>", colorlib1_servicecontent1).replace("<|SERVICE_HEAD2|>", colorlib1_servicehead2).replace("<|SERVICE_SUB2|>", colorlib1_servicecontent2).replace("<|SERVICE_HEAD3|>", colorlib1_servicehead3).replace("<|SERVICE_SUB3|>", colorlib1_servicecontent3).replace("<|SERVICE_HEAD4|>", colorlib1_servicehead4).replace("<|SERVICE_SUB4|>", colorlib1_servicecontent4).replace("<|TESTMONIAL_USER_IMG1|>", colorlib1_testominaluserimg1).replace("<|TESTMONIAL_USER_WORDS1|>", colorlib1_testominalusershort1).replace("<|TESTMONIAL_USER_NAME1|>", colorlib1_testominalusername1).replace("<|TESTMONIAL_USER_IMG2|>", colorlib1_testominaluserimg2).replace("<|TESTMONIAL_USER_WORDS2|>", colorlib1_testominalusershort2).replace("<|TESTMONIAL_USER_NAME2|>", colorlib1_testominalusername2).replace("<|TESTMONIAL_USER_IMG3|>", colorlib1_testominaluserimg3).replace("<|TESTMONIAL_USER_WORDS3|>", colorlib1_testominalusershort3).replace("<|TESTMONIAL_USER_NAME3|>", colorlib1_testominalusername3).replace("<|FAQ1|>", colorlib1_faq1).replace("<|FAQ_ANS1|>", colorlib1_faqans1).replace("<|FAQ2|>", colorlib1_faq2).replace("<|FAQ_ANS2|>", colorlib1_faqans2).replace("<|FAQ3|>", colorlib1_faq3).replace("<|FAQ_ANS3|>", colorlib1_faqans3).replace("<|PHONE_NUMBER|>", colorlib1_phonenumber).replace("<|MAIL|>", colorlib1_mail).replace("<|ADDRESS|>", colorlib1_address)
	with open('index.html', 'w', encoding='utf-8') as f:
		f.write(xxx)
	f.close()
	time.sleep(2)


	





elif y_or_n == "n":
	main()
elif y_or_n == "model":
	print("MOnjikko")