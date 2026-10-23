# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_4`
- **Input XML**: `output_showcase_final/FieldGoalBlock/FieldGoalBlock_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [18-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-120] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-60] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-54] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-76] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-39] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-60] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-34] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-37] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-115] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-65] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-57] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-120] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-109] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-92] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-113] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-46] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-63] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-29] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-36] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-80] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-63] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-120] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-118] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-87] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-105] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-120] for track '25' has 2 frames without a visible bounding box.
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