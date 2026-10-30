# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_42`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_42/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [16-88] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-79] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-70] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-83] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-83] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-79] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [57-61] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-49] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-51] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-66] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-36] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-54] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-84] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-34] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 30, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [30-30] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-85] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [16-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-87] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-54] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-88] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-19] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-24] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-40] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-70] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-37] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-43] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-76] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-89] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-190] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-208] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-151] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-160] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.