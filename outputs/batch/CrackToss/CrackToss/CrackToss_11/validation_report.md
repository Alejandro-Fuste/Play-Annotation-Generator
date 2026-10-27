# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_11`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 111 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 24: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 24: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '18' (Unknown) duration 93 frames exceeds threshold 90 frames [start=123, end=215].
> - Action 'Action_BallCarry' range [147-211] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-201] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [115-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [136-139] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [141-142] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [151-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-249] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-152] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-213] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-152] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-223] for track '5' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [226-269] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-247] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-97] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-142] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-174] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-194] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 118, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [118-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-26] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-21] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-47] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-107] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [112-113] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-231] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-108] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-119] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-141] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [123-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [147-202] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [204-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [210-215] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-144] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-174] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-158] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-233] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [235-254] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-257] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-228] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-269] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-269] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-269] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-240] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-269] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '40' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.