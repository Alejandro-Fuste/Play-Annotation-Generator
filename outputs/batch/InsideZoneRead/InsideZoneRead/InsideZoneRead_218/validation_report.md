# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_218`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_218/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 148 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 436: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [60–72], lower_priority='Action_ZoneBlock' annotated_start=63, effective_Action_ZoneBlock_start=73.
> - Action 'Action_None' range [60-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-151] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-239] for track '0' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [60-211] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-239] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-137] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-192] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [213-228] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-217] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-79] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [131-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-85] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-94] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-213] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-85] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-202] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-230] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [60-85] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-162] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-84] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-113] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-158] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-85] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [110-113] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [115-120] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [142-146] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 152, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [152-152] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-239] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [60-80] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-124] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [60-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-202] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-219] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-78] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [60-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-87] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-70] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-84] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-129] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-239] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [98-115] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-128] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-129] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-179] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-219] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-231] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-166] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-224] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-224] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.