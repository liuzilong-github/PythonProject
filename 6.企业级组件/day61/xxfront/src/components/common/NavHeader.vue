<template>
    <el-container>
        <el-header>
            <el-row>
                <el-col :span="18" :offset="3">
                    <el-row>
                        <el-col :span="3">
                            <div class="c1">
                                <img src="@/assets/header.svg" alt="">
                            </div>
                        </el-col>
                        <el-col :span="13">
                            <div class="c1">
                                <router-link to="/">免费课</router-link>
                                <router-link to="/">实战课</router-link>
                                <router-link to="/">轻课</router-link>
                                <router-link to="/">就夜班</router-link>
                                <router-link to="/">题库</router-link>
                                <router-link to="/">学员成果</router-link>
                            </div>
                        </el-col>
                        <el-col :span="8">
                            <div class="c1">
                                <div class="search-content" :class="{search_content2:!input_status}">
                                    <div style="height: 20px;" @click="change_input_status" :class="{hide:!input_status}">
                                        <router-link to="/">python</router-link>
                                        <router-link to="/">linux</router-link>
                                    </div>
                                    <input ref="sousuo" type="text" @blur="change_input_status" v-model="sousuoneirong" style="border: 0;outline: none;" placeholder="请求你要搜索的内容" :class="{hide:input_status}">
                                    <!-- <input type="text" style="border: 0;outline: none" placeholder="请求你要搜索的内容" :class="{hide:input_status}"> -->
                                </div>
                                <div class="sousuoanniu">
                                    <img src="@/assets/sousuo1.png" alt="" class="ss" :class="{hide:!input_status}">
                                    <img src="@/assets/sousuo2.png" alt="" class="ss" :class="{hide:!input_status}">
                                    <img src="@/assets/new.png" alt="" class="new">
                                </div>
                            </div>
                        </el-col>
                    </el-row>
                </el-col>
            </el-row>
        </el-header>
    </el-container>
</template>

<script>
    export default{
        name: "NavHeader",
        data(){
            return {
                input_status:true,
                sousuoneirong:''
            }
        },
        methods:{
            change_input_status(){
                this.sousuoneirong = '';
                this.input_status = !this.input_status;
                if (!this.input_status){
                    this.$nextTick(()=>{    // 延时回调方法,等待vue控制的dom对象加载完成之后,在进行如下动作
                        this.$refs.sousuo.focus();
                    })
                }
            }
        }
    }
</script>

<style scoped>
    .c1{
        display: flex;  /* 弹性盒子模型CSS3 */
        align-items: center;    /* 内部元素垂直居中 */
        height: 60px;
    }
    .c1 a{
        font-size: 15px;
        font-weight: 400;
        cursor: pointer;
        color: #4a4a4a;
        margin-left: 20px;
    }
    .hide{
        display: none;
    }
    .search-content{
        border-bottom: 1px solid gray;
        height: 20px;
        width: 190px;
    }
    .search-content2{
        border-bottom: 1px solid #ffc210;
    }
    .search-content a{
        color: #545c63;
        font-size: 12px;
        padding: 3px 12px;
        background: #eeeeef;
        cursor: pointer;
        margin-right: 3px;
        border-radius: 11px;
        margin-left: 0;
    }
    .sousuoanniu{
        position: relative;
    }
    .sousuoanniu .ss{
        width: 16px;
        height: 16px;
        cursor: pointer;
    }
    .sousuoanniu .new{
        width: 18px;
        height: 10px;
        position: absolute;
        left: 15px;
        top: 0;
    }
</style>