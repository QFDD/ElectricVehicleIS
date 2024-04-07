<template>
    <div class="row text-left mb-5">
      <!-- Category Dropdown -->
      <div class="col-lg-6 mb-3 mb-sm-0">
        <select class="form-control form-control-lg bg-white bg-op-9 text-sm w-lg-50" tabindex="-98">
          <option>Categories</option>
          <option>Learn</option>
          <option>Share</option>
          <option>Build</option>
        </select>
      </div>
      <!-- Filter Dropdown -->
      <div class="col-lg-6 text-lg-right">
        <select class="form-control form-control-lg bg-white bg-op-9 text-sm w-lg-50">
          <option>Filter by</option>
          <option>Votes</option>
          <option>Replies</option>
          <option>Views</option>
        </select>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ForumFilters',
  }
  </script>
  