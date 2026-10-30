# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_11`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [28-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-139] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-77] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-83] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-149] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-59] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-92] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-58] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [71-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-71] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [28-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-38] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-138] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '22' starts at frame 28, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [28-28] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-46] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-140] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-150] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.