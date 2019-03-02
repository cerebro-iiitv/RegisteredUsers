import xlwt
from xlwt import Workbook
from registered.parser import parse_json


def write_sheet(all_events):
    wb = Workbook()
    for event in all_events:
        part_num = 1
        sheet = wb.add_sheet(event[1][:10])
        style = xlwt.easyxf('font: bold 1')
        sheet.write(0, 0, 'Name', style)
        sheet.write(0, 1, 'Phone number', style)
        sheet.write(0, 2, 'Signature', style)
        # print(event[1], event[0])
        participant_list = parse_json(event_id=event[0])
        # print(participant_list[0][1])
        # print(len(participant_list[0][1]))
        for participant in participant_list[0][1]:
            # print(participant[0], participant[1])
            sheet.write(part_num, 0, str(participant[0]))
            sheet.write(part_num, 1, str(participant[1]))
            part_num += 1
    wb.save('participants.xls')