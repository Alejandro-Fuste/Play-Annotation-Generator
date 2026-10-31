# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_9`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [25–38], lower_priority='Action_PassBlock' annotated_start=28, effective_Action_PassBlock_start=39.
> - Action 'Action_PassBlock' range [28-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [136-145] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-138] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-37] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-57] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-103] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-69] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-37] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-194] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-148] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-203] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunHitchRoute' range [35-135] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '9' starts at frame 136, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [136-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-129] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-110] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' for track '16' starts at frame 25, but the player has no visible bounding box on this frame.
> - Action 'Action_BallSnap' range [25-25] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-152] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-215] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-120] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-222] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-232] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-140] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-269] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-204] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-242] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-229] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-264] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-238] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-269] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.