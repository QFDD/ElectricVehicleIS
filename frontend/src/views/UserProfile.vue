<template>
    <div class="root-element">
        <div class="container">
            <h2 class="mt-5">个人信息</h2>
            <div class="row">
                <!-- 个人信息展示区域 -->
                <div class="col-md-6">
                    <div class="mb-3">
                        <label class="form-label">姓名：</label>
                        <p class="form-control-plaintext">{{ user.name }}</p>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">联系方式：</label>
                        <p class="form-control-plaintext">{{ user.contact }}</p>
                        <button @click="editContact = true" class="btn btn-secondary">修改联系方式</button>
                    </div>

                    <div v-if="editContact" class="mb-3">
                        <label class="form-label">新联系方式：</label>
                        <input v-model="newContact" type="text" class="form-control">
                        <button @click="updateContact" class="btn btn-primary mt-2">更新联系方式</button>
                        <button @click="editContact = false" class="btn btn-secondary mt-2">取消</button>
                    </div>
                </div>

                <!-- 密码修改区域 -->
                <div class="col-md-6">
                    <h4>修改密码</h4>
                    <form @submit.prevent="changePassword">
                        <div class="mb-3">
                            <label for="current-password" class="form-label">当前密码</label>
                            <input type="password" class="form-control" id="current-password" v-model="currentPassword">
                        </div>
                        <div class="mb-3">
                            <label for="new-password" class="form-label">新密码</label>
                            <input type="password" class="form-control" id="new-password" v-model="newPassword">
                        </div>
                        <div class="mb-3">
                            <label for="confirm-password" class="form-label">确认新密码</label>
                            <input type="password" class="form-control" id="confirm-password" v-model="confirmPassword">
                        </div>
                        <button type="submit" class="btn btn-primary">更新密码</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            user: {},
            editContact: false,
            newContact: '',
            currentPassword: '',
            newPassword: '',
            confirmPassword: ''
        };
    },
    mounted() {
        this.fetchUserData();
    },
    methods: {
        fetchUserData() {
            const user_id = this.$store.state.user.id;
            axios.get(`http://10.193.160.177:5000/auth/user/${user_id}`)
                .then(response => {
                    this.user = response.data;
                })
                .catch(error => {
                    console.error("There was an error fetching the user data:", error);
                });
        },
        updateContact() {
            const user_id = this.$store.state.user.id;
            axios.post(`http://10.193.160.177:5000/auth/user/${user_id}/update_contact`, { contact: this.newContact })
                .then(response => {
                    console.log(response)
                    this.user.contact = this.newContact;
                    this.editContact = false;
                })
                .catch(error => {
                    console.error("There was an error updating the contact:", error);
                });
        },
        async changePassword() {
            if (this.newPassword !== this.confirmPassword) {
                alert('新密码和确认密码不匹配');
            return;
        }

        try {
            const response = await axios.post('http://10.193.160.177:5000/user/change_password', {
            currentPassword: this.currentPassword,
            newPassword: this.newPassword,
            user_id: this.$store.state.user.id
            });
            alert(response.data.message);
        } catch (error) {
            alert(error.response.data.message);
        }
        }
    }
};
</script>

<style>

</style>
