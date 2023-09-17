<template>
<nav class="flex mt-5 text-neutral-200 justify-between">
    <div class="flex gap-2 items-center">
        <IconPlanet class="text-[#853bce]" size="44" />
        <h3 class="text-4xl font-extrabold">Orbit</h3>
    </div>
    <div class="flex gap-5 relative">
        <a href="/issues">Github issues</a>
        <a href="/questions">StackOveflow</a>
    </div>
    <div class="flex gap-5 text-gray-500 items-center">
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
        IconPlanet
    }
}
</script>
<style>
body,
html {
    background-color: #13111c;
}
</style>
