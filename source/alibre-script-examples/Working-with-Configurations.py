#https://help.alibre.com/articles/#!alibre-help-v23/working-with-configurations
# create a new part
P = Part('Test')
# create a new configuration
Foo = P.AddConfiguration('Foo')
# it's already unlocked by default but this is how to unlock a configuration
Foo.UnlockAll()
# set a single lock
Foo.SetLocks(LockTypes.SuppressNewFeatures)
# set multiple locks
Foo.SetLocks(LockTypes.SuppressNewFeatures | LockTypes.LockColorProperties)
# activate the configuration
Foo.Activate()
# create a new configuration using 'Foo' as a base
Bar = P.AddConfiguration('Bar', 'Foo')
# activate it
Bar.Activate()
# get access to the default configuration and apply all locks to it
Config1 = P.GetConfiguration('Config<1>')
Config1.LockAll()
# show the name of the active configuration
ActiveConfig = P.GetActiveConfiguration()
print 'Current active configuration is: %s' % ActiveConfig.Name
# show the total number of configurations
print 'Total number of configurations: %d' % len(P.Configurations)
# show the name of the second configuration
print 'Second configuration is: %s' % P.Configurations[1].Name
# check if a couple of the confgurations are active
print 'Is second configuration active? %s' % ('yes' if P.Configurations[1].IsActive == True else 'no')
print 'Is configuration "Bar" active? %s' % ('yes' if Bar.IsActive == True else 'no')