import os



f = open("gallery_generated.html", "w+")
f.write(
        """<!DOCTYPE html>
<html lang="en">

<head>
    <title> Gallery</title>
    <link rel="icon" type="image/png" href="../images/icons/kenya.png">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://fonts.googleapis.com/css?family=Josefin+Sans:300i,400,700" rel="stylesheet">
    <link rel="stylesheet" href="fonts/icomoon/style.css">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/magnific-popup.css">
    <link rel="stylesheet" href="css/jquery-ui.css">
    <link rel="stylesheet" href="css/owl.carousel.min.css">
    <link rel="stylesheet" href="css/owl.theme.default.min.css">
    <link rel="stylesheet" href="css/lightgallery.min.css">
    <link rel="stylesheet" href="css/bootstrap-datepicker.css">
    <link rel="stylesheet" href="fonts/flaticon/font/flaticon.css">
    <link rel="stylesheet" href="css/swiper.css">
    <link rel="stylesheet" href="css/aos.css">
    <link rel="stylesheet" href="css/style.css">
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-153603735-1"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', 'UA-153603735-1');
    </script>
</head>

<body>
    <div class="site-wrap">
        <div class="site-mobile-menu">
            <div class="site-mobile-menu-header">
                <div class="site-mobile-menu-close mt-3">
                    <span class="icon-close2 js-menu-toggle"></span>
                </div>
            </div>
            <div class="site-mobile-menu-body"></div>
        </div>
        <header class="site-navbar py-3 border-bottom" role="banner">

            <div class="container-fluid">
                <div class="row align-items-center">

                    <div class="col-6 col-xl-2" data-aos="fade-down">
                        <h6 class="mb-0"><a href="../index.html" class="text-black h3 mb-0">Virtual
                                Bhutan</a></h6>
                    </div>
                    <div class="col-10 col-md-8 d-none d-xl-block" data-aos="fade-down">
                        <nav class="site-navigation position-relative text-right text-lg-center" role="navigation">

                            <ul class="site-menu js-clone-nav mx-auto d-none d-lg-block">
                                <li><a href="../index.html">Home</a></li>
                                <li class=" has-children">
                                    <a href="https://phuens.github.io/Watson/gallery_templates/gallery.html">VR
                                        Expereinces</a>
                                    <ul class="dropdown">
                                        <li><a href="Bhutan.html">Twin Waterfall</a></li>
                                        <li><a href="Nepal.html">Bird Watching</a></li>
                                        <li><a href="Mongolia.html">Rafting</a></li>
                                        <li><a href="Tanzania.html">Jungle Lodge</a></li>

                                    </ul>
                                </li>
                                <li class="active">
                                    <a href="https://phuens.github.io/Watson/Books/books.html">Gallery</a>
                                </li>
                            </ul>
                        </nav>
                    </div>
                    <!-----------------------------------------------------------------------------------------------
            S O C I A L     M E D I A
            ------------------------------------------------------------------------------------------------>
                    <div class="col-6 col-xl-2 text-right" data-aos="fade-down">
                        <div class="d-none d-xl-inline-block">
                            <ul class="site-menu js-clone-nav ml-auto list-unstyled d-flex text-right mb-0"
                                data-class="social">
                                <li>
                                    <a href="https://www.facebook.com/c.phuntshonorbu" class="pl-0 pr-3"><span
                                            class="icon-facebook"></span></a>
                                </li>
                                <li>
                                    <a href="https://twitter.com/Pnorbs09" class="pl-3 pr-3"><span
                                            class="icon-twitter"></span></a>
                                </li>
                                <li>
                                    <a href="https://www.instagram.com/phuens/" class="pl-3 pr-3"><span
                                            class="icon-instagram"></span></a>
                                </li>
                                <li>
                                    <a href="https://www.youtube.com/channel/UCUWdiufzkd3yDDD-18oRGhA?view_as=subscriber"
                                        class="pl-3 pr-3"><span class="icon-youtube-play"></span></a>
                                </li>
                            </ul>
                        </div>
                        <div class="d-inline-block d-xl-none ml-md-0 mr-auto py-3"
                            style="position: relative; top: 3px;"><a href="#"
                                class="site-menu-toggle js-menu-toggle text-black"><span
                                    class="icon-menu h3"></span></a></div>
                    </div>
                </div>
            </div>
        </header>

        <!-----------------------------------------------------------------------------------------------
      P I C T U R E S
      ------------------------------------------------------------------------------------------------>
        <div class="site-section" data-aos="fade">
            <div class="container-fluid">
                <div class="row justify-content-center">
                    <div class="col-md-7">
                        <div class="row mb-5">
                            <div class="col-12 ">
                                <h2 class="site-section-heading text-center">Gallery</h2>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row" id="lightgallery">
        """
        )
directory = "/Users/phuntsho/Desktop/Projects/virtual_bhutan/virtualbhutan/images/gallery"

for filename in os.listdir(directory):
     if filename.endswith(".jpg"):
        print("----> ", filename)
        f.write("""<div class="col-sm-6 col-md-4 col-lg-3 col-xl-2 item" data-aos="fade" 
                    data-src="../images/gallery/{src}" data-sub-html="<a href="#"> <img src="../images/gallery/{src}" alt="{src}" class="img-fluid"></a>
                    </div>""".format(src=filename))

f.write("""</div>
            </div>
        </div>
        <!-----------------------------------------------------------------------------------------------
    F O O T E R
    ------------------------------------------------------------------------------------------------>
        <script src="js/jquery-3.3.1.min.js"></script>
        <script src="js/jquery-migrate-3.0.1.min.js"></script>
        <script src="js/jquery-ui.js"></script>
        <script src="js/popper.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script src="js/owl.carousel.min.js"></script>
        <script src="js/jquery.stellar.min.js"></script>
        <script src="js/jquery.countdown.min.js"></script>
        <script src="js/jquery.magnific-popup.min.js"></script>
        <script src="js/bootstrap-datepicker.min.js"></script>
        <script src="js/swiper.min.js"></script>
        <script src="js/aos.js"></script>
        <script src="js/picturefill.min.js"></script>
        <script src="js/lightgallery-all.min.js"></script>
        <script src="js/jquery.mousewheel.min.js"></script>
        <script src="js/main.js"></script>
        <script>
            $(document).ready(function () { $("#lightgallery").lightGallery(); });
        </script>
</body>

</html>""")
f.close()
print("done writing it.")


