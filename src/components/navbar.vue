<template>
    <div class="nav">
        <div class="nav_left">
            <button @click="toggleSidebar">
                <img src="" alt="icon" />
            </button>
            <h1>{{ title }}</h1>
        </div>
        <button @click="search">
            <i class="fa fa-search"></i>
        </button>
    </div>
</template>
  
<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'Navbar',
    data() {
        return {
            title: '程序猿'
        };
    },
    methods: {
        toggleSidebar() {
            // implement your sidebar toggle logic here
        },
        search() {
            // implement your search logic here
        }
    }
})
</script>
  
<style scoped>
.nav {
    display: flex;
    width: 100%;
    height: 4em;
    justify-content: space-between;
    align-items: center;
    background-color: #50ca83;
}

.nav_left {
    display: flex;
    align-items: center;
}

.nav button {
    width: 2em;
    height: 2em;
    /* border: none; */
    background-color: white;
    margin: 1em;
    cursor: pointer;
    font-size: 1.5rem;
    color: #fff;
}

.nav h1 {
    margin: 0;
}
</style>
  