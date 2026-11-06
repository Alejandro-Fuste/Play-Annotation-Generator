# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_7`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 166 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 16: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 16: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '14' has invalid range: start=125, end=9. Clamping end to start.
> - Action 'Action_PreSnap' range [0-25] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-60] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-205] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-203] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-248] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-187] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [143-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-182] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-194] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-220] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-308] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-201] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-261] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-265] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-255] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-277] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-227] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-321] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-325] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-348] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-236] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-49] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-88] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-182] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-190] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-80] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-28] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-49] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-88] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-154] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-199] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-227] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-248] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-35] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-41] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-69] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-88] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-134] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-143] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-187] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-224] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-267] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-317] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-321] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-26] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-49] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-59] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-91] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-117] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-351] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-185] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-130] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-138] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-296] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-278] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-285] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-289] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-304] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-308] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-316] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-154] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-253] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-291] for track '26' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-182] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-239] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-283] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-291] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-302] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-314] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-319] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-182] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-274] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-246] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-269] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-294] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-307] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-216] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-277] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-286] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-359] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-224] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-239] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-212] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-233] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-261] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-287] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-240] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-310] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-313] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-317] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-243] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-312] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-274] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-327] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-293] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-299] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-307] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-310] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-355] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-336] for track '42' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.