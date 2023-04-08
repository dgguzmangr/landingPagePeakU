<template>
    <section>
        <div class="row mt-5">
            <div class="col d-flex justify-content-center text-center" style="background-color: var(--white2);">
                <div>
                    <h2>Get update with <span>latest blog</span></h2>
                </div>
            </div>
        </div>
        <div class="row d-flex justify-content-center align-items-center py-5" style="background-color: var(--white2);">
        <!--card section-->
            <div v-for="(card, index) in cards.slice(0, numCards)" :key="index" class="col d-flex align-items-center justify-content-center" style="background-color: var(--white);">
                <div class="d-flex flex-column align-items-center justify-content-center" style="width: 80%;">
                    <img loading="lazy" src="@/assets/img/Image-7.png" class="img-fluid" style="width: 100%;">
                    <!--card footer-->
                    <div>
                        <a href="#" class="text-decoration-none text-reset"><h5>{{ card.title }}</h5></a>
                        <p style="color: var(--colorB-1); font-weight: bold; margin: auto;">{{ new Date(card.publication_date).toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' }) }}</p>
                    </div>
                </div>
            </div>
            <!--button section-->
            <div class="col-12">
                <div class="row py-5 d-flex align-items-center justify-content-center text-center">
                    <button style="color: var(--colorB-1);" type="button" class="btn btn-unstyled">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-circle-fill" viewBox="0 0 16 16">
                            <circle cx="8" cy="8" r="8"/>
                        </svg>
                    </button>
                    <button style="color: var(--colorB-1);" type="button" class="btn btn-unstyled">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-circle-fill" viewBox="0 0 16 16">
                            <circle cx="8" cy="8" r="8"/>
                        </svg>
                    </button>
                    <button style="color: var(--colorB-1);" type="button" class="btn btn-unstyled">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-circle-fill" viewBox="0 0 16 16">
                            <circle cx="8" cy="8" r="8"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        data() {
            return {
                cards: [],
                numCards: 4
            }
        },
        methods: {
            getData() {
                fetch("http://127.0.0.1:8000/show_articles/")
                    .then(response => response.json())
                    .then(data => (this.cards = data));
            },
        },
        mounted () {
            this.getData();
        },
    }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>