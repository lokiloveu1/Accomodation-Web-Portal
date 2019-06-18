<template>
  <div>
  <login-header style="margin-bottom: 20px;margin-right: 5%"></login-header>

    <div style="padding: 50px 200px;background: #ececec">

      <div style="background: #fff;border-radius: 4px">
        <!--host name-->
          <div>
            <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
              <label class="text-left" >Host name</label>
            </div>
            <div style="float:left;text-align: left;width: 60%">
              <input class="text-right" placeholder="input your host name"></input>
            </div>
            <div style="clear: left"></div>
        </div>

        <!--number of guest-->
        <div>
          <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
            <label class="text-left" >The number of guest can live</label>
          </div>
          <div style="float:left;text-align: left;width: 60%">
            <select class="text-right"  >
              <option v-for="i in 5" :key="i">{{i}}</option>
            </select>
          </div>
          <div style="clear: left"></div>
        </div>

        <!--number of bedroom-->
        <div>
          <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
            <label class="text-left" >The number of bedroom</label>
          </div>
          <div style="float:left;text-align: left;width: 60%">
            <select class="text-right" >
              <option v-for="i in 5" :key="i">{{i}}</option>
            </select>
          </div>
          <div style="clear: left"></div>
        </div>

        <!--number of bed-->
        <div>
          <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
            <label class="text-left" >The number of bed</label>
          </div>
          <div style="float:left;text-align: left;width: 60%">
            <select class="text-right"  >
              <option v-for="i in 5" :key="i">{{i}}</option>
            </select>
          </div>
          <div style="clear: left"></div>
        </div>

        <!--number of bathroom-->
        <div>
          <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
            <label class="text-left" >The number of bathroom</label>
          </div>
          <div style="float:left;text-align: left;width: 60%">
            <select class="text-right" >
              <option v-for="i in 5" :key="i">{{i}}</option>
            </select>
          </div>
          <div style="clear: left"></div>
        </div>

        <!--property type-->
        <div>
          <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
            <label class="text-left" >Property type</label>
          </div>
          <div style="float:left;text-align: left;width: 60%">
            <select class="text-right"  >
              <option v-model="apartment">apartment</option>
              <option v-model="house">house</option>
            </select>
          </div>
          <div style="clear: left"></div>
        </div>

        <!--country-->
        <div>
          <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
            <label class="text-left" >Country</label>
          </div>
          <div style="float:left;text-align: left;width: 60%">
            <select class="text-right" >
              <option v-model="Australia">Australia</option>
            </select>
          </div>
          <div style="clear: left"></div>
        </div>

        <!--city-->
        <div>
          <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
            <label class="text-left" >City</label>
          </div>
          <div style="float:left;text-align: left;width: 60%">
            <select class="text-right" >
              <option v-model="Sydney">Sydney</option>
            </select>
          </div>
          <div style="clear: left"></div>
        </div>

        <!--suburb-->
        <div>
          <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
            <label class="text-left" >Suburb</label>
          </div>
          <div style="float:left;text-align: left;width:60%">
            <select class="text-right">
              <option v-model="Zetland">Zetland</option>
              <option v-model="Kingsford">Kingsford</option>
            </select>
          </div>
          <div style="clear: left"></div>
        </div>

        <!--price-->
        <div>
          <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
            <label class="text-left" >Price</label>
          </div>
          <div style="float:left;text-align: left;width:60%">
            <input class="text-right" placeholder="input the price"></input>$/night
          </div>
          <div style="clear: left"></div>
        </div>

        <!--description-->
        <div>
          <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
            <label class="text-left" >Description</label>
          </div>
          <div style="float:left;text-align: left;width:60%">
            <textarea class="text-right" placeholder="input the description" :rows="3"/>
          </div>
          <div style="clear: left"></div>
        </div>

        <!--amenities-->
        <div>
          <div style="width: 40%;float: left; margin-top: 30px;text-align: right;">
            <label class="text-left" >Amenities</label>
          </div>
          <div style="float:left;text-align: left;width:60%">
            <a-checkbox-group :options="options" @change="onChange" style="margin-top: 30px;width: 50%">
            </a-checkbox-group>
          </div>
          <div style="clear: left"></div>
        </div>
          <a-button type="primary" style="margin-top: 30px;margin-bottom: 30px">Saved</a-button>
      </div>
    </div>
  </div>
</template>

<script>
  import LoginHeader from '../components/LoginHeader'
  const options = ['TV', 'Kitchen', 'Elevator', 'WIFI', 'Balcony', 'Washer']
    export default {
        components:{LoginHeader},
      data(){
          return{
            apartment:'apartment',
            house:'house',
            Australia:'Australia',
            Sydney:'Sydney',
            Zetland:'Zetland',
            Kingsford:'Kingsford',
            options,
          }
      },
      methods:{
        onChange (checkedValues) {
          console.log('checked = ', checkedValues)
        },
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
