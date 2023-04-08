<template>
    <section>
        <div class="row mt-5 mx-auto w-75 p-3">
            <div class="col d-flex justify-content-center align-items-center text-left" style="background-color: var(--whiteGrey);">
                <div>
                    <h2> What people say <span>about us.</span></h2>
                    <p>Our Clients send us bunch of smilies with our services and we love them.</p>
                    <div class="row py-5">
                        <button style="color: var(--colorB-1);" type="button" class="btn btn-unstyled">
                            <svg xmlns="http://www.w3.org/2000/svg" width="54" height="54" fill="currentColor" class="bi bi-arrow-left-circle" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z"/>
                            </svg>
                        </button>
                        <button style="color: var(--primaryO);" type="button" class="btn btn-unstyled">
                            <svg xmlns="http://www.w3.org/2000/svg" width="54" height="54" fill="currentColor" class="bi bi-arrow-right-circle" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
                            </svg>
                        </button>
                    </div>
                </div>
                <div v-for="(card, index) in cards.slice(0, numCards)" :key="index" class="col " style="background-color: var(--white);">
                    <div style="width: 70px; height: 70px" class="rounded">
                        <img src= "@/assets/img/solenya.png" alt="userPhoto" width="70" height="70" class="rounded">
                    </div>
                    <p>{{ card.comment }}</p>
                    <h5>{{ card.customer.name }} {{ card.customer.last_name }}</h5>
                    <p>{{ card.destination.city }}, {{ card.destination.country }}</p>
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
        mounted () {
            this.getData();
        },
    }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
