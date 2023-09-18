<template>
<button @click="openModal" class="bg-primary justify-center text-sm rounded-md text-white px-6 py-1.5 items-center inline-flex gap-2">
    <IconPlus size="20" />
    Add github repo
</button>
<TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="closeModal" class="relative z-10">
        <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0" enter-to="opacity-100" leave="duration-200 ease-in" leave-from="opacity-100" leave-to="opacity-0">
            <div class="fixed inset-0 bg-black bg-opacity-25" />
        </TransitionChild>

        <div class="fixed inset-0 overflow-y-auto">
            <div class="flex min-h-full items-center justify-center p-4 text-center">
                <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0 scale-95" enter-to="opacity-100 scale-100" leave="duration-200 ease-in" leave-from="opacity-100 scale-100" leave-to="opacity-0 scale-95">
                    <DialogPanel class="w-full max-w-md transform overflow-hidden rounded-md bg-secondary p-6 text-left align-middle shadow-xl transition-all">
                        <DialogTitle as="h3" class="text-lg font-medium leading-6 text-white">
                            New Github repo
                        </DialogTitle>
                        <form class="mt-5 text-white">
                            <div class="flex flex-col gap-3">
                                <label for="">Repo Url</label>
                                <input v-model="url" type="text" class="border px-6 border-gray/20 placeholder:text-gray/30 bg-main py-2 rounded-md focus:outline-none focus:ring-0" placeholder="Enter repo url">

                            </div>
                        </form>

                        <div class="mt-4 flex gap-6">
                            <button @click.prevent="postRepo" class="text-white text-xs rounded-md bg-primary px-6 py-2">
                                Submit
                            </button>
                            <button @click="closeModal" class="text-white text-xs rounded-md border border-primary px-6 py-2">
                                Cancel
                            </button>
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
    IconPlus
} from '@tabler/icons-vue';
import { mapActions } from 'vuex';

export default {
    components: {
        TransitionRoot,
        TransitionChild,
        Dialog,
        DialogPanel,
        DialogTitle,
        IconPlus
    },
    data() {
        return {
            isOpen: false,
            url: ""
        }
    },
    methods: {
        ...mapActions({
            createOrganization: 'createOrganization'
        }),
        postRepo() {
            this.createOrganization({
                payload: {"url": this.url},
                cb: (() => {
                    this.url = ""
                    this.closeModal()
                    this.emitter.emit("refreshRepos")
                })
            })
        },
        closeModal() {
            this.isOpen = false
        },
        openModal() {
            this.isOpen = true
        }
    },
    mounted() {}
}
</script>
