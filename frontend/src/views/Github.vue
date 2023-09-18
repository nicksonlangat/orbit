<template>
<div class="container font-base mx-auto">
    <Navigation />
    <div class="flex gap-5 mt-10">
        <div class="lg:w-5/6 rounded-md">
            <div class="mx-5 lg:mx-0 rounded-md">
                <div class="grid relative text-gray lg:grid-cols-3 gap-5">
                    <select v-model="currentRepo" class="bg-secondary focus:border-primary text-sm w-[340px] lg:w-full focus:outline-none placeholder:text-gray focus:ring-0 py-2 pl-4 rounded-md" placeholder="Search issues">
                        <option class="text-sm" v-for="org in organizations" :value="org.url">{{org.name}} - {{ org.repo }}</option>
                    </select>
                    <input v-model="text" type="text" class="bg-secondary focus:outline-none focus:border-primary placeholder:text-gray text-sm focus:ring-0 py-2 px-6 pl-10 rounded-md" placeholder="Search issues">
                    <IconSearch size="20" class="absolute text-gray lg:top-2 top-16 mt-1 lg:mt-0 left-3  lg:left-80" />
                    <NewOrganizationModal />
                </div>
                <div v-if="isLoading" class="flex mt-20 flex-col justify-center items-center text-gray gap-3 text-2xl">
                    <svg aria-hidden="true" class="inline w-10 h-10 mr-2 text-secondary animate-spin fill-primary" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor" />
                        <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill" />
                    </svg>
                    <h3>Fetching issues, hold on...</h3>
                </div>
                <div class="lg:hidden grid gap-4 mt-5">
                    <div v-for="issue in filteredIssues" class="bg-secondary text-white rounded-md h-12">
                        <div class="mt-2 ml-3 mr-2 flex justify-between items-center">
                            <a target="_blank" :href="issue.html_url" class="text-xs">{{ truncateString(issue.title, 90) }}</a>
                            <div>
                                <a target="_blank" :href="issue.html_url">
                                    <IconGitBranch class="text-success" />
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                <table v-if="!isLoading" class="rounded-md w-full lg:block hidden bg-secondary mt-8 text-sm text-left">
                    <thead class="text-xs border-b border-gray/30 text-gray uppercase">
                        <tr>
                            <th scope="col" class="px-6 py-3">
                                Issue
                            </th>
                            <th scope="col" class="px-6 py-3">
                                owner
                            </th>
                            <th scope="col" class="px-6 py-3">
                                repo
                            </th>
                            <th scope="col" class="px-6 py-3">
                                Link
                            </th>

                        </tr>
                    </thead>
                    <tbody class="text-xs rounded-md shadow-md">
                        <tr v-for="issue of filteredIssues" class="text-white bg-secondary even:bg-main/50">
                            <th scope="row" class="px-4 py-4">
                                {{ truncateString(issue.title, 90) }}
                            </th>
                            <td class="px-6 py-4">
                                {{ currentOrganization?.name }}
                            </td>
                            <td class="px-6 py-4 whitespace-nowrap">
                                {{ currentOrganization?.repo }}
                            </td>
                            <td class="px-6 py-4">
                                <a target="_blank" :href="issue.html_url">
                                    <IconGitBranch class="text-success" />
                                </a>
                            </td>
                        </tr>
                    </tbody>
                </table>

                <ul v-if="!isLoading" class="flex mt-2 text-base divide-x divide-main">

                    <li>
                        <p @click="goToLastPage()" :class="pageNumber == 1 ? 'text-gray/20' : 'text-white'" class="flex cursor-pointer items-center justify-center px-4 h-10 leading-tight bg-secondary rounded-l-md">
                            Previous page
                        </p>
                    </li>
                    <li>
                        <p @click="goToNextPage()" :class="filteredIssues.length < 9 ? 'text-gray/20' : 'text-white'" class="flex cursor-pointer items-center justify-center px-4 h-10 leading-tight bg-secondary rounded-r-md">
                            Next page
                        </p>
                    </li>

                </ul>

            </div>
        </div>
        <div class="w-1/3 hidden lg:block text-white  rounded-md">
            <div class="grid grid-cols-2 gap-5">
                <div class="bg-secondary text-white uppercase h-28 rounded-md flex flex-col justify-center items-center">
                    <h3 class="text-gray font-bold text-2xl">repos</h3>
                    <h3 class="text-3xl font-bold">16</h3>
                </div>
                <div class="bg-secondary h-28 rounded-md text-white uppercase flex flex-col justify-center items-center">
                    <h3 class="text-gray font-bold text-2xl">issues</h3>
                    <h3 class="text-3xl font-bold">67</h3>
                </div>
            </div>
            <div class="bg-secondary pb-5 rounded-md">
                <h3 class="ml-2 mt-2 bg-secondary text-2xl uppercase text-gray text-start">Recent repos</h3>
                <table class="mt-5  text-sm text-left">
                    <thead class="text-xs bg-main/50 text-gray uppercase">
                        <tr>
                            <th scope="col" class="px-6 py-3">
                                Owner
                            </th>
                            <th scope="col" class="px-6 py-3">
                                Repo
                            </th>
                            <th scope="col" class="px-6 py-3">
                                Link
                            </th>
                        </tr>
                    </thead>
                    <tbody class="text-xs">
                        <tr v-for="organization in organizations.slice(0, 6)" class="text-white border-b border-gray/30 last:border-0">
                            <th scope="row" class="px-6 py-2 font-medium whitespace-nowrap">
                                {{ organization.name }}
                            </th>
                            <td class="px-6 py-4">
                                {{ organization.repo }}
                            </td>
                            <td class="px-6 py-4">
                                <a :href="organization.url" target="_blank">
                                    <IconBrandGithub class="text-primary" /></a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import {
    IconGitBranch,
    IconFilter,
    IconSearch,
    IconBrandGithub
} from '@tabler/icons-vue';
import Navigation from '@/components/Navigation.vue'
import NewOrganizationModal from '@/components/NewOrganizationModal.vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
export default {
    name: 'HomeView',
    components: {
        Navigation,
        NewOrganizationModal,
        IconSearch,
        IconGitBranch,
        IconFilter,
        IconBrandGithub
    },
    data() {
        return {
            pageNumber: 1,
            isLoading: false,
            initialIndex: 0,
            finalIndex: 9,
            text: "",
            currentRepo: "",
            currentOrganization: null,
        }
    },
    watch: {
        currentRepo(newVal, oldVal) {
            if (newVal) {
                this.init()
                this.currentOrganization = this.organizations.find(organization => organization.url == newVal)
            }
        }
    },
    computed: {
        ...mapGetters({
            getStoredOrganizations: 'getStoredOrganizations',
            getStoredIssues: 'getStoredIssues'
        }),
        organizations() {
            return this.getStoredOrganizations
        },
        filteredIssues() {
            return this.getStoredIssues.slice(this.initialIndex, this.finalIndex).filter((issue) => {
                return issue.title.toLowerCase().includes(this.text.toLowerCase())
            })
        },
    },
    methods: {
        ...mapActions({
            getAllOrganizations: 'getAllOrganizations',
            getAllIssues: 'getAllIssues'
        }),
        init() {
            this.isLoading = true
            this.getAllIssues({
                url: this.currentRepo,
                cb: () => {
                    this.isLoading = false
                }
            })
        },
        truncateString(str, num) {
            return str.length > num ? str.slice(0, num) : str
        },
        goToNextPage() {
            if (this.filteredIssues.length >= 9) {
                this.pageNumber++
                this.initialIndex += 9
                this.finalIndex += 9
            }
        },
        goToLastPage() {
            if (this.pageNumber > 1) {
                this.pageNumber--
                this.initialIndex -= 9
                this.finalIndex -= 9
            }
        }
    },
    mounted() {
        this.getAllOrganizations({
            cb: (res) => {
                if (res.length) {
                    this.currentRepo = res[0].url
                    this.currentOrganization = res[0]
                }
            }
        })
        this.init()
        this.emitter.on("refreshRepos", () => {
            this.init()
            this.getAllOrganizations({
                cb: () => {}
            })
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
