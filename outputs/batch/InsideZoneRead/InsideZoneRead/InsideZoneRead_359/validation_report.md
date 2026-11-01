# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_359`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_359/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 718: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [17–30], lower_priority='Action_ZoneBlock' annotated_start=20, effective_Action_ZoneBlock_start=31.
> - Action 'Action_None' range [17-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-84] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-176] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [62-129] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [133-136] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [141-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [150-210] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-76] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-129] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-163] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-165] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-47] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-26] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-28] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-208] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-42] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-186] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [20-39] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [42-45] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-140] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-35] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-167] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-45] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-77] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-116] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-134] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-169] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-175] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-160] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-167] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-182] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-201] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-174] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-191] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '37' has 1 frames without a visible bounding box.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.