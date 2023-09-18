<template>
<IconMenu2 size="32" class="lg:hidden" v-if="!isOpen" @click="openModal" />
<TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="closeModal" class="relative z-10">
        <div class="fixed inset-0 overflow-y-auto">
            <div class="flex h-72 text-center">
                <TransitionChild as="template" enter='transform transition ease-in-out duration-500 sm:duration-700' enterFrom='translate-x-full' enterTo='translate-x-0' leave='transform transition ease-in-out duration-500 sm:duration-700' leaveFrom='translate-x-0' leaveTo='translate-x-full'>
                    <DialogPanel class="w-full max-w-lg transform overflow-hidden font-base bg-[#181622] p-6 text-left align-middle shadow-xl transition-all">
                        <div class="mt-2 text-white font-base">
                            <div class="flex justify-between items-center">
                                <div class="flex gap-2  items-center">
                                    <IconPlanet class="text-primary" size="32" />
                                    <h3 class="text-2xl font-extrabold">Orbit</h3>
                                </div>
                                <IconX v-if="isOpen" size="32" @click="closeModal" />
                            </div>
                            <div class="text-gray mt-10 flex flex-col gap-5 text-xl">
                                <a href=""></a>
                                <a href="/issues">Github issues</a>
                                <a href="/questions">Stackoveflow questions</a>
                            </div>
                        </div>
                    </DialogPanel>
                </TransitionChild>
            </div>
        </div>
    </Dialog>
</TransitionRoot>
</template>
<script>
import {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle,
} from '@headlessui/vue'
import {
    IconMenu2,
    IconX,
    IconPlanet
} from '@tabler/icons-vue';
export default {
    components: {
        TransitionRoot,
        TransitionChild,
        Dialog,
        DialogPanel,
        DialogTitle,
        IconMenu2,
        IconX,
        IconPlanet
    },
    data() {
        return {
            isOpen: false
        }
    },
    methods: {
        closeModal() {
            this.isOpen = false
        },
        openModal() {
            this.isOpen = true
        }
    },
    mounted() {
    }
}
</script>