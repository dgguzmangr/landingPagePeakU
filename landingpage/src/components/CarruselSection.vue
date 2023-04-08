<template>
    <div class="principal">
        <div class="container text-center">
            <div class="row">
                <div class="col" id="firstext">
                    <h1>What people say <br> <span style="color: orange;">about us.</span></h1>
                    <p>Our Clients send us bunch of smilies with our services <br> and we love them.</p>
                </div>


                <div id="carouselExampleFade" class="carousel slide carousel-fade">
                    <div class="carousel-inner">
                        <div v-for="(card, index) in cards" :key="index" class="carousel-item"
                            :class="{ active: index === 0 }">
                            <!-- Cuando coloque la imagen colocarle los dos puntos antes del :src
                            y entre las comillas la ruta correspondiente a la database -->
                            <img src="../assets/img/Image-2.png" class="d-block w-100" :alt="image.alt">
                        </div>
                        <p>{{ card.comment }}</p>
                        <h5>{{card.customer.name}} {{ card.customer.last_name }}</h5>
                        <p>{{ card.destination.city }}, {{ card.destination.country }}</p>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade"
                        data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade"
                        data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    data() {
        return {
            cards: [],
            numCards: 1
        }
    },
    methods: {
        getData() {
            fetch("http://127.0.0.1:8000/show_opinions/")
                .then(response => response.json())
                .then(data => (this.cards = data));
        },
    },
    mounted() {
        this.getData();
    },
}
</script>

<!-- Estilos -->
<style scoped>
.principal {
    background: #F7F8FC;
    margin-bottom: 10%;
    /* border: 2px solid red; */
    margin-bottom: 5vh;
    background: #F7F8FC;
    padding: 5%;
    margin-bottom: 5%;
}

#carouselExampleFade {
    width: 25%;
    /* border: 2px solid red; */
    display: flex;
    align-items: center;
}

#firstext {
    /* border: 2px solid red; */
    text-align: start;
    align-items: center;
    padding: 7%;
}
</style>