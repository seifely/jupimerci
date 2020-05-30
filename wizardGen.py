import random
import pandas as pd # first step works with just csv files as data storage, could upgrade to database

#  pull in stored data
col_list = ["Name", "Adjective", "MagicType", "SizePlace", "TypePlace", "NamePlace",
            "DayJob", "SomethingAwesome", "SomethingSinister"]
df = pd.read_csv("WizardAttributes.csv", usecols=col_list)
names = df["Name"].tolist()
adjective = df["Adjective"].tolist()
magic_type = df["MagicType"].tolist()
size_place = df["SizePlace"].tolist()
type_place = df["TypePlace"].tolist()
name_place = df["NamePlace"].tolist()
day_job = df["DayJob"].tolist()
something_awesome = df["SomethingAwesome"].tolist()
something_sinister = df["SomethingSinister"].tolist()

# if the csv data isn't square, it will return nans - watch out!


def get_Var(list):
    index = random.randint(0,(len(list)-1))
    return list[index]


def make_Text(pnoun):

    nm = get_Var(names)
    adj = get_Var(adjective)
    mgtyp = get_Var(magic_type)
    szplc = get_Var(size_place)
    typplc = get_Var(type_place)
    nmplc = get_Var(name_place)
    dyjb = get_Var(day_job)
    smthaws = get_Var(something_awesome)
    smthsin = get_Var(something_sinister)

    # Base Text Frameworks
    single_pronoun = "%s is a %s %s magus from the %s %s of %s. %s mainly sells %s, " \
                     "but has been known to %s in the past. Rumour has it %s is %s." % (
                     nm, adj, mgtyp, szplc, typplc, nmplc, pnoun, dyjb, smthaws, pnoun.lower(), smthsin)
    plural_pronoun = "%s is a %s %s magus from the %s %s of %s. %s mainly sell %s, " \
                     "but have been known to %s in the past. Rumour has it %s are %s." % (
                     nm, adj, mgtyp, szplc, typplc, nmplc, pnoun, dyjb, smthaws, pnoun.lower(), smthsin)

    if pnoun == "They":
        return plural_pronoun
    else:
        return single_pronoun

if __name__ == "__main__":
    pronoun = ["He", "She", "They"]
    pn = get_Var(pronoun)
    print(make_Text(pn))
