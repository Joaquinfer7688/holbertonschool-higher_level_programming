fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    if (!response.ok) {
      throw new Error(error);
    }
    return response.json();
  })
  .then(data => {
    const element = document.getElementById('hello');
    element.textContent = data.hello;
  })
  .catch(error => {
    console.error(error);
  });
  