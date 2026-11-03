# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_71`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [9-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-49] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [20-62] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [64-98] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-169] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [71-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-190] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-169] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-95] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-83] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-100] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '27' has 1 frames without a visible bounding box.
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