import sqlite3
from typing import List
import pandas as pd

class DB:
    def __init__(self):
        self.SqlConnection = sqlite3.connect('prismDB.db')
        self.db=sqlite3.connect('prismDB.db')
        self.cmd = self.SqlConnection.cursor()

    def runSql(self, sql):
        self.db.execute(sql)
        self.db.commit()

    def runSelect(self, sql):
        cur = self.db.cursor()
        cur.execute(sql)
        return cur

    def check_duplicate(self, coloum_name: str, value: str, table_name: str, Condition: str) -> int:
        re = -1
        try:
            temp = ""
            if Condition == "":
                temp = f"select count(*) as row_count from {table_name} where {coloum_name} = '{value}'"
            else:
                temp = f"select count(*) as row_count from {table_name} where {coloum_name} = '{value}' and {Condition}"
            self.cmd.execute(temp)
            re = self.cmd.fetchone()[0]
            return re
        except Exception as ex:
            re = -1
            return re

    def Execute_Sql(self, sql: str) -> int:
        re = -1
        try:
            if sql != "":
                self.cmd.execute(sql)
                self.SqlConnection.commit()
                re = 1
            return re
        except Exception as ex:
            re = -1
            return re

    def get_value(self, coloum_name: str, table_name: str, Condition: str) -> str:
        re = ""
        try:
            temp = ""
            if Condition == "":
                temp = f"select {coloum_name} as max_val from {table_name}"
            else:
                temp = f"select {coloum_name} as max_val from {table_name} where {Condition}"
            self.cmd.execute(temp)
            re = str(self.cmd.fetchone()[0])
            return re
        except Exception as ex:
            return re

    def get_max_value(self, coloum_name: str, table_name: str, Condition: str) -> int:
        re = -1
        try:
            temp = ""
            if Condition == "":
                temp = f"select max({coloum_name}) as max_val from {table_name}"
            else:
                temp = f"select max({coloum_name}) as max_val from {table_name} where {Condition}"
            self.cmd.execute(temp)
            re = self.cmd.fetchone()[0]
            return re
        except Exception as ex:
            re = -1
            return re

    def get_coloum(self, coloum_name: str, table_name: str, Condition: str) -> List[str]:
        co = []
        try:
            temp = ""
            if Condition == "":
                temp = f"select {coloum_name} as col from {table_name}"
            else:
                temp = f"select {coloum_name} as col from {table_name} where {Condition}"
            self.cmd.execute(temp)
            co = [str(row[0]) for row in self.cmd.fetchall()]
            return co
        except Exception as ex:
            return co

    def get_coloum_group_by(self, coloum_name: str, table_name: str, Condition: str) -> List[str]:
        co = []
        try:
            temp = ""
            if Condition == "":
                temp = f"select {coloum_name} as col from {table_name} group by {coloum_name}"
            else:
                temp = f"select {coloum_name} as col from {table_name} group by {coloum_name} where {Condition}"
            self.cmd.execute(temp)
            co = [str(row[0]) for row in self.cmd.fetchall()]
            return co
        except Exception as ex:
            return co

    def Execute_updete(self, sql: str) -> bool:
        re = False
        try:
            self.cmd.execute(sql)
            self.SqlConnection.commit()
            return re
        except Exception as ex:
            return re

    def get_data_table(self, sql: str) -> pd.DataFrame:
        dt = pd.DataFrame()
        if sql != "":
            try:
                self.cmd.execute(sql)
                dt = pd.DataFrame(self.cmd.fetchall(), columns=[description[0] for description in self.cmd.description])
            except Exception as ex:
                pass
        return dt

    def add_comm_in_amount(self, amt: str) -> str:
        pp = ["", "", "", "", ""]
        if "." not in amt:
            amt = amt + ".00"
        pp = amt.split('.')
        if len(pp[0]) <= 3:
            pp[0] = pp[0] + "." + pp[1][0] + pp[1][1]
            return pp[0]
        else:
            if len(pp[0]) == 4:
                try:
                    pp[0] = pp[0][0] + "," + pp[0][1] + pp[0][2] + pp[0][3] + "." + pp[1][0] + pp[1][1]
                except:
                    pp[0] = pp[0][0] + "," + pp[0][1] + pp[0][2] + pp[0][3] + "." + pp[1][0] + "0"
                return pp[0]
            else:
                if len(pp[0]) == 5:
                    try:
                        pp[0] = pp[0][0] + pp[0][1] + "," + pp[0][2] + pp[0][3] + pp[0][4] + "." + pp[1][0] + pp[1][1]
                    except:
                        pp[0] = pp[0][0] + pp[0][1] + "," + pp[0][2] + pp[0][3] + pp[0][4] + "." + pp[1][0] + "0"
                    return pp[0]
                else:
                    if len(pp[0]) == 6:
                        try:
                            pp[0] = pp[0][0] + "," + pp[0][1] + pp[0][2] + "," + pp[0][3] + pp[0][4] + pp[0][5] + "." + pp[1][0] + pp[1][1]
                        except:
                            pp[0] = pp[0][0] + "," + pp[0][1] + pp[0][2] + "," + pp[0][3] + pp[0][4] + pp[0][5] + "." + pp[1][0] + "0"
                        return pp[0]
                    else:
                        if len(pp[0]) == 7:
                            try:
                                pp[0] = pp[0][0] + pp[0][1] + "," + pp[0][2] + pp[0][3] + "," + pp[0][4] + pp[0][5] + pp[0][6] + "." + pp[1][0] + pp[1][1]
                            except:
                                pp[0] = pp[0][0] + pp[0][1] + "," + pp[0][2] + pp[0][3] + "," + pp[0][4] + pp[0][5] + pp[0][6] + "." + pp[1][0] + "0"
                            return pp[0]
                        else:
                            return amt

    def round_value(self, xx: str) -> str:
        ans = ""
        val = xx.split('.')
        ans = val[0]
        if len(val) > 1:
            pp = val[1]
            y = int(pp[0])
            if y >= 5:
                ans = str(int(ans) + 1)
        ans = ans + ".00"
        return ans

    def get_round_off_value(self, xx: str) -> str:
        ans = "0"
        val = xx.split('.')
        if len(val) > 1:
            pp = val[1]
            y = int(pp[0])
            nnn = 0
            if int(pp) > 9:
                if int(pp[0]) != 0:
                    nnn = int(pp[0] + pp[1])
                else:
                    nnn = 0
            else:
                nnn = int(pp[0])
            if y >= 5:
                if nnn < 91:
                    ans = str(100 - nnn)
                else:
                    ans = "0" + str(100 - nnn)
            else:
                ans = str(0 - nnn)
            if y == 0:
                try:
                    ans = "-0" + str(pp[1])
                except:
                    ans = "-0" + str(pp[0])
        qq = str(ans)
        return ans


