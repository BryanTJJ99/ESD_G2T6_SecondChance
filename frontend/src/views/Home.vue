<template>
    <div>
        <TopNavbar/>
        <Sidebar/>
    </div>
</template>




<script>
    import TopNavbar from "@/components/Navbar/TopNavbar.vue";
    import Sidebar from "@/components/Navbar/Sidebar.vue"

    export default {
        data(){
        },
        components: {
            TopNavbar,
            Sidebar
        },
        
    }

</script>
