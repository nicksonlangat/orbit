<template>
<button @click="openModal" class="bg-secondary justify-center rounded-md text-white px-6 py-2 items-center inline-flex gap-2">
    <IconTag />
    Select my tags
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
                        <DialogTitle as="h3" class="text-lg font-medium text-white">
                            Select tags
                        </DialogTitle>
                        <div class="mt-2 grid grid-cols-4 gap-y-3">
                            <p @click="addToTags(tag)" v-for="tag in tags" class="text-sm inline-flex gap-2 cursor-pointer text-gray">
                                {{ tag.name }}

                                <svg v-if="selectedTags.includes(tag.id)" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler mt-0.5 icon-tabler-check" width="16" height="16" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                    <path d="M5 12l5 5l10 -10"></path>
                                </svg>

                            </p>
                        </div>

                        <div class="mt-4 flex gap-6">
                            <button @click.prevent="updateUserTags" class="text-white text-xs rounded-md bg-primary px-6 py-2">
                                Save tags
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
    IconCheck,
    IconTag
} from '@tabler/icons-vue'
import {
    mapActions,
    mapGetters
} from 'vuex';
export default {
    components: {
        TransitionRoot,
        TransitionChild,
        Dialog,
        DialogPanel,
        DialogTitle,
        IconCheck,
        IconTag
    },
    data() {
        return {
            isOpen: false,
            selectedTags: [],
            selectionId: null,
        }
    },
    computed: {
        ...mapGetters({
            getStoredTags: 'getStoredTags',
            getStoredTagSelections: 'getStoredTagSelections',
            getStoredUser: 'getStoredUser',
        }),
        tags() {
            return this.getStoredTags
        },
        my_tags() {
            return this.getStoredTagSelections
        },
        user() {
            return this.getStoredUser
        }
    },
    methods: {
        ...mapActions({
            getAllTags: 'getAllTags',
            getAllTagSelections: 'getAllTagSelections',
            createTagSelection: 'createTagSelection',
            getUsersMe: 'getUsersMe',
            updateTagSelection: 'updateTagSelection'
        }),
        init() {
            this.getAllTags({
                cb: (() => {})
            })
            this.getAllTagSelections({
                cb: ((res) => {
                    this.selectedTags = res.length ? [...res[0].tags.map(item => item.id)] : []
                    this.selectionId = res.length ? res[0].id : null
                })
            })
            this.getUsersMe({
                cb: () => {}
            })
        },
        addToTags(tag) {
            if (this.selectedTags.includes(tag.id)) {
                const index = this.selectedTags.indexOf(tag.id)
                if (index > -1) {
                    this.selectedTags.splice(index, 1)
                }
            } else {
                this.selectedTags.push(tag.id)
            }
        },
        updateUserTags() {
            if (this.selectionId != null) {
                this.updateTagSelection({
                    id: this.selectionId,
                    payload: {
                        "tags": this.selectedTags
                    },
                    cb: () => {
                        this.closeModal()
                        this.emitter.emit("refreshTags")
                    }
                })
            } else {
                this.createTagSelection({
                    payload: {
                        "tags": this.selectedTags
                    },
                    cb: () => {
                        this.closeModal()
                        this.emitter.emit("refreshTags")
                    }
                })
            }
        },
        closeModal() {
            this.isOpen = false
        },
        openModal() {
            this.isOpen = true
        }
    },
    mounted() {
        this.init()
        this.emitter.on("refreshTagSelections", () => {
            this.init()
        })
    }
}
</script>
