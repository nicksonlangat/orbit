<template>
<div class="container font-base mx-auto">
    <Navigation />
    <div class="mt-5">
        <div class="mx-5 lg:mx-0 grid lg:grid-cols-4 text-white gap-5">
            <h3 class="text-gray text-3xl lg:text-2xl">{{ currentTag }} questions</h3>
            <TagSelectionModal />
            <select v-model="currentTag" class="bg-secondary focus:border-primary text-sm text-gray focus:outline-none placeholder:text-gray  focus:ring-0 py-2 pl-4 rounded-md" placeholder="Search issues">
                <option v-for="tag in my_tags" class="text-sm" :value="tag.name">{{ tag.name }}</option>
            </select>
            <!-- <div class="relative"> -->
            <input v-model="text" type="text" class="bg-secondary focus:outline-none focus:border-primary focus:ring-0 py-2 px-6 pl-10 placeholder:text-gray  rounded-md" placeholder="Search questions">
            <!-- <IconSearch class="absolute text-gray lg:top-2.5 top-16 mt-1 lg:mt-0 left-2 lg:right-96" /> -->
            <!-- </div> -->
        </div>
        <div v-if="isLoading" class="flex mt-20 flex-col justify-center items-center text-gray gap-3 text-2xl">
            <svg aria-hidden="true" class="inline w-10 h-10 mr-2 text-secondary animate-spin fill-primary" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor" />
                <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill" />
            </svg>
            <h3>Fetching questions, hold on...</h3>
        </div>
        <div v-if="!isLoading" class="grid mx-5 lg:mx-0 lg:grid-cols-2 mt-3 gap-5 gap-y-5">
            <div v-for="question in filteredQuestions" class="text-white bg-secondary lg:h-48 rounded-md">
                <div class="p-3">
                    <a target='_blank' :href=question.link>
                        <h3 class='text-white lg:text-xl'>{{truncateString(question.title,70)}}</h3>
                        <div class="flex mt-2 gap-5 text-xs items-center">
                            <div v-for="stat in question.stats">
                                <span v-if="stat.unit === 'answers' && stat.number > 0 || stat.unit === 'answer'" class='inline-flex gap-1 items-center text-green-500'>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="w-6 h-6">
                                        <path strokeLinecap="round" strokeLinejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z" />
                                    </svg>
                                    {{stat.number}} answer(s)
                                </span>
                                <span v-else class='inline-flex gap-2 text-gray font-bold'>{{stat.number}} {{stat.unit}}</span>
                            </div>
                            <span class='inline-flex gap-2 text-gray font-bold'>
                                {{question.time}}
                            </span>
                        </div>
                        <p class="text-xs mt-2 text-gray">{{ truncateString(question.description, 120) }}...</p>
                        <div class="grid mt-5 grid-cols-3 gap-5">
                            <a v-for="tag in question.tags.slice(-3)" :href=tag.link target='_blank' class='bg-main/60 text-center text-xs lg:text-sm text-gray rounded-md py-1.5'>{{tag.name}}</a>
                        </div>
                    </a>
                </div>
            </div>
        </div>
        <ul v-if="!isLoading" class="flex mx-5 lg:mx-0 mt-2 text-base divide-x pb-5 lg:pb-0 divide-main">

            <li>
                <p @click="goToLastPage()" :class="pageNumber == 1 ? 'text-gray/20' : 'text-white'" class="flex cursor-pointer items-center justify-center px-4 h-10 leading-tight bg-secondary rounded-l-md">
                    Previous page
                </p>
            </li>
            <li>
                <p @click="goToNextPage()" :class="pageNumber == 9 ? 'text-gray/20' : 'text-white'" class="flex cursor-pointer items-center justify-center px-4 h-10 leading-tight bg-secondary rounded-r-md">
                    Next page
                </p>
            </li>

        </ul>

    </div>
</div>
</template>

<script>
import {
    IconSearch
} from '@tabler/icons-vue'
import {
    mapActions,
    mapGetters
} from 'vuex'
import Navigation from '@/components/Navigation.vue'
import TagSelectionModal from '@/components/TagSelectionModal.vue'

export default {
    name: 'StackOverflow',
    components: {
        Navigation,
        IconSearch,
        TagSelectionModal
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
            getStoredUser: 'getStoredUser',
            getStoredTagSelections: 'getStoredTagSelections'
        }),
        filteredQuestions() {
            return this.getStoredQuestions.slice(this.initialIndex, this.finalIndex).filter((question) => {
                return question.title.toLowerCase().includes(this.text.toLowerCase())
            })
        },
        user() {
            return this.getStoredUser
        },
        my_tags() {
            return this.getStoredTagSelections.length ? this.getStoredTagSelections[0].tags : []
        }
    },
    methods: {
        ...mapActions({
            getAllQuestions: 'getAllQuestions',
            getUsersMe: 'getUsersMe',
            getAllTagSelections: 'getAllTagSelections',
        }),
        init() {
            this.isLoading = true
            this.getAllQuestions({
                tag: this.currentTag.toLowerCase(),
                cb: () => {
                    this.isLoading = false
                }
            })
            this.getUsersMe({
                cb: () => {}
            })
            this.getAllTagSelections({
                cb: () => {
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
        this.emitter.on("refreshTags", () => {
            this.init()
        })
    }
}
</script>

<style>
body,
html {
    background-color: #13111c;
}
</style>
