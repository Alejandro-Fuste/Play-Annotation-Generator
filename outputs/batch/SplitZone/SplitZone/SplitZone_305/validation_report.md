# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_305`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_305/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 58 |
| Player Tracks | 58 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 132 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 612: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_None' range [85-118] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-191] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [90-117] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [120-121] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-106] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-206] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-169] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-156] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-359] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-196] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-168] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [174-192] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [85-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-214] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [124-189] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [85-176] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-195] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [135-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-191] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-78] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [125-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [141-144] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-38] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-189] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-175] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-195] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [127-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-160] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-155] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-191] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-235] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-212] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-240] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-358] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-203] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-239] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-296] for track '42' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [197-208] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-270] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-207] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-220] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-266] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-240] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-283] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-309] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-347] for track '53' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '55' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.