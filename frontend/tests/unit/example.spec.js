import MainPage from '@/pages/MainPage.vue';
import { shallowMount } from '@vue/test-utils';
import { expect } from 'chai';

describe('MainPage.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'Enter your name:'
    const wrapper = shallowMount(MainPage, {
      props: { msg }
    })
    expect(wrapper.text()).to.include(msg)
  })
})
