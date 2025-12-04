const boxes = document.querySelectorAll('.otp-box');
const hiddenInput = document.getElementById('otp-hidden');

boxes.forEach((box, i) => {
    box.addEventListener('input', () => {
        // avanzar automáticamente al siguiente
        if (box.value.length === 1 && i < boxes.length - 1) {
            boxes[i + 1].focus();
        }

        // actualizar el input oculto
        hiddenInput.value = Array.from(boxes).map(b => b.value).join('');
    });
});
