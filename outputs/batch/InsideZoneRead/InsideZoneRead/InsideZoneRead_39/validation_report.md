# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_39`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 80: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 80: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [104-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-183] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-249] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-243] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-181] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-211] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-234] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-240] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-255] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [104-188] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [122-132] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-256] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-165] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-172] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-249] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-269] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-174] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-195] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [145-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-175] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-150] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-193] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-201] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-269] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [125-145] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [147-165] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [168-173] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [183-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-267] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-17] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-83] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-116] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-229] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-257] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-232] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-234] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-240] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-257] for track '28' has 3 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.