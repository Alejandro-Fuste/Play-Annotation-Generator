# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_73`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_73/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 78: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_ScreenBlock' range [38-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [81-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-105] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-150] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-118] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-146] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-89] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-128] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-102] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-29] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-37] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-101] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-130] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-80] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-121] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-120] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-55] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-23] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-52] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-102] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [105-148] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-89] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-95] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-136] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [114-124] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '26' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.