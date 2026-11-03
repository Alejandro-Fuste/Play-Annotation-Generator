# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_3`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 8: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [21-58] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-92] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [98-141] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [155-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-72] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-83] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-88] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-140] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-152] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-37] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-180] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [21-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-65] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-40] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-43] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-150] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '28' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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