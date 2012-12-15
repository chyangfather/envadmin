CREATE OR REPLACE PROCEDURE PRO_CopyGDSYXMFJ_TOEMAIL(o_nCode OUT Number,
                                               o_sMessage OUT VarChar2,
                                               i_sFJ IN VarChar2,
                                               i_SJR IN VarChar2,
                                               i_CSR IN VarChar2,
                                               i_ZT IN VarChar2,
                                               i_NR IN VarChar2,
                                               i_FSR IN VarChar2) IS
/******************************************************************************
*
*�ļ����ƣ�PRO_CopyGDSYXMFJ_TOEMAIL
*��Ŀ���ƣ����Ƹ����� tGDSY_EMAIL ���ʼ�����ʹ��
*
*������Ա�����ѵ�
*�������ڣ�2011-06-15
*����˵�������Ƹ����� tGDSY_EMAIL ���ʼ�����ʹ��
*          i_sFJ - ���ݸ�����ID��
*          i_SJR -�����ռ��˵�ID��
*          i_CSR -������
*          i_ZT -����
*          i_NR -����
*------------------------------------------------------------------------------
*
*�޸���        �汾��        �޸�����        ˵��
*���ѵ�        1.0.0        2011-06-15      ����
******************************************************************************/
  v_nNextID Number(16,0);
  v_Email varchar2(500);
BEGIN
  FOR cTmp IN (SELECT YX
                   FROM tGDSY_YXQZ
                   WHERE INSTR(';'||i_SJR||';',';'||ID||';')>0) LOOP
     v_Email := v_Email || cTmp.YX ||';';
  END LOOP;

  pNextID('tGDSY_EMAIL', v_nNextID);
  INSERT INTO tGDSY_EMAIL (ID,SJR,CSR,ZT,NR,userid)
         VALUES(v_nNextID,v_Email,i_CSR,i_ZT,i_NR,i_FSR);

  FOR cEMAILTmp IN (SELECT ROWNUM,WDFJ
                      FROM tGDSY_XMWD
                      WHERE INSTR(';'||i_sFJ||';',';'||ID||';')>0) LOOP
      CASE cEMAILTmp.Rownum
      WHEN 1 THEN
          UPDATE tGDSY_EMAIL SET FJ1=cEMAILTmp.WDFJ;
      WHEN 2 THEN
          UPDATE tGDSY_EMAIL SET FJ2=cEMAILTmp.WDFJ;
      WHEN 3 THEN
          UPDATE tGDSY_EMAIL SET FJ3=cEMAILTmp.WDFJ;
      WHEN 4 THEN
          UPDATE tGDSY_EMAIL SET FJ4=cEMAILTmp.WDFJ;
      WHEN 5 THEN
          UPDATE tGDSY_EMAIL SET FJ5=cEMAILTmp.WDFJ;
      WHEN 6 THEN
          UPDATE tGDSY_EMAIL SET FJ6=cEMAILTmp.WDFJ;
      WHEN 7 THEN
          UPDATE tGDSY_EMAIL SET FJ7=cEMAILTmp.WDFJ;
      WHEN 8 THEN
          UPDATE tGDSY_EMAIL SET FJ8=cEMAILTmp.WDFJ;
      WHEN 9 THEN
          UPDATE tGDSY_EMAIL SET FJ9=cEMAILTmp.WDFJ;
      WHEN 10 THEN
          UPDATE tGDSY_EMAIL SET FJ10=cEMAILTmp.WDFJ;
      ELSE
        UPDATE tGDSY_EMAIL SET FJ10=FJ10;
      END CASE;
  END LOOP;
  COMMIT;
  o_nCode := 1;
  o_sMessage := '�ɹ�';

  EXCEPTION
    WHEN OTHERS THEN
      o_nCode := -1;
      o_sMessage := '�����������󣬴������Ϊ' + SQLCODE + '��' + SQLERRM;

END PRO_CopyGDSYXMFJ_TOEMAIL;
/
