<template>
    <section >
        <div class="row mt-5">
            <div class="col d-flex justify-content-center text-center" style="background-color: var(--whiteGrey);">
                <div>
                    <h2> Things you need <span>to do</span></h2>
                    <p >We ensure that you’ll embark on a perfectly planned, safe vacation at a price you can afford.</p>
                </div>
            </div>
        </div>
        <div class="row d-flex justify-content-center align-items-center py-5" style="background-color: var(--whiteGrey);">
            <div class="col p-5 m-3 border border-muted rounded" style="background-color: var(--white);">
                <img src="@/assets/img/Group.png" loading="lazy" class="img-fluid">
                <h3 class="pt-5">Sign Up</h3>
                <p class="pt-3">Completes all the work associated with planning and processing.</p>
            </div>
            <div class="col p-5 m-3 border border-muted rounded" style="background-color: var(--white);">
                <img src="@/assets/img/Group-1.png" loading="lazy" class="img-fluid">
                <h3 class="pt-5">Worth of Money</h3>
                <p class="pt-3">After successful access then book from exclusive deals & pricing.</p>
            </div>
            <div class="col p-5 m-3 border border-muted rounded" style="background-color: var(--white);">
                <img src="@/assets/img/Group-2.png" loading="lazy" class="img-fluid">
                <h3 class="pt-5">Exciting Travel</h3>
                <p class="pt-3">Start and explore a wide range of exciting travel experience.</p>
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