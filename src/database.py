from mysql import connector

def createConnection():
    connection = connector.connect(host="0.0.0.0",user="root",password="root",auth_plugin='mysql_native_password',database="rest_api_flask",)

    context = connection.cursor()
    context.execute("create table if not exists users(id varchar(64) primary key DEFAULT (UUID()),name varchar(120),email varchar(120) not null unique,password varchar(120) not null)")
    connection.commit()

    return (connection,context)