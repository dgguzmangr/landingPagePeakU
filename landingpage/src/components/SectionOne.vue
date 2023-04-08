<template>
    <section>
        <div  class="container-fluid p-0 m-0">
            <div class="row mt-5 px-0 mx-0">
                <div class="col d-flex justify-content-center align-items-center mx-auto w-100" style="background-color: var(--white2);">
                    <div class="text-justify align-items-start text-left">
                        <h1 class="col-9 w-100" style="font-size: 2.8rem;"> Get stared your exiting <span>journey</span> with us.</h1>
                        <p class="col-9 w-100 mb-5" style="font-size: 0.7rem;">A Team of experienced tourism professionals will provide you  with the best advice and tips for your desire place.</p>
                        <button class="btn3">Discover Now</button>
                    </div>
                </div>
                <div class="col">
                    <img src="@/assets/img/tourist-with-thumb-up__1_-removebg 1.png" loading="lazy" class="img-fluid">
                </div>
            </div>
        </div>
        <div class="row d-flex justify-content-center align-items-center p-5 rounded-lg border mt-5 mx-auto" style="background-color: var(--whiteGrey); font-family: var(--primaryFont);">
            <div class="col">
                <select class="form-select" aria-label="Floating label select example" style="color: var(--colorB-1); border: none; font-weight: bold;">
                    <option selected>Location</option>
                    <option value="1">Bogotá</option>
                    <option value="2">Medellín</option>
                    <option value="3">Cartagena</option>
                </select>
                <br>
                <label for="floatingSelect" class="small">Where are you going</label>
            </div>
            <div class="col">
                <select class="form-select" aria-label="Floating label select example"  style="color: var(--colorB-1); border: none; font-weight: bold;">
                    <option selected>Date</option>
                    <option value="1">Tomorrow</option>
                </select>
                <br>
                <label for="floatingSelect" class="small">When you will go</label>
            </div>
            <div class="col">
                <select class="form-select" aria-label="Floating label select example"  style="color: var(--colorB-1); border: none; font-weight: bold;">
                    <option selected>Guest</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                <br>
                <label for="floatingSelect" class="small">Number of guest</label>
            </div>
            <div class="col">
                <button class="btn1">Explore Now</button>
            </div>
        </div>

    </section>
</template>

<script>
export default {
name: 'HelloWorld',
props: {
    msg: String
}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
  