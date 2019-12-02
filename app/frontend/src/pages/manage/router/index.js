import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  // base:
  {
    path: "/",
    // name: "manage",
    component: Home
  },
  {
    path: "/test",
    // name: "test",
    component: () => import(/* webpackChunkName: "about" */ "../views/test.vue")
  }
];

const router = new VueRouter({
  // mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
