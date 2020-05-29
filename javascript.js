var pronoun = ['He', 'She', 'They']
var names = ['Glorbulon', 'Fringle', 'Laxidasicus', 'Jupiterian', 'Mercurial']
var adjective = ['beautiful', 'cautious', 'sexy', 'creepy', 'clingy', 'maniacal']
var magic_type = ['necromancy', 'summoning', 'evocation', 'divination', 'cybermancy']
var size_place = ['small', 'large', 'tiny', 'vast', 'floating', 'sea-floating']
var type_place = ['city', 'town', 'hamlet', 'village','principality']
var name_place = ['Oolong Riche', 'Lastigon', 'Loughborough', 'Mara Mah']
var day_job = ['sell/s potions to the poor and sick', 'entrance/s lovers for a fee', 'sell/s their fanfiction online', 'heal/s sick pets and cleans windows']
var something_awesome = ['kill dragons', 'destroy whole armies', 'obliterate the moon', 'open wormholes']
var something_sinister = ['have recently fallen in love with an elf', 'are under an eldritch curse', 'plan to enact a coup on the queen']

function getItem(list) {

  var randomNumber = Math.floor(Math.random() * list.length);
  return list[randomNumber]

}

function newWizard() {
  // We get the base string with gaps and insert an item, randomly selected,
  // from each list
    var pn = getItem(pronoun)
    var nm = getItem(names)
    var adj = getItem(adjective)
    var mgtyp = getItem(magic_type)
    var szplc = getItem(size_place)
    var typplc = getItem(type_place)
    var nmplc = getItem(name_place)
    var dyjb = getItem(day_job)
    var smthaws = getItem(something_awesome)
    var smthsin = getItem(something_sinister)

    var wizardText = (nm + " is a " + adj + " " + mgtyp + " magus from the " + szplc + " " + typplc + " of " + nmplc + ". " + pn + " mainly " + dyjb + ", but has been known to " + smthaws + " in the past. Rumour has it they " + smthsin + ". ")
    document.getElementById('wizardDisplay').innerHTML = wizardText
}
