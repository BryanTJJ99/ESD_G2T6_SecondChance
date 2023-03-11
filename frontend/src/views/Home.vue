<template>
    <div>
        <TopNavbar :organization="organization" :department="department"/>
        <Sidebar/>
        <Footer/>
    </div>
</template>

<script>
    import TopNavbar from "@/components/Navbar/TopNavbar.vue";
    import Sidebar from "@/components/Navbar/Sidebar.vue"
    import Footer from "@/components/Footer.vue"

    export default {
        data(){
            return {
                department : "Finance",
                organization : "SMU",
            }
        },
        components: {
            TopNavbar,
            Sidebar,
            Footer
        },
        
    }

</script>
