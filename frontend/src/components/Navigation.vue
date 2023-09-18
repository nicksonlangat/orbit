<template>
<nav class="flex mx-5 items-center lg:mx-0 mt-5 text-neutral-200 justify-between">
    <div class="flex gap-2  items-center">
        <IconPlanet class="text-primary" size="40" />
        <h3 class="lg:text-4xl text-2xl font-extrabold">Orbit</h3>
    </div>
    <div class="hidden lg:flex text-gray text-lg gap-5 relative">
        <a :class="page === 'issues' ? 'text-white underline decoration-primary' : ''" class="hover:text-white transition-all duration-300" href="/issues">Github issues</a>
        <a :class="page === 'questions' ? 'text-white underline decoration-primary' : ''" class="hover:text-white transition-all duration-300" href="/questions">StackOveflow</a>
    </div>
    <div>
        <Mobile/>
    </div>
    <div class="hidden lg:flex gap-5 text-gray-500 items-center">
        <IconSettings />
        <IconBell />
        <span class="px-2 py-2 bg-zinc-800/50 rounded-full">
            <IconUser />
        </span>
    </div>
</nav>
</template>

<script>
import {
    IconMenu2
} from '@tabler/icons-vue';
import Mobile from './Mobile.vue'
import {
    IconBell,
    IconUser,
    IconSettings,
    IconPlanet
} from '@tabler/icons-vue';
export default {
    name: 'Navigation',
    components: {
        IconBell,
        IconUser,
        IconSettings,
        IconPlanet,
        IconMenu2,
        Mobile
    },
    data () {
      return {
        page: ""
      }
    },
    mounted() {
        this.page = this.$route.name
    }
}
</script>