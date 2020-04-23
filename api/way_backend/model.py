from .extensions import db
from .utilities.database import Database

# Custom ORM to fetct from Database
class Websites:
    def all(self):
        with Database() as db:
            db.execute("SELECT websites.website_id AS id,websites.website_name AS name, websites.img_path,websites.url,websites.description,websites.status,categories.name AS category_name FROM websites INNER JOIN website_cat ON websites.website_id = website_cat.website_id INNER JOIN categories ON categories.category_id = website_cat.category_id;")
            websites = db.fetchall()
        if not websites:
            return jsonify({"msg": "table is emptey"})
        else:
            return websites

    def getWebsiteById(self, id):
        with Database() as db:
            db.execute("SELECT websites.website_id AS id,websites.website_name AS name, websites.img_path,websites.url,websites.description,websites.status,categories.name AS category_name FROM websites INNER JOIN website_cat ON websites.website_id = website_cat.website_id INNER JOIN categories ON categories.category_id = website_cat.category_id WHERE websites.website_id = %s", [id])
            result = db.fetchone()
        if not result:
            return {"error":"invalid id"}
        else:
            return result

    def getWebsite(self, id):
        with Database() as db:
            db.execute("SELECT websites.website_id AS id,websites.website_name AS name, websites.img_path,websites.url,websites.description,websites.status,categories.name AS category_name FROM websites INNER JOIN website_cat ON websites.website_id = website_cat.website_id INNER JOIN categories ON categories.category_id = website_cat.category_id WHERE websites.website_id = %s AND websites.status = 1 ", [id])
            result = db.fetchone()
        if not result:
            return {"error":"invalid id"}
        else:
            return result

    def getCategories(self):
        with Database() as db:
            db.execute("SELECT * FROM categories;")
            return db.fetchall()

    def deleteById(self,id):
        with Database() as db:
            db.execute("SELECT website_id from websites where website_id = %s;", [id])
            website_id = db.fetchone()
            if website_id == None:
                return {"msg": "Invalid ID;"}
            else:
                db.execute("START TRANSACTION;")
                db.execute("DELETE FROM website_cat WHERE website_id = %s;", [id])
                db.execute("DELETE FROM websites WHERE website_id = %s;", [id])
                db.execute("COMMIT;")
                return {"msg": "Deleted"}

    def toggleStatus(self,id):
        with Database() as db:
            db.execute("SELECT status,website_id from websites WHERE website_id = %s;", [id])
            status = db.fetchone()
            if status == None:
                return {"msg": "Invalid ID"}
            else:
                if not status["status"]:
                    db.execute("UPDATE websites SET status = 1 WHERE website_id=%s;", [id])
                else:
                    db.execute("UPDATE websites SET status = 0 WHERE website_id=%s;", [id])
                return {"msg": "Updated"}

    def allByStatus(self, published=True):
        # If Status is True fetch all Published websites
        # Else fetch all Unpublished websites
        if published:
            conduction = 1
        else:
            conduction = 0
        with Database() as db:
            db.execute("SELECT websites.website_id,websites.website_name,websites.img_path,websites.url,websites.description,websites.status,categories.name FROM websites INNER JOIN website_cat ON websites.website_id = website_cat.website_id INNER JOIN categories ON categories.category_id = website_cat.category_id WHERE websites.status = %s;", [conduction])
            result = db.fetchall()
        if not result:
            return {"msg": "table is emptey"}
        else:
            return result

    def add(self, name, url, user_email, description, category_id):
        args = [name, url, description,user_email]
        with Database() as db:
            db.execute("START TRANSACTION;")
            db.execute("INSERT INTO websites(website_name,url,description,user_email) VALUES(%s,%s,%s,%s);", args)
            db.execute("SET @website_key = LAST_INSERT_ID();")
            db.execute("SELECT @website_key;")
            website_key = db.fetchone()
            args = [category_id,website_key['@website_key']]
            db.execute("INSERT INTO website_cat( category_id , website_id ) VALUES(%s,%s);", args)
            db.execute("COMMIT;")
        return {"msg":"Inserted"}
