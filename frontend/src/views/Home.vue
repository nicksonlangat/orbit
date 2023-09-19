<template>
<div class="container font-base mx-auto">
    <HeroNavigation />
    <div class="grid place-content-center place-items-center mx-5 lg:mx-0 lg:grid-cols-2 gap-5 mt-10">
        <div class="text-white rounded-md">
            <h1 class="lg:text-5xl text-3xl leading-6">Take your open source contribution to the next level
            </h1>
            <p class="text-gray mt-6 lg:text-xl">Are you an open source fanatic? Orbit will enhance your open source contribution journey exponentially by allowing you to track issues from your favourite github repos and follow questions from your favourite tags on Stackoveflow.</p>
            <button @click="goToSignup" class="bg-primary w-full lg:w-72 text-white py-2 rounded-md mt-6">Get started today</button>
        </div>
        <div class="bg-secondary rounded-md">
            <img src="../assets/1.png" class="rounded-md w-full border border-gray/40" alt="">
        </div>
    </div>
    <div id="how" class="hidden lg:block mx-5 lg:mx-0 text-white mt-10 pb-5 ">
        <!-- <h3>Join other open source enthusiasts, developers and code mentors <br class="hidden lg:block"> and help build great software, unblock  and teach <br> others the art of writing clean code.</h3> -->
        <!-- <button class="bg-primary w-full text-sm lg:w-72 text-white py-2 rounded-md mt-6">Get started today</button> -->
        <!-- <p class="text-gray mt-5 text-sm">Created by <a target="_blank" href="https://www.techwithnick.com">Nick Langat</a></p> -->
        <h3 class="text-center text-4xl font-extrabold uppercase text-gray">how it works</h3>
        <div class="grid lg:grid-cols-4 gap-5 mt-5">
            <div class="flex flex-col gap-2 rounded-md">
                <img src="../assets/2.png" class="rounded-md w-full border border-gray/40" alt="">
                <h3>(a) Select your favourite tags</h3>
            </div>
            <div class="flex flex-col gap-2 rounded-md">
                <img src="../assets/1.png" class="rounded-md w-full border border-gray/40" alt="">
                <h3>(b) Get questions based on your tags</h3>
            </div>
            <div class="flex flex-col gap-2 rounded-md">
                <img src="../assets/4.png" class="rounded-md w-full border border-gray/40" alt="">
                <h3>(c) Add your favourite repos</h3>
            </div>
            <div class="flex flex-col gap-2 rounded-md">
                <img src="../assets/3.png" class="rounded-md w-full border border-gray/40" alt="">
                <h3>(d) Get open issues for your repos</h3>
            </div>
        </div>
    </div>
</div>
</template>
<script>
import HeroNavigation from '@/components/HeroNavigation.vue'
export default {
    name: 'Hero',
    components: {
        HeroNavigation
    },
    data() {
        return {}
    },
    computed: {},
    methods: {
        goToSignup() {
            this.$router.push({
                "name": "signup"
            })
        },
    },
    mounted() {

    }
}
</script>

<style>
body,
html {
    background-color: #13111c;
}
</style>
