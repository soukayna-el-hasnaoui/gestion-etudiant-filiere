import mysql.connector as mysql

def create_database():
    db = mysql.connect(
        host='localhost',
        user='root',
        passwd=''
    )
    cursor = db.cursor()
    cursor.execute('create database cours_python')
    cursor.close()

    db = mysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database = 'cours_python'
    )
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `etudiant` ( `id` int(11) NOT NULL AUTO_INCREMENT, `matricule` varchar(30)   NOT NULL, `nom` varchar(30)   NOT NULL, `prenom` varchar(30)   NOT NULL, `age` varchar(30)   NOT NULL, `filiere` varchar(255)   NOT NULL, PRIMARY KEY (`id`) )")
    cursor.execute("CREATE TABLE IF NOT EXISTS `filiere` ( `id` int(11) NOT NULL AUTO_INCREMENT, `nom` varchar(30)   NOT NULL, PRIMARY KEY (`id`)) ")
    
    #ajout des filieres
    values = ['Info', 'Ro', 'Stat-Eco', 'Stat-Demo', 'Actuariat']
    for i in values:
        cursor.execute('insert into filiere (nom) values (%s)', [i])

#creation de la base de données
create_database()