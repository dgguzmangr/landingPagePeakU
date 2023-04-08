<template>
    <section>
        <!--title section-->
        <div class="row mt-5">
            <div class="col d-flex justify-content-center text-center" style="background-color: var(--white2);">
                <div>
                    <h2>Best <span>vacation plan</span></h2>
                    <p>Plan your perfect vacation with our travel agency. Choose among hundreds of all-inclusive offers!</p>
                </div>
            </div>
        </div>
        <!--button section-->
        <div class="row d-flex justify-content-center align-items-center py-5" style="background-color: var(--white2);">
            <div class="col-12">
                <div class="row d-flex justify-content-end align-items-center py-3">
                    <button style="color: var(--colorB-1);" type="button" class="btn btn-unstyled">
                        <svg xmlns="http://www.w3.org/2000/svg" width="54" height="54" fill="currentColor" class="bi bi-arrow-left-circle" viewBox="0 0 16 16">
                            <path fill-rule="evenodd"
                                d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z" />
                        </svg>
                    </button>
                    <button style="color: var(--primaryO);" type="button" class="btn btn-unstyled">
                        <svg xmlns="http://www.w3.org/2000/svg" width="54" height="54" fill="currentColor" class="bi bi-arrow-right-circle" viewBox="0 0 16 16">
                            <path fill-rule="evenodd"
                                d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z" />
                        </svg>
                    </button>
                </div>
            </div>
            <!--card section-->
            <div v-for="(card, index) in cards.slice(0, numCards)" :key="index" class="col d-flex align-items-center justify-content-center px-4" style="background-color: var(--white);">
                <div class="d-flex flex-column align-items-center justify-content-center border rounded">
                    <img loading="lazy" src="@/assets/img/Image-5.png" class="img-fluid">
                    <!--card footer-->
                    <div>
                        <div class="row d-flex">
                            <div class="col d-flex align-items-start text-start">
                                <a href="#" class="text-decoration-none text-reset">
                                    <h3>{{ card.destination.city }}, {{ card.destination.country }}</h3>
                                </a>
                            </div>
                            <div class="col d-flex align-items-end justify-content-center text-end">
                                <p class="rounded" style="color: var(--primaryO); font-weight: bold; margin: auto;">
                                    ${{ (card.plan_cost / 1000).toFixed(1) }}k</p>
                            </div>
                        </div>
                        <div class="row d-flex justify-content-between">
                            <div class="col d-flex align-items-center text-left">
                                <img loading="lazy" src="@/assets/img/rowVector.png" class="img-fluid"
                                    style="width: auto; height: 45%;">
                                <p style="color: var(--colorB-1); font-weight: bold; margin: auto;">{{ card.trip_length }} Days Trip</p>
                            </div>
                            <div class="col d-flex align-items-center justify-content-center text-right">
                                <img loading="lazy" src="@/assets/img/icons8-estrella-48.png" class="img-fluid"
                                    style="width: auto; height: 50%;">
                                <p style="color: var(--colorB-1); font-weight: bold; margin: auto;">{{ card.destination.average_mark }}</p>
                            </div>
                        </div>
                    </div>
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
                numCards: 3
            }
        },
        methods: {
            getData() {
                fetch("http://127.0.0.1:8000/show_promotions/")
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