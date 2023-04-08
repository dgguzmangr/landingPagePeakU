<template>
    <section>
        <!--title section-->
            <div class="row mt-5">
                <div class="col d-flex justify-content-center text-center" style="background-color: var(--white2);">
                    <div>
                        <h2>Exclusive <span>deals & discounts</span></h2>
                        <p>Discover our fantastic early booking discounts & start planning your journey.</p>
                    </div>
                </div>
            </div>
        <vue-carousel :per-page="1" :autoplay="false">
            <!--card section-->
            <div class="row d-flex justify-content-center align-items-center py-5" style="background-color: var(--white2);">
                <div v-for="(card, index) in cards.slice(0, numCards)" :key="index" class="col d-flex align-items-center justify-content-center px-4"  style="background-color: var(--white);">
                    <div class="d-flex flex-column align-items-center justify-content-center border rounded">
                        <img loading="lazy" src="@/assets/img/Image-1.png">

                        <!--<img loading="lazy" :src="getImageUrl ('/media/destinations/Image-1.png')">-->
                        <!--:src="destinations[0].destination_img"-->
                        <!--"@/assets/img/Image-1.png"-->
                        <!--card footer-->
                        <div class="py-5 mx-auto">
                            <div class="row d-flex justify-content-between">
                                <div class="d-flex align-items-center text-left">
                                    <a href="#" class="text-decoration-none text-reset">
                                        <h3>{{ card.city }}</h3>
                                    </a>
                                </div>
                                <div class="d-flex align-items-center justify-content-center text-right">
                                    <img loading="lazy" src="@/assets/img/icons8-estrella-48.png" class="img-fluid" style="width: auto; height: 50%;">
                                    <p style="color: var(--colorB-1); font-weight: bold; margin: auto;">{{card.average_mark}}</p>
                                </div>
                            </div>
                            <div class="row d-flex justify-content-between">
                                <div class="d-flex align-items-center text-left">
                                    <img loading="lazy" src="@/assets/img/pin_gps.png" class="img-fluid" style="width: auto; height: 80%;">
                                    <a href="#" class="text-decoration-none text-reset px-2">
                                        <p style="color: var(--colorB-1); font-weight: bold; margin: auto;">{{ card.country }}</p>
                                    </a>
                                </div>
                                <div class="d-flex align-items-center justify-content-center text-right">
                                    <p class="px-4" style="color: var(--colorB-1); font-weight: bold; margin: auto; text-decoration: line-through;">$ {{ card.cost }}</p>
                                    <p class="rounded" style="color: var(--primaryO); font-weight: bold; margin: auto; background-color: #FFE7DB;">$ {{ Math.floor(card.discount_price) }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!--button section-->
                <div class="col-12">
                    <div class="row py-5 d-flex align-items-center justify-content-center text-center">
                        <button style="color: var(--colorB-1);" type="button" class="btn btn-unstyled" @click="moveCarousel(-1)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="54" height="54" fill="currentColor" class="bi bi-arrow-left-circle" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z"/>
                            </svg>
                        </button>
                        <button style="color: var(--primaryO);" type="button" class="btn btn-unstyled" @click="moveCarousel(1)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="54" height="54" fill="currentColor" class="bi bi-arrow-right-circle" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </vue-carousel>
    </section>
</template>
  
<script>

    export default {
        data() {
            return {
                cards: [],
                numCards: 4,
                currentIndex: 0,
            }
        },
        methods: {
            getData() {
                fetch("http://127.0.0.1:8000/show-destinations/")
                    .then(response => response.json())
                    .then(data => (this.cards = data));
            },
            moveCarousel(step) {
                const cardsPerPage = 4;
                const maxIndex = this.cards.length - cardsPerPage;
                let index = this.numCards;
                index = Math.max(0, Math.min(index + step, maxIndex));
                this.numCards = index;
            },
            getImageUrl(imagePath) {
                // construye la URL de la imagen
                return `http://127.0.0.1:8000/get_image/${imagePath}`;
                }
        },
        mounted () {
            this.getData();
        },
    }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>