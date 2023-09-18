<template>
<div class="container font-base mx-auto">
    <Navigation />
    <div class="grid place-content-center place-items-center mx-5 lg:mx-0 lg:grid-cols-2 gap-5 mt-20">
        <div class="text-white rounded-md">
            <h1 class="lg:text-6xl text-3xl">Open source contribution with ease...
            </h1>
            <p class="text-gray mt-6 lg:text-xl">Are you an open source fanatic? Orbit will enhance your open source contribution journey exponentially by allowing you to track issues from your favourite github repos and follow questions from your favourite tags on Stackoveflow.</p>
            <button class="bg-primary w-full lg:w-72 text-white py-2 rounded-md mt-6">Get started today</button>
        </div>

        <div class="bg-secondary rounded-md">
            <img src="../assets/home.png" class="rounded-md w-full border border-gray/40" alt="">
        </div>
    </div>
    <div class="mx-5 lg:mx-0 text-white lg:text-3xl lg:text-center mt-10">
        <h3>Join other open source enthusiasts, developers and code mentors <br class="hidden lg:block"> and help build great software, unblock  and teach <br> others the art of writing clean code.</h3>
        <button class="bg-primary w-full text-sm lg:w-72 text-white py-2 rounded-md mt-6">Get started today</button>
        <p class="text-gray mt-5 text-sm">Created by <a target="_blank" href="https://www.techwithnick.com">Nick Langat</a></p>
    </div>
    
</div>
</template>

<script>
import {
    IconFilter,
    IconSearch
} from '@tabler/icons-vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import Navigation from '@/components/Navigation.vue'
export default {
    name: 'StackOverflow',
    components: {
        Navigation,
        IconSearch,
        IconFilter
    },
    data() {
        return {
            text: "",
            currentTag: "Django",
            questions: [],
            initialIndex: 0,
            finalIndex: 6,
            pageNumber: 1,
            isLoading: false
        }
    },
    watch: {
        currentTag(newVal, oldVal) {
            if (newVal) {
                this.init()
            }
        }
    },
    computed: {
        ...mapGetters({
            getStoredQuestions: 'getStoredQuestions',
        }),
        filteredQuestions() {
            return this.getStoredQuestions.slice(this.initialIndex, this.finalIndex).filter((question) => {
                return question.title.toLowerCase().includes(this.text.toLowerCase())
            })
        },
    },
    methods: {
        ...mapActions({
            getAllQuestions: 'getAllQuestions',
        }),
        init() {
            this.isLoading = true
            this.getAllQuestions({
                tag: this.currentTag.toLowerCase(),
                cb: () => {
                    this.isLoading = false
                }
            })
        },
        truncateString(str, num) {
            return str.length > num ? str.slice(0, num) : str
        },
        goToNextPage() {

            if (this.pageNumber < 9) {
                this.pageNumber++
                this.initialIndex += 6,
                    this.finalIndex += 6
            }
        },
        goToLastPage() {
            if (this.pageNumber > 1) {
                this.pageNumber--
                this.initialIndex -= 6,
                    this.finalIndex -= 6
            }
        }
    },
    mounted() {
        this.init()
    }
}
</script>

<style>
body,
html {
    background-color: #13111c;
}
</style>
