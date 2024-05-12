var characterElement = document.getElementById("character");

fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then(response => {

    if (!response.ok) {
      throw new Error(error);
    }
    return response.json();
  })
  .then(data => {

    var characterName = data.name;
    characterElement.textContent = characterName;
  })
  .catch(error => {
    console.error(error);
  });
