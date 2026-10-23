# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_2`
- **Input XML**: `output_showcase_final/QuickScreens/QuickScreens_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [21-59] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-63] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-71] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-64] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-72] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-66] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowScreenPass' range [48-50] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-68] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-69] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-167] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-204] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-170] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-199] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-157] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [101-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-144] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-157] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '25' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.