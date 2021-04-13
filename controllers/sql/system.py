# Author: Gerard Hickey <hickey@kinetic-compute.com>

import sys
import web
import settings

from libs import iredutils, form_utils
from libs.l10n import TIMEZONES

from libs.sqllib import SQLWrap, decorators, sqlutils
from libs.sqllib import domain as sql_lib_domain
from libs.sqllib import admin as sql_lib_admin

session = web.config.get('_session')

class Settings:
    @decorators.require_global_admin
    def GET(self):
        form = web.input(_unicode=False)
        all_domain_profiles = []

        # _wrap = SQLWrap()
        # conn = _wrap.conn
#
        # # Get first characters of all domains
        # _qr = sql_lib_domain.get_first_char_of_all_domains(conn=conn)
        # if _qr[0]:
        #     all_first_chars = _qr[1]
#
        # total = sql_lib_admin.num_managed_domains(conn=conn,
        #                                           disabled_only=disabled_only,
        #                                           first_char=first_char)
#
        # if total:
        #     qr = sql_lib_domain.get_paged_domains(cur_page=cur_page,
        #                                           first_char=first_char,
        #                                           disabled_only=disabled_only,
        #                                           conn=conn)
        #     if qr[0]:
        #         all_domain_profiles = qr[1]
#
        #     if settings.SHOW_USED_QUOTA:
        #         domains = []
        #         for i in all_domain_profiles:
        #             domains.append(str(i.domain))
#
        #         domain_used_quota = sql_lib_domain.get_domain_used_quota(conn=conn,
        #                                                                  domains=domains)
#
        # if session.get('is_global_admin'):
        #     days_to_keep_removed_mailbox = settings.DAYS_TO_KEEP_REMOVED_MAILBOX_FOR_GLOBAL_ADMIN
        # else:
        #     days_to_keep_removed_mailbox = settings.DAYS_TO_KEEP_REMOVED_MAILBOX

        try:
            page = web.render('sql/system.html',
                          msg=form.get('msg', None))
        except Exception as e:
            print(e, file=sys.stderr)
            fp = open('/tmp/error', 'a')
            fp.print(e)
            fp.close()

        return page



class DomainOwnership:
    pass



class SpamPolicy:
    pass



class WBList:
    pass



class Greylisting:
    pass




class Throttling:
    pass

