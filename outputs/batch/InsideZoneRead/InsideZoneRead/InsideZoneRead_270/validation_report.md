# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_270`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_270/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 540: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [1–13], lower_priority='Action_ZoneBlock' annotated_start=4, effective_Action_ZoneBlock_start=14.
> - Action 'Action_None' range [1-127] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-47] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-123] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [72-94] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-74] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-98] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-171] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [19-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [49-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-8] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-22] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-44] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-172] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-183] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-210] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-168] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-186] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-177] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-189] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-197] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-189] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-208] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '45' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.