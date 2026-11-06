# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_56`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 114: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [114-157] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-225] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-135] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-131] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-157] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-170] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-206] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-269] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-212] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-110] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-123] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-155] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-96] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-170] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-24] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-39] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-47] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-74] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-143] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-107] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-268] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-223] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-225] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-232] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-242] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-172] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-224] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-245] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-269] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-212] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-220] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-268] for track '35' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.