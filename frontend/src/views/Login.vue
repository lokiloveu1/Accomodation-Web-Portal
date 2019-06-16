<template>
    <div class="bg">
      <header-component></header-component>
      <div style="margin-top:20px">
        <div class="login-box">
          <div class="login-inner-box">
            <div class="span-login">
              <span >Log in with your email</span>
            </div><br/>
            <div class="login-label">
              <label>Email address</label>
              <a-input id="email-add" size="large" placeholder="Email address" v-model="email"/>
            </div>
            <span v-show="warningPwd" style="color: red">Password is empty.</span>
            <span v-show="warningPwd1" style="color: red">Password is wrong.</span>
            <div class="login-label">
              <label>Password</label>

              <a-input size="large" type="text" v-if="pwdtype" v-model="eyetxt"></a-input>
              <a-input  size="large" placeholder="Password" type="password" v-model="eyetxt" v-else/>
            </div>
            <div >
              <div style="text-align: left;display: inline">
                <a-checkbox @change="onChange">Show password</a-checkbox>
              </div>
              <div style="text-align: right;display: inline">
                <a href="#">Forgot your password?</a>
              </div>
            </div>
            <div>
              <a-button type="primary" icon="login" class="login-btn" v-on:click="onLogin">Login</a-button>
            </div>
            <div style="text-align: left">
              Don't have an account?<a v-on:click="signup">Sign up</a>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    import HeaderComponent from '../components/headercomponents'
    import Cookies from 'js-cookie'
    export default {
      components: {
        HeaderComponent: HeaderComponent
      },
      methods:{
        onChange (e) {
          this.pwdtype = !this.pwdtype
          console.log(`checked = ${e.target.checked}`)
        },
        onLogin(){
          let redirect = decodeURIComponent(this.$route.query.redirect || '/')
          if(this.eyetxt === ""){
            this.warningPwd = true
          }
          else{
            this.warningPwd = false
          }
          if(this.eyetxt === "123"){
            this.warningPwd1 = false
          }else{
            this.warningPwd1 = true
          }
          this.axios.post("/login",{
            username : this.email,
            password:this.eyetxt
          }).then((response)=>{
            let res = response.data;
            if(res.status == 200){
              Cookies.set('username',this.email,{expires:7})
              const userinfo = {'username':this.email}
              sessionStorage.setItem('userinfo',JSON.stringify(userinfo))
              this.$router.push({path:redirect})
            }
          })
        },
        signup(){
          this.$router.push('/signup')
        }
      },
      data(){
        return{
          eyetxt:"",
          pwdtype:false,
          warningPwd:false,
          warningPwd1:false,
          email:''
        }
      }
    }
</script>

