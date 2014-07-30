import handbookof.dimensions.arithmetic as da
import unittest as ut

class TestDim(ut.TestCase):
    def setUp(self):
        self.m1 = da.Dn('1 si:m')
        self.m2 = da.Dn('2m')
        self.m3 = da.Dn('3m')
        self.kg3 = da.Dn('3 kg')
        self.s1_2 = da.Dn('1s^2')

    def test_01mul(self):
        m = self.m1 * self.m2
        self.assertEqual(m, da.Dn('2 m^2'))
        s = str(m)
        self.assertEqual(s,'2m^2')

    def test_02mul(self):
        t = self.m2 *self.m3 * self.kg3
        self.assertEqual(t,da.Dn('18kg-m^2'))
        s = str(t)
        self.assertEqual(s,'18kg-m^2')

    def test_03div(self):
        t = self.m3 / self.s1_2
        self.assertEqual(t, da.Dn('3m/s^2'))
        s = str(t)
        self.assertEqual(s,'3m/s^2')

    def test04mul_div(self):
        t = (self.m2*self.m3*self.kg3)/self.s1_2
        self.assertEqual(t, da.Dn('18m^2-kg/s^2'))
        s = str(t)
        self.assertEqual(s,'18J')
        
    
if __name__ == '__main__':
    ut.main()

    if False:
        # FIXME: re-write these quick tests as proper test cases.
        print DimensionSystem.si.unit_for('length')
        print DimensionSystem.si.base_unit_order
        print '^^^^'
        print DimensionSystem.si._derived_units
        print DimensionSystem.si.unit_for('charge')
        print si_system.unit_for('charge').name
        print si_system['K']
        print si_system['coulomb']

    
        m = SIDimension(meter=1)
        n = SIDimension(meter=1)

        print repr(m), m
        print repr(n), n
        print repr( m*n), m*n
        v = SIDimension(meter=1, second=-1)
        print repr(v), v
        hertz = SIDimension(second=-1)
        print repr( hertz),hertz
        print repr(m*hertz), m*hertz

        print 'adding meters:',m+n
        #print m+hertz

        kmps2 = SIDimension(kilogram=1,meter=1,second=-2)
        print repr(kmps2), kmps2

        print '==============='
        print DimensionSystem._implied_system
        print '---'
        print 'meter',repr(si_system.parse('m'))
        print 'kelvin',repr(si_system.parse('  K '))
        print 'coulomb', repr(si_system.parse('C'))
        print '+++++'
        print repr(si_system.parse_dimension_exp('m'))
        t,_ = si_system.parse_dimension_exp('kg-m')
        print 'kg-m',repr(t),str(t)



