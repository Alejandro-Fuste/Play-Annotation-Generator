# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_78`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 143 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 158: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [71-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 64, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [64-64] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-217] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-80] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-103] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [66-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-128] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-161] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-267] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-95] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-191] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-215] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-198] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-46] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-88] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-201] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-78] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-27] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-42] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-196] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-238] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-247] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-7] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-20] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-48] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-63] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-166] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-91] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-135] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-244] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-80] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-194] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-148] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-253] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-285] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-105] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-219] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-237] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-130] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-299] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-154] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-135] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-249] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-124] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-134] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-152] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-189] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-235] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-260] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-196] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-261] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-279] for track '33' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.