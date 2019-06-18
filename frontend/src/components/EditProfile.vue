<template>
    <div style="border: #ececec 1px solid;width: 100%;margin: 0 12px;">
      <!--title-->
      <div style="background-color: #ececec;width: 100%;text-align: left;height: 45px">
        <h2 style="padding: 6px 12px 0 12px;color: #484848">Personal Information</h2>
      </div>
      <!--user name-->
      <div>
        <div style="width: 30%;float: left; margin-top: 30px;text-align: right;">
        <label class="text-left" >Username</label>
        </div>
        <div style="float:left;text-align: left;width: 60%">
        <input class="text-right" placeholder="input your username"></input>
        </div>
        <div style="clear: left"></div>
      </div>
      <!--gender-->
      <div>
        <div style="width: 30%;float: left; margin-top: 30px;text-align: right;">
          <label class="text-left" >I am</label>
        </div>
        <div style="float:left;text-align: left;width: 60%">
          <select class="text-right" style="width: 50%">
            <option v-model="male">Male</option>
            <option v-model="female">Female</option>
          </select>
        </div>
        <div style="clear: left"></div>
      </div>
      <!--birthday-->
      <div>
        <div style="width: 30%;float: left; margin-top: 30px;text-align: right;">
          <label class="text-left">Birthday</label>
        </div>
        <div style="float:left;text-align: left;width: 60%">
          <a-date-picker
            showTime
            format="YYYY-MM-DD"
            placeholder="Date of birth"
            @change="onChange"
            @ok="onOk"
            style="margin-top: 30px;height: 100%;width: 50%"
          ></a-date-picker>
        </div>
        <div style="clear: left"></div>
      </div>

      <!--email address-->
      <div>
        <div style="width: 30%;float: left; margin-top: 30px;text-align: right;">
          <label class="text-left" >Email address</label>
        </div>
        <div style="float:left;text-align: left;width: 60%">
          <input class="text-right" placeholder="e.g. 123456@gmail.com"></input>
        </div>
        <div style="clear: left"></div>
      </div>
     <!-- Phone number-->
      <div>
        <div style="width: 30%;float: left; margin-top: 30px;text-align: right;">
          <label class="text-left" >Phone number</label>
        </div>
        <div style="float:left;text-align: left;width: 60%">
          <input class="text-right" placeholder="input your phone number"></input>
        </div>
        <div style="clear: left"></div>
      </div>
      <!--address-->
      <div>
        <div style="width: 30%;float: left; margin-top: 30px;text-align: right;">
          <label class="text-left" >Where you live</label>
        </div>
        <div style="float:left;text-align: left;width: 60%">
          <input class="text-right" placeholder="input your address"></input>
        </div>
        <div style="clear: left"></div>
      </div>
      <a-divider></a-divider>
      <div style="text-align: right;margin-right: 20px;margin-bottom: 20px">
        <a-button type="danger" :size="size" v-on:click="update_pwd">Update password</a-button>
      </div>

    </div>
</template>

<script>
    export default {
      data(){
        return{
          size:'large',
          male:'male',
          female: 'female'
        }
      },
      methods:{
        update_pwd(){

    },
        onOk(value) {
          console.log('onOk: ', value);
        },
        onChange(value, dateString) {
          console.log('Selected Time: ', value);
          console.log('Formatted Selected Time: ', dateString);
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
    width: 100%;
    margin-top: 30px;
    height: 40px;
    padding: 8px 10px;
    border: 1px solid #aaa;
    font-size: 16px;
    border-radius: 4px;
  }
</style>
