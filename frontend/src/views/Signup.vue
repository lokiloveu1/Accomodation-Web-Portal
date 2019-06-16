<template>
  <div class="bg">
    <header-component></header-component>
    <div style="margin-top:20px">
      <div class="login-box">
        <div class="login-inner-box">
          <div class="span-login">
            <span >Register with your email</span>
          </div><br/>
          <div class="login-label">
            <label>Email address</label>
            <a-input id="email-add" size="large" placeholder="Email address" />
          </div>
          <div class="login-label">
            <label>Username</label>
            <a-input size="large" placeholder="Input username"></a-input>
          </div>
          <div class="login-label">
            <label>Password</label>
            <a-input size="large" type="text" v-if="pwdtype" v-model="eyetxt"></a-input>
            <a-input  size="large" placeholder="Password" type="password" v-model="eyetxt" v-else/>
            <password v-model="eyetxt" :strength-meter-only="true"></password>
          </div>
          <div style="text-align: left">
            <a-checkbox @change="onChange">Show password</a-checkbox>
          </div>
          <div>
            <a-button type="primary" icon="login" class="login-btn" v-on:click="onRegister">Register</a-button>
          </div>
          <div style="text-align: left">
            Already got an account?<a v-on:click="login">Login</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import HeaderComponent from '../components/headercomponents'
  import Password from 'vue-password-strength-meter'
  export default {
    components: {
      HeaderComponent: HeaderComponent,
      Password:Password
    },
    methods:{
      onChange (e) {
        this.pwdtype = !this.pwdtype
        console.log(`checked = ${e.target.checked}`)
      },
      onRegister(){
        if(this.eyetxt === ""){
          this.$message.warning("Password should not be be empty!")
        }
        if(this.username === ""){
          this.$message.warning("Username should not be be empty!")
        }
        this.axios.post("/register").then((response)=>{
          let res = response.data
          if(res.status === 200){
            this.$router.push('/login')
          }
        })
      },
      login(){
        this.$router.push('/login')
      }
    },
    data(){
      return{
        eyetxt:"",
        rusername:"",
        pwdtype:false
      }
    }
  }
</script>

