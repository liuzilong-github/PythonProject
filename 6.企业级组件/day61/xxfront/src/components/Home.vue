<template>
    <div>
        <NavHeader></NavHeader>
        <h1>内容区域部分</h1>
    </div>
</template>

<script>
    import NavHeader from "./common/NavHeader";

    export default{
        name:"Home",
        data(){
            return {}
        },
        components:{
            NavHeader,
        }
    }
</script>

<style scoped>

</style>