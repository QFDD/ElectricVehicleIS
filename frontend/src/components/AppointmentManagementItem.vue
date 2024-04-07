<script setup>
import { defineProps, defineEmits } from 'vue';
import {  RouterLink } from 'vue-router'
defineEmits(['remove'])
defineProps(['n','user'])
</script>

<template>
    <tr>
        <td>{{n}}</td>
        <td><a href="#"><img src="/examples/images/avatar/5.jpg" class="avatar" alt="Avatar">{{ user.name }}</a></td>
        <td>{{user.created_date}}</td>
        <td>{{user.role}}</td>
        <td><span class="status text-warning">&bull;</span>{{ user.status }}</td>
        <td>
            <RouterLink to="" class="settings" title="Settings" data-toggle="tooltip"><i
                    class="material-icons">&#xE8B8;</i></RouterLink>
            <button @click=" $emit('remove') " class="delete" title="Delete" data-toggle="tooltip"><i class="material-icons">&#xE5C9;</i></button>
        </td>
    </tr>
</template>
