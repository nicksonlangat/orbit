<template>
<div class="container font-base mx-auto  flex items-center justify-center">
    <div class="mx-3 pb-10 lg:mt-44 mt-28 bg-secondary rounded-md lg:mx-0 w-full max-w-md">
       <div class="flex flex-col items-center mt-5 gap-2">
        <IconPlanet size="48" class="text-primary"/>
        <h3 class="text-gray text-2xl font-bold"> Welcome back</h3>
        
       </div>
        <form class="mt-5 mx-5  flex flex-col gap-5">
            <div class="flex flex-col gap-3 text-white">
                <label for="username">Username</label>
                <input v-model="user.username" type="text" class="bg-secondary focus:outline-none focus:border-primary placeholder:text-gray text-sm focus:ring-0 py-2 px-6 pl-4 rounded-md" placeholder="Enter username">
            </div>
            <div class="flex flex-col gap-3 text-white">
                <label for="password">Password</label>
                <input v-model="user.password" type="password" class="bg-secondary focus:outline-none focus:border-primary placeholder:text-gray text-sm focus:ring-0 py-2 px-6 pl-4 rounded-md" placeholder="********">
            </div>
            <div class="flex flex-col justify-center items-center gap-4">
                <button @click.prevent="submitLogin" class="bg-primary w-full text-sm text-white py-2 rounded-md mt-6">Login</button>
                <a class="text-gray" href="/signup">Don't have an account? <span class="text-primary underline">Sign up</span></a>
         
            </div>
        </form>
    </div>
</div>
</template>

<script>
import {
    IconPlanet
} from '@tabler/icons-vue'
import {
    mapActions
} from 'vuex'
export default {
    name: 'Login',
    components: {
        IconPlanet
    },
    data() {
        return {
           user: {
            username: "",
            password: ""
           }
        }
    },
    methods: {
        ...mapActions({
            loginUser: 'loginUser',
        }),
        submitLogin() {
            this.loginUser({
                payload: this.user,
                cb: (res) => {
                    localStorage.setItem("orbit", res.access)
                    localStorage.setItem("hasOrbitPermission", true)
                    this.$router.push({"name": "questions"})
                }
            })
        }
    }
}
</script>
<style>
body,
html {
    background-color: #13111c;
}
</style>
