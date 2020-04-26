import {ctx} from "./canvas.js";

class Shape {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    draw() {
        ctx.fillRect(x, y, 20, 20);
    }
    update() {
        this.draw();
    }
}

export {Shape}