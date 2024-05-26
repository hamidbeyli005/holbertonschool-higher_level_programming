document.addEventListener('DOMContentLoaded', () => {
  const translateButton = document.getElementById('btn_translate');
  const languageCodeSelect = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  translateButton.addEventListener('click', () => {
    const languageCode = languageCodeSelect.value;
    if (languageCode) {
      fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`)
        .then((response) => response.json())
        .then((data) => {
          helloDiv.textContent = data.hello;
        })
        .catch((error) => {
          console.error('Error fetching translation:', error);
          helloDiv.textContent = 'Error fetching translation';
        });
    } else {
      helloDiv.textContent = 'Please select a language';
    }
  });
});
