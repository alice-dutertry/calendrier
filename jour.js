function check(bonResultat) {
    let valeurSaisie = document.getElementById("result").value
    if(valeurSaisie == bonResultat) {
        alert("Bravo, tu as trouvé !")
    } else {
        alert("Oups, ce n'est pas le bon résultat, réessaye -.-")
    }
}