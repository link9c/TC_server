# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Index, Integer, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class FormtableMain367(Base):
    __tablename__ = 'formtable_main_367'

    id = Column(Integer, primary_key=True)
    requestId = Column(Integer)
    ccjy = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    jhjy = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    scgc = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    qt = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    qtwb = Column(String(500, 'Chinese_PRC_CI_AS'))
    fabh = Column(String(500, 'Chinese_PRC_CI_AS'))
    sk = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    wsk = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    sygs = Column(Integer)
    sybm = Column(Integer)
    syry = Column(Integer)
    fj = Column(String(500, 'Chinese_PRC_CI_AS'))
    ypmc = Column(String(500, 'Chinese_PRC_CI_AS'))
    ypzsl = Column(Integer)
    sfcp = Column(Integer)
    cbzx = Column(Integer)
    syrq = Column(CHAR(10, 'Chinese_PRC_CI_AS'))
    ydwcrq = Column(CHAR(10, 'Chinese_PRC_CI_AS'))
    mjph = Column(String(500, 'Chinese_PRC_CI_AS'))
    gn = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    ce = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    fda = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    qt2 = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    qtwb2 = Column(String(500, 'Chinese_PRC_CI_AS'))
    fhyps = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    fhypf = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    ypycsfh = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    cw = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    lc = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    ld = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    qt3 = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    qtwb3 = Column(String(500, 'Chinese_PRC_CI_AS'))
    yjgzjg = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    ysdzsj = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    yszzjl = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    zsbg = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    songyr = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    qt4 = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    qt4wb = Column(String(500, 'Chinese_PRC_CI_AS'))
    bxz = Column(Text(2147483647, 'Chinese_PRC_CI_AS'))
    tsyqq = Column(Text(2147483647, 'Chinese_PRC_CI_AS'))
    tsyqfj = Column(Text(2147483647, 'Chinese_PRC_CI_AS'))
    syryy = Column(Integer)
    syrqq = Column(CHAR(10, 'Chinese_PRC_CI_AS'))
    csryy = Column(Integer)
    wcrqq = Column(CHAR(10, 'Chinese_PRC_CI_AS'))
    bgbhh = Column(String(500, 'Chinese_PRC_CI_AS'))
    bzz = Column(String(500, 'Chinese_PRC_CI_AS'))
    sfcps = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    sfcpf = Column(CHAR(1, 'Chinese_PRC_CI_AS'))
    cbzxspr = Column(Integer)
    manger = Column(Integer)
    scbg = Column(Text(2147483647, 'Chinese_PRC_CI_AS'))
    fysscbzx = Column(String(1000, 'Chinese_PRC_CI_AS'))
    csbmm = Column(String(500, 'Chinese_PRC_CI_AS'))
    ypmcwb = Column(String(500, 'Chinese_PRC_CI_AS'))
    khbmwb = Column(String(500, 'Chinese_PRC_CI_AS'))
    khgswb = Column(String(500, 'Chinese_PRC_CI_AS'))
    syrqwb = Column(String(500, 'Chinese_PRC_CI_AS'))
    bhwb = Column(String(500, 'Chinese_PRC_CI_AS'))
    ypmcwb2 = Column(String(500, 'Chinese_PRC_CI_AS'))
    khbmwb2 = Column(String(500, 'Chinese_PRC_CI_AS'))
    khgswb2 = Column(String(500, 'Chinese_PRC_CI_AS'))
    syrqwb2 = Column(String(500, 'Chinese_PRC_CI_AS'))
    bhwb2 = Column(String(500, 'Chinese_PRC_CI_AS'))
    sydz = Column(Integer)
    dyno = Column(String(500, 'Chinese_PRC_CI_AS'))
    dyno1 = Column(String(500, 'Chinese_PRC_CI_AS'))
    sfscbg = Column(Integer)
    dqjd = Column(String(500, 'Chinese_PRC_CI_AS'))
    csry1 = Column(Text(2147483647, 'Chinese_PRC_CI_AS'))
    xmjg = Column(String(500, 'Chinese_PRC_CI_AS'))
    sysmc = Column(Integer)
    csyy = Column(Integer)
    zysx = Column(String(500, 'Chinese_PRC_CI_AS'))
    zysxx = Column(String(500, 'Chinese_PRC_CI_AS'))
    wxdcxjg = Column(Text(2147483647, 'Chinese_PRC_CI_AS'))
    ypmcc = Column(String(500, 'Chinese_PRC_CI_AS'))
    zongji = Column(DECIMAL(15, 2))
    no2 = Column(String(500, 'Chinese_PRC_CI_AS'))
    no3 = Column(String(500, 'Chinese_PRC_CI_AS'))
    zd2 = Column(String(500, 'Chinese_PRC_CI_AS'))
    mb1 = Column(Text(2147483647, 'Chinese_PRC_CI_AS'))


