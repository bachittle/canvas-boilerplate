import {Shape} from './shape.js';

const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

canvas.width = 800;
canvas.height = 600;

let middle = {
    x: canvas.width / 2,
    y: canvas.height / 2
}

function init() {}

function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillRect(10, 10, 10, 10);
}

init();
animate();

export {canvas, ctx};