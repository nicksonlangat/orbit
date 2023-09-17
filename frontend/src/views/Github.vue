<template>
<div class="container mx-auto">
    <Navigation/>

    <div class="flex gap-5 mt-10">
        <div class="w-5/6 rounded-md">
            <div class="relative overflow-x-auto shadow-md">
                <div class="flex justify-between">
                    <h3 class="text-white text-4xl">Github Issues</h3>
                    <div class="flex text-white gap-5 relative">

                        <button class="bg-[#181622] rounded-md text-white px-6 py-1.5 items-center inline-flex gap-2">
                            <IconFilter />
                            Filters
                        </button>
                        <input type="text" class="bg-[#181622] focus:outline-none focus:ring-0 py-1.5 px-6 pl-10 rounded-md" placeholder="Search issues">
                        <IconSearch class="absolute top-2.5 left-40" />
                        <button class="bg-[#853bce] rounded-md text-white px-6 py-1.5 items-center inline-flex gap-2">
                            <IconPlus />
                            Add github repo
                        </button>
                    </div>
                </div>
                <table class="w-full mt-5 text-sm text-left">

                    <thead class="text-xs text-stone-500 uppercase">
                        <tr>
                            <th scope="col" class="px-6 py-3">
                                Company
                            </th>
                            <th scope="col" class="px-6 py-3">
                                Repo
                            </th>
                            <th scope="col" class="px-6 py-3">
                                Issue
                            </th>
                            <th scope="col" class="px-6 py-3">
                                Link
                            </th>

                        </tr>
                    </thead>
                    <tbody class="bg-zinc-900/50 rounded-md shadow-md">
                        <tr class="text-white bg-zinc-900/70">
                            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
                                chiefonboarding
                            </th>
                            <td class="px-6 py-4">
                                ChiefOnboarding
                            </td>
                            <td class="px-6 py-4">
                                Notification - Couldn't deliver email message: provider error
                            </td>
                            <td class="px-6 py-4">
                                <IconGitBranch class="text-[#238636]" />
                            </td>

                        </tr>
                        <tr class="text-white">
                            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
                                chiefonboarding
                            </th>
                            <td class="px-6 py-4">
                                ChiefOnboarding
                            </td>
                            <td class="px-6 py-4">
                                Notification - Couldn't deliver email message: provider error
                            </td>
                            <td class="px-6 py-4">
                                <IconGitBranch class="text-[#238636]" />
                            </td>

                        </tr>
                        <tr class="text-white bg-zinc-900/70">
                            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
                                chiefonboarding
                            </th>
                            <td class="px-6 py-4">
                                ChiefOnboarding
                            </td>
                            <td class="px-6 py-4">
                                Notification - Couldn't deliver email message: provider error
                            </td>
                            <td class="px-6 py-4">
                                <IconGitBranch class="text-[#238636]" />
                            </td>

                        </tr>
                        <tr class="text-white ">
                            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
                                chiefonboarding
                            </th>
                            <td class="px-6 py-4">
                                ChiefOnboarding
                            </td>
                            <td class="px-6 py-4">
                                Notification - Couldn't deliver email message: provider error
                            </td>
                            <td class="px-6 py-4">
                                <IconGitBranch class="text-[#238636]" />
                            </td>

                        </tr>
                        <tr class="text-white bg-zinc-900/70">
                            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
                                chiefonboarding
                            </th>
                            <td class="px-6 py-4">
                                ChiefOnboarding
                            </td>
                            <td class="px-6 py-4">
                                Notification - Couldn't deliver email message: provider error
                            </td>
                            <td class="px-6 py-4">
                                <IconGitBranch class="text-[#238636]" />
                            </td>

                        </tr>
                        <tr class="text-white ">
                            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
                                chiefonboarding
                            </th>
                            <td class="px-6 py-4">
                                ChiefOnboarding
                            </td>
                            <td class="px-6 py-4">
                                Notification - Couldn't deliver email message: provider error
                            </td>
                            <td class="px-6 py-4">
                                <IconGitBranch class="text-[#238636]" />
                            </td>

                        </tr>
                        <tr class="text-white bg-zinc-900/70">
                            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
                                chiefonboarding
                            </th>
                            <td class="px-6 py-4">
                                ChiefOnboarding
                            </td>
                            <td class="px-6 py-4">
                                Notification - Couldn't deliver email message: provider error
                            </td>
                            <td class="px-6 py-4">
                                <IconGitBranch class="text-[#238636]" />
                            </td>

                        </tr>
                        <tr class="text-white">
                            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
                                chiefonboarding
                            </th>
                            <td class="px-6 py-4">
                                ChiefOnboarding
                            </td>
                            <td class="px-6 py-4">
                                Notification - Couldn't deliver email message: provider error
                            </td>
                            <td class="px-6 py-4">
                                <IconGitBranch class="text-[#238636]" />
                            </td>

                        </tr>
                        <tr class="text-white bg-zinc-900/70">
                            <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap">
                                chiefonboarding
                            </th>
                            <td class="px-6 py-4">
                                ChiefOnboarding
                            </td>
                            <td class="px-6 py-4">
                                Notification - Couldn't deliver email message: provider error
                            </td>
                            <td class="px-6 py-4">
                                <IconGitBranch class="text-[#238636]" />
                            </td>

                        </tr>

                    </tbody>
                </table>

                <ul class="flex mt-2 text-base">
                    <li>
                        <a href="#" class="flex items-center justify-center px-4 h-10 leading-tight text-stone-600 bg-zinc-800/30 border border-zinc-900 rounded-l-md">
                            <span class="sr-only">Previous</span>
                            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 1 1 5l4 4" />
                            </svg>
                        </a>
                    </li>

                    <li>
                        <a href="#" class="flex items-center justify-center px-4 h-10 leading-tight text-stone-600 bg-zinc-800/30 border border-zinc-900">2</a>
                    </li>

                    <li>
                        <a href="#" class="flex items-center justify-center px-4 h-10 leading-tight text-stone-600 bg-zinc-800/30 border border-zinc-900">5</a>
                    </li>
                    <li>
                        <a href="#" class="flex items-center justify-center px-4 h-10 leading-tight text-stone-600 bg-zinc-800/30 border border-zinc-900 rounded-r-md">
                            <span class="sr-only">Next</span>
                            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4" />
                            </svg>
                        </a>
                    </li>
                </ul>

            </div>

        </div>
        <div class="w-1/3 text-white bg-zinc-800/30 h-86 rounded-md">
          <h3 class="mx-5 mt-2 text-3xl">Recent repos</h3>
        </div>
    </div>
</div>
</template>

<script>
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
import Navigation from '@/components/Navigation.vue'
export default {
    name: 'HomeView',
    components: {
        Navigation,
        IconBell,
        IconUser,
        IconSettings,
        IconPlanet,
        IconPlus,
        IconSearch,
        IconGitBranch,
        IconFilter
    }
}
</script>

<style>
body,
html {
    background-color: #13111c;
}
</style>
