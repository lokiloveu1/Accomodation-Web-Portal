<template>
  <div style="border: #ececec 1px solid;width: 100%;margin: 0 12px;">

    <!--title-->
    <div style="background-color: #ececec;width: 100%;text-align: left;height: 45px">
      <h2 style="padding: 6px 12px 0 12px;color: #484848">Change Your Password</h2>
    </div>

    <!--old password-->
    <div>
      <div style="width: 30%;float: left; margin-top: 30px;text-align: right;">
        <label class="text-left" >Old password</label>
      </div>
      <div style="float:left;text-align: left;width: 60%">
        <input class="text-right"  name="oldPassword" type="password" v-model="oldPassword" v-validate="'required'"></input>
      </div>
      <div style="clear: left"></div>
      <div style="width: 30%;float: left;text-align: right;">
        <p></p>
      </div>
      <div style="float:left;text-align: left;width: 60%">
        <span  style="color: red">{{ errors.first('oldPassword') }}</span>
      </div>
      <div style="clear: left"></div>
    </div>

    <!--new password-->
    <div>
      <div style="width: 30%;float: left; margin-top: 30px;text-align: right;">
        <label class="text-left" >New password</label>
      </div>
      <div style="float:left;text-align: left;width: 60%">
        <input class="text-right" name="newPassword" type="password" v-model="newPassword" v-validate="{'required':'true','min':8}"></input>
      </div>
      <div style="clear: left"></div>
      <div style="width: 30%;float: left;text-align: right;">
        <p></p>
      </div>
      <div style="float:left;text-align: left;width: 60%">
        <span  style="color: red">{{ errors.first('newPassword') }}</span>
      </div>
      <div style="clear: left"></div>
    </div>

    <!--Confirm  password-->
    <div>
      <div style="width: 30%;float: left; margin-top: 30px;text-align: right;">
        <label class="text-left" >Confirm  password</label>
      </div>
      <div style="float:left;text-align: left;width: 60%">
        <input class="text-right" type="password" name="confirmPassword" v-model="confirmPassword" v-validate="{'required':'true','is':newPassword}"></input>
      </div>
      <div style="clear: left"></div>
      <div style="width: 30%;float: left;text-align: right;">
        <p></p>
      </div>
      <div style="float:left;text-align: left;width: 60%">
        <span style="color: red">{{ errors.first('confirmPassword') }}</span>
      </div>
      <div style="clear: left"></div>
    </div>


    <a-divider></a-divider>
    <div style="text-align: right;margin-right: 20px">
    <a-button type="danger" :size="size">Update password</a-button>
    </div>
  </div>
</template>

<script>

    export default {

      data(){
          return{
            newPassword:'',
            confirmPassword:'',
            oldPassword:'',
            size:'large'
          }
      }
    }
</script>

<style scoped>
  .text-left{
    padding: 0 20px;
    font-size: 16px
  }
  .text-right{
    width: 50%;
    margin-top: 30px;
    height: 40px;
    padding: 8px 10px;
    border: 1px solid #aaa;
    font-size: 16px;
    border-radius: 4px;
  }
</style>
