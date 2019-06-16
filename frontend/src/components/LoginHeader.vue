<template>
  <div >
  <a-row class="btn-header" type="flex" justify="end" >
    <a-button v-show="!user_show" class="btn-login" v-on:click="login" :size="size" >Log in</a-button>
    <a-button  v-show="!user_show" v-on:click="signup" :size="size">Sign up</a-button>

    <a-dropdown v-show="user_show">
      <a class="ant-dropdown-link" href="#">
         <span v-text="username"/><a-icon type="down" />
      </a>
      <a-menu slot="overlay">
        <a-menu-item>
          <a href="javascript:; " v-on:click="myprofile">My profile</a>
        </a-menu-item>
        <a-menu-item>
          <a href="javascript:;">My order</a>
        </a-menu-item>
        <a-menu-item>
          <a href="javascript:;" v-on:click="logout">Log out</a>
        </a-menu-item>
      </a-menu>
    </a-dropdown>
  </a-row>
  </div>
</template>

<script>
  import Cookies from 'js-cookie'



  export default {

      data() {
        return {
          size: 'large',
          username:'',
          user_show:false
        }
      },
      methods:{

        login(){
          this.$router.push('/login')
        },
        signup(){
          this.$router.push('/signup')
        },
        logout(){
          this.user_show = false
          Cookies.remove('username')//remove cookies
          sessionStorage.removeItem('userinfo')//remove user information
          this.username = ''
          this.$router.push('/')

        },
        isLogin(){
          const userinfo1 = JSON.parse(sessionStorage.getItem('userinfo'))
          if(userinfo1 !== null){
            this.user_show = true
            this.username = userinfo1['username']
          }else {
            this.user_show = false
          }
        },
        myprofile(){
          this.$router.push('/profile')
        }

    },
    mounted:function () {
      this.isLogin();
    }
    }
</script>

<style scoped>
.btn-login{
  margin-right: 10px;
}
</style>
