# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_60`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_60/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' for track '0' starts at frame 68, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [68-68] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-150] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [63-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-89] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-150] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-148] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-81] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-86] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-115] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-86] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-53] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-82] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-6] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-37] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-55] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-123] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-150] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-118] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '29' has 4 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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