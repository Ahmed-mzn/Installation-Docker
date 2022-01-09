<template>
  <div class="home">
    <div class="container"><br><br>
      <div class="columns is-multiline">
        <div class="column is-2 is-offset-1">
          <h2 class="title">Products</h2>
        </div>
        <di class="column is-2 is-offset-7">
          <button @click="AddMode()" class="button is-link">+ Add</button>
        </di>
        <div class="column is-10 is-offset-1">
          <div class="box">
            <table class="table is-fullwidth is-hoverable">
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Description</th>
                <th>Qty</th>
                <th>Created at</th>
                <th>action</th>
              </tr>

              <tr
                v-for="product in products"
                :key="product.id"
              >
                <td>{{product.id}}</td>
                <td>{{product.name}}</td>
                <td>{{product.description}}</td>
                <td>{{product.qty}}</td>
                <td>{{product.get_created_at}}</td>
                <td>
                  <div class="buttons">
                    <button @click="DeleteProduct(product.id)" class="button is-danger is-outlined">Delete</button>
                    <button @click="UpdateMode(product)" class="button is-info is-outlined">Modify</button>
                  </div>
                </td>
              </tr>
            </table>
          </div>
        </div>
      </div>
    </div>

<!-- Modal -->

  <div class="modal" id="modal">
    <div @click="closeModal" class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p v-show="editMode" class="modal-card-title">Update Product</p>
        <p v-show="!editMode" class="modal-card-title">Add Product</p>
        <button @click="closeModal" class="delete" aria-label="close"></button>
      </header>
      <section class="modal-card-body">
        <div class="colums is-multiline">
          <form @submit.prevent="editMode ? updateProduct : AddProduct">
            <div class="column is-12">
              <div class="field">
                <label class="label">Name</label>
                <div class="control">
                  <input type="text" class="input" v-model="product.name">
                </div>
              </div>
            </div>

            <div class="column is-12">
              <div class="field">
                <label class="label">Description</label>
                <div class="control">
                  <textarea class="textarea" v-model="product.description"></textarea>
                </div>
              </div>
            </div>

            <div class="column is-12">
              <div class="field">
                <label class="label">Qty</label>
                <div class="control">
                  <input type="number" class="input" v-model="product.qty">
                </div>
              </div>
            </div>
          </form>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button @click="closeModal" class="button">Cancel</button>
        <button @click="AddProduct" v-show="!editMode" class="button is-success" type="submit">Add</button>
        <button @click="UpdateProduct" v-show="editMode" class="button is-success" type="submit">Save changes</button>
      </footer>
    </div>
  </div>


<!-- end Modal-->
  </div>
</template>

<script>
import { toast } from 'bulma-toast'
import axios from 'axios'
export default {
  name: 'Home',
  data(){
    return {
      products: [],
      editMode : false,
      product : {
        id: 0,
        name: '',
        description : '',
        qty: 0
      }
    }
  },
  mounted(){
    this.getProducts()
  },
  methods:{
    getProducts(){
      axios.get("/products/")
      .then(response =>{
        this.products = response.data
      })
      .catch(error =>{
        console.log(JSON.stringify(error))
      })
    },
    AddProduct(){
      const body = {
        name: this.product.name,
        description: this.product.description,
        qty: this.product.qty
      }
      axios.post("/products/", body)
      .then(response =>{
        toast({
          message: 'Product was added ',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })
        this.getProducts()
        this.closeModal()
      })
      .catch(error =>{
        console.log(JSON.stringify(error))
      })
    },
    UpdateProduct(){
      const body = {
        id: this.product.id,
        name: this.product.name,
        description: this.product.description,
        qty: this.product.qty
      }
      console.log(body.id)
      axios.patch(`/products/${body.id}/`, body)
      .then(response =>{
        toast({
          message: 'Product was updated ',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })
        this.getProducts()
        this.closeModal()
      })
      .catch(error =>{
        console.log(JSON.stringify(error))
      })
    },
    DeleteProduct(id){
      axios.delete(`/products/${id}`, )
      .then(response =>{
        toast({
          message: 'Product was deleted ',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })
        this.getProducts()
      })
      .catch(error =>{
        console.log(JSON.stringify(error))
      })
    },
    AddMode(){
      this.editMode = false
      this.product.name = ''
      this.product.description = ''
      this.product.qty = 0
      document.getElementById("modal").classList.add('is-active')
    },
    UpdateMode(product){
      this.editMode = true
      this.product.id = product.id
      this.product.name = product.name
      this.product.description = product.description
      this.product.qty = product.qty
      document.getElementById("modal").classList.add('is-active')
    },
    closeModal(){
      document.getElementById("modal").classList.remove('is-active');
      this.product.name = ''
      this.product.description = ''
      this.product.qty = 0
    }
  }
}
</script>
