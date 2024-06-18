<template>
  <div id="app">
    <div class="background1">
      <div class="overlay">
        <h1>Model D</h1>
        <p>性能旗舰轿跑</p>
        <p>了解更多</p>
        <div class="buttons">
          <button class="custom-button">定制我的 Model D</button>
          <button class="test-drive-button">预约试驾</button>
        </div>
      </div>
    </div>
    <div class="background2">
      <div class="overlay">
        <h1>以旧换新</h1>
        <p>助力可持续发展</p>
        <p>了解更多</p>
        <div class="buttons">
          <button class="custom-button">以旧换新</button>
          <button class="test-drive-button">预约</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rotation: 0,
      spinning: false,
      segments: [
        { label: 'Prize 1', color: '#f44336' },
        { label: 'Prize 2', color: '#e91e63' },
        { label: 'Prize 3', color: '#9c27b0' },
        { label: 'Prize 4', color: '#673ab7' },
        { label: 'Prize 5', color: '#3f51b5' },
        { label: 'Prize 6', color: '#2196f3' },
        { label: 'Prize 7', color: '#03a9f4' },
        { label: 'Prize 8', color: '#00bcd4' },
      ],
      segmentAngle: 360 / 8
    };
  },
  methods: {
    spinWheel() {
      if (this.spinning) return;
      this.spinning = true;
      const spinAmount = Math.floor(Math.random() * 360) + 360 * 5; // At least 5 full rotations
      this.rotation += spinAmount;
      setTimeout(() => {
        this.spinning = false;
        const winningSegmentIndex = Math.floor((360 - (this.rotation % 360)) / this.segmentAngle) % this.segments.length;
        alert(`Congratulations! You won ${this.segments[winningSegmentIndex].label}`);
      }, 5000); // 5 seconds for the spin animation
    }
  },
  name: 'App',
}
</script>

<style>
html, body, #app {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
}

.background1 {
  background-image: url('@/assets/svg/car_2.PNG'); 
  background-size: cover;
  background-position: center;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.background2 {
  background-image: url('@/assets/svg/car_3.PNG'); 
  background-size: cover;
  background-position: center;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.overlay {
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
}

h1 {
  font-size: 3em;
  margin: 0.5em 0;
}

p {
  margin: 0.5em 0;
}

.buttons {
  display: flex;
  justify-content: center;
  gap: 1em;
  margin-top: 1em;
}

.custom-button, .test-drive-button {
  padding: 0.5em 1em;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1em;
}

.custom-button {
  background-color: black;
  color: white;
}

.test-drive-button {
  background-color: white;
  color: black;
}
#wheel-container {
  position: relative;
  width: 300px;
  height: 300px;
  margin: 50px auto;
}

.wheel {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  transition: transform 5s ease-out;
}

.segment {
  position: absolute;
  width: 50%;
  height: 50%;
  left: 50%;
  top: 50%;
  transform-origin: 0% 100%;
  clip-path: polygon(0 0, 100% 0, 100% 100%);
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-weight: bold;
  text-align: center;
}
</style>
