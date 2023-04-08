<template>
    <nav class="container">
        <!--section typeA (four columns, each colum img[align items center] + <p> under the img[align items left] )-->
        <section class="row d-flex justify-content-center align-items-center text-center py-3" style="background-color: var(--white);">
            <div class="col text-left">
                <a href="index.html">
                    <img src="@/assets/img/logo_company.png">
                    <!--landingpage\src\assets\nav_img-->
                </a>
            </div>
            <div class="col text-center">
                <div class="d-flex justify-content-between row list-unstyled font-weight-bold"
                    style="font-family: var(--primaryFont); color: var(--colorB-1);">
                    <li><a href="#" class="text-decoration-none text-reset">Home</a></li> <!--vínculo-->
                    <li><a href="#" class="text-decoration-none text-reset">About</a></li> <!--vínculo-->
                    <li><a href="#" class="text-decoration-none text-reset">Destination</a></li> <!--vínculo-->
                    <li><a href="#" class="text-decoration-none text-reset">Tour</a></li> <!--vínculo-->
                    <li><a href="#" class="text-decoration-none text-reset">Blog</a></li> <!--vínculo-->
                </div>
            </div>
            <div class="col text-right">
                <button class="btn1 float-right">Sign up</button>
                <button class="btn2 float-right">Login</button>
            </div>
        </section>
    </nav>
</template>
  