# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_31`
- **Input XML**: `outputs/batch/SlantAndGo/SlantAndGo/SlantAndGo_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 44: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [41–56], lower_priority='Action_PassBlock' annotated_start=49, effective_Action_PassBlock_start=57.
> - Segment 'Action_ThrowPass' for track '17' has invalid range: start=125, end=114. Clamping end to start.
> - Action 'Action_None' range [41-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '2' starts at frame 41, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [41-44] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-53] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-66] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SellRoute' range [64-95] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [98-102] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [104-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-149] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-188] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-71] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-96] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-210] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [41-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 41, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [41-50] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-74] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-123] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [127-155] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [159-210] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-52] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-46] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-132] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '22' starts at frame 41, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [41-50] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-100] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-98] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-94] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-120] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-109] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-202] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.