class FormtableMain367Dt1(Base):
    __tablename__ = 'formtable_main_367_dt1'

    id = Column(Integer, primary_key=True)
    mainid = Column(Integer)
    ypmc = Column(String(500, 'Chinese_PRC_CI_AS'))
    ypgg = Column(String(500, 'Chinese_PRC_CI_AS'))
    ypph = Column(String(500, 'Chinese_PRC_CI_AS'))
    ypssl = Column(Integer)
    csxm = Column(String(500, 'Chinese_PRC_CI_AS'))
    cssl = Column(Integer)
    csgcyj = Column(String(500, 'Chinese_PRC_CI_AS'))
    jgpdyj = Column(String(500, 'Chinese_PRC_CI_AS'))
    csgcyj2 = Column(String(1000, 'Chinese_PRC_CI_AS'))
    xjjg = Column(String(500, 'Chinese_PRC_CI_AS'))
    xjy = Column(DECIMAL(15, 1))
    xsxmdj = Column(DECIMAL(15, 1))


class FormtableMain367Dt2(Base):
    __tablename__ = 'formtable_main_367_dt2'

    id = Column(Integer, primary_key=True)
    mainid = Column(Integer)
    ypjjr = Column(String(500, 'Chinese_PRC_CI_AS'))
    ypjsr1 = Column(String(500, 'Chinese_PRC_CI_AS'))
    sl1 = Column(Integer)
    ypjsr2 = Column(String(500, 'Chinese_PRC_CI_AS'))
    sl2 = Column(Integer)
    ypjsr3 = Column(String(500, 'Chinese_PRC_CI_AS'))
    sl3 = Column(Integer)
    zt = Column(String(500, 'Chinese_PRC_CI_AS'))
    zt1 = Column(String(500, 'Chinese_PRC_CI_AS'))
    zt2 = Column(String(500, 'Chinese_PRC_CI_AS'))
    xhh = Column(String(500, 'Chinese_PRC_CI_AS'))


t_workflow_viewlog = Table(
    'workflow_viewlog', metadata,
    Column('id', Integer, nullable=False),
    Column('p_nodeid', String(1000, 'Chinese_PRC_CI_AS')),
    Column('p_opteruid', String(1000, 'Chinese_PRC_CI_AS')),
    Column('p_date', String(1000, 'Chinese_PRC_CI_AS')),
    Column('p_addip', String(1000, 'Chinese_PRC_CI_AS')),
    Column('p_number', String(1000, 'Chinese_PRC_CI_AS')),
    Column('requestid', String(1000, 'Chinese_PRC_CI_AS')),
    Column('p_nodename', String(1000, 'Chinese_PRC_CI_AS')),
    Column('requestname', String(1000, 'Chinese_PRC_CI_AS')),
    Column('workflowtype', String(1000, 'Chinese_PRC_CI_AS')),
    Column('workflowtypeid', String(1000, 'Chinese_PRC_CI_AS')),
    Column('workflowid', String(1000, 'Chinese_PRC_CI_AS')),
    Index('IX_WORKFLOW_VIEWLOG_RPP', 'requestid', 'p_opteruid', 'p_nodeid')
)
