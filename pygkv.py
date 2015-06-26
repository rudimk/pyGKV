import rython

def initialize():
	ctx = rython.RubyContext(requires=["rubygems", "gkv"])
	db = ctx("Gkv::Database.new")
	return db


def set(db, key, val):
	k = db.set(key, val)
	return k


def get(db, key):
	v = db.get(key)
	return v

def get_version(db, version, key):
	vv = db.get_version(version, key)
	return vv
