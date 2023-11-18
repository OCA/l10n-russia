import re
from datetime import datetime

from pytils import dt, numeral

from odoo.tools import pycompat


class QWebHelper(object):
    def img(self, img, img_type="png", width=0, height=0):
        if width:
            width = "width='%spx'" % (width)
        else:
            width = " "
        if height:
            height = "height='%spx'" % (height)
        else:
            height = " "
        toreturn = "<img %s %s src='data:image/%s;base64,%s' />" % (
            width,
            height,
            img_type,
            str(pycompat.to_text(img)),
        )
        return toreturn

    def numer(self, name):
        if name:
            numeration = re.findall(r"\d+$", name)
            if numeration:
                return numeration[0]
        return ""

    def ru_date(self, date):
        if date and date != "False":
            return dt.ru_strftime(
                '"%d" %B %Y года',
                date=datetime.strptime(date, "%Y-%m-%d"),
                inflected=True,
            )
        return ""

    def ru_date2(self, date):
        if date and date != "False":
            return dt.ru_strftime(
                "%d %B %Y г.",
                date=datetime.strptime(date, "%Y-%m-%d %H:%M:%S"),
                inflected=True,
            )
        return ""

    def in_words(self, number):
        return numeral.in_words(number)

    def rubles(self, amount):
        "Transform amount number in rubles to text"
        text_rubles = numeral.rubles(int(amount))
        copeck = round((amount - int(amount)) * 100)
        text_copeck = numeral.choose_plural(
            int(copeck), ("копейка", "копейки", "копеек")
        )
        return ("%s %02d %s") % (text_rubles, copeck, text_copeck)

    def initials(self, fio):
        if fio:
            return (
                fio.split()[0]
                + " "
                + "".join([fio[0:1] + "." for fio in fio.split()[1:]])
            ).strip()
        return ""

    def address(self, partner):
        address = []
        if partner.zip:
            address.append(partner.zip)
        if partner.city:
            address.append(partner.city)
        if partner.street:
            address.append(partner.street)
        if partner.street2:
            address.append(partner.street2)
        return ", ".join(address)

    def representation(self, partner):
        requisites = []
        if partner.name:
            requisites.append(partner.name)
        if partner.vat:
            requisites.append("ИНН " + partner.vat)
        if partner.kpp:
            requisites.append("КПП " + partner.kpp)
        requisites.append(self.address(partner))
        return ", ".join(requisites)

    def full_representation(self, partner):
        requisites = [self.representation(partner)]
        if partner.phone:
            requisites.append("тел.: " + partner.phone)
        elif partner.parent_id.phone:
            requisites.append("тел.: " + partner.parent_id.phone)
        bank = None
        if partner.bank_ids:
            bank = partner.bank_ids[0]
        elif partner.parent_id.bank_ids:
            bank = partner.parent_id.bank_ids[0]
        if bank and bank.acc_number:
            requisites.append("р/сч " + bank.acc_number)
        if bank and bank.bank_name:
            requisites.append("в банке " + bank.bank_name)
        if bank and bank.bank_bic:
            requisites.append("БИК " + bank.bank_bic)
        if bank and bank.bank_corr_acc:
            requisites.append("к/с " + bank.bank_corr_acc)
        return ", ".join(requisites)
