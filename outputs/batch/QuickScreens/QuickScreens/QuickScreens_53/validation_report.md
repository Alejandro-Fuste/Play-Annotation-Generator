# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_53`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [89-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-41] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-61] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-108] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-121] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-48] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-22] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-125] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [65-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [77-163] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-22] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-58] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-167] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-60] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-167] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '28' has 1 frames without a visible bounding box.
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