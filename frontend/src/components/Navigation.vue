<template>
<nav class="flex font-base mx-5 items-center lg:mx-0 mt-5 text-neutral-200 justify-between">
    <div class="flex gap-2  items-center">
        <IconPlanet class="text-primary hidden lg:block" size="48" />
        <IconPlanet class="text-primary lg:hidden" size="36" />
        <a href="/" class="lg:text-4xl text-2xl font-extrabold">Orbit</a>
    </div>

    <div class="hidden lg:flex text-gray text-lg gap-5 relative">
        <a :class="page === 'issues' ? 'text-white underline decoration-primary' : ''" class="hover:text-white transition-all duration-300" href="/issues">Github issues</a>
        <a :class="page === 'questions' ? 'text-white underline decoration-primary' : ''" class="hover:text-white transition-all duration-300" href="/questions">Stackoveflow questions</a>
    </div>
    <div>
        <Mobile />
    </div>
    <div class="hidden lg:block" v-if="user?.is_superuser && page === 'questions'">
        <NewTagModal />
    </div>

    <div v-if="page === 'home'" class="hidden lg:block">
        <a href="/login" class="text-gray hover:text-white transition-all duration-500 py-2 rounded-md">Log in</a>

    </div>

    <div v-else class="hidden lg:flex gap-5 text-gray items-center">
        <div class="flex items-center gap-2">
            <span class="px-2 py-2 bg-secondary cursor-pointer rounded-full">
                <IconUser />
            </span>
            <div>
                <h3>{{ user?.username }}</h3>
            </div>
        </div>
        <IconLogout @click="logoutUser" class="cursor-pointer" />
    </div>
</nav>
</template>

<script>
import Mobile from './Mobile.vue'
import {
    IconBell,
    IconUser,
    IconSettings,
    IconPlanet,
    IconMenu2,
    IconLogout
} from '@tabler/icons-vue'
import {
    mapActions,
    mapGetters
} from 'vuex'
import NewTagModal from './NewTagModal.vue'
export default {
    name: 'Navigation',
    components: {
        IconBell,
        IconUser,
        IconSettings,
        IconPlanet,
        IconMenu2,
        Mobile,
        IconLogout,
        NewTagModal
    },
    data() {
        return {
            page: ""
        }
    },
    computed: {
        ...mapGetters({
            getStoredUser: 'getStoredUser',
        }),
        user() {
            return this.getStoredUser
        },
    },
    methods: {
        ...mapActions({
            getUsersMe: 'getUsersMe',
        }),
        init() {
            this.getUsersMe({
                cb: () => {}
            })
        },
        logoutUser() {
            localStorage.removeItem("orbit")
            localStorage.removeItem("hasOrbitPermission")
            this.$router.push({
                "name": "login"
            })
        }
    },
    mounted() {
        this.init()
        this.page = this.$route.name
    }
}
</script>
