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
*文件名称：PRO_CopyGDSYXMFJ_TOEMAIL
*项目名称：复制附件到 tGDSY_EMAIL 供邮件发送使用
*
*创建人员：李友德
*创建日期：2011-06-15
*功能说明：复制附件到 tGDSY_EMAIL 供邮件发送使用
*          i_sFJ - 传递附件的ID串
*          i_SJR -传递收件人的ID串
*          i_CSR -抄送人
*          i_ZT -主题
*          i_NR -内容
*------------------------------------------------------------------------------
*
*修改者        版本号        修改日期        说明
*李友德        1.0.0        2011-06-15      创建
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
  o_sMessage := '成功';

  EXCEPTION
    WHEN OTHERS THEN
      o_nCode := -1;
      o_sMessage := '发生其它错误，错误代码为' + SQLCODE + '：' + SQLERRM;

END PRO_CopyGDSYXMFJ_TOEMAIL;
/
