<template>
    <div class="c1">
        <h1>xxx</h1>
        <h2>{{ msg }}</h2>
    </div>
</template>

<script>
    export default{
        name: "Home",   // 组件名称
        data(){
            return {
                msg:"停车坐爱风铃晚"
            }
        }
    }
</script>

<style>
    h1{
        color: red;
    }
</style>