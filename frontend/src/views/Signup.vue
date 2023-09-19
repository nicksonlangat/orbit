<template>
<div class="container font-base mx-auto  flex items-center justify-center">
    <div class="mx-3 pb-10 lg:mt-24 mt-4 bg-secondary rounded-md lg:mx-0 w-full max-w-lg">
        <div class="flex flex-col items-center mt-5 gap-2">
            <IconPlanet size="48" class="text-primary" />
            <h3 class="text-gray text-2xl font-bold">Set up your account</h3>
        </div>
        <form class="mt-5 mx-5  flex flex-col gap-5">
            <div class="flex flex-col gap-3 text-white">
                <label for="username">Username</label>
                <input v-model="user.username" type="text" class="bg-secondary focus:outline-none focus:border-primary placeholder:text-gray text-sm focus:ring-0 py-2 px-6 pl-4 rounded-md" placeholder="Enter username">
            </div>
            <div class="flex flex-col gap-3 text-white">
                <label for="last_name">First name</label>
                <input v-model="user.first_name" type="text" class="bg-secondary focus:outline-none focus:border-primary placeholder:text-gray text-sm focus:ring-0 py-2 px-6 pl-4 rounded-md" placeholder="Enter first name">
            </div>
            <div class="flex flex-col gap-3 text-white">
                <label for="last_name">Last name</label>
                <input v-model="user.last_name" type="text" class="bg-secondary focus:outline-none focus:border-primary placeholder:text-gray text-sm focus:ring-0 py-2 px-6 pl-4 rounded-md" placeholder="Enter last name">
            </div>
            <div class="flex flex-col gap-3 text-white">
                <label for="password">Password</label>
                <input v-model="user.password" type="password" class="bg-secondary focus:outline-none focus:border-primary placeholder:text-gray text-sm focus:ring-0 py-2 px-6 pl-4 rounded-md" placeholder="********">
            </div>
            <div class="flex flex-col justify-center items-center gap-4">
                <button @click.prevent="submitSignup" class="bg-primary w-full text-sm text-white py-2 rounded-md mt-6">Signup</button>
                <a class="text-gray" href="/login">Already have an account? <span class="text-primary underline">Log in</span></a>
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
    name: 'Signup',
    components: {
        IconPlanet
    },
    data() {
        return {
            user: {
                username: "",
                first_name: "",
                last_name: "",
                password: ""
            }
        }
    },
    methods: {
        ...mapActions({
            signupUser: 'signupUser',
        }),
        submitSignup() {
            this.signupUser({
                payload: this.user,
                cb: () => {
                    this.$router.push({"name": "login"})
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
