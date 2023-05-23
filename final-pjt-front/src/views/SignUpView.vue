<template>
  <b-container role="group" class="p-5">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="input-group-1" label="ID" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="username"
          placeholder="Enter ID"
          :state="idState"
          aria-descibedby="input-id-feedback"
        ></b-form-input>
        <b-form-invalid-feedback id="input-id-feedback" class="text-right">
          알파벳/숫자 3글자 이상
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group id="input-group-2" label="이름" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="name"
          placeholder="Enter name"
          trim
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="비밀번호" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="password"
          placeholder="Enter Password"
          :state="passwordState"
          aria-descibedby="input-password-feedback"
          trim
          type="password"
        ></b-form-input>
        <b-form-invalid-feedback
          id="input-password-feedback"
          class="text-right"
        >
          비밀번호는 최소 8자리 이상입니다.
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group
        id="input-group-2"
        label="비밀번호 확인"
        label-for="input-2"
      >
        <b-form-input
          id="input-2"
          v-model="password2"
          placeholder="One More Time"
          :state="password2State"
          aria-descibedby="input-password2-feedback"
          trim
          type="password"
        ></b-form-input>
        <b-form-invalid-feedback
          id="input-password2-feedback"
          class="text-right"
        >
          비밀번호가 일치하지 않습니다.
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group
        id="input-group-3"
        label="성별"
        label-for="input-3"
        description="성별은 필수입니다."
      >
        <b-form-select
          id="input-3"
          v-model="gender"
          :options="genders"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-group
        id="input-group-4"
        label="MBTI"
        label-for="input-4"
        description="MBTI 4글자 중 가운데 두 글자를 골라주세요!"
      >
        <b-form-select
          id="input-4"
          v-model="mbti"
          :options="mbtis"
          required
        ></b-form-select>
      </b-form-group>

      <b-button type="submit" variant="primary" @click="signup"
        >회원가입</b-button
      >
      <b-button type="reset" variant="danger">초기화</b-button>
    </b-form>
  </b-container>
</template>

<script>

export default {
  name: "SignUpView",
  data() {
    return {
      username: "",
      name: "",
      password: "",
      password2: "",
      gender: "",
      genders: ["Male", "Female"],
      mbti: "",
      mbtis: ["NT", "NF", "ST", "SF"],
      show: true,
    };
  },
  methods: {
    signup() {
      const username = this.username;
      const name = this.name;
      const password = this.password;
      const password2 = this.password2;
      const genders = this.gender;
      const mbtis = this.mbti

      const payload = {
        username, name, password, password2, genders, mbtis
      }

      this.$store.dispatch('signUp', payload)
    },
    onSubmit(event) {
      event.preventDefault();
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.username = "";
      this.name = "";
      this.password = "";
      this.password2 = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
  computed: {
    idState() {
      return this.username.length >= 3 ? true : false;
    },
    passwordState() {
      return this.password.length >= 8 ? true : false;
    },
    password2State() {
      return this.password === this.password2 ? true : false;
    },
  },
};
</script>