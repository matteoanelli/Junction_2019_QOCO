function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getParameters() {
    let result = {};
    location.search
        .substr(1)
        .split("&")
        .forEach(function (item) {
          let tmp = item.split("=");
          console.log(tmp);
          result[tmp[0]] = decodeURIComponent(tmp[1]).toLowerCase();
        });
    return result;
}