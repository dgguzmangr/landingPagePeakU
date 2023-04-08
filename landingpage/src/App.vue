<template>
  <!---->
  <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="css/style.css">
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
      <title>Trabook</title>

      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@200;400&family=Volkhov:wght@700&display=swap" rel="stylesheet">
    </head>

    <body>
      <div id="app">
        <header style="background-color: var(--white2);">
          <SectionNav/>
        </header>

        <main class="container">
        <div class="primercontainer">
          <SectionOne/>
        </div>

        <div class="segundocontainer">
          <SectionTwo/>
        </div>
        <div class="tercercontainer">
          <SectionThree/>
        </div>
          
        <div class="cuartocontainer">
            <SectionFour/>
        </div>
          
        <div class="quintocontainer">
            <SectionFive/>
        </div>
          
        <div class="sextocontainer">
            <SectionSix/>
        </div>
        
        <div class="septimocontainer">
          <SectionSeven/>
        </div>
        </main>

        
      </div>
      <div class="footer">
          <SectionFooter/>
        </div>
    </body>
  </html>
</template>

<script>
import SectionNav from './components/SectionNav.vue'
import SectionOne from './components/SectionOne.vue'
import SectionTwo from './components/SectionTwo.vue'
import SectionThree from './components/SectionThree.vue'
import SectionFour from './components/SectionFour.vue'
import SectionFive from './components/SectionFive.vue'
import SectionSix from './components/SectionSix.vue'
import SectionSeven from './components/SectionSeven.vue'
import SectionFooter from './components/SectionFooter.vue'

export default {
  name: 'App',
  components: {
    SectionNav,
    SectionOne,
    SectionTwo,
    SectionThree,
    SectionFour,
    SectionFive,
    SectionSix,
    SectionSeven,
    SectionFooter
}
}
</script>

<style>
/*Global*/
:root {
    --primaryFont: 'Poppins', sans-serif;
    --secondaryFont: 'Volkhov', serif;

    --primaryO: #FA7436;
    --paragraph: #666666;
    --primaryB: #222222;
    --colorB-1: #444444;
    --white: #FFFFFF;
    --white2: #FEFCFB;
    --whiteGray: #CCCCCC;
    --yellowOrange: #FD8D3A;
}

body{
    background-color: var(--whiteGray);
}

.header{
    margin: 0;
    width: 50%;
    background-color: #FD8D3A;
/*     margin-left: 710px;
    margin-right: 710px;
    margin-bottom: 0px;
    background-color: #F7F8FC; */
}

.primercontainer{
  margin: 0;
  background: #FEFCFB;
}

.segundocontainer{
  margin: 0;
  padding-top: 40px;
  background: #F7F8FC;
}

.tercercontainer{
  margin: 0;
  background: #F7F8FC;
}

.quintocontainer{
  margin: 0;
  background: #F7F8FC;
}
.sextocontainer{
  margin: 0;
  padding-top: 40px;
  background: #F7F8FC;
}

.septimocontainer{
  margin: 0;
  background: #F7F8FC;
}


.footer{
    margin: 0;
/*     margin-left: 730px;
    margin-right: 730px;
    margin-bottom: 500px;
    background-color: #F7F8FC;
    padding: 4%; */
}
/*button*/

.btn1 {
    background-color: var(--primaryO);
    color: var(--white);
    border-radius: 5px;
    border: none;
    width: auto;
    padding: 0.75rem 3rem;
    font-weight: bold;
}

.btn2 {
    background-color: var(--white);
    color: var(--primaryO);
    border-radius: 5px;
    border: none;
    width: auto;
    padding: 0.75rem 3rem;
    font-weight: bold;
}

.btn3 {
    background-color: var(--white);
    color: var(--primaryO);
    border-radius: 5px;
    border-color: var(--primaryO);
    width: auto;
    padding: 0.75rem 3rem;
    font-weight: bold;
}
/*section typeB*/
h1, h2 {
    font-family: var(--secondaryFont);
    font-weight: bold;
    color: var(--primaryB);
}

span {
    font-family: var(--secondaryFont);
    font-weight: bold;
    color: var(--primaryO);
}

p {
    font-family: var(--primaryFont);
    color: var(--primaryB);
}


</style>

