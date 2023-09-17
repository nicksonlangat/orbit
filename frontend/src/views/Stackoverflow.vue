<template>
<div class="container mx-auto">
    <nav class="flex text-neutral-200 justify-between">
        <div class="flex gap-2 items-center">
            <IconPlanet class="text-[#853bce]" size="44" />
            <h3 class="text-4xl font-extrabold">Orbit</h3>
        </div>
        <div class="flex gap-5 relative">
            <a href="">Github issues</a>
            <a href="">StackOveflow</a>
        </div>
        <div class="flex gap-5 text-gray-500 items-center">
            <IconSettings />
            <IconBell />
            <span class="px-2 py-2 bg-zinc-800/50 rounded-full">
                <IconUser />
            </span>
        </div>
    </nav>

    <div class="flex gap-5 mt-5">
        <div class="w-full rounded-md">
            <div class="">
                <div class="flex justify-between">
                    <h3 class="text-white text-4xl">Django questions</h3>
                    <div class="flex text-white gap-5 relative">

                        <button class="bg-[#181622] rounded-md text-white px-6 py-1.5 items-center inline-flex gap-2">
                            <IconFilter />
                            Tags
                        </button>
                        <input type="text" class="bg-[#181622] focus:outline-none focus:ring-0 py-1.5 px-6 pl-10 rounded-md" placeholder="Search questions">
                        <IconSearch class="absolute top-2.5 left-36" />

                    </div>
                </div>

                <div class="grid grid-cols-2 mt-5 gap-5 gap-y-5">
                    <div v-for="question in filteredQuestions" class="text-white bg-[#181622] h-44 rounded-md">
                        <div class="p-3">
                            <a target='_blank' :href=question.link>
                                <h3 class='text-stone-300 text-xl'>{{truncateString(question.title,70)}}</h3>
                                <div class="flex mt-2 gap-5 text-xs items-center">
                                    <div v-for="stat in question.stats">
                                        <span v-if="stat.unit === 'answers' && stat.number > 0 || stat.unit === 'answer'" class='inline-flex gap-1 items-center text-green-500'>
                                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="w-6 h-6">
                                                <path strokeLinecap="round" strokeLinejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z" />
                                            </svg>
                                            {{stat.number}} answer(s)
                                        </span>
                                        <span v-else class='inline-flex gap-2 text-stone-500 font-bold'>{{stat.number}} {{stat.unit}}</span>
                                    </div>
                                    <span class='inline-flex gap-2 text-stone-500 font-bold'>
                                        {{question.time}}
                                    </span>
                                </div>
                                <p class="text-xs mt-2 text-stone-500">{{ truncateString(question.description, 120) }}...</p>
                                <div class="grid mt-5 grid-cols-3 gap-5">
                                    <a v-for="tag in question.tags.slice(-3)" :href=tag.link target='_blank' class='bg-[#13111c] text-center text-xs lg:text-sm text-gray-300 rounded-md py-1.5'>{{tag.name}}</a>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
                <ul class="flex mt-2 text-base divide-x divide-stone-800">
                    
                    <li>
                        <p @click="goToLastPage()" class="flex cursor-pointer items-center justify-center px-4 h-10 leading-tight text-stone-600 bg-zinc-800/30 border border-zinc-900 rounded-l-md">
                            Previous page
                        </p>
                    </li>
                    <li>
                        <p @click="goToNextPage()" class="flex cursor-pointer items-center justify-center px-4 h-10 leading-tight text-stone-600 bg-zinc-800/30 border rounded-r-md border-zinc-900">
                            Next page
                        </p>
                    </li>

        
                   
                </ul>

            </div>

        </div>

    </div>
</div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
import {
    IconPlanet
} from '@tabler/icons-vue';
import {
    IconSearch
} from '@tabler/icons-vue';
import {
    IconFilter
} from '@tabler/icons-vue';
import {
    IconGitBranch
} from '@tabler/icons-vue';
import {
    IconPlus
} from '@tabler/icons-vue';
import {
    IconSettings
} from '@tabler/icons-vue';
import {
    IconUser
} from '@tabler/icons-vue';
import {
    IconBell
} from '@tabler/icons-vue';
import {
    mapActions,
    mapGetters
} from 'vuex';

export default {
    name: 'StackOverflow',
    components: {
        HelloWorld,
        IconBell,
        IconUser,
        IconSettings,
        IconPlanet,
        IconPlus,
        IconSearch,
        IconGitBranch,
        IconFilter
    },
    data() {
        return {
            text: "",
            currentTag: "",
            questions: [],
            initialIndex: 0,
            finalIndex: 6,
            totalPages: 9
        }
    },
    computed: {
        ...mapGetters({
            getStoredQuestions: 'getStoredQuestions',
        }),
        filteredQuestions() {
            return this.questions.slice(this.initialIndex, this.finalIndex).filter((question) => {
                return question.title.toLowerCase().includes(this.text.toLowerCase())
            })
        },
    },
    methods: {
        ...mapActions({
            getAllQuestions: 'getAllQuestions',
        }),
        init() {
            this.getAllQuestions({
                tag: this.currentTag,
                cb: (res) => {
                    this.questions = res.data
                }
            })
        },
        formatDate(date) {
            return moment(date).format("MMM Do YY")
        },
        truncateString(str, num) {
            return str.length > num ? str.slice(0, num) : str
        },
        goToNextPage() {
            this.initialIndex += 6,
            this.finalIndex += 6
        },
        goToLastPage() {
            this.initialIndex -= 6,
            this.finalIndex -= 6
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
