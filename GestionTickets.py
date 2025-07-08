from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate

class GestionTickets:
    def __init__(self, db):
        self.db = db

    def ajouter_ticket(self, sujet, statut='ouvert', priorite='moyenne', nom_utilisateur=None, date=None):
        """Ajoute un nouveau ticket"""
        query = QSqlQuery(self.db)
        query.prepare("""
            INSERT INTO tickets (sujet, statut, priorite, nom_utilisateur, date)
            VALUES (?, ?, ?, ?, ?)
        """)
        query.addBindValue(sujet)
        query.addBindValue(statut)
        query.addBindValue(priorite)
        query.addBindValue(nom_utilisateur)
        query.addBindValue(date if date else QDate.currentDate())

        if not query.exec():
            error = query.lastError().text()
            QMessageBox.critical(None, "Erreur d'ajout", f"Impossible d'ajouter le ticket:\n{error}")
            return False
        return True

    def modifier_ticket(self, id_ticket, sujet=None, statut=None, priorite=None, nom_utilisateur=None, date=None):
        """Modifie un ticket existant"""
        champs = []
        valeurs = []

        if sujet is not None:
            champs.append("sujet = ?")
            valeurs.append(sujet)
        if statut is not None:
            champs.append("statut = ?")
            valeurs.append(statut)
        if priorite is not None:
            champs.append("priorite = ?")
            valeurs.append(priorite)
        if nom_utilisateur is not None:
            champs.append("nom_utilisateur = ?")
            valeurs.append(nom_utilisateur)
        if date is not None:
            champs.append("date = ?")
            valeurs.append(date)

        if not champs:
            QMessageBox.warning(None, "Avertissement", "Aucune modification à effectuer")
            return False

        query = QSqlQuery(self.db)
        requete = f"UPDATE tickets SET {', '.join(champs)} WHERE id = ?"
        query.prepare(requete)

        for valeur in valeurs:
            query.addBindValue(valeur)
        query.addBindValue(id_ticket)

        if not query.exec():
            error = query.lastError().text()
            QMessageBox.critical(None, "Erreur de modification", f"Impossible de modifier le ticket:\n{error}")
            return False
        return True

    def supprimer_ticket(self, id_ticket):
        """Supprime un ticket"""
        query = QSqlQuery(self.db)
        query.prepare("DELETE FROM tickets WHERE id = ?")
        query.addBindValue(id_ticket)

        if not query.exec():
            error = query.lastError().text()
            QMessageBox.critical(None, "Erreur de suppression", f"Impossible de supprimer le ticket:\n{error}")
            return False
        return True

    def lister_tickets(self, filtre_statut=None):
        """Retourne tous les tickets ou filtrés par statut"""
        query = QSqlQuery(self.db)
        if filtre_statut:
            query.prepare("SELECT * FROM tickets WHERE statut = ? ORDER BY date DESC")
            query.addBindValue(filtre_statut)
            query.exec()
        else:
            query.exec("SELECT * FROM tickets ORDER BY date DESC")

        tickets = []
        while query.next():
            tickets.append({
                'id': query.value(0),
                'sujet': query.value(1),
                'statut': query.value(2),
                'priorite': query.value(3),
                'nom_utilisateur': query.value(4),
                'date': query.value(5)
            })
        return tickets

    def rechercher_ticket(self, critere, valeur):
        """Recherche des tickets par critère"""
        query = QSqlQuery(self.db)
        query.prepare(f"SELECT * FROM tickets WHERE {critere} LIKE ? ORDER BY date DESC")
        query.addBindValue(f"%{valeur}%")

        if not query.exec():
            error = query.lastError().text()
            QMessageBox.critical(None, "Erreur de recherche", f"Erreur lors de la recherche:\n{error}")
            return []

        tickets = []
        while query.next():
            tickets.append({
                'id': query.value(0),
                'sujet': query.value(1),
                'statut': query.value(2),
                'priorite': query.value(3),
                'nom_utilisateur': query.value(4),
                'date': query.value(5)
            })
        return tickets

    def changer_statut_ticket(self, id_ticket, nouveau_statut):
        """Change le statut d'un ticket"""
        return self.modifier_ticket(id_ticket, statut=nouveau_statut)

    def obtenir_ticket_par_id(self, id_ticket):
        """Récupère un ticket par son ID"""
        query = QSqlQuery(self.db)
        query.prepare("SELECT * FROM tickets WHERE id = ?")
        query.addBindValue(id_ticket)

        if not query.exec():
            error = query.lastError().text()
            QMessageBox.critical(None, "Erreur de recherche", f"Erreur lors de la recherche:\n{error}")
            return None

        if query.next():
            return {
                'id': query.value(0),
                'sujet': query.value(1),
                'statut': query.value(2),
                'priorite': query.value(3),
                'nom_utilisateur': query.value(4),
                'date': query.value(5)
            }
        return None

    def lister_tickets_par_utilisateur(self, nom_utilisateur):
        """Retourne tous les tickets d'un utilisateur"""
        query = QSqlQuery(self.db)
        query.prepare("SELECT * FROM tickets WHERE nom_utilisateur = ? ORDER BY date DESC")
        query.addBindValue(nom_utilisateur)

        if not query.exec():
            return []

        tickets = []
        while query.next():
            tickets.append({
                'id': query.value(0),
                'sujet': query.value(1),
                'statut': query.value(2),
                'priorite': query.value(3),
                'nom_utilisateur': query.value(4),
                'date': query.value(5)
            })
        return tickets

    def compter_tickets_par_statut(self):
        """Compte les tickets par statut"""
        query = QSqlQuery(self.db)
        query.exec("SELECT statut, COUNT(*) FROM tickets GROUP BY statut")

        compteurs = {}
        while query.next():
            compteurs[query.value(0)] = query.value(1)
        return compteurs
