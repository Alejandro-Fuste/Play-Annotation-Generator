# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_351`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_351/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 199 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 702: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [13–28], lower_priority='Action_ZoneBlock' annotated_start=16, effective_Action_ZoneBlock_start=29.
> - Action 'Action_None' range [13-278] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-292] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-227] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [230-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-276] for track '2' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [281-315] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-322] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-329] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-48] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-147] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-227] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-55] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-126] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-183] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [44-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [69-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [82-211] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [216-217] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-133] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [33-34] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-323] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-181] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [242-248] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-256] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-54] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-72] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-49] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-64] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-74] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-154] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-173] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-208] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-219] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-31] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-38] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-89] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-92] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-159] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-258] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-279] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [283-289] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-66] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-125] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [130-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-196] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-99] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-223] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-316] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-329] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-183] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-212] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-116] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-173] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-213] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-244] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-291] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-309] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-329] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-158] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-181] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-197] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-208] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-247] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-133] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-142] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-173] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-207] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-217] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-248] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-329] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-288] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-320] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-238] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-280] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-290] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-304] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-263] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-280] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [269-275] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-290] for track '33' has 2 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.